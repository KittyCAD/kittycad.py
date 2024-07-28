import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.ai_prompt import AiPrompt
from .base64data import Base64Data


class AiPromptResultsPage(BaseModel):
    """A single page of results"""

    items: List[AiPrompt]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
