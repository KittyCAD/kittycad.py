from .base import KittyCadBaseModel


class UploadOrgDatasetFilesResponse(KittyCadBaseModel):
    """Response payload for uploading files into a Zoo-managed dataset."""

    queued_conversions: int

    uploaded_files: int
