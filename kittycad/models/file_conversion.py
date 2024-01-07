import datetime
from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.file_import_format import FileImportFormat
from ..models.input_format import InputFormat
from ..models.output_format import OutputFormat
from ..models.uuid import Uuid
from .base64data import Base64Data


class FileConversion(BaseModel):
    """A file conversion."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    output_format: FileExportFormat

    output_format_options: Optional[OutputFormat] = None

    outputs: Optional[Dict[str, Base64Data]] = None

    src_format: FileImportFormat

    src_format_options: Optional[InputFormat] = None

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
