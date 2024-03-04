from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class Currency(str):
    """Currency is the list of supported currencies. Always lowercase.

    This comes from the Stripe API docs: For more details see <https://support.stripe.com/questions/which-currencies-does-stripe-support>.
    """

    def __str__(self) -> str:
        return self

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(str))
