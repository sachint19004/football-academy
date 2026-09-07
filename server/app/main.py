from fastapi import FastAPI

from app.database import db

app = FastAPI(title="Football Academy API")


@app.get("/")
def root():
    return {"message": "Football Academy API is running"}


@app.get("/health")
def health():
    try:
        db.command("ping")
        return {"status": "healthy", "database": "connected"}
    except Exception:
        return {"status": "unhealthy", "database": "disconnected"}