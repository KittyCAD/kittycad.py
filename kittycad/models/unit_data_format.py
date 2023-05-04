from enum import Enum


class UnitDataFormat(str, Enum):
    """The valid types of data unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Byte> """  # noqa: E501
    BYTE = "byte"
    """# <https://en.wikipedia.org/wiki/Byte#Multiple-byte_units> """  # noqa: E501
    EXABYTE = "exabyte"
    """# <https://en.wikipedia.org/wiki/Bit> """  # noqa: E501
    BIT = "bit"
    """# <https://en.wikipedia.org/wiki/Exabit> """  # noqa: E501
    EXABIT = "exabit"

    def __str__(self) -> str:
        return str(self.value)
