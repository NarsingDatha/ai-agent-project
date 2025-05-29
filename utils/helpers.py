def detect_format(data):
    if isinstance(data, dict):
        return "json"
    elif isinstance(data, str):
        if "@" in data and "Subject" in data:
            return "email"
        else:
            return "text"
    else:
        return "pdf"

def classify_intent(text):
    text = text.lower()
    if "invoice" in text:
        return "Invoice"
    elif "rfq" in text:
        return "RFQ"
    elif "complaint" in text:
        return "Complaint"
    elif "regulation" in text:
        return "Regulation"
    else:
        return "General"

