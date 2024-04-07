from sqlalchemy import (Integer, String, Bool,Column)
from src.database import BaseDBModel


class Users(BaseDBModel):   # string of users' table
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, index=False)
    number = Column(String, unique=True, index=False)
    hash_password = Column(String, unique=False, index=False)
    is_active = Column(Bool, default=True)

