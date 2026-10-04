from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(
    path="rag/qdrant_data"
)

COLLECTION_NAME = "career_knowledge"


def search_knowledge(query, top_k=3):

    query_embedding = model.encode(query).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=top_k
    ).points

    return results


if __name__ == "__main__":

    query = "How can I process very large datasets?"

    results = search_knowledge(query)

    print("\nQuery:")
    print(query)

    print("\nRetrieved knowledge:")

    for result in results:

        print("\n---")
        print("Score:", result.score)
        print("Text:")
        print(result.payload["text"])