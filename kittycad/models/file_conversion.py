import datetime
from typing import Dict, Optional

from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.file_import_format import FileImportFormat
from ..models.input_format3d import InputFormat3d
from ..models.output_format3d import OutputFormat3d
from ..models.uuid import Uuid
from .base import KittyCadBaseModel
from .base64data import Base64Data


class FileConversion(KittyCadBaseModel):
    """A file conversion."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_format: FileExportFormat

    output_format_options: Optional[OutputFormat3d] = None

    outputs: Optional[Dict[str, Base64Data]] = None

    src_format: FileImportFormat

    src_format_options: Optional[InputFormat3d] = None

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid
