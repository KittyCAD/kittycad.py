from typing import List, Optional

from ..models.o_auth2_app_grant_type import OAuth2AppGrantType
from .base import KittyCadBaseModel


class UpdateOAuth2AppRequest(KittyCadBaseModel):
    """Request body for updating a public OAuth app."""

    grant_types: Optional[List[OAuth2AppGrantType]] = None

    name: Optional[str] = None

    redirect_uris: Optional[List[str]] = None
