import base64
from typing import Any, Type

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema


class Base64Data(bytes):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.union_schema(
                [
                    core_schema.str_schema(),
                    core_schema.bytes_schema(),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                cls.serialize
            ),
        )

    @classmethod
    def validate(cls, v):
        return base64.urlsafe_b64decode(v.strip("=") + "===")

    @classmethod
    def serialize(cls, v: "Base64Data") -> bytes:
        return v
