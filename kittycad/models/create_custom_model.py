from typing import List, Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class CreateCustomModel(KittyCadBaseModel):
    """Body for creating a custom ML model."""

    dataset_ids: List[Uuid]

    name: str

    system_prompt: Optional[str] = None
