from pydantic import BaseModel, ConfigDict


class UpdateShortlinkRequest(BaseModel):
    """Request to update a shortlink."""

    restrict_to_org: bool

    model_config = ConfigDict(protected_namespaces=())
