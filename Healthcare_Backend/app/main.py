from fastapi import FastAPI
from app.core.database import engine
from sqlalchemy import text

app = FastAPI()

@app.get("/health")
def health_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "DB connected"}
