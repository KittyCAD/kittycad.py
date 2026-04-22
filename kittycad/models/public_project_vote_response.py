from .base import KittyCadBaseModel


class PublicProjectVoteResponse(KittyCadBaseModel):
    """Signed-in viewer vote state for a public project."""

    like_count: int

    liked: bool
