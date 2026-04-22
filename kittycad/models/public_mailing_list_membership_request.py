from .base import KittyCadBaseModel


class PublicMailingListMembershipRequest(KittyCadBaseModel):
    """Request body for public mailing-list membership changes."""

    email: str
