from enum import Enum


class DxfStorage(str, Enum):
    """Export storage."""  # noqa: E501

    """# Plaintext encoding.

This is the default setting."""  # noqa: E501

    ASCII = "ascii"

    """# Binary encoding."""  # noqa: E501

    BINARY = "binary"

    def __str__(self) -> str:
        return str(self.value)
