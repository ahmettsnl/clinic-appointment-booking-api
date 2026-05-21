from sqlalchemy import Column, Integer, String
from app.database.database import Base

class AppointmentType(Base):
    __tablename__ = "appointment_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    buffer_minutes = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)