from enum import Enum


class AggregateUsageCollectionThresholdSource(str, Enum):
    """Precedence source that determines an account's effective threshold."""  # noqa: E501

    ADMIN = "admin"

    CUSTOMER = "customer"

    SYSTEM_DEFAULT = "system_default"

    def __str__(self) -> str:
        return str(self.value)
