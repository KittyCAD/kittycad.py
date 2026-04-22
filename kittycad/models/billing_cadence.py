from enum import Enum


class BillingCadence(str, Enum):
    """How often a contract is expected to bill or renew operationally."""  # noqa: E501

    """# The contract is managed on an annual cycle."""  # noqa: E501

    ANNUAL = "annual"

    """# The contract is managed on a quarterly cycle."""  # noqa: E501

    QUARTERLY = "quarterly"

    """# The contract is managed on a monthly cycle."""  # noqa: E501

    MONTHLY = "monthly"

    """# The contract does not follow a fixed automated cadence."""  # noqa: E501

    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
