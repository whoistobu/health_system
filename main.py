from fastapi import FastAPI
from database import Base, engine
from routes import router

# Database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Health System",
    description="Manages and stimulates health information for clients",
)

app.include_router(router)
