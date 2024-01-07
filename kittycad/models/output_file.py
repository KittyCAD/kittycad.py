from typing import Optional

from pydantic import BaseModel, ConfigDict



class OutputFile(BaseModel):
    """Output file contents."""

    contents: Optional[str] = None

    name: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
