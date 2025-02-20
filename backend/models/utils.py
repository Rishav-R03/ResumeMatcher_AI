import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
# Set up Gemini API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Replace with actual key
genai.configure(api_key=GOOGLE_API_KEY)

def extract_entities_gemini(text):
    """Extracts job titles, skills, and experience level using Gemini AI."""
    
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    Extract key details from the following job description:
    - Job Titles
    - Required Skills
    - Experience Level (e.g., Junior, Mid-Level, Senior)

    Job Description:
    {text}

    Return the output as a structured JSON format with 'job_titles', 'skills', and 'experience_level'.
    """

    response = model.generate_content(prompt)
    
    return response.text  # Gemini returns structured JSON
