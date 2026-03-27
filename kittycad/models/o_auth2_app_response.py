import datetime
from typing import List

from ..models.o_auth2_app_client_type import OAuth2AppClientType
from ..models.o_auth2_app_grant_type import OAuth2AppGrantType
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OAuth2AppResponse(KittyCadBaseModel):
    """API response for a managed OAuth app."""

    client_id: Uuid

    client_type: OAuth2AppClientType

    created_at: datetime.datetime

    first_party: bool

    grant_types: List[OAuth2AppGrantType]

    is_active: bool

    name: str

    updated_at: datetime.datetime
