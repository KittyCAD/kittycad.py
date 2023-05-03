from enum import Enum


class ApiCallQueryGroupBy(str, Enum):
    """The field of an API call to group by."""  # noqa: E501

    """# The email of the user that requested the API call. """  # noqa: E501
    EMAIL = "email"
    """# The HTTP method of the API call. """  # noqa: E501
    METHOD = "method"
    """# The endpoint of the API call. """  # noqa: E501
    ENDPOINT = "endpoint"
    """# The user ID of the user that requested the API call. """  # noqa: E501
    USER_ID = "user_id"
    """# The origin of the API call. This is parsed from the `Origin` header. """  # noqa: E501
    ORIGIN = "origin"
    """# The IP address of the user making the API call. """  # noqa: E501
    IP_ADDRESS = "ip_address"

    def __str__(self) -> str:
        return str(self.value)
