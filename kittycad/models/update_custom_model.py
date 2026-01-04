from typing import Optional

from .base import KittyCadBaseModel


class UpdateCustomModel(KittyCadBaseModel):
    """Body for updating a custom ML model."""

    name: Optional[str] = None

    system_prompt: Optional[str] = None
