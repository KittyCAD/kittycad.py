import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class Point3d(BaseModel):
    """A point in 3D space"""

    x: float

    y: float

    z: float

    model_config = ConfigDict(protected_namespaces=())
