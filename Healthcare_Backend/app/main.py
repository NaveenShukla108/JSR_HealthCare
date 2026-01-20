from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine, Base
from app.appointments.models import Appointment

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "DB connected"}
