from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "Local RAG Agent"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Model settings
    MODEL_NAME: str = "llama3.2"
    EMBEDDER_MODEL: str = "openhermes"
    
    # Vector store settings
    COLLECTION_NAME: str = "document-index"
    QDRANT_URL: str = "http://localhost:6333/"
    
    # Knowledge base settings
    PDF_URLS: List[str] = [
        "https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"
    ]
    
    class Config:
        env_file = ".env"

settings = Settings() 