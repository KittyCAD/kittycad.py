from typing import List, Optional

from ..models.inquiry_type import InquiryType
from .base import KittyCadBaseModel


class InquiryForm(KittyCadBaseModel):
    """The form for a public inquiry submission."""

    cad_platforms: Optional[List[str]] = None

    company: Optional[str] = None

    email: str

    first_name: str

    industry: Optional[str] = None

    inquiry_type: InquiryType

    job_title: Optional[str] = None

    last_name: str

    message: str

    num_cad_users: Optional[str] = None

    phone: Optional[str] = None
