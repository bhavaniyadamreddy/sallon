from sqlalchemy.orm import Session
from app.models.service_model import Service

def create_service(db: Session, service):
    new_service = Service(**service.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service


def get_services_by_salon(db, salon_id: int):
    return db.query(Service).filter(Service.salon_id == salon_id).all()