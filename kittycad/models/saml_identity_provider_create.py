import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.idp_metadata_source import IdpMetadataSource


from ..models.der_encoded_key_pair import DerEncodedKeyPair



class SamlIdentityProviderCreate(BaseModel):
    """Parameters for creating a SAML identity provider."""
    
    
    idp_entity_id: Optional[str] = None
    
    
    
    idp_metadata_source: IdpMetadataSource
    
    
    
    signing_keypair: Optional[DerEncodedKeyPair] = None
    
    
    
    technical_contact_email: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )