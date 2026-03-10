from fastapi import FastAPI
from app.database.database import Base, engine

# import models
from app.models import user_model, admin_model, salon_model, barber_model, slot_model, booking_model

# import routers
from app.routers import user_router, admin_router, barber_router, booking_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

# include routers
app.include_router(user_router.router)
app.include_router(admin_router.router)
app.include_router(barber_router.router)
app.include_router(booking_router.router)