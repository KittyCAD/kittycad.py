from enum import Enum


class InvoiceRefundStatus(str, Enum):
    """Summary of the refund state for an invoice's captured payments."""  # noqa: E501

    """# Some, but not all, captured funds tied to the invoice were refunded."""  # noqa: E501

    PARTIALLY_REFUNDED = "partially_refunded"

    """# All captured funds tied to the invoice were refunded."""  # noqa: E501

    REFUNDED = "refunded"

    def __str__(self) -> str:
        return str(self.value)
