from pydantic import BaseModel, ConfigDict


class Loft(BaseModel):
    """The response from the `Loft` command."""

    solid_id: str

    model_config = ConfigDict(protected_namespaces=())
