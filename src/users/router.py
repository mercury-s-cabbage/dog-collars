from fastapi import APIRouter
from src.users.schemas import User
import uuid
from src.users.crud import create_user
from src.database import DBSession


router = APIRouter(prefix="/users")


@router.post("/register")
def new_user(nickname, number, password):
    user_new = User(nickname=nickname, number=number, password=password)
    create_user(DBSession, user_new)
    #   saving to database
    return {"user": user_new}

@router.post("/auth")
def user_auth(number, password):
    #   checking database
    return {"uuid": uuid.uuid4()}

@router.post("/add_collar")
def add_collar(user_uuid, collar_number):
    #   make new connection
    return {"result": "ok"}



