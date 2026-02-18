from .base import KittyCadBaseModel
from .base64data import Base64Data


class OrgDatasetSnapshotImage(KittyCadBaseModel):
    """Detailed response that bundles conversion metadata with the converted file contents."""

    data_base64: Base64Data

    mime_type: str
