from typing import Any

from .base import KittyCadBaseModel


class MlCopilotClientCommand(KittyCadBaseModel):
    """One client-owned command that Zookeeper may discover and request over the current copilot WebSocket connection.

    Command definitions are connection-scoped capabilities, not durable user data. Clients replace the complete catalog whenever its revision changes."""

    description: str

    id: str

    input_schema: Any

    title: str
