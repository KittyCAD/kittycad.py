from typing import Optional

from ..models.inquiry_type import InquiryType
from .base import KittyCadBaseModel


class InquiryForm(KittyCadBaseModel):
    """The form for a public inquiry submission."""

    company: Optional[str] = None

    email: str

    first_name: str

    industry: Optional[str] = None

    inquiry_type: InquiryType

    last_name: str

    message: str

    phone: Optional[str] = None
