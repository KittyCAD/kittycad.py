from typing import Any, Dict, Optional, Union

from pydantic import RootModel

from ..models.ml_tool_result import MlToolResult
from .base import KittyCadBaseModel
from .reasoning_message import ReasoningMessage


class Delta(KittyCadBaseModel):
    """"""

    delta: str


class ToolOutput(KittyCadBaseModel):
    """"""

    result: MlToolResult


class Error(KittyCadBaseModel):
    """"""

    detail: str


class Info(KittyCadBaseModel):
    """"""

    text: str


reasoning = ReasoningMessage


class EndOfStream(KittyCadBaseModel):
    """"""

    whole_response: Optional[str] = None


class MlCopilotServerMessage0(KittyCadBaseModel):
    """Delta of the response, e.g. a chunk of text/tokens."""

    delta: Dict[str, Any]


class MlCopilotServerMessage1(KittyCadBaseModel):
    """Completed tool call result."""

    tool_output: Dict[str, Any]


class MlCopilotServerMessage2(KittyCadBaseModel):
    """Error sent by server."""

    error: Dict[str, Any]


class MlCopilotServerMessage3(KittyCadBaseModel):
    """Log / banner text."""

    info: Dict[str, Any]


class MlCopilotServerMessage4(KittyCadBaseModel):
    """Assistant reasoning / chain-of-thought (if you expose it)."""

    reasoning: ReasoningMessage


class MlCopilotServerMessage5(KittyCadBaseModel):
    """Marks the end of a streamed answer."""

    end_of_stream: Dict[str, Any]


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
