from datetime import datetime
import re

def format_dob(dob):
    try:
        # Convert DD/MM/YYYY → YYYY-MM-DD
        return datetime.strptime(dob, "%d/%m/%Y").strftime("%Y-%m-%d")
    except:
        return dob


def validate_data(data):
    errors = []

    # Format DOB first
    if data.get("dob"):
        data["dob"] = format_dob(data["dob"])

    # Validate DOB
    if not re.match(r"\d{4}-\d{2}-\d{2}", data.get("dob", "")):
        errors.append("Invalid DOB format (YYYY-MM-DD)")

    if not data.get("name"):
        errors.append("Missing name")

    # Optional field
    if not data.get("address"):
        data["address"] = "Not Available"

    if not data.get("id_number"):
        errors.append("Missing ID number")

    return errors