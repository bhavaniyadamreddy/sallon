from sqlalchemy.orm import Session
from app.models.booking_model import Booking

def create_booking(db: Session, booking):
    new_booking = Booking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def get_user_booking(db, user_id):
    booking = db.query(Booking).filter(Booking.user_id == user_id).all()
    return booking
    
def delete_booking(db, booking_id: int):

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    db.delete(booking)
    db.commit()

    return {"message": "Booking cancelled"}
   
def get_all_booking(db):

    bookings = db.query(Booking).all()

    return bookings