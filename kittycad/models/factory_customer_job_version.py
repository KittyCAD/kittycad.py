import datetime
from typing import Any, List

from ..models.factory_customer_job_file import FactoryCustomerJobFile
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FactoryCustomerJobVersion(KittyCadBaseModel):
    """Customer-visible submitted snapshot with authenticated Factory download links."""

    created_at: datetime.datetime

    file_names: List[str]

    files: List[FactoryCustomerJobFile]

    id: Uuid

    specs: Any
