from .base import KittyCadBaseModel


class ClientErrorReportAccepted(KittyCadBaseModel):
    """Response acknowledging that the error report was accepted for logging."""

    accepted: bool
