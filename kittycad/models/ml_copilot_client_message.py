from typing import Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.ml_copilot_system_command import MlCopilotSystemCommand
from ..models.source_range_prompt import SourceRangePrompt


class OptionHeaders(BaseModel):
    """Authentication header request."""

    headers: Dict[str, str]

    type: Literal["headers"] = "headers"

    model_config = ConfigDict(protected_namespaces=())


class OptionUser(BaseModel):
    """The user message, which contains the content of the user's input."""

    content: str

    current_files: Optional[Dict[str, bytes]] = None

    project_name: Optional[str] = None

    source_ranges: Optional[List[SourceRangePrompt]] = None

    type: Literal["user"] = "user"

    model_config = ConfigDict(protected_namespaces=())


class OptionSystem(BaseModel):
    """The system message, which can be used to set the context or instructions for the AI."""

    command: MlCopilotSystemCommand

    type: Literal["system"] = "system"

    model_config = ConfigDict(protected_namespaces=())


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
