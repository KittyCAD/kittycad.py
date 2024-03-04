from enum import Enum


class FbxStorage(str, Enum):
    """Describes the storage format of an FBX file."""  # noqa: E501

    """# ASCII FBX encoding. """  # noqa: E501
    ASCII = "ascii"
    """# Binary FBX encoding. """  # noqa: E501
    BINARY = "binary"

    def __str__(self) -> str:
        return str(self.value)
