import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class KclCodeCompletionParams(BaseModel):
    """Extra params for the completions."""

    language: Optional[str] = None

    next_indent: Optional[int] = None

    prompt_tokens: Optional[int] = None

    suffix_tokens: Optional[int] = None

    trim_by_indentation: Optional[bool] = None

    model_config = ConfigDict(protected_namespaces=())
