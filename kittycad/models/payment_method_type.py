from enum import Enum


class PaymentMethodType(str, Enum):
    CARD = 'card'

    def __str__(self) -> str:
        return str(self.value)
