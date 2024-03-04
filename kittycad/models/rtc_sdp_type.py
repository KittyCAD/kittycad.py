from enum import Enum


class RtcSdpType(str, Enum):
    """SDPType describes the type of an SessionDescription."""  # noqa: E501

    """# Unspecified indicates that the type is unspecified. """  # noqa: E501
    UNSPECIFIED = "unspecified"
    """# indicates that a description MUST be treated as an SDP offer. """  # noqa: E501
    OFFER = "offer"
    """# indicates that a description MUST be treated as an SDP answer, but not a final answer. A description used as an SDP pranswer may be applied as a response to an SDP offer, or an update to a previously sent SDP pranswer. """  # noqa: E501
    PRANSWER = "pranswer"
    """# indicates that a description MUST be treated as an SDP final answer, and the offer-answer exchange MUST be considered complete. A description used as an SDP answer may be applied as a response to an SDP offer or as an update to a previously sent SDP pranswer. """  # noqa: E501
    ANSWER = "answer"
    """# indicates that a description MUST be treated as canceling the current SDP negotiation and moving the SDP offer and answer back to what it was in the previous stable state. Note the local or remote SDP descriptions in the previous stable state could be null if there has not yet been a successful offer-answer negotiation. """  # noqa: E501
    ROLLBACK = "rollback"

    def __str__(self) -> str:
        return str(self.value)
