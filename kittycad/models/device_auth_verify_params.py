
from pydantic import BaseModel



class DeviceAuthVerifyParams(BaseModel):
    """The request parameters to verify the `user_code` for the OAuth 2.0 Device Authorization Grant."""

    user_code: str
