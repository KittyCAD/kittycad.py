from enum import Enum


class RtcIceProtocol(str, Enum):
    """ICEProtocol indicates the transport protocol type that is used in the ice.URL structure."""  # noqa: E501

    """# Unspecified indicates that the protocol is unspecified. """  # noqa: E501
    UNSPECIFIED = "unspecified"
    """# UDP indicates the URL uses a UDP transport. """  # noqa: E501
    UDP = "udp"
    """# TCP indicates the URL uses a TCP transport. """  # noqa: E501
    TCP = "tcp"

    def __str__(self) -> str:
        return str(self.value)
