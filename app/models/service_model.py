from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    salon_id = Column(Integer, ForeignKey("salon.id"))
    service_name = Column(String(100))
    price = Column(Integer)
    duration = Column(Integer)