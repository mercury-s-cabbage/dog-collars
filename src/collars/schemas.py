from pydantic import BaseModel
class collar(BaseModel):
    id: int
    is_active: bool
