from enum import Enum


class UnitChargeFormat(str, Enum):
    """The valid types of charge unit formats."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Coulomb> """  # noqa: E501
    COULOMB = "coulomb"
    """# <https://en.wikipedia.org/wiki/Ampere_hour> """  # noqa: E501
    AMPERE_HOUR = "ampere_hour"

    def __str__(self) -> str:
        return str(self.value)
