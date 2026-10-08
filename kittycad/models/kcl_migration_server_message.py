from typing import List, Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.kcl_migration_application import KclMigrationApplication
from ..models.kcl_migration_history_entry import KclMigrationHistoryEntry
from ..models.kcl_migration_operation import KclMigrationOperation
from ..models.ml_copilot_server_message import MlCopilotServerMessage
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OptionOperation(KittyCadBaseModel):
    """Current durable state, including a reviewable candidate when successful."""

    operation: KclMigrationOperation

    type: Literal["operation"] = "operation"


class OptionProgress(KittyCadBaseModel):
    """Best-effort, display-only progress on the execution connection. Only text, informational and supported reasoning messages are forwarded; candidate edits are returned solely in a validated terminal operation."""

    message: MlCopilotServerMessage

    operation_id: Uuid

    type: Literal["progress"] = "progress"


class OptionHistory(KittyCadBaseModel):
    """Read-only history; never route these entries through file-edit handlers."""

    conversation_id: Uuid

    entries: List[KclMigrationHistoryEntry]

    type: Literal["history"] = "history"


class OptionApplication(KittyCadBaseModel):
    """Current durable application acknowledgement."""

    application: KclMigrationApplication

    operation_id: Uuid

    type: Literal["application"] = "application"


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
            OptionProgress,
            OptionHistory,
            OptionApplication,
            OptionError,
            OptionPong,
        ],
        Field(discriminator="type"),
    ]
]
