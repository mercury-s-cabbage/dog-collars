from sqlalchemy import (Integer, String, Boolean, Column)
from src.database import BaseDBModel, engine


class Collars(BaseDBModel):   # string of users' table
    __tablename__ = "collars"

    id = Column(Integer, primary_key=True, index=True)
    mac = Column(String, unique=True, index=False)
    is_active = Column(Boolean, unique=False, index=False)

BaseDBModel.metadata.create_all(bind=engine)
