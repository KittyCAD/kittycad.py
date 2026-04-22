from enum import Enum


class BillingItemCode(str, Enum):
    """Canonical product or service code for a contract item."""  # noqa: E501

    """# Fixed or recurring enterprise support entitlement."""  # noqa: E501

    ENTERPRISE_SUPPORT = "enterprise_support"

    """# Full deployment environment or similar managed environment charge."""  # noqa: E501

    FDE = "fde"

    """# GovCloud-specific management or hosting charge."""  # noqa: E501

    GOVCLOUD_MANAGEMENT = "govcloud_management"

    """# Billing for the first successful conversion of a file version."""  # noqa: E501

    FILE_INGESTION_CONVERSION = "file_ingestion_conversion"

    """# Contract-rated API usage credits."""  # noqa: E501

    LICENSED_API_CREDITS = "licensed_api_credits"

    def __str__(self) -> str:
        return str(self.value)
