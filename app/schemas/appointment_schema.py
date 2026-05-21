from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_type_id: int
    start_time: datetime

class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    appointment_type_id: int
    start_time: datetime
    end_time: datetime
    status: str

    class Config:
        from_attributes = True