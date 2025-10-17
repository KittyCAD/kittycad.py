from typing import Optional

from ..models.mbd_symbol import MbdSymbol
from .base import KittyCadBaseModel


class AnnotationMbdControlFrame(KittyCadBaseModel):
    """Parameters for defining an MBD Geometric control frame"""

    diameter_symbol: Optional[MbdSymbol] = None

    modifier: Optional[MbdSymbol] = None

    primary_datum: Optional[str] = None

    secondary_datum: Optional[str] = None

    symbol: MbdSymbol

    tertiary_datum: Optional[str] = None

    tolerance: float
