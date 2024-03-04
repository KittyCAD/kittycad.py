from enum import Enum


class ModelingAppSubscriptionTierName(str, Enum):
    """An enum representing a Modeling App subscription tier name."""  # noqa: E501

    """# The free tier. """  # noqa: E501
    FREE = "free"
    """# The pro tier. """  # noqa: E501
    PRO = "pro"
    """# The team tier. """  # noqa: E501
    TEAM = "team"
    """# The enterprise tier. """  # noqa: E501
    ENTERPRISE = "enterprise"

    def __str__(self) -> str:
        return str(self.value)
