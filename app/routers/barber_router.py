from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.barber_schema import BarberCreate
from app.services.barber_service import create_barber
from app.schemas.slot_schema import SlotCreate
from app.services.barber_service import create_slot
from app.services.barber_service import get_slot_by_barber
from app.services.barber_service import get_barber_by_salon
from app.services.barber_service import update_barber


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admin/barber")
def add_barber(barber: BarberCreate, db: Session = Depends(get_db)):
    return create_barber(db, barber)

@router.get("/salon/{salon_id}/barber")
def get_barber(salon_id: int, db: Session = Depends(get_db)):
    return get_barber_by_salon(db, salon_id)

@router.post("/slot")
def add_slot(slot: SlotCreate, db: Session = Depends(get_db)):
    return create_slot(db, slot)

@router.get("/barber/{barber_id}/slot")
def get_slot(barber_id: int, db: Session = Depends(get_db)):
    return get_slot_by_barber(db, barber_id)

@router.put("/barber/{barber_id}")
def edit_barber(barber_id: int, barber: BarberCreate, db: Session = Depends(get_db)):
    return update_barber(db, barber_id, barber)

