from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine, Base
from app.appointments.models import Appointment

from app.appointments.routes import router as appointment_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(appointment_router)

@app.get("/health")
def health_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "DB connected"}
