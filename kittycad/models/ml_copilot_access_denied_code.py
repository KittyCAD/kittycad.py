from enum import Enum


class MlCopilotAccessDeniedCode(str, Enum):
    """Stable machine-readable reasons that an account cannot open a Copilot websocket until its billing or support state changes."""  # noqa: E501

    """# The account has no payment method on file."""  # noqa: E501

    MISSING_PAYMENT_METHOD = "missing_payment_method"

    """# The account's payment method failed."""  # noqa: E501

    PAYMENT_METHOD_FAILED = "payment_method_failed"

    """# The account reached its configured billing threshold."""  # noqa: E501

    BILLING_THRESHOLD_REACHED = "billing_threshold_reached"

    """# The account exhausted its credits without enabling pay-as-you-go."""  # noqa: E501

    PAY_AS_YOU_GO_DISABLED = "pay_as_you_go_disabled"

    """# The account was blocked after repeated plan changes recycled credits."""  # noqa: E501

    UPGRADE_DOWNGRADE_ABUSE = "upgrade_downgrade_abuse"

    """# Zoo support explicitly blocked the account."""  # noqa: E501

    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
