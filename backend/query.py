import chromadb

def search(query_text, n_results=3):
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="banking_faq")

    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )

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
    search("What happens if my card is stolen?")