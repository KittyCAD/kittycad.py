from typing import Optional

from pydantic import BaseModel



class RtcIceCandidateInit(BaseModel):
    """ICECandidateInit is used to serialize ice candidates"""

    candidate: str

    sdpMLineIndex: Optional[int] = None

    sdpMid: Optional[str] = None

    usernameFragment: Optional[str] = None
