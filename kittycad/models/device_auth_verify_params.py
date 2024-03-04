
from pydantic import BaseModel, ConfigDict



class DeviceAuthVerifyParams(BaseModel):
    """The request parameters to verify the `user_code` for the OAuth 2.0 Device Authorization Grant."""

    user_code: str

    model_config = ConfigDict(protected_namespaces=())
