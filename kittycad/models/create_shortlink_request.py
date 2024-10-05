from pydantic import BaseModel, ConfigDict


class CreateShortlinkRequest(BaseModel):
    """Request to create a shortlink."""

    restrict_to_org: bool

    url: str

    model_config = ConfigDict(protected_namespaces=())
