import os


def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def create_chunks(text):
    sections = text.split("\n\n")

    chunks = []

    for section in sections:
        section = section.strip()

        if section:
            chunks.append(section)

    return chunks


if __name__ == "__main__":

    file_path = os.path.join(
        os.path.dirname(__file__),
        "documents",
        "career_skills.txt"
    )

    text = load_document(file_path)

    chunks = create_chunks(text)

    print("Number of chunks:", len(chunks))

    for i, chunk in enumerate(chunks):
        print("\n--- Chunk", i + 1, "---")
        print(chunk)