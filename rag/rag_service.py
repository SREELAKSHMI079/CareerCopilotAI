from rag.retrieve import search_knowledge
from google import genai
from dotenv import load_dotenv

import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_skill_guidance(skill):

    query = f"""
    How should someone learn {skill}?
    What are the important concepts and practical skills related to {skill}?
    """

    results = search_knowledge(
        query,
        top_k=3
    )

    context = ""

    for result in results:
        context += result.payload["text"]
        context += "\n\n"

    prompt = f"""
You are CareerCopilotAI, an AI career assistant.

The user is missing the following skill:

{skill}

Use the retrieved career knowledge below to provide practical
guidance for learning this skill.

Retrieved career knowledge:
{context}

Provide:
1. What the skill is.
2. What concepts the user should learn first.
3. What practical skills they should develop.
4. A small project idea if the retrieved knowledge supports one.

Important:
- Use the retrieved knowledge as your primary source.
- Do not invent specific information that is not supported by it.
- Keep the answer practical and concise.
"""

    try:

        response = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt
        )

        return response.output_text

    except Exception as e:

        return f"RAG guidance temporarily unavailable: {str(e)}"
