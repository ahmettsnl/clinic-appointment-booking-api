from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from app.database.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    doctor_id = Column(Integer, nullable=False)
    patient_id = Column(Integer, nullable=False)
    appointment_type_id = Column(Integer, nullable=False)

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    status = Column(String, default="scheduled")