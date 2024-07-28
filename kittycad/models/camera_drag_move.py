import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.camera_settings import CameraSettings
from .base64data import Base64Data


class CameraDragMove(BaseModel):
    """The response from the `CameraDragMove` command. Note this is an \"unreliable\" channel message, so this data may need more data like a \"sequence\" """

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
