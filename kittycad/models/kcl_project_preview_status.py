from enum import Enum


class KclProjectPreviewStatus(str, Enum):
    """Preview generation status for a KCL project."""  # noqa: E501

    """# A preview has not been generated yet."""  # noqa: E501

    PENDING = "pending"

    """# The preview is available for display."""  # noqa: E501

    READY = "ready"

    """# Preview generation failed and needs attention."""  # noqa: E501

    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
