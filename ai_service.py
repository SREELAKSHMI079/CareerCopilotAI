from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Say hello to CareerCopilotAI in one sentence."
)

print(interaction.output_text)