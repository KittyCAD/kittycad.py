from enum import Enum


class InquiryType(str, Enum):
    """The type of inquiry."""  # noqa: E501

    """# Inquiries related to pilots (on the enterprise page)."""  # noqa: E501

    PILOT_INQUIRY = "pilot_inquiry"

    """# General inquiry about the service or product."""  # noqa: E501

    GENERAL_INQUIRY = "general_inquiry"

    """# Questions related to sales or purchasing."""  # noqa: E501

    SALES_QUESTION = "sales_question"

    """# Inquiry from a developer, typically technical in nature."""  # noqa: E501

    DEVELOPER_INQUIRY = "developer_inquiry"

    """# Opportunity for partnership or collaboration."""  # noqa: E501

    PARTNERSHIP_OPPORTUNITY = "partnership_opportunity"

    """# Other inquiries related to sales that do not fit predefined categories."""  # noqa: E501

    OTHER_SALES_INQUIRY = "other_sales_inquiry"

    """# Request for technical support or troubleshooting."""  # noqa: E501

    TECHNICAL_SUPPORT = "technical_support"

    """# Questions or requests related to account management."""  # noqa: E501

    ACCOUNT_MANAGEMENT = "account_management"

    """# Other support-related inquiries that do not fit predefined categories."""  # noqa: E501

    OTHER_SUPPORT_INQUIRY = "other_support_inquiry"

    def __str__(self) -> str:
        return str(self.value)
