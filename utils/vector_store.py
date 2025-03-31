from agno.vectordb.qdrant import Qdrant
from agno.embedder.ollama import OllamaEmbedder
from config import settings
from utils.logger import setup_logger

logger = setup_logger()

def setup_vector_store():
    """
    Initialize and configure the vector store (Qdrant)
    """
    try:
        vector_db = Qdrant(
            collection=settings.COLLECTION_NAME,
            url=settings.QDRANT_URL,
            embedder=OllamaEmbedder()
        )
        logger.info(f"Vector store initialized successfully at {settings.QDRANT_URL}")
        return vector_db
    except Exception as e:
        logger.error(f"Failed to initialize vector store: {str(e)}")
        raise 