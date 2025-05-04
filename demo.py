import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

for model in genai.list_models():
    print(f"Model: {model.name}")
    for method in model.supported_generation_methods:
        print(f"- Supports: {method}")