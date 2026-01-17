from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine

app = FastAPI(title="TrailLog API", version="0.1.0")


@app.on_event("startup")
def startup_db_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))


@app.get("/health")
def health():
    return {"status": "ok"}
