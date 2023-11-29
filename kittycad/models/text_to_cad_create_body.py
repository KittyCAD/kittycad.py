
from pydantic import BaseModel



class TextToCadCreateBody(BaseModel):
    """Body for generating models from text."""

    prompt: str
