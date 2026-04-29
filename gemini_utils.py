import google.generativeai as genai
import json
import re
import os

genai.configure(api_key=os.getenv("AIzaSyCbjCd8qKyUhVacHnwwX92MYCqy2nxIia8"))

model = genai.GenerativeModel("gemini-2.5-flash")


def clean_json(text):
    text = re.sub(r"```json|```", "", text)
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    else:
        raise Exception(f"Invalid JSON from AI: {text}")


def extract_kyc_data(image_bytes):
    prompt = """
    You are a strict KYC extraction system.

    Extract:
    - Name
    - Date of Birth
    - Address
    - ID Number

    Return ONLY JSON:
    {
        "name": "",
        "dob": "",
        "address": "",
        "id_number": ""
    }
    """

    response = model.generate_content([
        prompt,
        {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }
    ])

    text_output = response.text
    print("RAW OUTPUT:", text_output)

    return clean_json(text_output)