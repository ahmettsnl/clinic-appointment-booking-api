from pydantic import BaseModel

class AppointmentTypeCreate(BaseModel):
    name: str
    duration_minutes: int
    buffer_minutes: int
    price: int

class AppointmentTypeResponse(BaseModel):
    id: int
    name: str
    duration_minutes: int
    buffer_minutes: int
    price: int

    class Config:
        from_attributes = True