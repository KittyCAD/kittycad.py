from enum import Enum


class UnitCurrent(str, Enum):
    """The valid types of current units."""  # noqa: E501

    """# Amperes <https://en.wikipedia.org/wiki/Ampere> """  # noqa: E501
    AMPERES = "amperes"
    """# Microamperes <https://en.wikipedia.org/wiki/Microampere> """  # noqa: E501
    MICROAMPERES = "microamperes"
    """# Milliamperes <https://en.wikipedia.org/wiki/Milliampere> """  # noqa: E501
    MILLIAMPERES = "milliamperes"
    """# Nanoamperes <https://en.wikipedia.org/wiki/Nanoampere> """  # noqa: E501
    NANOAMPERES = "nanoamperes"

    def __str__(self) -> str:
        return str(self.value)
