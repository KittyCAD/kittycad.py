from enum import Enum


class BillingContractStatus(str, Enum):
    """Lifecycle state for a billing contract."""  # noqa: E501

    """# Contract terms are still being assembled and should not drive billing yet."""  # noqa: E501

    DRAFT = "draft"

    """# Contract is committed for a future start date and should not drive billing yet."""  # noqa: E501

    SCHEDULED = "scheduled"

    """# Contract is in force and may be used for rating and funding decisions."""  # noqa: E501

    ACTIVE = "active"

    """# Contract finished its intended term and is no longer accruing new periods."""  # noqa: E501

    CLOSED = "closed"

    """# Contract was intentionally terminated before completing its intended term."""  # noqa: E501

    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)
