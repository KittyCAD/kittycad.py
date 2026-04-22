from enum import Enum


class SubscriptionBillingMode(str, Enum):
    """How a subscription plan is billed operationally."""  # noqa: E501

    """# Standard self-serve billing through the normal subscription flow."""  # noqa: E501

    STANDARD = "standard"

    """# Contract-managed billing controlled outside the standard subscription flow."""  # noqa: E501

    CONTRACT = "contract"

    def __str__(self) -> str:
        return str(self.value)
