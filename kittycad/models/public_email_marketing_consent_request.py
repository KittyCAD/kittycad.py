from .base import KittyCadBaseModel


class PublicEmailMarketingConsentRequest(KittyCadBaseModel):
    """The data for subscribing a user to the newsletter."""

    email: str
