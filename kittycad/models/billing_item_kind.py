from enum import Enum


class BillingItemKind(str, Enum):
    """Pricing model used by a contract item."""  # noqa: E501

    """# A flat amount that does not vary with measured usage."""  # noqa: E501

    FIXED_FEE = "fixed_fee"

    """# Usage is rated by one or more explicit pricing tiers."""  # noqa: E501

    USAGE_TIERED = "usage_tiered"

    """# Usage burns down a commitment bucket before any overage path."""  # noqa: E501

    USAGE_COMMITMENT_BUCKET = "usage_commitment_bucket"

    def __str__(self) -> str:
        return str(self.value)
