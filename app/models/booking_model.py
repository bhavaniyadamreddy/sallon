from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    salon_id = Column(Integer, ForeignKey("salon.id"))
    barber_id = Column(Integer, ForeignKey("barber.id"))
    slot_id = Column(Integer, ForeignKey("slot.id"))

    service = Column(String(100))
    booking_status = Column(String(50), default="booked")

    created_at = Column(DateTime(timezone=True), server_default=func.now())