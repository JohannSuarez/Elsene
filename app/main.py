from fastapi import FastAPI
from app import Configs
from .routers import yt2mp3

app = FastAPI()
app.include_router(yt2mp3.router)

@app.get("/")
async def root():
    return {"message": "Health check, yeah we're up!"}

