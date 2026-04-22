from enum import Enum


class BillingUnitGranularity(str, Enum):
    """Optional finer-grained measurement rule for a billed unit."""  # noqa: E501

    """# Usage should be normalized or rounded at the minute level."""  # noqa: E501

    MINUTE = "minute"

    """# Usage should be normalized or rounded at the second level."""  # noqa: E501

    SECOND = "second"

    def __str__(self) -> str:
        return str(self.value)
