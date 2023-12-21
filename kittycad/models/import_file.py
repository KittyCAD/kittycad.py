
from pydantic import BaseModel



class ImportFile(BaseModel):
    """File to import into the current model If you are sending binary data for a file, be sure to send the WebSocketRequest as binary/bson, not text/json."""

    data: bytes

    path: str
