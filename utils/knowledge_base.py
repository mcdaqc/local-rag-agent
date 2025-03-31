from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from config import settings
from utils.logger import setup_logger

logger = setup_logger()

def setup_knowledge_base(vector_db):
    """
    Initialize and configure the knowledge base with PDF documents
    """
    try:
        knowledge_base = PDFUrlKnowledgeBase(
            urls=settings.PDF_URLS,
            vector_db=vector_db,
        )
        
        # Load the knowledge base
        logger.info("Loading knowledge base...")
        knowledge_base.load(recreate=True, upsert=True)
        logger.info("Knowledge base loaded successfully")
        
        return knowledge_base
    except Exception as e:
        logger.error(f"Failed to initialize knowledge base: {str(e)}")
        raise 