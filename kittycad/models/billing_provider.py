from enum import Enum


class BillingProvider(str, Enum):
    """Billing provider that owns downstream invoice or statement delivery."""  # noqa: E501

    """# Charges are ultimately collected through Stripe."""  # noqa: E501

    STRIPE = "stripe"

    """# Charges are collected outside Stripe, usually by finance or contract workflow."""  # noqa: E501

    MANUAL_INVOICE = "manual_invoice"

    def __str__(self) -> str:
        return str(self.value)
