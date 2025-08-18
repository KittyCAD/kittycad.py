from typing import Optional

from .base import KittyCadBaseModel


class TextToCadCreateBody(KittyCadBaseModel):
    """Body for generating models from text."""

    kcl_version: Optional[str] = None

    project_name: Optional[str] = None

    prompt: str
