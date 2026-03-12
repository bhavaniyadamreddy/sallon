from pydantic import BaseModel

class ServiceCreate(BaseModel):
    salon_id: int
    service_name: str
    price: int
    duration: int