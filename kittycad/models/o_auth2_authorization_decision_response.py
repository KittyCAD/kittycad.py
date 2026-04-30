from .base import KittyCadBaseModel


class OAuth2AuthorizationDecisionResponse(KittyCadBaseModel):
    """Result of approving or denying an OAuth authorization request."""

    redirect_url: str
