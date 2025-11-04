from typing import Dict, List, Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.ml_copilot_mode import MlCopilotMode
from ..models.ml_copilot_supported_models import MlCopilotSupportedModels
from ..models.ml_copilot_system_command import MlCopilotSystemCommand
from ..models.ml_copilot_tool import MlCopilotTool
from ..models.ml_reasoning_effort import MlReasoningEffort
from ..models.source_range_prompt import SourceRangePrompt
from .base import KittyCadBaseModel


class OptionHeaders(KittyCadBaseModel):
    """Authentication header request."""

    headers: Dict[str, str]

    type: Literal["headers"] = "headers"


class OptionUser(KittyCadBaseModel):
    """The user message, which contains the content of the user's input."""

    content: str

    current_files: Optional[Dict[str, bytes]] = None

    forced_tools: Optional[List[MlCopilotTool]] = None

    mode: Optional[MlCopilotMode] = None

    model: Optional[MlCopilotSupportedModels] = None

    project_name: Optional[str] = None

    reasoning_effort: Optional[MlReasoningEffort] = None

    source_ranges: Optional[List[SourceRangePrompt]] = None

    type: Literal["user"] = "user"


class OptionSystem(KittyCadBaseModel):
    """The system message, which can be used to set the context or instructions for the AI."""

    command: MlCopilotSystemCommand

    type: Literal["system"] = "system"


MlCopilotClientMessage = RootModel[
    Annotated[
        Union[
            OptionHeaders,
            OptionUser,
            OptionSystem,
        ],
        Field(discriminator="type"),
    ]
]
