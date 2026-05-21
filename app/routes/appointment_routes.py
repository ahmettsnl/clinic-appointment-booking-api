from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from app.services.slot_service import generate_slots

from app.database.database import SessionLocal
from app.models.appointment import Appointment
from app.models.appointment_type import AppointmentType
from app.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentResponse
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/appointments", response_model=AppointmentResponse)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):
    appointment_type = db.query(AppointmentType).filter(
        AppointmentType.id == appointment.appointment_type_id
    ).first()

    if not appointment_type:
        raise HTTPException(status_code=404, detail="Appointment type not found")

        duration = appointment_type.duration_minutes
        buffer_time = appointment_type.buffer_minutes

        calculated_end_time = (
            appointment.start_time +
            timedelta(minutes=duration + buffer_time)
        )

        existing_appointment = db.query(Appointment).filter(
            Appointment.doctor_id == appointment.doctor_id,
            Appointment.start_time < calculated_end_time,
            Appointment.end_time > appointment.start_time,
            Appointment.status != "cancelled"
        ).first()

        if existing_appointment:
            raise HTTPException(
                status_code=400,
                detail="This time slot is already booked"
        )

    new_appointment = Appointment(
        doctor_id=appointment.doctor_id,
        patient_id=appointment.patient_id,
        appointment_type_id=appointment.appointment_type_id,
        start_time=appointment.start_time,
        end_time=calculated_end_time,
        status="scheduled"
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment

@router.get("/doctors/{doctor_id}/slots")
def get_available_slots(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    all_slots = generate_slots()

    appointments = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_id
    ).all()

    booked_slots = [
        appointment.start_time.strftime("%H:%M")
        for appointment in appointments
    ]

    available_slots = [
        slot for slot in all_slots
        if slot not in booked_slots
    ]

    return {
        "doctor_id": doctor_id,
        "available_slots": available_slots
    }

@router.get("/appointments", response_model=list[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()


@router.get("/appointments/{appointment_id}", response_model=AppointmentResponse)
def get_appointment_by_id(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment


@router.patch("/appointments/{appointment_id}/status", response_model=AppointmentResponse)
def update_appointment_status(
    appointment_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    allowed_statuses = ["scheduled", "confirmed", "completed", "cancelled"]

    if status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid appointment status"
        )

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    appointment.status = status

    db.commit()
    db.refresh(appointment)

    return appointment