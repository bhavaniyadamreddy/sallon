from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.salon_schema import SalonCreate
from app.services.admin_service import create_salon,get_salon

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admin/salon")
def add_salon(salon: SalonCreate, db: Session = Depends(get_db)):
    return create_salon(db, salon)
  
@router.get("/salon")
def fetch_salon(db: Session = Depends(get_db)):
    return get_salon(db)