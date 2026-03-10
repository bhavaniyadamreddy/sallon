from pydantic import BaseModel

class SalonCreate(BaseModel):
    name: str
    address: str
    phone: str