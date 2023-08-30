from enum import Enum


class StlStorage(str, Enum):
    """Export storage."""  # noqa: E501

    """# Plaintext encoding. """  # noqa: E501
    ASCII = "ascii"
    """# Binary STL encoding.

This is the default setting. """  # noqa: E501
    BINARY = "binary"

    def __str__(self) -> str:
        return str(self.value)
