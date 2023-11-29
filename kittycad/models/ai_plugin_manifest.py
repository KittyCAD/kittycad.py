from typing import Optional

from pydantic import BaseModel

from ..models.ai_plugin_api import AiPluginApi
from ..models.ai_plugin_auth import AiPluginAuth


class AiPluginManifest(BaseModel):
    """AI plugin manifest.

    This is used for OpenAI's ChatGPT plugins. You can read more about them [here](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest).
    """

    api: AiPluginApi

    auth: AiPluginAuth

    contact_email: Optional[str] = None

    description_for_human: Optional[str] = None

    description_for_model: Optional[str] = None

    legal_info_url: str

    logo_url: str

    name_for_human: Optional[str] = None

    name_for_model: Optional[str] = None

    schema_version: Optional[str] = None
