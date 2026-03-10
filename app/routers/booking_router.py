from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.booking_schema import BookingCreate
from app.services.booking_service import create_booking
from app.services.booking_service import get_user_booking
from app.services.booking_service import delete_booking
from app.services.booking_service import get_all_booking
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/booking")
def book_service(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db, booking)

@router.get("/users/{user_id}/booking")
def fetch_user_booking(user_id: int, db: Session = Depends(get_db)):
    return get_user_booking(db, user_id)

@router.delete("/booking/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    return delete_booking(db, booking_id)

@router.get("/booking")
def fetch_all_booking(db: Session = Depends(get_db)):
    return get_all_booking(db)