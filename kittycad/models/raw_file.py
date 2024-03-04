
from pydantic import BaseModel, ConfigDict



class RawFile(BaseModel):
    """A raw file with unencoded contents to be passed over binary websockets. When raw files come back for exports it is sent as binary/bson, not text/json."""

    contents: bytes

    name: str

    model_config = ConfigDict(protected_namespaces=())
