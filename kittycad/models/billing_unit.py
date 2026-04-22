from enum import Enum


class BillingUnit(str, Enum):
    """Base unit that measured usage or pricing is expressed in."""  # noqa: E501

    """# Quantity is counted in files."""  # noqa: E501

    FILE = "file"

    """# Quantity is counted in whole or rounded minutes."""  # noqa: E501

    MINUTE = "minute"

    """# Quantity is counted in seconds."""  # noqa: E501

    SECOND = "second"

    """# Quantity is counted in years."""  # noqa: E501

    YEAR = "year"

    """# Quantity is counted once per billing period."""  # noqa: E501

    PERIOD = "period"

    def __str__(self) -> str:
        return str(self.value)
