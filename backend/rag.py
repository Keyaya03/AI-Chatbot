import os
from anthropic import Anthropic
from query import search
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def ask(question):
    # Step 1: Retrieve relevant chunks using the search function we already built
    results = search(question, n_results=3)

    # Step 2: Build a context string from those chunks
    context = ""
    for doc in results["documents"][0]:
        context += doc + "\n\n"

    # Step 3: Send question + context to Claude
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": f"You are a helpful banking assistant. Answer the question using ONLY the context below. If the answer isn't in the context, say you don't have that information.\n\nContext:\n{context}\n\nQuestion: {question}"
            }
        ]
    )

    return message.content[0].text

if __name__ == "__main__":
    answer = ask("What happens if my card is stolen?")
    print(answer)