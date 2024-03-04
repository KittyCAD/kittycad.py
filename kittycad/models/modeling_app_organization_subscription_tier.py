from enum import Enum


class ModelingAppOrganizationSubscriptionTier(str, Enum):
    """The subscription tiers we offer for the Modeling App to organizations."""  # noqa: E501

    """# The team tier. """  # noqa: E501
    TEAM = "team"
    """# The enterprise tier. """  # noqa: E501
    ENTERPRISE = "enterprise"

    def __str__(self) -> str:
        return str(self.value)
