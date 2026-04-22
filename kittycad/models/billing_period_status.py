from enum import Enum


class BillingPeriodStatus(str, Enum):
    """Operational status for a contract billing period."""  # noqa: E501

    """# Period is active and may still accrue usage or adjustments."""  # noqa: E501

    OPEN = "open"

    """# Period is finalized and should be treated as read-only for billing purposes."""  # noqa: E501

    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
