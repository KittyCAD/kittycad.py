from pydantic import BaseModel, ConfigDict


class Createshortlinkresponse(BaseModel):
    """Response from creating a shortlink."""

    key: str

    url: str

    model_config = ConfigDict(protected_namespaces=())
