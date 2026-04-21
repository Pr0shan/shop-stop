from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.get("/")
def healthcheck():
    return {
        "environment": settings.environment,
        "debug": settings.debug,
        "version": settings.version,
        "service": settings.service
    }

