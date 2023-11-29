
from pydantic import BaseModel



class ImportFile(BaseModel):
    """File to import into the current model"""

    data: bytes

    path: str
