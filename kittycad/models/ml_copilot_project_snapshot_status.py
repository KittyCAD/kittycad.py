from enum import Enum


class MlCopilotProjectSnapshotStatus(str, Enum):
    """Outcome of comparing a client project snapshot with canonical state."""  # noqa: E501

    """# The snapshot was based on current state and became canonical."""  # noqa: E501

    ACCEPTED = "accepted"

    """# Non-overlapping client changes were merged into canonical state."""  # noqa: E501

    MERGED = "merged"

    """# A clean snapshot based on an older revision was not accepted."""  # noqa: E501

    REJECTED_STALE = "rejected_stale"

    """# Client changes overlap canonical changes and require explicit resolution."""  # noqa: E501

    CONFLICT = "conflict"

    def __str__(self) -> str:
        return str(self.value)
