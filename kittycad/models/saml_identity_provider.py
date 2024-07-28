import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.uuid import Uuid
from .base64data import Base64Data


class SamlIdentityProvider(BaseModel):
    """A SAML identity provider."""

    acs_url: str

    created_at: datetime.datetime

    id: Uuid

    idp_entity_id: Optional[str] = None

    idp_metadata_document_string: Optional[str] = None

    org_id: Uuid

    private_key: Optional[Base64Data] = None

    public_cert: Optional[Base64Data] = None

    slo_url: str

    technical_contact_email: Optional[str] = None

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
