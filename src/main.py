from fastapi import FastAPI
from src.users.schemas import User
from src.users.router import router as users_router
from src.database import BaseDBModel, engine

app = FastAPI()
app.include_router(users_router)

BaseDBModel.metadata.create_all(bind=engine)

