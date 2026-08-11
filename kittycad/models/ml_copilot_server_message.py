import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import RootModel, model_serializer, model_validator

from ..models.ml_copilot_file import MlCopilotFile
from ..models.ml_copilot_mode_option import MlCopilotModeOption
from ..models.ml_tool_result import MlToolResult
from ..models.reasoning_message import ReasoningMessage
from ..models.uuid import Uuid
from ..models.zookeeper_auto_router_metadata import (
    ZookeeperAutoRouterMetadata as ZookeeperAutoRouterMetadataModel,
)
from ..models.zookeeper_turn_usage import ZookeeperTurnUsage as ZookeeperTurnUsageModel
from .base import KittyCadBaseModel


class Pong(KittyCadBaseModel):
    """Pong response to a Ping message."""

    pong: Dict[str, Any]


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


class ModesResponse(KittyCadBaseModel):
    """Available mode metadata for clients."""

    default_mode: str

    modes: List[MlCopilotModeOption]

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "modes_response" in data
            and isinstance(data["modes_response"], dict)
        ):
            return data["modes_response"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"modes_response": payload}


class BackendShutdown(KittyCadBaseModel):
    """Notification that the backend is shutting down."""

    reason: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "backend_shutdown" in data
            and isinstance(data["backend_shutdown"], dict)
        ):
            return data["backend_shutdown"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"backend_shutdown": payload}


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


class RequestAttachments(KittyCadBaseModel):
    """Backend-only request for API to reload client attachments from storage.

    API handles this message internally and responds upstream with `MlCopilotClientMessage::AttachmentResponse`; it is not forwarded to the browser."""

    conversation_id: Optional[Uuid] = None

    names: Optional[List[str]] = None

    only_metadata: Optional[bool] = False

    prompt_id: Optional[Uuid] = None

    request_id: Optional[str] = None

    seq: Optional[int] = None

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "request_attachments" in data
            and isinstance(data["request_attachments"], dict)
        ):
            return data["request_attachments"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"request_attachments": payload}


class AttachmentsLoaded(KittyCadBaseModel):
    """Notification that API finished loading all attachments for the conversation."""

    request_id: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "attachments_loaded" in data
            and isinstance(data["attachments_loaded"], dict)
        ):
            return data["attachments_loaded"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"attachments_loaded": payload}


class ZookeeperAutoRouterMetadata(KittyCadBaseModel):
    """Backend-only Zookeeper Auto-router metadata.

    API persists this on the active prompt and does not forward it to clients or replay it as a chat message."""

    zookeeper_auto_router_metadata: ZookeeperAutoRouterMetadataModel


class ZookeeperOpenAiResponseCheckpoint(KittyCadBaseModel):
    """Backend-only completed OpenAI response checkpoint.

    API persists this on the active prompt and includes the latest completed checkpoint only in replay sent to the text-to-CAD backend. It is never forwarded to browser clients."""

    response_id: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "zookeeper_open_ai_response_checkpoint" in data
            and isinstance(data["zookeeper_open_ai_response_checkpoint"], dict)
        ):
            return data["zookeeper_open_ai_response_checkpoint"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"zookeeper_open_ai_response_checkpoint": payload}


class ZookeeperTurnUsage(KittyCadBaseModel):
    """Backend-only token usage and cost for one completed Zookeeper turn.

    Sent just before `EndOfStream`. API records it in `meta.usage` on the turn's `EndOfStream` message row, alongside the `meta.billing` revenue figures, and never forwards it to clients or replays it as a chat message. It exists so spend can be compared against what the turn was billed; it is not customer-facing."""

    zookeeper_turn_usage: ZookeeperTurnUsageModel


class ZookeeperRecoveryToolOutput(KittyCadBaseModel):
    """Backend-only completed tool result used for portable Zookeeper recovery.

    API persists this message and includes it only in replay sent to the text-to-CAD backend. It is never forwarded to browser clients."""

    call_id: str

    output: str

    project_updated: Optional[bool] = False

    tool_name: str

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "zookeeper_recovery_tool_output" in data
            and isinstance(data["zookeeper_recovery_tool_output"], dict)
        ):
            return data["zookeeper_recovery_tool_output"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"zookeeper_recovery_tool_output": payload}


class Replay(KittyCadBaseModel):
    """Replay containing raw bytes for previously-saved messages for a conversation. Includes server messages and client `User` messages.

    Invariants: - Client replay includes server messages: `Info`, `Error`, `Reasoning(..)`, `ToolOutput { .. }`, `Files { .. }`, `ProjectUpdated { .. }`, and `EndOfStream { .. }`. - Client replay also includes client `User` messages. - Backend replay includes client `User` messages plus selected reasoning, edit metadata, recovery output, and final responses. - The following are NEVER included from persisted chat rows: `SessionData`, `ConversationId`, `Delta`, `BackendShutdown`, `ZookeeperAutoRouterMetadata`, `ZookeeperOpenAiResponseCheckpoint`, or `ZookeeperTurnUsage`. - `ZookeeperRecoveryToolOutput` is included only in replay sent to the text-to-CAD backend and is filtered from client replay. - The latest completed `ZookeeperOpenAiResponseCheckpoint` is synthesized from prompt metadata only for replay sent to the text-to-CAD backend. - Ordering is stable: messages are ordered by prompt creation time within the conversation, then by the per-prompt `seq` value (monotonically increasing as seen in the original stream).

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


class Files(KittyCadBaseModel):
    """Files sent from the server to the client."""

    files: List[MlCopilotFile]

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "files" in data
            and isinstance(data["files"], dict)
        ):
            return data["files"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        return {"files": payload}


MlCopilotServerMessage = RootModel[
    Union[
        Pong,
        SessionData,
        ConversationId,
        Delta,
        ToolOutput,
        Error,
        Info,
        ModesResponse,
        BackendShutdown,
        ProjectUpdated,
        Reasoning,
        RequestAttachments,
        AttachmentsLoaded,
        ZookeeperAutoRouterMetadata,
        ZookeeperOpenAiResponseCheckpoint,
        ZookeeperTurnUsage,
        ZookeeperRecoveryToolOutput,
        Replay,
        EndOfStream,
        Files,
    ]
]
