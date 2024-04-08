from pydantic import BaseModel
#   FastAPI objects


class User(BaseModel):
    nickname: str
    password: str
    number: str
    superuser: bool


class UserAuth(BaseModel):
    number: str
    password: str

