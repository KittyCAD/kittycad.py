from enum import Enum


class PlyStorage(str, Enum):
    """The storage for the output PLY file."""  # noqa: E501

    """# Write numbers in their ascii representation (e.g. -13, 6.28, etc.). Properties are separated by spaces and elements are separated by line breaks. """  # noqa: E501
    ASCII = "ascii"
    """# Encode payload as binary using little endian. """  # noqa: E501
    BINARY_LITTLE_ENDIAN = "binary_little_endian"
    """# Encode payload as binary using big endian. """  # noqa: E501
    BINARY_BIG_ENDIAN = "binary_big_endian"

    def __str__(self) -> str:
        return str(self.value)
