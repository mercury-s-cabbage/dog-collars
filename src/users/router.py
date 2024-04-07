from fastapi import APIRouter
from typing import Annotated
from src.users.schemas import User


router = APIRouter(prefix="/users")


@router.post("/register")
async def new_user(nickname, number, password):
    user_new = User(nickname=nickname, number=number, password=password)

    return {"user": user_new}


