from fastapi import APIRouter, Depends
from src.users.models import UsersSessions, Users
import uuid
from src.database import DBSession
from src.collars.crud import create_collar
from typing import Annotated
from src.collars.models import Collars


router = APIRouter(prefix="/user/collars")


@router.post("/new_collar")
def new_collar(token, mac):
    access = DBSession.query(UsersSessions).filter_by(token=token).one()
    is_admin = DBSession.query(Users).filter_by(id=access.id).one()
    is_admin = is_admin.is_superuser

    if (is_admin):
        create_collar(DBSession, mac)
        return {'access': 'yes'}
    else:
        return {'access': 'no'}

@router.post("/add_collar")
def add_collar(collar_id, user_id):
    access = DBSession.query(UsersSessions).filter_by(token=token).one()
