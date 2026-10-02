from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.kcl_migration_operation import KclMigrationOperation
from .base import KittyCadBaseModel


class OptionOperation(KittyCadBaseModel):
    """Current durable state, including a reviewable candidate when successful."""

    operation: KclMigrationOperation

    type: Literal["operation"] = "operation"


class OptionError(KittyCadBaseModel):
    """A rejected request, without starting or charging for work."""

    detail: str

    type: Literal["error"] = "error"


class OptionPong(KittyCadBaseModel):
    """Heartbeat response."""

    type: Literal["pong"] = "pong"


KclMigrationServerMessage = RootModel[
    Annotated[
        Union[
            OptionOperation,
            OptionError,
            OptionPong,
        ],
        Field(discriminator="type"),
    ]
]
