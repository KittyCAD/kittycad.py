import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.camera_settings import CameraSettings
from .base64data import Base64Data


class DefaultCameraGetSettings(BaseModel):
    """The response from the `DefaultCameraGetSettings` command."""

    settings: CameraSettings

    model_config = ConfigDict(protected_namespaces=())
