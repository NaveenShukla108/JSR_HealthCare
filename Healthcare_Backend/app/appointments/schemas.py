from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date, time, datetime

from app.appointments.constants import AppointmentStatus



class AppointmentBase(BaseModel):
    doctor_id: UUID
    reason: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    pass 


class AppointmentSchedule(BaseModel):
    appointment_date: date
    start_time: time
    end_time: time


class AppointmentResponse(BaseModel):

    id: UUID
    doctor_id: UUID
    patient_id: UUID

    appointment_date: date
    start_time: time
    end_time: time

    status: AppointmentStatus
    reason: Optional[str]

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True