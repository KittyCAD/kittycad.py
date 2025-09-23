import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import RootModel

from ..models.ml_tool_result import MlToolResult
from ..models.uuid import Uuid
from .base import KittyCadBaseModel
from .reasoning_message import ReasoningMessage


class SessionData(KittyCadBaseModel):
    """"""

    api_call_id: str


class ConversationId(KittyCadBaseModel):
    """"""

    conversation_id: str


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


class Replay(KittyCadBaseModel):
    """"""

    messages: List[bytes]


class EndOfStream(KittyCadBaseModel):
    """"""

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Optional[str] = None

    id: Optional[Uuid] = None

    started_at: Optional[datetime.datetime] = None

    whole_response: Optional[str] = None


class MlCopilotServerMessage0(KittyCadBaseModel):
    """Session metadata sent by the server right after authentication.

    Semantics: - This message is NOT persisted in the database and will NEVER appear in a subsequent `Replay` message. However, we do have the `api_call_id` in the database. - Timing: sent immediately after a client is authenticated on a websocket. Useful for correlating logs and traces."""

    session_data: Dict[str, Any]


class MlCopilotServerMessage1(KittyCadBaseModel):
    """The ID of the conversation, which can be used to track the session."""

    conversation_id: Dict[str, Any]


class MlCopilotServerMessage2(KittyCadBaseModel):
    """Delta of the response, e.g. a chunk of text/tokens."""

    delta: Dict[str, Any]


class MlCopilotServerMessage3(KittyCadBaseModel):
    """Completed tool call result."""

    tool_output: Dict[str, Any]


class MlCopilotServerMessage4(KittyCadBaseModel):
    """Error sent by server."""

    error: Dict[str, Any]


class MlCopilotServerMessage5(KittyCadBaseModel):
    """Log / banner text."""

    info: Dict[str, Any]


class MlCopilotServerMessage6(KittyCadBaseModel):
    """Assistant reasoning / chain-of-thought (if you expose it)."""

    reasoning: ReasoningMessage


class MlCopilotServerMessage7(KittyCadBaseModel):
    """Replay containing raw bytes for previously-saved messages for a conversation. Includes server messages and client `User` messages.

    Invariants: - Includes server messages: `Info`, `Error`, `Reasoning(..)`, `ToolOutput { .. }`, and `EndOfStream { .. }`. - Also includes client `User` messages. - The following are NEVER included: `SessionData`, `ConversationId`, or `Delta`. - Ordering is stable: messages are ordered by prompt creation time within the conversation, then by the per-prompt `seq` value (monotonically increasing as seen in the original stream).

    Wire format: - Each element is canonical serialized bytes (typically JSON) for either a `MlCopilotServerMessage` or a `MlCopilotClientMessage::User`. - When delivered as an initial replay over the websocket (upon `?replay=true&conversation_id=<uuid>`), the server sends a single WebSocket Binary frame containing a BSON-encoded document of this enum: `Replay { messages }`."""

    replay: Dict[str, Any]


class MlCopilotServerMessage8(KittyCadBaseModel):
    """Marks the end of a streamed answer."""

    end_of_stream: Dict[str, Any]


MlCopilotServerMessage = RootModel[
    Union[
        SessionData,
        ConversationId,
        Delta,
        ToolOutput,
        Error,
        Info,
        ReasoningMessage,
        Replay,
        EndOfStream,
        MlCopilotServerMessage0,
        MlCopilotServerMessage1,
        MlCopilotServerMessage2,
        MlCopilotServerMessage3,
        MlCopilotServerMessage4,
        MlCopilotServerMessage5,
        MlCopilotServerMessage6,
        MlCopilotServerMessage7,
        MlCopilotServerMessage8,
    ]
]
