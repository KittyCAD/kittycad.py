
from pydantic import BaseModel, ConfigDict



class ModelingSessionData(BaseModel):
    """Successful Websocket response."""

    api_call_id: str

    model_config = ConfigDict(protected_namespaces=())
