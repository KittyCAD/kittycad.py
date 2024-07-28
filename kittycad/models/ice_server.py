import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class IceServer(BaseModel):
    """Representation of an ICE server used for STUN/TURN Used to initiate WebRTC connections based on <https://developer.mozilla.org/en-US/docs/Web/API/RTCIceServer>"""

    credential: Optional[str] = None

    urls: List[str]

    username: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
