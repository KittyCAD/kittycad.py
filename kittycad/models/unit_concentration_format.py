from enum import Enum


class UnitConcentrationFormat(str, Enum):
    """The valid types of concentration unit formats."""  # noqa: E501

    """# Per Million - <https://en.wikipedia.org/wiki/Parts-per_notation> """  # noqa: E501
    PARTS_PER_MILLION = "parts_per_million"
    """# Per Billion - <https://en.wikipedia.org/wiki/Parts-per_notation> """  # noqa: E501
    PARTS_PER_BILLION = "parts_per_billion"
    """# Per Trillion - <https://en.wikipedia.org/wiki/Parts-per_notation> """  # noqa: E501
    PARTS_PER_TRILLION = "parts_per_trillion"
    """# <https://en.wikipedia.org/wiki/Concentration>, <https://en.wikipedia.org/wiki/Percentage> """  # noqa: E501
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
