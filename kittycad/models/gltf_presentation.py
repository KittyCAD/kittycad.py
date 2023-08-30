from enum import Enum


class GltfPresentation(str, Enum):
    """Describes the presentation style of the glTF JSON."""  # noqa: E501

    """# Condense the JSON into the smallest possible size. """  # noqa: E501
    COMPACT = "compact"
    """# Expand the JSON into a more human readable format.

This is the default setting. """  # noqa: E501
    PRETTY = "pretty"

    def __str__(self) -> str:
        return str(self.value)
