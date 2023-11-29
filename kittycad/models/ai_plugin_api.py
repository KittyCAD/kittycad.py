from typing import Optional

from pydantic import BaseModel

from ..models.ai_plugin_api_type import AiPluginApiType


class AiPluginApi(BaseModel):
    """AI plugin api information."""

    is_user_authenticated: Optional[bool] = None

    type: Optional[AiPluginApiType] = None

    url: str
