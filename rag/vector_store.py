from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

from chunking import load_document, create_chunks

import os


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Create local Qdrant database
client = QdrantClient(path="rag/qdrant_data")


COLLECTION_NAME = "career_knowledge"


def create_collection():

    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )


def add_documents():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "documents",
        "career_skills.txt"
    )

    text = load_document(file_path)

    chunks = create_chunks(text)

    embeddings = model.encode(chunks)

    points = []

    for index, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):

        point = PointStruct(
            id=index,
            vector=embedding.tolist(),
            payload={
                "text": chunk
            }
        )

        points.append(point)

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"Added {len(points)} documents to Qdrant.")


if __name__ == "__main__":

    create_collection()

    add_documents()

    print("Qdrant setup complete!")