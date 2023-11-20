from enum import Enum


class AiFeedback(str, Enum):
    """Human feedback on an AI response."""  # noqa: E501

    """# Thumbs up. """  # noqa: E501
    THUMBS_UP = "thumbs_up"
    """# Thumbs down. """  # noqa: E501
    THUMBS_DOWN = "thumbs_down"

    def __str__(self) -> str:
        return str(self.value)
