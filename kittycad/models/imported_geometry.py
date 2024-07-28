import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class ImportedGeometry(BaseModel):
    """Data from importing the files"""

    id: str

    value: List[str]

    model_config = ConfigDict(protected_namespaces=())
