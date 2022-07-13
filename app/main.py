from fastapi import FastAPI
from .sampackage.pack import sayHi
from .schemas.convert_request import ConversionRequest

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/convert")
async def mail(request: ConversionRequest):
    """
    Steps:
        Verify schema with Pydantic
        Call wrapper around youtube-dl
        If no immediate error, return JSON reply indicating that
        conversion is being processed
    """

    return {"message": "Mail path invoked"}
