# pydantic_ai_model.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

api_key = os.getenv("GEMINI_API_KEY")  # Get the Google API key from the environment

import nest_asyncio
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel  # Try this import path
import os
import google.generativeai as genai

# Apply nest_asyncio to allow for event loops in environments like Jupyter notebooks
nest_asyncio.apply()

# Fetch API Key from environment or directly set it here
# Make sure the environment variable is set

# Or alternatively, hardcode the API key:
# api_key = "your-api-key-here"

if not api_key:
    raise ValueError("API key is required for Google Gemini. Set the GOOGLE_API_KEY environment variable or hardcode the key.")

# Configure the Google API key
genai.configure(api_key=api_key)

# Initialize Gemini model
# In your pydantic_ai_model.py
model = GeminiModel(model_name="gemini-1.5-flash")


# Define the system prompt for summarization
system_prompt = "You are a helpful assistant who summarizes long text concisely and accurately."

# Create the agent with the system prompt
basic_agent = Agent(model=model, system_prompt=system_prompt)

def summarize_text(text: str) -> str:
    """Summarize the extracted text using PydanticAI agent with Gemini."""
    prompt = f"Extract only on the essential content into markdown file :\n{text}"
    response = basic_agent.run_sync(prompt)
    return response.data

if __name__ == "__main__":
    long_text = """
    The quick brown fox jumps over the lazy dog. This is a well-known pangram, a sentence that contains every letter of the English alphabet. Pangrams are often used to test the fonts or the typewriters. The most famous pangram is arguably the one mentioned at the beginning of this sentence. It's concise and easy to remember. Creating good pangrams can be a fun linguistic challenge. There are many other interesting facts about the English language, such as the existence of words that are spelled the same forwards and backwards, called palindromes. Another interesting linguistic phenomenon is the existence of words with no true vowels, although these are less common in English compared to some other languages. The study of language is a vast and fascinating field, covering everything from the history of words to the way we process and understand speech.
    """
    summary = summarize_text(long_text)
    print(f"Original Text:\n{long_text}\n")
    print(f"Summary:\n{summary}")