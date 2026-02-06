from typing import Dict, Optional

from .base import KittyCadBaseModel


class MlCopilotFile(KittyCadBaseModel):
    """A file that can be transferred between the client and server."""

    data: bytes

    metadata: Optional[Dict[str, str]] = None

    mimetype: str

    name: str
