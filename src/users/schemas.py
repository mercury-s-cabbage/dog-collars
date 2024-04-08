from pydantic import BaseModel
import uuid
#FastAPI objects
class User(BaseModel):
    nickname: str
    password: str
    number: str
    superuser: bool

class User_auth(BaseModel):
    number: str
    password: str



