from typing import List, Optional

from ..models.execution_job_response import ExecutionJobResponse
from .base import KittyCadBaseModel


class ExecutionJobResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ExecutionJobResponse]

    next_page: Optional[str] = None
