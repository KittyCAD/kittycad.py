
from pydantic import BaseModel



class RawFile(BaseModel):
    """A raw file with unencoded contents to be passed over binary websockets."""

    contents: bytes

    name: str
