from ..models.rtc_sdp_type import RtcSdpType
from .base import KittyCadBaseModel


class RtcSessionDescription(KittyCadBaseModel):
    """SessionDescription is used to expose local and remote session descriptions."""

    sdp: str

    type: RtcSdpType
