from typing import Any, Dict, Optional, Union

from pydantic import BaseModel, ConfigDict, RootModel

from ..models.ml_tool_result import MlToolResult
from .reasoning_message import ReasoningMessage


class Delta(BaseModel):
    """"""

    delta: str

    model_config = ConfigDict(protected_namespaces=())


class ToolOutput(BaseModel):
    """"""

    result: MlToolResult

    model_config = ConfigDict(protected_namespaces=())


class Error(BaseModel):
    """"""

    detail: str

    model_config = ConfigDict(protected_namespaces=())


class Info(BaseModel):
    """"""

    text: str

    model_config = ConfigDict(protected_namespaces=())


reasoning = ReasoningMessage


class EndOfStream(BaseModel):
    """"""

    whole_response: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())


class MlCopilotServerMessage0(BaseModel):
    """Delta of the response, e.g. a chunk of text/tokens."""

    delta: Dict[str, Any]

    model_config = ConfigDict(protected_namespaces=())


class MlCopilotServerMessage1(BaseModel):
    """Completed tool call result."""

    tool_output: Dict[str, Any]

    model_config = ConfigDict(protected_namespaces=())


class MlCopilotServerMessage2(BaseModel):
    """Error sent by server."""

    error: Dict[str, Any]

    model_config = ConfigDict(protected_namespaces=())


class MlCopilotServerMessage3(BaseModel):
    """Log / banner text."""

    info: Dict[str, Any]

    model_config = ConfigDict(protected_namespaces=())


class MlCopilotServerMessage4(BaseModel):
    """Assistant reasoning / chain-of-thought (if you expose it)."""

    reasoning: ReasoningMessage

    model_config = ConfigDict(protected_namespaces=())


class MlCopilotServerMessage5(BaseModel):
    """Marks the end of a streamed answer."""

    end_of_stream: Dict[str, Any]

    model_config = ConfigDict(protected_namespaces=())


MlCopilotServerMessage = RootModel[
    Union[
        Delta,
        ToolOutput,
        Error,
        Info,
        ReasoningMessage,
        EndOfStream,
        MlCopilotServerMessage0,
        MlCopilotServerMessage1,
        MlCopilotServerMessage2,
        MlCopilotServerMessage3,
        MlCopilotServerMessage4,
        MlCopilotServerMessage5,
    ]
]
