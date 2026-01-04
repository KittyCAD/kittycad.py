from enum import Enum


class SubscriptionPlanBillingModel(str, Enum):
    """Billing model for a modeling-app plan price."""  # noqa: E501

    """# A flat amount charged every interval."""  # noqa: E501

    FLAT = "flat"

    """# A per-seat amount charged every interval."""  # noqa: E501

    PER_USER = "per_user"

    def __str__(self) -> str:
        return str(self.value)
