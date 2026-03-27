from enum import Enum


class KclProjectPublicationStatus(str, Enum):
    """Publication workflow state for a KCL project."""  # noqa: E501

    """# The project is not yet submitted for review."""  # noqa: E501

    DRAFT = "draft"

    """# The project is awaiting moderation review."""  # noqa: E501

    PENDING_REVIEW = "pending_review"

    """# The project is publicly visible in the gallery."""  # noqa: E501

    PUBLISHED = "published"

    """# The project was reviewed and rejected."""  # noqa: E501

    REJECTED = "rejected"

    """# The project was removed from public display."""  # noqa: E501

    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
