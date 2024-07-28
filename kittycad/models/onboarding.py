import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class Onboarding(BaseModel):
    """Onboarding details"""

    first_call_from_modeling_app_date: Optional[datetime.datetime] = None

    first_call_from_text_to_cad_date: Optional[datetime.datetime] = None

    first_token_date: Optional[datetime.datetime] = None

    model_config = ConfigDict(protected_namespaces=())
