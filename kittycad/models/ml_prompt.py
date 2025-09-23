import datetime
from typing import Optional

from ..models.api_call_status import ApiCallStatus
from ..models.ml_feedback import MlFeedback
from ..models.ml_prompt_metadata import MlPromptMetadata
from ..models.ml_prompt_type import MlPromptType
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class MlPrompt(KittyCadBaseModel):
    """A ML prompt."""

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Optional[Uuid] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[MlFeedback] = None

    id: Uuid

    kcl_version: Optional[str] = None

    metadata: Optional[MlPromptMetadata] = None

    model_version: str

    output_file: Optional[str] = None

    project_name: Optional[str] = None

    prompt: str

    seconds: Optional[int] = None

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: MlPromptType

    updated_at: datetime.datetime

    user_id: Uuid
