import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.export_file import ExportFile
from .base64data import Base64Data


class Export(BaseModel):
    """The response from the `Export` endpoint."""

    files: List[ExportFile]

    model_config = ConfigDict(protected_namespaces=())
