from typing import List, Optional

from ..models.o_auth2_app_grant_type import OAuth2AppGrantType
from ..models.o_auth2_app_mode import OAuth2AppMode
from .base import KittyCadBaseModel


class UpdateOAuth2AppRequest(KittyCadBaseModel):
    """Request body for updating a public OAuth app."""

    grant_types: Optional[List[OAuth2AppGrantType]] = None

    mode: Optional[OAuth2AppMode] = None

    name: Optional[str] = None

    redirect_uris: Optional[List[str]] = None
