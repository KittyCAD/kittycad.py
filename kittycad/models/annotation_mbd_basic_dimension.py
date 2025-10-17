from typing import Optional

from ..models.mbd_symbol import MbdSymbol
from .base import KittyCadBaseModel


class AnnotationMbdBasicDimension(KittyCadBaseModel):
    """Parameters for defining an MBD basic dimension"""

    dimension: Optional[float] = None

    symbol: Optional[MbdSymbol] = None

    tolerance: float
