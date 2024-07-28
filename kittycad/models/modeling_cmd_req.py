import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from .base64data import Base64Data


class ModelingCmdReq(BaseModel):
    """A graphics command submitted to the KittyCAD engine via the Modeling API."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId

    model_config = ConfigDict(protected_namespaces=())
