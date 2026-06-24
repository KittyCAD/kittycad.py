from enum import Enum


class KclProjectPublicationStatus(str, Enum):
    """Publication workflow state for a KCL project."""  # noqa: E501

    """# The project is owner-visible only and not intended for publication."""  # noqa: E501

    PRIVATE = "private"

    """# The project is being prepared for publication but is not yet submitted."""  # noqa: E501

    DRAFT = "draft"

    """# The project is awaiting moderation review."""  # noqa: E501

    PENDING_REVIEW = "pending_review"

    """# The project is publicly visible in the gallery."""  # noqa: E501

    PUBLISHED = "published"

    """# The project was reviewed and rejected."""  # noqa: E501

    REJECTED = "rejected"

    """# The project was removed from public display."""  # noqa: E501

    DELETED = "deleted"

    """# The project was reviewed and changes were requested before it can be published."""  # noqa: E501

    CHANGES_REQUESTED = "changes_requested"

    def __str__(self) -> str:
        return str(self.value)
