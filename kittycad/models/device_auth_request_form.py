from .base import KittyCadBaseModel


class DeviceAuthRequestForm(KittyCadBaseModel):
    """The request parameters for the OAuth 2.0 Device Authorization Grant flow."""

    client_id: str
