from enum import Enum


class InvoiceStatus(str, Enum):
    """An enum representing the possible values of an `Invoice`'s `status` field."""  # noqa: E501

    """# Draft. """  # noqa: E501
    DRAFT = "draft"
    """# Open. """  # noqa: E501
    OPEN = "open"
    """# Paid. """  # noqa: E501
    PAID = "paid"
    """# Uncollectible. """  # noqa: E501
    UNCOLLECTIBLE = "uncollectible"
    """# Void. """  # noqa: E501
    VOID = "void"

    def __str__(self) -> str:
        return str(self.value)
