import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.async_api_call import AsyncApiCall
from .base64data import Base64Data


class AsyncApiCallResultsPage(BaseModel):
    """A single page of results"""

    items: List[AsyncApiCall]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
