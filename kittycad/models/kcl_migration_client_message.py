from typing import Dict, Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.kcl_migration_request import KclMigrationRequest
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OptionHeaders(KittyCadBaseModel):
    """Authenticate the connection."""

    headers: Dict[str, str]

    type: Literal["headers"] = "headers"


class OptionStart(KittyCadBaseModel):
    """Start or retrieve the same attempt after a delivery retry."""

    request: KclMigrationRequest

    type: Literal["start"] = "start"


class OptionStatus(KittyCadBaseModel):
    """Read an existing attempt without resuming it or changing its deadline."""

    operation_id: Uuid

    type: Literal["status"] = "status"


class OptionCancel(KittyCadBaseModel):
    """Cancel an existing attempt. Cancellation is idempotent."""

    operation_id: Uuid

    type: Literal["cancel"] = "cancel"


class OptionPing(KittyCadBaseModel):
    """Application heartbeat."""

    type: Literal["ping"] = "ping"


KclMigrationClientMessage = RootModel[
    Annotated[
        Union[
            OptionHeaders,
            OptionStart,
            OptionStatus,
            OptionCancel,
            OptionPing,
        ],
        Field(discriminator="type"),
    ]
]
