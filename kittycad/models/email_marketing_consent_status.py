from enum import Enum


class EmailMarketingConsentStatus(str, Enum):
    """Email marketing consent state for a user."""  # noqa: E501

    """# No choice has been made yet."""  # noqa: E501

    UNKNOWN = "unknown"

    """# User has seen and dismissed the modal without deciding."""  # noqa: E501

    DISMISSED = "dismissed"

    """# User requested opt-in and must confirm via email."""  # noqa: E501

    PENDING = "pending"

    """# User explicitly confirmed via email flow."""  # noqa: E501

    CONFIRMED = "confirmed"

    """# User explicitly declined."""  # noqa: E501

    DECLINED = "declined"

    def __str__(self) -> str:
        return str(self.value)
