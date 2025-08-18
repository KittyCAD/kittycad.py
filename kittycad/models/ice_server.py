from typing import List, Optional

from .base import KittyCadBaseModel


class IceServer(KittyCadBaseModel):
    """Representation of an ICE server used for STUN/TURN Used to initiate WebRTC connections based on <https://developer.mozilla.org/en-US/docs/Web/API/RTCIceServer>"""

    credential: Optional[str] = None

    urls: List[str]

    username: Optional[str] = None
