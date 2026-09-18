# Banking FAQ RAG Chatbot

An AI-powered chatbot that answers banking questions using Retrieval Augmented Generation (RAG), built with React, FastAPI, Chroma vector database, and the Claude API.

## Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Python (FastAPI)
- **Vector Database:** ChromaDB
- **AI Model:** Claude API (Anthropic)
- **Deployment:** AWS EC2 (backend server), AWS S3 (frontend static hosting)

## How It Works

1. User submits a question through the chat interface.
2. The question is converted into a vector embedding.
3. The system searches the Chroma vector database for the most relevant document chunks based on semantic similarity.
4. The retrieved chunks are combined with the user's question into a prompt sent to Claude.
5. Claude generates an answer using only the provided context, keeping responses accurate and grounded in the actual banking policy documents.

## Key Features

- Semantic search across banking FAQ documents
- Context-aware answers powered by Claude
- Full-stack deployment on AWS
- Clean, simple React chat interface

## Architecture

User → React Frontend (S3) → FastAPI Backend (EC2) → Chroma Vector DB → Claude API → Response


## Setup (Local Development)

### Backend
```bash
cd backend
pip install -r requirements.txt
# Add ANTHROPIC_API_KEY to a .env file
python3 -m uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Notes

This project was independently built to deepen hands-on understanding of RAG pipelines, vector databases, and full-stack AI integration.

#Live URL 

http://keya-banking-chatbot.s3-website.us-east-2.amazonaws.com/

## Note
Backend may be offline, contact me to see a live run
