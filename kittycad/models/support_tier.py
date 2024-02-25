from enum import Enum


class SupportTier(str, Enum):
    """The support tier the subscription provides."""  # noqa: E501

    """# Community support. """  # noqa: E501
    COMMUNITY = "community"
    """# Standard support. """  # noqa: E501
    STANDARD = "standard"
    """# Premium support. """  # noqa: E501
    PREMIUM = "premium"
    """# Priority support. """  # noqa: E501
    PRIORITY = "priority"

    def __str__(self) -> str:
        return str(self.value)
