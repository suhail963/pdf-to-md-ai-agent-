from flask import Flask, request, jsonify, send_from_directory, render_template
import os
from pathlib import Path
from pydantic_ai_model import summarize_text
from converter import extract_pdf_text

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    # Render the upload UI
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert_pdf():
    """Handle PDF upload, extract text, convert to markdown (via summarize_text), and return info."""
    if 'file' not in request.files:
        return jsonify(success=False, message="No file part"), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify(success=False, message="No selected file"), 400

    if not file.filename.lower().endswith('.pdf'):
        return jsonify(success=False, message="Only PDF files are allowed"), 400

    try:
        # Save the uploaded PDF
        pdf_filename = Path(file.filename).name
        pdf_path = os.path.join(UPLOAD_FOLDER, pdf_filename)
        file.save(pdf_path)

        # Extract text
        pdf_text = extract_pdf_text(pdf_path)
        if not pdf_text.strip():
            return jsonify(success=False, message="No text could be extracted."), 400

        # Summarize (you can adjust this to produce Markdown if desired)
        markdown = summarize_text(pdf_text)

        # Save markdown file
        md_filename = Path(pdf_filename).stem + ".md"
        md_path = os.path.join(UPLOAD_FOLDER, md_filename)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        return jsonify(success=True, markdown=markdown, filename=md_filename)

    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route('/download/<filename>')
def download_markdown(filename):
    """Serve the generated Markdown file for download."""
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    # Enable debug only for development
    app.run(debug=True)
