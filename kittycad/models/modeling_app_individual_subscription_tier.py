from enum import Enum


class ModelingAppIndividualSubscriptionTier(str, Enum):
    """The subscription tiers we offer for the Modeling App to individuals."""  # noqa: E501

    """# The free tier."""  # noqa: E501

    FREE = "free"

    """# The plus tier."""  # noqa: E501

    PLUS = "plus"

    """# The pro tier."""  # noqa: E501

    PRO = "pro"

    def __str__(self) -> str:
        return str(self.value)
