from enum import Enum


class RtcIceCandidateType(str, Enum):
    """ICECandidateType represents the type of the ICE candidate used."""  # noqa: E501

    """# Unspecified indicates that the candidate type is unspecified. """  # noqa: E501
    UNSPECIFIED = "unspecified"
    """# ICECandidateTypeHost indicates that the candidate is of Host type as described in <https://tools.ietf.org/html/rfc8445#section-5.1.1.1>. A candidate obtained by binding to a specific port from an IP address on the host. This includes IP addresses on physical interfaces and logical ones, such as ones obtained through VPNs. """  # noqa: E501
    HOST = "host"
    """# ICECandidateTypeSrflx indicates the the candidate is of Server Reflexive type as described <https://tools.ietf.org/html/rfc8445#section-5.1.1.2>. A candidate type whose IP address and port are a binding allocated by a NAT for an ICE agent after it sends a packet through the NAT to a server, such as a STUN server. """  # noqa: E501
    SRFLX = "srflx"
    """# ICECandidateTypePrflx indicates that the candidate is of Peer Reflexive type. A candidate type whose IP address and port are a binding allocated by a NAT for an ICE agent after it sends a packet through the NAT to its peer. """  # noqa: E501
    PRFLX = "prflx"
    """# ICECandidateTypeRelay indicates the the candidate is of Relay type as described in <https://tools.ietf.org/html/rfc8445#section-5.1.1.2>. A candidate type obtained from a relay server, such as a TURN server. """  # noqa: E501
    RELAY = "relay"

    def __str__(self) -> str:
        return str(self.value)
