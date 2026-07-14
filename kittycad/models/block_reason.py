from enum import Enum


class BlockReason(str, Enum):
    """The reason for blocking a user."""  # noqa: E501

    """# The user is missing a payment method and has exceeded their free API call credits for the month."""  # noqa: E501

    MISSING_PAYMENT_METHOD = "missing_payment_method"

    """# The users payment method has failed."""  # noqa: E501

    PAYMENT_METHOD_FAILED = "payment_method_failed"

    """# The user repeatedly upgraded and downgraded to recycle free-plan credits."""  # noqa: E501

    UPGRADE_DOWNGRADE_ABUSE = "upgrade_downgrade_abuse"

    """# An explicit admin block that can only be removed by admin intervention."""  # noqa: E501

    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
