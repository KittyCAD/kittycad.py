from typing import Optional

from pydantic import BaseModel, ConfigDict


class TextToCadCreateBody(BaseModel):
    """Body for generating models from text."""

    kcl_version: Optional[str] = None

    project_name: Optional[str] = None

    prompt: str

    model_config = ConfigDict(protected_namespaces=())
