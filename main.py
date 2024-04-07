from fastapi import FastAPI
from schemas import User

app = FastAPI()

@app.get("/register")
def register():
    user1 = User(nickname="Lena", password="123")
    return {"user":user1}