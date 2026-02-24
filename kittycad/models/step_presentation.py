from enum import Enum


class StepPresentation(str, Enum):
    """Describes the presentation style of the EXPRESS exchange format."""  # noqa: E501

    """# Condenses the text to reduce the size of the file."""  # noqa: E501

    COMPACT = "compact"

    """# Add extra spaces to make the text more easily readable.

This is the default setting."""  # noqa: E501

    PRETTY = "pretty"

    def __str__(self) -> str:
        return str(self.value)
