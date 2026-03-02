from typing import List, Optional

from ..models.sales_inquiry_type import SalesInquiryType
from .base import KittyCadBaseModel


class WebsiteSalesForm(KittyCadBaseModel):
    """Request body for website sales form submissions."""

    cad_platforms: Optional[List[str]] = None

    company: Optional[str] = None

    email: str

    first_name: str

    industry: Optional[str] = None

    inquiry_type: SalesInquiryType

    job_title: Optional[str] = None

    last_name: str

    message: str

    num_cad_users: Optional[str] = None

    phone: Optional[str] = None
