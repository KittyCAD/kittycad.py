from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class UuidBinary(str):
    """A uuid stored as binary(16).

    Mysql binary(16) storage for UUIDs. Uses Version 7 UUID by default, a universally unique identifier that is generated using random numbers and a timestamp. UUIDv7 are recommended for database ids/primary keys because they are sequential and this helps with efficient indexing, especially on MySQL. For other uses cases, like API tokens, UUIDv4 makes more sense because it's completely random.

    However, both should be stored as binary on MySQL! Both versions use the same data format, so they can be used interchangeably with this data type.
    """

    def __str__(self) -> str:
        return self

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(str))
