from enum import Enum


class KclMigrationApplicationStatus(str, Enum):
    """Client-reported application state, separate from conversion success."""  # noqa: E501

    """# The client has not confirmed application. API does not infer project state."""  # noqa: E501

    NOT_APPLIED = "not_applied"

    """# The client reports completing the guarded project write (or redo)."""  # noqa: E501

    APPLIED = "applied"

    """# The client reports undoing the migration."""  # noqa: E501

    UNDONE = "undone"

    def __str__(self) -> str:
        return str(self.value)
