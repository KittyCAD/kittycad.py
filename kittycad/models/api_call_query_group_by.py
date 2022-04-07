from enum import Enum


class ApiCallQueryGroupBy(str, Enum):
    EMAIL = 'email'
    METHOD = 'method'
    ENDPOINT = 'endpoint'
    USER_ID = 'user_id'
    ORIGIN = 'origin'
    IP_ADDRESS = 'ip_address'

    def __str__(self) -> str:
        return str(self.value)
