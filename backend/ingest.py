import chromadb
from prep import load_documents, chunk_text

def build_vector_db():
    # Persistent client saves the DB to disk in backend/chroma_db/
    client = chromadb.PersistentClient(path="chroma_db")

    # Create (or reset) the collection that will hold our chunks
    collection = client.get_or_create_collection(name="banking_faq")

    documents = load_documents()
    ids = []
    texts = []
    metadatas = []

    chunk_counter = 0
    for doc in documents:
        for chunk in chunk_text(doc["text"]):
            chunk_counter += 1
            ids.append(f"chunk_{chunk_counter}")
            texts.append(chunk)
            metadatas.append({"source": doc["source"]})

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas
    )

    print(f"Stored {chunk_counter} chunks in the vector database.")

if __name__ == "__main__":
    build_vector_db()