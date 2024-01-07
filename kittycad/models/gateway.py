from typing import Optional

from pydantic import BaseModel, ConfigDict



class Gateway(BaseModel):
    """Gateway information."""

    auth_timeout: Optional[int] = None

    host: Optional[str] = None

    name: Optional[str] = None

    port: Optional[int] = None

    tls_timeout: Optional[int] = None

    model_config = ConfigDict(protected_namespaces=())
