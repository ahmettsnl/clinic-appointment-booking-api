from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.appointment_type import AppointmentType
from app.schemas.appointment_type_schema import (
    AppointmentTypeCreate,
    AppointmentTypeResponse
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/appointment-types", response_model=AppointmentTypeResponse)
def create_appointment_type(
    appointment_type: AppointmentTypeCreate,
    db: Session = Depends(get_db)
):
    new_type = AppointmentType(
        name=appointment_type.name,
        duration_minutes=appointment_type.duration_minutes,
        buffer_minutes=appointment_type.buffer_minutes,
        price=appointment_type.price
    )

    db.add(new_type)
    db.commit()
    db.refresh(new_type)

    return new_type

@router.get("/appointment-types", response_model=list[AppointmentTypeResponse])
def get_appointment_types(db: Session = Depends(get_db)):
    return db.query(AppointmentType).all()