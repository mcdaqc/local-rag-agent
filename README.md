# 🧠 Local RAG Agent

A sophisticated local Retrieval-Augmented Generation (RAG) system powered by Llama 3.2 through Ollama, with Qdrant as the vector database. This project provides a fully local implementation of a RAG system with enhanced features and better organization.

## 🌟 Features

- **Fully Local Implementation**: No external API dependencies required
- **Modern Architecture**: 
  - FastAPI-based REST API
  - Modular and maintainable code structure
  - Configuration management with environment variables
  - Comprehensive logging system
- **Advanced Components**:
  - Llama 3.2 for text generation
  - Qdrant for vector storage
  - Interactive playground interface
  - PDF document processing
- **Developer Experience**:
  - Hot reloading for development
  - Structured logging
  - Environment-based configuration
  - Clear project organization

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Docker (for Qdrant)
- Ollama installed locally

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/local-rag-agent.git
cd local-rag-agent
```

2. Create and configure a virtual environment:

For Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip
```

For Linux/Mac:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip
```

3. Install dependencies:
```bash
# Install all requirements
pip install -r requirements.txt

# Verify installation
pip list
```

4. Set up environment variables:
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
# You can use any text editor to modify the settings
```

5. Start Qdrant:
```bash
# Pull Qdrant image
docker pull qdrant/qdrant

# Run Qdrant container
docker run -p 6333:6333 qdrant/qdrant
```

6. Install Ollama models:
```bash
# Pull required models
ollama pull llama3.2
ollama pull openhermes
```

7. Run the application:
```bash
# Make sure your virtual environment is activated
# You should see (venv) at the start of your command prompt

# Run the application
python main.py
```

The application will be available at:
- API: http://localhost:8000
- Playground: http://localhost:8000/playground
- API Documentation: http://localhost:8000/docs

### Managing the Virtual Environment

To deactivate the virtual environment when you're done:
```bash
deactivate
```

To reactivate the virtual environment later:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

## 📁 Project Structure

```
local-rag-agent/
├── main.py              # Main application entry point
├── config.py           # Configuration management
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
├── logs/              # Application logs
└── utils/
    ├── logger.py      # Logging configuration
    ├── vector_store.py # Vector store setup
    └── knowledge_base.py # Knowledge base management
```

## 🔧 Configuration

The application can be configured through environment variables or the `.env` file:

- `APP_NAME`: Application name
- `DEBUG`: Debug mode (True/False)
- `HOST`: Server host
- `PORT`: Server port
- `MODEL_NAME`: Ollama model name
- `EMBEDDER_MODEL`: Embedding model name
- `COLLECTION_NAME`: Qdrant collection name
- `QDRANT_URL`: Qdrant server URL
- `PDF_URLS`: List of PDF URLs to process

## 📝 Logging

Logs are stored in the `logs` directory with rotation enabled:
- Maximum file size: 10MB
- Backup count: 5 files
- Format: timestamp - name - level - message

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. 