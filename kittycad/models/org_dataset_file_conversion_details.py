from ..models.org_dataset_file_conversion_summary import OrgDatasetFileConversionSummary
from .base import KittyCadBaseModel


class OrgDatasetFileConversionDetails(KittyCadBaseModel):
    """Detailed response that bundles conversion metadata with the converted file contents."""

    conversion: OrgDatasetFileConversionSummary

    output: str
