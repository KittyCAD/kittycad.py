
from pydantic import BaseModel, ConfigDict



class TextToCadCreateBody(BaseModel):
    """Body for generating models from text."""

    prompt: str

    model_config = ConfigDict(protected_namespaces=())
