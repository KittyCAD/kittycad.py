from enum import Enum


class InvoiceStatus(str, Enum):
    DELETED = 'deleted'
    DRAFT = 'draft'
    OPEN = 'open'
    PAID = 'paid'
    UNCOLLECTIBLE = 'uncollectible'
    VOID = 'void'

    def __str__(self) -> str:
        return str(self.value)
