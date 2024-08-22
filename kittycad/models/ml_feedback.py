from enum import Enum


class MlFeedback(str, Enum):
    """Human feedback on an ML response."""  # noqa: E501

    """# Thumbs up. """  # noqa: E501
    THUMBS_UP = "thumbs_up"
    """# Thumbs down. """  # noqa: E501
    THUMBS_DOWN = "thumbs_down"
    """# Accepted. """  # noqa: E501
    ACCEPTED = "accepted"
    """# Rejected. """  # noqa: E501
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
