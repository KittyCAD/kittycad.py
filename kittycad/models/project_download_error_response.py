from typing import List, Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectDownloadErrorResponse(KittyCadBaseModel):
    """Error returned when project download query parameters are invalid."""

    error_code: Optional[str] = None

    message: str

    missing_file_ids: Optional[List[Uuid]] = None

    request_id: str
