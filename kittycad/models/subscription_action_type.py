from enum import Enum


class SubscriptionActionType(str, Enum):
    """Indicates which kind of Stripe intent requires customer action during subscription creation."""  # noqa: E501

    """# The client secret belongs to a PaymentIntent (initial invoice payment)."""  # noqa: E501

    PAYMENT_INTENT = "payment_intent"

    """# The client secret belongs to a SetupIntent (trial or setup-only flow)."""  # noqa: E501

    SETUP_INTENT = "setup_intent"

    def __str__(self) -> str:
        return str(self.value)
