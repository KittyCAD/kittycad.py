
from pydantic import BaseModel, ConfigDict



class ImportFiles(BaseModel):
    """Data from importing the files"""

    object_id: str

    model_config = ConfigDict(protected_namespaces=())
