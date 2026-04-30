import datetime
from typing import List, Optional

from ..models.o_auth2_scope import OAuth2Scope
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OAuth2AuthorizationRequestResponse(KittyCadBaseModel):
    """Details rendered by the OAuth consent page."""

    app_name: str

    expires_at: datetime.datetime

    owner_name: Optional[str] = None

    redirect_uri: str

    request_id: Uuid

    scopes: List[OAuth2Scope]
