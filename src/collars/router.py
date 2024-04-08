from fastapi import APIRouter, Depends
from src.users.models import UsersSessions, Users
import uuid
from src.database import DBSession
import src.collars.crud as crud
from typing import Annotated
from src.collars.models import Collars


router = APIRouter(prefix="/user/collars")


@router.post("/new_collar")
def new_collar(token, mac):
    access = DBSession.query(UsersSessions).filter_by(token=token).one()
    is_admin = DBSession.query(Users).filter_by(id=access.id).one()
    is_admin = is_admin.is_superuser

    if (is_admin):
        crud.create_collar(DBSession, mac)
        return {'access': 'yes'}
    else:
        return {'access': 'no'}

@router.post("/add_collar")
def add_collar(collar_id, token):
    access = DBSession.query(UsersSessions).filter_by(token=token).one()
    user_id = access.id
    crud.add_me_collar(DBSession, user_id, collar_id)
    return {"access": "True"}

@router.post("/remove_collar")
def remove_my_collar(collar_id, token):
    access = DBSession.query(UsersSessions).filter_by(token=token).one()
    user_id = access.id
    crud.remove_collar(DBSession, user_id, collar_id)
    return {"access": "True"}

@router.get("/my_collars")
def my_collars(token):
    access = DBSession.query(UsersSessions).filter_by(token=token).one()
    user_id = access.id
    return crud.collar_group(DBSession, user_id)

@router.post("/delete_collar")
def delete_collar(collar_id, token):
    access = DBSession.query(UsersSessions).filter_by(token=token).one()
    is_admin = DBSession.query(Users).filter_by(id=access.id).one()
    is_admin = is_admin.is_superuser

    if (is_admin):
        crud.delete_collar(DBSession, collar_id)
        return {'access': 'yes'}
    else:
        return {'access': 'no'}


