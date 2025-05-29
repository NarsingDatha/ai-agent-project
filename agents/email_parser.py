import re
import random

def email_parser(email_text):
    # Extract sender, subject, urgency from email body text
    sender_match = re.search(r"From:\s*(.*)", email_text)
    subject_match = re.search(r"Subject:\s*(.*)", email_text)
    
    sender = sender_match.group(1).strip() if sender_match else "Unknown"
    subject = subject_match.group(1).strip() if subject_match else "No Subject"

    # Naive urgency detection based on keywords
    urgency = "Normal"
    if re.search(r"\burgent\b|\basap\b|\bimmediately\b", email_text, re.IGNORECASE):
        urgency = "High"
    elif re.search(r"\bwhenever\b|\bno rush\b", email_text, re.IGNORECASE):
        urgency = "Low"

    thread_id = random.getrandbits(64)

    return {
        "sender": sender,
        "subject": subject,
        "urgency": urgency,
        "thread_id": thread_id
    }

