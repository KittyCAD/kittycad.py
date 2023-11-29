from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class Uuid(str):
    """A uuid stored as a varchar(191).

    A Version 4 UUID is a universally unique identifier that is generated using random numbers.
    """

    def __str__(self) -> str:
        return self

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(str))
