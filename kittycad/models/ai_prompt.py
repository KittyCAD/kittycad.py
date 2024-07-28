import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.ai_feedback import AiFeedback
from ..models.ai_prompt_type import AiPromptType
from ..models.api_call_status import ApiCallStatus
from ..models.uuid import Uuid
from .base64data import Base64Data


class AiPrompt(BaseModel):
    """An AI prompt."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    feedback: Optional[AiFeedback] = None

    id: Uuid

    metadata: Optional[Any] = None

    model_version: str

    output_file: Optional[str] = None

    prompt: str

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: AiPromptType

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
