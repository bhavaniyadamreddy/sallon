from pydantic import BaseModel

class BookingCreate(BaseModel):
    user_id: int
    salon_id: int
    barber_id: int
    slot_id: int
    service: str