"""Generated enum examples must evaluate to the corresponding model member."""

from enum import Enum
from types import ModuleType

import pytest

from generate.generate import generate_type_and_example_python
from generate.type_generators import generate_enum_type_code


@pytest.mark.parametrize("documented", [False, True])
@pytest.mark.parametrize(
    ("value", "member_name"),
    [
        ("1.0", "VAL_1_0"),
        ("3.0-preview", "VAL_3_0_PREVIEW"),
        ("", "EMPTY"),
        ("1", "ONE"),
        ("2", "TWO"),
        ("3", "THREE"),
        ("active", "ACTIVE"),
    ],
)
def test_enum_example_evaluates_to_generated_member(
    value: str, member_name: str, documented: bool
) -> None:
    enum_schema = {"type": "string", "enum": [value]}
    schema = {"oneOf": [enum_schema]} if documented else enum_schema
    generated = generate_enum_type_code("ExampleEnum", schema)
    _, example, _ = generate_type_and_example_python(
        "ExampleEnum", schema, {}, None, None
    )

    module = ModuleType("generated_enum")
    exec(generated, module.__dict__)
    member = eval(example, module.__dict__)

    assert isinstance(member, Enum)
    assert member.value == value
    assert member.name == member_name
