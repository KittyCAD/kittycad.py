from .base import KittyCadBaseModel


class ModelingSessionData(KittyCadBaseModel):
    """Successful Websocket response."""

    api_call_id: str
