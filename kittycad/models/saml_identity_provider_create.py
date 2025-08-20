from typing import Optional

from ..models.der_encoded_key_pair import DerEncodedKeyPair
from ..models.idp_metadata_source import IdpMetadataSource
from .base import KittyCadBaseModel


class SamlIdentityProviderCreate(KittyCadBaseModel):
    """Parameters for creating a SAML identity provider."""

    idp_entity_id: Optional[str] = None

    idp_metadata_source: IdpMetadataSource

    signing_keypair: Optional[DerEncodedKeyPair] = None

    technical_contact_email: Optional[str] = None
