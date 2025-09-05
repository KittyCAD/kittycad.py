import datetime
from typing import Dict, List, Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.ml_feedback import MlFeedback
from ..models.source_range_prompt import SourceRangePrompt
from ..models.text_to_cad_model import TextToCadModel
from ..models.uuid import Uuid
from .base import KittyCadBaseModel
from .base64data import Base64Data


class OptionTextToCad(KittyCadBaseModel):
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

    type: Literal["text_to_cad"] = "text_to_cad"

    updated_at: datetime.datetime

    user_id: Uuid


class OptionTextToCadIteration(KittyCadBaseModel):
    """A response from a text to CAD iteration."""

    code: str

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Uuid

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

    type: Literal["text_to_cad_iteration"] = "text_to_cad_iteration"

    updated_at: datetime.datetime

    user_id: Uuid


class OptionTextToCadMultiFileIteration(KittyCadBaseModel):
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

    type: Literal["text_to_cad_multi_file_iteration"] = (
        "text_to_cad_multi_file_iteration"
    )

    updated_at: datetime.datetime

    user_id: Uuid


TextToCadResponse = RootModel[
    Annotated[
        Union[
            OptionTextToCad,
            OptionTextToCadIteration,
            OptionTextToCadMultiFileIteration,
        ],
        Field(discriminator="type"),
    ]
]
