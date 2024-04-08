from fastapi import FastAPI
from src.users.router import router as users_router
from src.collars.router import router as collars_router
#from src.community.router import router as community_router

app = FastAPI()
app.include_router(users_router)
app.include_router(collars_router)
#app.include_router(community_router)



