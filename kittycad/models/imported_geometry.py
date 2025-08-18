from typing import List

from .base import KittyCadBaseModel


class ImportedGeometry(KittyCadBaseModel):
    """Data from importing the files"""

    id: str

    value: List[str]
