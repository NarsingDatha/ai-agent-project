# flowbit_project/mcp/orchestrator.py

from agents.classifier_agent import classifier_agent
from agents.json_agent import json_agent
from agents.email_parser import email_parser
from agents.pdf_agent import pdf_agent      # <-- new import
from memory.memory_store import SharedMemory

# Simulated inputs including JSON, Email and PDF file path
json_input = {"id": 1, "name": "Alice", "email": "alice@example.com"}

email_input = """
From: bob@example.com
Subject: Request for Quote

Hello, I need an RFQ for 100 units.
"""

pdf_input_path = "data/sample_file.pdf"  # Path to PDF file

# Controller / shared memory instance
memory = SharedMemory()

# Process JSON input
fmt, intent = classifier_agent(json_input, memory)
if fmt == "json":
    result = json_agent(json_input)
    memory.store_extracted("JSON Agent", result)

# Process Email input
fmt, intent = classifier_agent(email_input, memory)
if fmt == "email":
    result = email_parser(email_input)
    memory.store_extracted("Email Agent", result)
    memory.store_thread(result["thread_id"], result)

# Process PDF input manually (no classification of raw PDF in this example)
pdf_result = pdf_agent(pdf_input_path)
memory.store_extracted("PDF Agent", pdf_result)

# Print final memory state (pretty JSON)
import json
print(json.dumps(memory.get_memory(), indent=2))

