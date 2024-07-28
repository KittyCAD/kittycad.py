import datetime
from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict

from ..models.ai_feedback import AiFeedback
from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.uuid import Uuid
from .base64data import Base64Data


class TextToCad(BaseModel):
    """A response from a text to CAD prompt."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[AiFeedback] = None

    id: Uuid

    model_version: str

    output_format: FileExportFormat

    outputs: Optional[Dict[str, Base64Data]] = None

    prompt: str

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
