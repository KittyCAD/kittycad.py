from enum import Enum


class Method(str, Enum):
    OPTIONS = 'OPTIONS'
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    HEAD = 'HEAD'
    TRACE = 'TRACE'
    CONNECT = 'CONNECT'
    PATCH = 'PATCH'
    EXTENSION = 'EXTENSION'

    def __str__(self) -> str:
        return str(self.value)
