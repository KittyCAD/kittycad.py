from pydantic import BaseModel, ConfigDict


class AuthApiKeyResponse(BaseModel):
    """The response from the `/auth/api-key` endpoint."""

    session_token: str

    model_config = ConfigDict(protected_namespaces=())
