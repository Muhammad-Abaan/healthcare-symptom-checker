import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash" 

SYSTEM_RULES = (
    "You are a strict, clinical educational symptom-checking assistant.\n"
    "Your ONLY purpose is to analyze health-related symptoms. If the user's input "
    "is NOT about health symptoms, you MUST refuse to answer and politely explain that you are solely an educational symptom checker.\n\n"
    "CRITICAL INSTRUCTION: You MUST ALWAYS include a clear educational disclaimer stating that this is for "
    "educational purposes only, does not constitute medical advice, and the user should consult "
    "with a qualified healthcare provider. Format your response cleanly using Markdown."
)

def analyze_symptoms_multi(symptoms: str, db_history: list) -> str:
    """
    Sends the user's symptoms along with multi-turn history.
    """
    if not API_KEY or API_KEY == "your_gemini_api_key_here":
        return "Error: API Key is not configured. Please set GEMINI_API_KEY in the .env file."

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        
        # Convert DB history format mapping to Gemini format
        # Gemini handles 'user' and 'model'
        gemini_history = []
        for msg in db_history:
            gemini_role = "model" if msg['role'] == "ai" else "user"
            gemini_history.append({'role': gemini_role, 'parts': [msg['content']]})
            
        chat = model.start_chat(history=gemini_history)
        
        # We append the system rules quietly inside every new prompt so it never hallucinates outside of boundaries
        strict_prompt = f"{SYSTEM_RULES}\n\nUser Question:\n{symptoms}"
        
        response = chat.send_message(strict_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while communicating with the AI service: {str(e)}"
