from pydantic import BaseModel
class collar(BaseModel):
    id: int
    mac: str
    is_active: bool
