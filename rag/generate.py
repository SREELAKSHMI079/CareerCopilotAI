from retrieve import search_knowledge
from google import genai
from dotenv import load_dotenv

import os


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(query):

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

Answer the user's question using the provided career knowledge.

User question:
{query}

Retrieved career knowledge:
{context}

Instructions:
- Use the retrieved knowledge as your primary source.
- Give a practical and clear answer.
- Do not invent information that is not supported by the retrieved knowledge.
- If the retrieved knowledge is insufficient, say that more information is needed.
"""

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":

    question = "How should I start learning Apache Spark?"

    answer = generate_answer(question)

    print("\nQuestion:")
    print(question)

    print("\nCareerCopilotAI:")
    print(answer)