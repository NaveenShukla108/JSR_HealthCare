from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.database import get_db
from app.appointments import schemas, models
from app.appointments.constants import AppointmentStatus

from app.core.security import CurrentUser, get_current_user
router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.post("/create", 
            response_model=schemas.AppointmentResponse,
            status_code=status.HTTP_201_CREATED 
            )
def create_appointment(
    payload: schemas.AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user)
):
    
    appointment = models.Appointment(
        patient_id=current_user.id,
        doctor_id=payload.doctor_id,
        reason = payload.reason,
        status=AppointmentStatus.PENDING
    )

    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment