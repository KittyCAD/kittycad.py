import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.rtc_sdp_type import RtcSdpType
from .base64data import Base64Data


class RtcSessionDescription(BaseModel):
    """SessionDescription is used to expose local and remote session descriptions."""

    sdp: str

    type: RtcSdpType

    model_config = ConfigDict(protected_namespaces=())
