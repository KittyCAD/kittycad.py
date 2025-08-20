import datetime
from typing import Dict, List, Optional

from ..models.api_call_status import ApiCallStatus
from ..models.ml_feedback import MlFeedback
from ..models.source_range_prompt import SourceRangePrompt
from ..models.text_to_cad_model import TextToCadModel
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class TextToCadMultiFileIteration(KittyCadBaseModel):
    """A response from a text to CAD multi-file iteration."""

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Uuid

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[MlFeedback] = None

    id: Uuid

    kcl_version: Optional[str] = None

    model: TextToCadModel

    model_version: str

    outputs: Optional[Dict[str, str]] = None

    project_name: Optional[str] = None

    prompt: Optional[str] = None

    source_ranges: List[SourceRangePrompt]

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid
