
from pydantic import BaseModel, ConfigDict



class SourcePosition(BaseModel):
    """A position in the source code."""

    column: int

    line: int

    model_config = ConfigDict(protected_namespaces=())
