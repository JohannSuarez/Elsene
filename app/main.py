from fastapi import FastAPI, HTTPException
from .sampackage.pack import sayHi
from .schemas.convert_request import ConversionRequest
from .converter.ytdl import Converter
from subprocess import TimeoutExpired

import time

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/convert", status_code=200)
async def mail(request: ConversionRequest):
    """
    Steps:
        Verify schema with Pydantic
        Call wrapper around youtube-dl
        If no immediate error, return JSON reply indicating that
        conversion is being processed
    """

    # Call converter, give it the requests youtube-url
    cnv = Converter()
    proc = cnv.convert(request.yt_url)

    try:
        # We just need to determine whether the process lives long enough.
        _, _ = proc.communicate(timeout=0.5)
    except TimeoutExpired:
        # If the process is still running after 0.5 seconds,
        # youtube-dl must have taken a valid yt-url string
        return {"message": "Conversion process started. Please check e-mail after 5 mins"}

    return {"error": "Conversion failed"}
