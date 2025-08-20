from enum import Enum


class SupportTier(str, Enum):
    """The support tier the subscription provides."""  # noqa: E501

    """# Community support."""  # noqa: E501

    COMMUNITY = "community"

    """# Standard email support."""  # noqa: E501

    STANDARD_EMAIL = "standard_email"

    """# Priority email support."""  # noqa: E501

    PRIORITY_EMAIL = "priority_email"

    """# Premium support."""  # noqa: E501

    PREMIUM = "premium"

    def __str__(self) -> str:
        return str(self.value)
