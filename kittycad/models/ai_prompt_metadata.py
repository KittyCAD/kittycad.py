from typing import Optional

from pydantic import BaseModel, ConfigDict



class AiPromptMetadata(BaseModel):
    """Metadata for an AI prompt."""

    code: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
