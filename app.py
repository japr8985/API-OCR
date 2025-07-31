from flask import Flask, request, jsonify
import tempfile
import pytesseract
from pdf2image import convert_from_bytes

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "File is not a PDF"}), 400

    pdf_bytes = file.read()
    images = convert_from_bytes(pdf_bytes)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"

    return jsonify({"text": text.strip()})

