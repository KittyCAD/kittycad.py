from typing import Dict

from .base import KittyCadBaseModel


class CreateRegion(KittyCadBaseModel):
    """The response from the 'CreateRegion'. The region should have an ID taken from the ID of the 'CreateRegion' modeling command."""

    region_mapping: Dict[str, str]
