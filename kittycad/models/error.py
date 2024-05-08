
from pydantic import BaseModel, ConfigDict



class Error(BaseModel):
    """Error information from a response."""

    error_code: str

    message: str

    request_id: str

    model_config = ConfigDict(protected_namespaces=())
