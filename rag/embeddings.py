from sentence_transformers import SentenceTransformer
from chunking import load_document, create_chunks
import os


model = SentenceTransformer("all-MiniLM-L6-v2")


if __name__ == "__main__":

    file_path = os.path.join(
        os.path.dirname(__file__),
        "documents",
        "career_skills.txt"
    )

    text = load_document(file_path)

    chunks = create_chunks(text)

    embeddings = model.encode(chunks)

    print("Number of chunks:", len(chunks))
    print("Number of embeddings:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))

    print("\nFirst chunk:")
    print(chunks[0])

    print("\nFirst embedding:")
    print(embeddings[0])