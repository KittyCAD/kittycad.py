import datetime
from typing import Optional, Union

from pydantic import RootModel, model_serializer, model_validator

from ..models.ml_tool_result import MlToolResult
from ..models.reasoning_message import ReasoningMessage
from .base import KittyCadBaseModel


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


class Reasoning(KittyCadBaseModel):
    """Assistant reasoning / chain-of-thought (if you expose it)."""

    reasoning: ReasoningMessage

    @model_validator(mode="before")
    @classmethod
    def _unwrap(cls, data):
        if (
            isinstance(data, dict)
            and "reasoning" in data
            and isinstance(data["reasoning"], dict)
        ):
            return data["reasoning"]

        return data

    @model_serializer(mode="wrap")
    def _wrap(self, handler, info):
        payload = handler(self, info)

        if isinstance(payload, dict) and "reasoning" in payload:
            value = payload["reasoning"]

        else:
            value = payload

        return {"reasoning": value}


class EndOfStream(KittyCadBaseModel):
    """Marks the end of a streamed answer."""

    completed_at: Optional[datetime.datetime] = None

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
        ConversationId,
        Delta,
        ToolOutput,
        Error,
        Info,
        Reasoning,
        EndOfStream,
    ]
]
