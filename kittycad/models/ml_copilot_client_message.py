from typing import Dict, List, Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.ml_copilot_file import MlCopilotFile
from ..models.ml_copilot_mode import MlCopilotMode
from ..models.ml_copilot_supported_models import MlCopilotSupportedModels
from ..models.ml_copilot_system_command import MlCopilotSystemCommand
from ..models.ml_copilot_tool import MlCopilotTool
from ..models.ml_reasoning_effort import MlReasoningEffort
from ..models.source_range_prompt import SourceRangePrompt
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OptionPing(KittyCadBaseModel):
    """The client-to-server Ping to ensure the copilot protocol stays alive."""

    type: Literal["ping"] = "ping"


class OptionListModes(KittyCadBaseModel):
    """Request available mode metadata for the copilot session."""

    type: Literal["list_modes"] = "list_modes"


class OptionHeaders(KittyCadBaseModel):
    """Authentication header request."""

    headers: Dict[str, str]

    type: Literal["headers"] = "headers"


class OptionProjectContext(KittyCadBaseModel):
    """Updates the active project context without creating a new prompt."""

    current_files: Optional[Dict[str, bytes]] = None

    project_name: Optional[str] = None

    type: Literal["project_context"] = "project_context"


class OptionUser(KittyCadBaseModel):
    """The user message, which contains the content of the user's input."""

    additional_files: Optional[List[MlCopilotFile]] = None

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


class OptionAttachmentResponse(KittyCadBaseModel):
    """Attachments returned by API in response to a backend `RequestAttachments` message."""

    error: Optional[str] = None

    files: Optional[List[MlCopilotFile]] = None

    prompt_id: Optional[Uuid] = None

    request_id: Optional[str] = None

    seq: Optional[int] = None

    type: Literal["attachment_response"] = "attachment_response"


MlCopilotClientMessage = RootModel[
    Annotated[
        Union[
            OptionPing,
            OptionListModes,
            OptionHeaders,
            OptionProjectContext,
            OptionUser,
            OptionSystem,
            OptionAttachmentResponse,
        ],
        Field(discriminator="type"),
    ]
]
