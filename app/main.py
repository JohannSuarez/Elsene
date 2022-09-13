from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app import Configs
from .routers import yt2mp3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(yt2mp3.router)
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

'''
@app.get("/")
async def root():
    return {"message": "Health check, yeah we're up!"}

'''
