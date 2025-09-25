from typing import Optional

from .base import KittyCadBaseModel


class TextToCadCreateBody(KittyCadBaseModel):
    """Body for generating parts from text."""

    kcl_version: Optional[str] = None

    model_version: Optional[str] = None

    project_name: Optional[str] = None

    prompt: str
