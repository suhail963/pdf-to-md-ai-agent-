# 🧠 PDF to Markdown AI Converter (Flask API)

A Flask REST API that converts PDF files to structured Markdown using AI. It supports both regular and scanned PDFs by combining OCR and AI reasoning.

---

## 📚 Libraries and Tools Used

- **Flask** – REST API framework
- **pydantic** – Data validation and models
- **pydantic_ai** – Framework for AI agent integration
- **GeminiModel** – Google Generative AI model via pydantic_ai
- **google-generativeai** – Official Gemini API client
- **pdfplumber** – Extracts text from native PDFs
- **pytesseract** – OCR engine to read text from images
- **pdf2image** – Converts PDF pages to images for OCR
- **python-dotenv** – Loads environment variables from `.env`
- **nest_asyncio** – Enables running async code in Flask
- **Tesseract OCR** – External tool used by pytesseract
- **Poppler** – External tool required by pdf2image

---

## 📁 Project Structure

project/
│
├── .venv/ # Virtual environment
├── outputs/ # Folder for output Markdown files
├── templates/ # Optional HTML templates
├── uploads/ # Uploaded PDF files
│
├── .env # Contains Google API key
├── app.py # Main Flask app
├── converter.py # PDF to text/OCR logic
├── demo.py # Optional testing script(for available gemini_model)
├── pydantic_ai_model.py # Defines the AI agent



---

## ✅ Setup Instructions

### 1. Install Python libraries

```bash
pip install Flask pydantic pydantic_ai pdfplumber pytesseract pdf2image python-dotenv google-generativeai nest_asyncio
2. Install System Tools
Ubuntu
bash
Copy
Edit
sudo apt install tesseract-ocr poppler-utils
macOS
bash
Copy
Edit
brew install tesseract poppler
🔐 Environment Setup
Create a .env file:

GOOGLE_API_KEY=your_google_api_key_here
🚀 Running the App
export FLASK_APP=app.py
flask run
#📡 API Usage
Send a PDF file to the API:

curl -X POST http://localhost:5000/convert \
  -F "file=@yourfile.pdf"
The API will return structured Markdown text.

🔄 How It Works
Upload a PDF to the /convert endpoint.

If the PDF is text-based, it uses pdfplumber.

If the PDF is scanned, it uses pdf2image + pytesseract.

The extracted text is sent to an AI agent using Google Gemini.

The agent returns Markdown content which is saved in outputs/.

📌 Notes
Tesseract and Poppler must be installed on your system.

A valid Google Generative AI API key is required.

Works with both text-based and scanned PDFs.