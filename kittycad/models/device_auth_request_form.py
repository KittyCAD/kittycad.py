
from pydantic import BaseModel



class DeviceAuthRequestForm(BaseModel):
    """The request parameters for the OAuth 2.0 Device Authorization Grant flow."""

    client_id: str
