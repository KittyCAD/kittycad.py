import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_call_status import ApiCallStatus
from ..models.ml_feedback import MlFeedback
from ..models.ml_prompt_metadata import MlPromptMetadata
from ..models.ml_prompt_type import MlPromptType
from ..models.uuid import Uuid


class MlPrompt(BaseModel):
    """A ML prompt."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[MlFeedback] = None

    id: Uuid

    metadata: Optional[MlPromptMetadata] = None

    model_version: str

    output_file: Optional[str] = None

    prompt: str

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: MlPromptType

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
