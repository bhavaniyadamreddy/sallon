from sqlalchemy import Column, Integer, ForeignKey, Date, Time, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class Slot(Base):
    __tablename__ = "slot"

    id = Column(Integer, primary_key=True, index=True)
    barber_id = Column(Integer, ForeignKey("barber.id"))

    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    status = Column(String(50), default="available")

    created_at = Column(DateTime(timezone=True), server_default=func.now())