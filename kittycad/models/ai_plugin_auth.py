from typing import Optional

from pydantic import BaseModel

from ..models.ai_plugin_auth_type import AiPluginAuthType
from ..models.ai_plugin_http_auth_type import AiPluginHttpAuthType


class AiPluginAuth(BaseModel):
    """AI plugin auth information."""

    authorization_type: Optional[AiPluginHttpAuthType] = None

    type: Optional[AiPluginAuthType] = None
