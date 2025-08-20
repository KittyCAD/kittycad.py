from .base import KittyCadBaseModel


class DeviceAuthConfirmParams(KittyCadBaseModel):
    """The request parameters to confirm the `user_code` for the OAuth 2.0 Device Authorization Grant."""

    user_code: str
