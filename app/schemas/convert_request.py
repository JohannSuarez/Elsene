from pydantic import BaseModel

class ConversionRequest(BaseModel):
    yt_url: str
    recipient: str

    class Config:
        schema_extra = {
            "example": {
                "yt_url": "https://www.youtube.com/watch?v=lrbL1s9qwBs",
                "recipient": "juandelacruz@email.com"
            }
        }
