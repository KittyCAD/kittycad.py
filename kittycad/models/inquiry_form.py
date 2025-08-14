from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.inquiry_type import InquiryType


class InquiryForm(BaseModel):
    """The form for a public inquiry submission."""

    company: Optional[str] = None

    email: str

    first_name: str

    industry: Optional[str] = None

    inquiry_type: InquiryType

    last_name: str

    message: str

    phone: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
