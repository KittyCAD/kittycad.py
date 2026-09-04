from typing import Dict, Optional

from ..models.attachment_ref import AttachmentRef
from .base import KittyCadBaseModel


class MlCopilotFile(KittyCadBaseModel):
    """A file that can be transferred between the client and server."""

    attachment_ref: Optional[AttachmentRef] = None

    data: bytes

    data_ref: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    mimetype: str

    name: str
