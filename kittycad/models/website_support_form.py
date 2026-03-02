from typing import Optional

from ..models.support_inquiry_type import SupportInquiryType
from .base import KittyCadBaseModel


class WebsiteSupportForm(KittyCadBaseModel):
    """Request body for website support form submissions."""

    company: Optional[str] = None

    email: str

    first_name: str

    inquiry_type: SupportInquiryType

    last_name: str

    message: str

    phone: Optional[str] = None
