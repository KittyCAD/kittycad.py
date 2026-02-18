from typing import List

from ..models.org_dataset_file_conversion_summary import OrgDatasetFileConversionSummary
from ..models.org_dataset_snapshot_image import OrgDatasetSnapshotImage
from .base import KittyCadBaseModel


class OrgDatasetFileConversionDetails(KittyCadBaseModel):
    """Detailed response that bundles conversion metadata with converted file and snapshot contents."""

    conversion: OrgDatasetFileConversionSummary

    original_snapshot_images: List[OrgDatasetSnapshotImage]

    output: str

    raw_kcl_snapshot_images: List[OrgDatasetSnapshotImage]

    salon_kcl_snapshot_images: List[OrgDatasetSnapshotImage]
