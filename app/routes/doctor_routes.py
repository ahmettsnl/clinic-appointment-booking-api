from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.doctor import Doctor
from app.schemas.doctor_schema import DoctorCreate, DoctorResponse

router = APIRouter()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create doctor
@router.post("/doctors", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    new_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        email=doctor.email,
        phone=doctor.phone
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor

# Get all doctors
@router.get("/doctors", response_model=list[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    doctors = db.query(Doctor).all()
    return doctors