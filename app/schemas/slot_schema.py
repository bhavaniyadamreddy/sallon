from pydantic import BaseModel
from datetime import date, time

class SlotCreate(BaseModel):
    barber_id: int
    date: date
    start_time: time
    end_time: time