from flask import Flask, request, jsonify
from database import init_db, insert_record
from gemini_utils import extract_kyc_data
from schema import validate_data

app = Flask(__name__)
init_db()

@app.route("/process", methods=["POST"])
def process_document():
    file = request.files["file"]
    image_bytes = file.read()

    try:
        data = extract_kyc_data(image_bytes)
        errors = validate_data(data)

        if errors:
            return jsonify({"status": "error", "errors": errors})

        insert_record(data)

        return jsonify({"status": "success", "data": data})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)