from enum import Enum


class SupportInquiryType(str, Enum):
    """The type of support inquiry for website support forms."""  # noqa: E501

    """# Request for technical support or troubleshooting."""  # noqa: E501

    TECHNICAL_SUPPORT = "technical_support"

    """# Questions or requests related to account management."""  # noqa: E501

    ACCOUNT_MANAGEMENT = "account_management"

    """# Other support-related inquiries that do not fit predefined categories."""  # noqa: E501

    OTHER_SUPPORT_INQUIRY = "other_support_inquiry"

    def __str__(self) -> str:
        return str(self.value)
