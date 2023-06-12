import asyncio
import time
from fastapi import APIRouter, Response, WebSocket
from app import ConversionQueue
from ..schemas.convert_request import ConversionRequest
from ..converter.ytdl import Converter
from ..utils.random_string_generator import generate
from subprocess import Popen, TimeoutExpired, PIPE, STDOUT

import threading

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # assuming the bash script outputs progress as percentage
    subprocess = Popen(['bash', 'split_and_zip.sh'], stdout=PIPE, stderr=STDOUT)
    while subprocess.poll() is None:
        output = subprocess.stdout.readline() # type: ignore
        if output == '':
            break
        if output:
            progress = output.strip().decode('utf-8')
            await websocket.send_json({"progress": progress})
            print("Sent!")
            await asyncio.sleep(1) # non-blocking delay
        
    # send final progress update
    await websocket.send_json({"progress": 100})

@router.post("/convert", status_code=200)
async def convert(request: ConversionRequest, response: Response):
    """
    Steps:
        Verify schema with Pydantic
        Call wrapper around youtube-dl
        If no immediate error, return JSON reply indicating that
        conversion is being processed
    """

    # Call converter, give it the requests youtube-url
    cnv = Converter()
    output_name_salt: str = generate(length=5)
    proc = cnv.convert(request.yt_url, output_name_salt)

    try:
        # We just need to determine whether the process lives long enough.
        _, _ = proc.communicate(timeout=0.5)
    except TimeoutExpired:
        # If the process is still running after 0.5 seconds,
        # youtube-dl must have taken a valid yt-url string

        # The conversion commences, we keep a track of it in our singleton.
        ConversionQueue.push(dict(request), output_name_salt)

        # Return the proc to follow_up, where it will wait for the process to end.
        # Once it does. It commences e-mailing
        follow_up_thread = threading.Thread(target=cnv.follow_up, args=[proc])
        follow_up_thread.start()

        return {"message": "Conversion process started. Please check e-mail after 5 mins"}

    response.status_code = 400
    return {"error": "Conversion failed"}
