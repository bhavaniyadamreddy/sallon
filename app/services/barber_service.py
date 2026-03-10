from sqlalchemy.orm import Session
from app.models.barber_model import Barber
from app.models.slot_model import Slot

def create_barber(db: Session, barber):
    new_barber = Barber(**barber.dict())
    db.add(new_barber)
    db.commit()
    db.refresh(new_barber)
    return new_barber

def get_barber_by_salon(db: Session, salon_id: int):
    barber = db.query(Barber).filter(Barber.salon_id == salon_id).all()
    return barber

def create_slot(db, slot):
    new_slot = Slot(**slot.dict())
    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)
    return new_slot


def get_slot_by_barber(db, barber_id: int):
    slots = db.query(Slot).filter(Slot.barber_id == barber_id).all()
    return slots

def update_barber(db, barber_id: int, barber):

    existing_barber = db.query(Barber).filter(Barber.id == barber_id).first()

    existing_barber.name = barber.name
    existing_barber.phone = barber.phone
    existing_barber.specialization = barber.specialization

    db.commit()
    db.refresh(existing_barber)

    return existing_barber

