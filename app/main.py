from fastapi import FastAPI

from app.database.database import engine, Base
from app.models.doctor import Doctor
from app.routes.doctor_routes import router as doctor_router
from app.models.appointment_type import AppointmentType
from app.routes.appointment_type_routes import router as appointment_type_router
from app.models.appointment import Appointment
from app.routes.appointment_routes import router as appointment_router
from app.routes.patient_record_routes import router as patient_record_router
from fastapi.middleware.cors import CORSMiddleware
from app.models.user import User
from app.routes.auth_routes import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(doctor_router)
app.include_router(appointment_type_router)
app.include_router(appointment_router)
app.include_router(patient_record_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Clinic Appointment Booking API"}