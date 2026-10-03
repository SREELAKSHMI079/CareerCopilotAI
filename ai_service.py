from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume_with_ai(resume_text, target_role):

    prompt = f"""
You are a career assistant analyzing a resume.

Target role:
{target_role}

Resume:
{resume_text}

Analyze the resume for the target role.

Provide:
1. A short summary of the candidate's profile.
2. The candidate's strongest skills and experience relevant to the role.
3. Areas where the candidate could improve.
4. Specific suggestions for improving their resume for this role.

Keep the response practical and concise.
"""

    try:
        response = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"AI analysis temporarily unavailable: {str(e)}"