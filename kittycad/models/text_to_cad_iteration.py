import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_call_status import ApiCallStatus
from ..models.ml_feedback import MlFeedback
from ..models.source_range_prompt import SourceRangePrompt
from ..models.text_to_cad_model import TextToCadModel
from ..models.uuid import Uuid


class TextToCadIteration(BaseModel):
    """A response from a text to CAD iteration."""

    code: str

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[MlFeedback] = None

    id: Uuid

    model: TextToCadModel

    model_version: str

    original_source_code: str

    prompt: Optional[str] = None

    source_ranges: List[SourceRangePrompt]

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
