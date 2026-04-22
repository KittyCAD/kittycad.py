from enum import Enum


class BillingRolloverPolicy(str, Enum):
    """What happens to unused commitment when a contract period closes."""  # noqa: E501

    """# Unused commitment expires at the end of the period."""  # noqa: E501

    NONE = "none"

    """# Unused year-one commitment may roll once into year two, but not beyond."""  # noqa: E501

    YEAR1_TO_YEAR2_ONCE = "year1_to_year2_once"

    def __str__(self) -> str:
        return str(self.value)
