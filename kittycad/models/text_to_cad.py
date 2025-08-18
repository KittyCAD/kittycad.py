import datetime
from typing import Dict, Optional

from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.ml_feedback import MlFeedback
from ..models.text_to_cad_model import TextToCadModel
from ..models.uuid import Uuid
from .base import KittyCadBaseModel
from .base64data import Base64Data


class TextToCad(KittyCadBaseModel):
    """A response from a text to CAD prompt."""

    code: Optional[str] = None

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Uuid

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[MlFeedback] = None

    id: Uuid

    kcl_version: Optional[str] = None

    model: TextToCadModel

    model_version: str

    output_format: FileExportFormat

    outputs: Optional[Dict[str, Base64Data]] = None

    prompt: str

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid
