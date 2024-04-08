from fastapi import APIRouter
from src.collars.schemas import collar

router = APIRouter(prefix="/collars")

@router.get("/get_cords")
def cords(uuid, collar_id):
    #   get cords
    return {"last_coord": "23455"}





