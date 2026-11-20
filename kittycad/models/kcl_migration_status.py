from enum import Enum


class KclMigrationStatus(str, Enum):
    """Durable state of a migration attempt."""  # noqa: E501

    """# Preparation, conversion, or validation is still running."""  # noqa: E501

    RUNNING = "running"

    """# Conversion and final validation succeeded. Copilot delivers edits live."""  # noqa: E501

    SUCCEEDED = "succeeded"

    """# The attempt failed."""  # noqa: E501

    FAILED = "failed"

    """# Admission setup expired before execution could begin."""  # noqa: E501

    TIMED_OUT = "timed_out"

    """# The attempt was cancelled."""  # noqa: E501

    CANCELLED = "cancelled"

    """# The source, target, or project is not supported."""  # noqa: E501

    UNSUPPORTED = "unsupported"

    """# Execution, geometry, or behavioral equivalence could not be established."""  # noqa: E501

    VALIDATION_FAILED = "validation_failed"

    def __str__(self) -> str:
        return str(self.value)
