
from pydantic import BaseModel, ConfigDict



class Gateway(BaseModel):
    """Gateway information."""

    auth_timeout: int = 0

    host: str = ""

    name: str = ""

    port: int = 0

    tls_timeout: int = 0

    model_config = ConfigDict(protected_namespaces=())
