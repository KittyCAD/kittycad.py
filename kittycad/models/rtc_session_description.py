
from pydantic import BaseModel

from ..models.rtc_sdp_type import RtcSdpType


class RtcSessionDescription(BaseModel):
    """SessionDescription is used to expose local and remote session descriptions."""

    sdp: str

    type: RtcSdpType
