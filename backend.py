from google import genai
import os
from dotenv import load_dotenv


load_dotenv()
API = os.getenv("API_KEY")
client = genai.Client(api_key=API)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)