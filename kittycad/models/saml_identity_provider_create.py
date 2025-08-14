from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.der_encoded_key_pair import DerEncodedKeyPair
from ..models.idp_metadata_source import IdpMetadataSource


class SamlIdentityProviderCreate(BaseModel):
    """Parameters for creating a SAML identity provider."""

    idp_entity_id: Optional[str] = None

    idp_metadata_source: IdpMetadataSource

    signing_keypair: Optional[DerEncodedKeyPair] = None

    technical_contact_email: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
