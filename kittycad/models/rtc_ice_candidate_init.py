from typing import Optional

from .base import KittyCadBaseModel


class RtcIceCandidateInit(KittyCadBaseModel):
    """ICECandidateInit is used to serialize ice candidates"""

    candidate: str

    sdpMLineIndex: Optional[int] = None

    sdpMid: Optional[str] = None

    usernameFragment: Optional[str] = None
