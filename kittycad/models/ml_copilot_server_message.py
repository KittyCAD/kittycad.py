import datetime
from typing import Dict, List, Optional, Union

from pydantic import RootModel, model_serializer, model_validator

from ..models.ml_tool_result import MlToolResult
from ..models.reasoning_message import ReasoningMessage
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class SessionData(KittyCadBaseModel):
    """Session metadata sent by the server right after authentication.

    Semantics: - This message is NOT persisted in the database and will NEVER appear in a subsequent `Replay` message. However, we do have the `api_call_id` in the database. - Timing: sent immediately after a client is authenticated on a websocket. Useful for correlating logs and traces."""

    api_call_id: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "session_data" in data
            and isinstance(data["session_data"], dict)
        ):
            return data["session_data"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"session_data": payload}


class ConversationId(KittyCadBaseModel):
    """The ID of the conversation, which can be used to track the session."""

    conversation_id: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "conversation_id" in data
            and isinstance(data["conversation_id"], dict)
        ):
            return data["conversation_id"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"conversation_id": payload}


class Delta(KittyCadBaseModel):
    """Delta of the response, e.g. a chunk of text/tokens."""

    delta: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "delta" in data
            and isinstance(data["delta"], dict)
        ):
            return data["delta"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"delta": payload}


class ToolOutput(KittyCadBaseModel):
    """Completed tool call result."""

    result: MlToolResult

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "tool_output" in data
            and isinstance(data["tool_output"], dict)
        ):
            return data["tool_output"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"tool_output": payload}


class Error(KittyCadBaseModel):
    """Error sent by server."""

    detail: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "error" in data
            and isinstance(data["error"], dict)
        ):
            return data["error"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"error": payload}


class Info(KittyCadBaseModel):
    """Log / banner text."""

    text: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if isinstance(data, dict) and "info" in data and isinstance(data["info"], dict):
            return data["info"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"info": payload}


class ProjectUpdated(KittyCadBaseModel):
    """Notification that the KCL project has been updated."""

    files: Dict[str, str]

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "project_updated" in data
            and isinstance(data["project_updated"], dict)
        ):
            return data["project_updated"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"project_updated": payload}


class Reasoning(KittyCadBaseModel):
    """Assistant reasoning / chain-of-thought (if you expose it)."""

    reasoning: ReasoningMessage


class Replay(KittyCadBaseModel):
    """Replay containing raw bytes for previously-saved messages for a conversation. Includes server messages and client `User` messages.

    Invariants: - Includes server messages: `Info`, `Error`, `Reasoning(..)`, `ToolOutput { .. }`, `ProjectUpdated { .. }`, and `EndOfStream { .. }`. - Also includes client `User` messages. - The following are NEVER included: `SessionData`, `ConversationId`, or `Delta`. - Ordering is stable: messages are ordered by prompt creation time within the conversation, then by the per-prompt `seq` value (monotonically increasing as seen in the original stream).

    Wire format: - Each element is canonical serialized bytes (typically JSON) for either a `MlCopilotServerMessage` or a `MlCopilotClientMessage::User`. - When delivered as an initial replay over the websocket (upon `?replay=true&conversation_id=<uuid>`), the server sends a single WebSocket Binary frame containing a MsgPack-encoded document of this enum: `Replay { messages }`."""

    messages: List[bytes]

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "replay" in data
            and isinstance(data["replay"], dict)
        ):
            return data["replay"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"replay": payload}


class EndOfStream(KittyCadBaseModel):
    """Marks the end of a streamed answer."""

    completed_at: Optional[datetime.datetime] = None

    conversation_id: Optional[str] = None

    id: Optional[Uuid] = None

    started_at: Optional[datetime.datetime] = None

    whole_response: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "end_of_stream" in data
            and isinstance(data["end_of_stream"], dict)
        ):
            return data["end_of_stream"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"end_of_stream": payload}


MlCopilotServerMessage = RootModel[
    Union[
        SessionData,
        ConversationId,
        Delta,
        ToolOutput,
        Error,
        Info,
        ProjectUpdated,
        Reasoning,
        Replay,
        EndOfStream,
    ]
]
