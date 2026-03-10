from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class Salon(Base):
    __tablename__ = "salon"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(15), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())