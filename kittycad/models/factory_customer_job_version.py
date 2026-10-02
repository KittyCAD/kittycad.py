import datetime
from typing import Any, List

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FactoryCustomerJobVersion(KittyCadBaseModel):
    """Customer-visible snapshot of the current job version. File names are display metadata; no private storage URI or download capability is exposed."""

    created_at: datetime.datetime

    file_names: List[str]

    id: Uuid

    specs: Any
