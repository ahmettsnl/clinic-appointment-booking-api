from pydantic import BaseModel

from pydantic import BaseModel, Field

class AppointmentTypeCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)

    duration_minutes: int = Field(
        ...,
        ge=5,
        le=180
    )

    buffer_minutes: int = Field(
        ...,
        ge=0,
        le=60
    )

class AppointmentTypeResponse(BaseModel):
    id: int
    name: str
    duration_minutes: int
    buffer_minutes: int
    price: int

    class Config:
        from_attributes = True