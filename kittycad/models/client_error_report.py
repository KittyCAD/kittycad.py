from typing import Optional

from .base import KittyCadBaseModel


class ClientErrorReport(KittyCadBaseModel):
    """Structured client-side error report sent by authenticated clients."""

    client: str

    code: Optional[str] = None

    error_name: Optional[str] = None

    message: str

    release: str

    route: Optional[str] = None

    stack: Optional[str] = None
