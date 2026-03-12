from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.service_schema import ServiceCreate
from app.services.service_service import create_service, get_services_by_salon

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/service")
def add_service(service: ServiceCreate, db: Session = Depends(get_db)):
    return create_service(db, service)

@router.get("/salon/{salon_id}/services")
def get_services(salon_id: int, db: Session = Depends(get_db)):
    return get_services_by_salon(db, salon_id)