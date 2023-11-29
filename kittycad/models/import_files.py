
from pydantic import BaseModel



class ImportFiles(BaseModel):
    """Data from importing the files"""

    object_id: str
