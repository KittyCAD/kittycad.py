from typing import Optional

from .base import KittyCadBaseModel


class AppClientInfo(KittyCadBaseModel):
    """Information about a third party app client."""

    url: Optional[str] = None
