import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

__version__ = '1.0'
__service_name__ = "shop-stop"

def get_db_settings():
    return {
        "ECHO": True
    }

class Settings(BaseSettings):

    api_key:str = os.getenv("API_KEY", 'test-key-1234')
    environment:str = os.getenv("ENVIRONMENT", "development")
    debug:bool = environment == "development"
    version:str = __version__
    service:str = __service_name__
    
    DATABASE_URL:str|None = os.getenv('DATABASE_URL')
    DB_SETTINGS:dict = get_db_settings()

    class Config:
        env_file = ".env"

settings = Settings()