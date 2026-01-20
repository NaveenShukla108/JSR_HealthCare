from sqlalchemy import (
    Column,
    Date, Time, DateTime,
    String, 
    Enum as sqlEnum
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from uuid import uuid4

from app.core.database import Base
from app.appointments.constants import AppointmentStatus


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    patient_id = Column(UUID(as_uuid=True), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), nullable=False)

    appointment_date =  Column(Date, nullable=True)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)

    status = Column(
        sqlEnum(AppointmentStatus), 
        default=AppointmentStatus.PENDING,
        nullable=False
    )

    reason = Column(String, nullable=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
        )
    
    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )