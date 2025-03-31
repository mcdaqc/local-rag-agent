from fastapi import FastAPI
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.qdrant import Qdrant
from agno.embedder.ollama import OllamaEmbedder
from agno.playground import Playground, serve_playground_app
from config import settings
from utils.logger import setup_logger
from utils.vector_store import setup_vector_store
from utils.knowledge_base import setup_knowledge_base

# Setup logging
logger = setup_logger()

# Initialize FastAPI app
app = FastAPI(
    title="Local RAG Agent API",
    description="A local RAG implementation using Llama 3.2 and Qdrant",
    version="1.0.0"
)

# Setup vector store
vector_db = setup_vector_store()

# Setup knowledge base
knowledge_base = setup_knowledge_base(vector_db)

# Create the Agent
agent = Agent(
    name="Local RAG Agent",
    model=Ollama(id=settings.MODEL_NAME),
    knowledge=knowledge_base,
)

# Create playground app
playground_app = Playground(agents=[agent]).get_app()

# Mount the playground app
app.mount("/playground", playground_app)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Local RAG Agent API",
        "version": "1.0.0",
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    ) 