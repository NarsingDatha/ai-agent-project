def json_agent(input_json):
    # Expected schema: user_id, full_name, email_address
    # Simple example: remap keys if needed and find missing fields
    schema = ["user_id", "full_name", "email_address"]
    
    output = {}
    missing = []

    output["user_id"] = input_json.get("id") or input_json.get("user_id")
    output["full_name"] = input_json.get("name") or input_json.get("full_name")
    output["email_address"] = input_json.get("email") or input_json.get("email_address")

    for key in schema:
        if output.get(key) is None:
            missing.append(key)

    return {"output": output, "missing_fields": missing}

