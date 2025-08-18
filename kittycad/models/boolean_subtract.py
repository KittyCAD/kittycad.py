from typing import List, Optional

from .base import KittyCadBaseModel


class BooleanSubtract(KittyCadBaseModel):
    """The response from the 'BooleanSubtract'."""

    extra_solid_ids: Optional[List[str]] = None
