from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class Barber(Base):
    __tablename__ = "barber"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    specialization = Column(String(100))
    salon_id = Column(Integer, ForeignKey("salon.id"))
    password = Column(String(255), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())