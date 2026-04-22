from enum import Enum


class BillingCommitmentScope(str, Enum):
    """How commitment funds are shared across contract items."""  # noqa: E501

    """# One shared commitment pool may fund multiple contract items."""  # noqa: E501

    POOLED = "pooled"

    """# Each contract item effectively manages its own commitment budget."""  # noqa: E501

    PER_ITEM = "per_item"

    def __str__(self) -> str:
        return str(self.value)
