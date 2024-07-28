from typing import Optional

from pydantic import BaseModel, ConfigDict



class AppClientInfo(BaseModel):
    """Information about a third party app client."""

    url: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
