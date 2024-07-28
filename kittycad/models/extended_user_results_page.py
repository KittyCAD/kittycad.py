import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.extended_user import ExtendedUser
from .base64data import Base64Data


class ExtendedUserResultsPage(BaseModel):
    """A single page of results"""

    items: List[ExtendedUser]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
