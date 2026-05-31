from google import genai
from dotenv import load_dotenv
import json
import os

# Load .env variables
load_dotenv()

# Get API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Assign API key
client = genai.Client(api_key= API_KEY)

# Get Prompts File
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_FILE = os.path.join(BASE_DIR, "templates", "prompts.json")

with open(PROMPTS_FILE, "r", encoding= "utf-8") as file:
    data = json.load(file)

def generate_output(user_prompt, input_role):

    # Get User Input Role prompt 
    role_prompt = data["PROMPTS"].get(input_role, {})
    
    # Insert User Input into Role Prompt
    final_prompt = role_prompt.format(user_input = user_prompt)

    # Generate Response
    response = client.models.generate_content(model= "gemini-3.5-flash", contents= final_prompt)

    return response.text
