from typing import List

from pydantic import BaseModel, ConfigDict



class ImportedGeometry(BaseModel):
    """Data from importing the files"""

    id: str

    value: List[str]

    model_config = ConfigDict(protected_namespaces=())
