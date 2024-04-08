from fastapi import APIRouter, Depends
from src.users.schemas import User, UserAuth
from src.users.models import Users as db_user
import uuid
from src.users.crud import create_user, create_user_session
from src.database import DBSession
from typing import Annotated

#router = APIRouter(prefix="/user/community")

#@router.post("/add_task")
#def add_task(token, collar_id):



