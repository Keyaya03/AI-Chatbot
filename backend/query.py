import chromadb

SIMILARITY_THRESHOLD = 1.3 

def search(query_text, n_results=3):
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="banking_faq")

    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )

     # Debug print you already had
    print(f"distances: {results['distances'][0]}")

    top_distance = results['distances'][0][0]

    if top_distance > SIMILARITY_THRESHOLD:
        # No confident match — signal this back to rag.py
        return None

    # results contains lists-of-lists since Chroma supports batch queries
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for i in range(len(documents)):
        print(f"\n--- Match {i+1} (distance: {distances[i]:.4f}) ---")
        print(f"Source: {metadatas[i]['source']}")
        print(documents[i])

    return results

if __name__ == "__main__":
    search(" Do you need my help Kaps?")