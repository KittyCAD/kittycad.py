from .base import KittyCadBaseModel
from .base64data import Base64Data


class DerEncodedKeyPair(KittyCadBaseModel):
    """The DER encoded key pair."""

    private_key: Base64Data

    public_cert: Base64Data
