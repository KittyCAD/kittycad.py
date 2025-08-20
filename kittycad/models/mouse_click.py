from typing import List

from .base import KittyCadBaseModel


class MouseClick(KittyCadBaseModel):
    """The response from the `MouseClick` command."""

    entities_modified: List[str]

    entities_selected: List[str]
