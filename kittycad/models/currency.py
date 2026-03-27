from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class Currency(str):
    """A billing currency code.

    This is intentionally billing-owned instead of Stripe-owned, so contract and manual invoice flows can use the same validated type without reaching back into a provider-specific crate."""

    def __str__(self) -> str:
        return self

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(str))
