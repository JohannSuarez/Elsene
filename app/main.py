from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
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

app.mount(
        "/static", 
        StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), 
        name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
            "index.html",
            {"request": request}
    )
