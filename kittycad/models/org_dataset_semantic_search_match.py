from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class OrgDatasetSemanticSearchMatch(KittyCadBaseModel):
    """Semantic-search match returned for an org dataset chunk."""

    chunk_index: int

    content: str

    conversion_id: Uuid

    similarity: float

    source_file_path: str
