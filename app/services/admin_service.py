from sqlalchemy.orm import Session
from app.models.salon_model import Salon

def create_salon(db: Session, salon):
    new_salon = Salon(**salon.dict())
    db.add(new_salon)
    db.commit()
    db.refresh(new_salon)
    return new_salon

def get_salon(db: Session):
    salon = db.query(Salon).all()
    return salon