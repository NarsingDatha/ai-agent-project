import os
os.environ["TRANSFORMERS_NO_TF"] = "1"  # Disable TensorFlow usage

from transformers import pipeline
from memory.memory_store import SharedMemory
import json

# Load zero-shot classifier once
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

INTENTS = ["Invoice", "RFQ", "Complaint", "Regulation", "Request for Quote", "Other"]

def classifier_agent(input_data, memory: SharedMemory):
    fmt = None
    content_to_classify = ""

    if isinstance(input_data, dict):
        fmt = "json"
        content_to_classify = json.dumps(input_data)
    elif isinstance(input_data, str):
        if input_data.strip().startswith("From:") or "Subject:" in input_data:
            fmt = "email"
        else:
            fmt = "text"
        content_to_classify = input_data
    else:
        fmt = "unknown"
        content_to_classify = str(input_data)

    result = classifier(content_to_classify, INTENTS)
    intent = result["labels"][0]

    memory.store_metadata(fmt, intent)
    return fmt, intent

