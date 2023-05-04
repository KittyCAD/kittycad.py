from enum import Enum


class PaymentMethodType(str, Enum):
    """An enum representing the possible values of an `PaymentMethod`'s `type` field."""  # noqa: E501

    """# A card payment method. """  # noqa: E501
    CARD = "card"

    def __str__(self) -> str:
        return str(self.value)
