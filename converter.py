# converter.py
import pdfplumber
import pytesseract
from pdf2image import convert_from_path

def extract_pdf_text(pdf_path: str) -> str:
    """Extract text from PDF using pdfplumber and OCR if necessary."""
    all_text = []
    
    # Try extracting text using pdfplumber
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text() or ""
                if text.strip():
                    all_text.append(text)
                else:
                    # If no text, use OCR to extract text from images on the page
                    images = convert_from_path(pdf_path, first_page=page.page_number, last_page=page.page_number)
                    text = pytesseract.image_to_string(images[0])
                    all_text.append(text)
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    
    return "\n".join(all_text)
