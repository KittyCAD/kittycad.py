from typing import Optional

from ..models.selected_region import SelectedRegion
from .base import KittyCadBaseModel


class SelectRegionFromPoint(KittyCadBaseModel):
    """The response from the 'SelectRegionFromPoint'. If there are multiple ways to construct this region, this chooses arbitrarily."""

    region: Optional[SelectedRegion] = None
