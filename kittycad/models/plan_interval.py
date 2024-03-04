from enum import Enum


class PlanInterval(str, Enum):
    """A plan's interval."""  # noqa: E501

    """# Day. """  # noqa: E501
    DAY = "day"
    """# Month. """  # noqa: E501
    MONTH = "month"
    """# Week. """  # noqa: E501
    WEEK = "week"
    """# Year. """  # noqa: E501
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
