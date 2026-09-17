import os

def load_documents(data_dir="data"):
    docs = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(data_dir, filename), "r") as f:
                docs.append({"source": filename, "text": f.read()})
    return docs

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    documents = load_documents()
    all_chunks = []
    for doc in documents:
        for chunk in chunk_text(doc["text"]):
            all_chunks.append({"source": doc["source"], "text": chunk})
    print(f"Loaded {len(documents)} documents, produced {len(all_chunks)} chunks")