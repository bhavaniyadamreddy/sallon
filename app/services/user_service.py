from sqlalchemy.orm import Session
from app.models.user_model import User

def create_user(db: Session, user):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user