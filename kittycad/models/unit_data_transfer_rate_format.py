from enum import Enum


class UnitDataTransferRateFormat(str, Enum):
    """The valid types of data transfer unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Byte> """  # noqa: E501
    BYTES_PER_SECOND = "bytes_per_second"
    """# <https://en.wikipedia.org/wiki/Byte#Multiple-byte_units> """  # noqa: E501
    EXABYTES_PER_SECOND = "exabytes_per_second"
    """# <https://en.wikipedia.org/wiki/Bit> """  # noqa: E501
    BITS_PER_SECOND = "bits_per_second"
    """# <https://en.wikipedia.org/wiki/Exabit> """  # noqa: E501
    EXABITS_PER_SECOND = "exabits_per_second"

    def __str__(self) -> str:
        return str(self.value)
