from enum import Enum


class Method(str, Enum):
    """The Request Method (VERB)

    This type also contains constants for a number of common HTTP methods such as GET, POST, etc.

    Currently includes 8 variants representing the 8 methods defined in [RFC 7230](https://tools.ietf.org/html/rfc7231#section-4.1), plus PATCH, and an Extension variant for all extensions.
    """  # noqa: E501

    """# The `OPTIONS` method as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.2.1). """  # noqa: E501
    OPTIONS = "OPTIONS"
    """# The `GET` method as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3.1). """  # noqa: E501
    GET = "GET"
    """# The `POST` method as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3.1). """  # noqa: E501
    POST = "POST"
    """# The `PUT` method as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3.1). """  # noqa: E501
    PUT = "PUT"
    """# The `DELETE` method as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3.5). """  # noqa: E501
    DELETE = "DELETE"
    """# The `HEAD` method as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3.2). """  # noqa: E501
    HEAD = "HEAD"
    """# The `TRACE` method as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3). """  # noqa: E501
    TRACE = "TRACE"
    """# The `CONNECT` method as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4.3.6). """  # noqa: E501
    CONNECT = "CONNECT"
    """# The `PATCH` method as defined in [RFC 5789](https://tools.ietf.org/html/rfc5789). """  # noqa: E501
    PATCH = "PATCH"
    """# A catch all. """  # noqa: E501
    EXTENSION = "EXTENSION"

    def __str__(self) -> str:
        return str(self.value)
