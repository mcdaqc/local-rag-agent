# Simple RAG Chat

A simple chat application that uses RAG (Retrieval Augmented Generation) to answer questions about your documents. Built with Streamlit, Ollama, and Qdrant.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Qdrant:
```bash
docker-compose up -d
```

3. Install Ollama models:
```bash
ollama pull llama2
ollama pull nomic-embed-text
```

4. Run the app:
```bash
streamlit run app.py
```

## Features

- Upload PDF or TXT documents
- Chat with AI about document content
- Uses llama2 for text generation
- Uses nomic-embed-text for embeddings
- Stores vectors in Qdrant

## Configuration

Create a `.env` file with:
```env
LLM_MODEL=llama2
EMBEDDING_MODEL=nomic-embed-text
COLLECTION_NAME=document-index
QDRANT_URL=http://localhost:6333
```

## How It Works

1. Upload a document
2. Document is split into chunks
3. Chunks are converted to embeddings
4. When you ask a question:
   - Similar chunks are retrieved
   - LLM generates response using retrieved context

## Project Structure

```
simple-rag-agent/
├── app.py              # Main Streamlit application
├── config.py           # Configuration settings
├── docker-compose.yml  # Docker configuration for Qdrant
├── requirements.txt    # Python dependencies
└── .env               # Environment variables (create this)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

