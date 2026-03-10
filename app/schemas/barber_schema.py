from pydantic import BaseModel

class BarberCreate(BaseModel):
    name: str
    phone: str
    specialization: str
    salon_id: int
    password: str