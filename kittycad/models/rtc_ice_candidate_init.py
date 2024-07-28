import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class RtcIceCandidateInit(BaseModel):
    """ICECandidateInit is used to serialize ice candidates"""

    candidate: str

    sdpMLineIndex: Optional[int] = None

    sdpMid: Optional[str] = None

    usernameFragment: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
