from typing import List, Optional

from ..models.o_auth2_app_grant_type import OAuth2AppGrantType
from .base import KittyCadBaseModel


class CreateOAuth2AppRequest(KittyCadBaseModel):
    """Request body for creating a public OAuth app."""

    grant_types: Optional[List[OAuth2AppGrantType]] = None

    name: str

    redirect_uris: Optional[List[str]] = None
