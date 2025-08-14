from pydantic import BaseModel, ConfigDict

from ..models.entity_type import EntityType


class Getentitytype(BaseModel):
    """The response from the `GetEntityType` command."""

    entity_type: EntityType

    model_config = ConfigDict(protected_namespaces=())
