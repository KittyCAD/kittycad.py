
from pydantic import BaseModel

from ..models.entity_type import EntityType


class GetEntityType(BaseModel):
    """The response from the `GetEntityType` command."""

    entity_type: EntityType
