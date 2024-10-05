from pydantic import BaseModel, ConfigDict


class CreateShortlinkResponse(BaseModel):
    """Response from creating a shortlink."""

    key: str

    url: str

    model_config = ConfigDict(protected_namespaces=())
