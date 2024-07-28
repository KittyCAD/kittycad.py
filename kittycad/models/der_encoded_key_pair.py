
from pydantic import BaseModel, ConfigDict

from .base64data import Base64Data


class DerEncodedKeyPair(BaseModel):
    """The DER encoded key pair."""

    private_key: Base64Data

    public_cert: Base64Data

    model_config = ConfigDict(protected_namespaces=())
