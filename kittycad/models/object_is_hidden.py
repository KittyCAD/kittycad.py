from typing import List

from ..models.hidden_state import HiddenState
from .base import KittyCadBaseModel


class ObjectIsHidden(KittyCadBaseModel):
    """The response from the `ObjectIsHidden` endpoint."""

    hidden: List[HiddenState]
