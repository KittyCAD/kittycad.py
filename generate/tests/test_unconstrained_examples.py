"""Unconstrained JSON fields must have usable generated examples."""

import json
from types import ModuleType

import pytest

from generate.generate import generate_type_and_example_python
from generate.type_generators import generate_object_type_code


@pytest.mark.parametrize(
    "field_schema",
    [{}, {"description": "JSON Schema describing the command arguments."}],
)
def test_unconstrained_field_example_serializes_in_referenced_model(
    field_schema,
) -> None:
    command_schema = {
        "type": "object",
        "properties": {
            "input_schema": field_schema,
        },
        "required": ["input_schema"],
    }
    data = {"components": {"schemas": {"ClientCommand": command_schema}}}
    generated = generate_object_type_code(
        "ClientCommand", command_schema, "object", data, None, None
    )
    _, example, _ = generate_type_and_example_python(
        "",
        {"type": "array", "items": {"$ref": "#/components/schemas/ClientCommand"}},
        data,
        None,
        None,
    )

    module = ModuleType("kittycad.models.generated_client_command")
    module.__package__ = "kittycad.models"
    exec(generated, module.__dict__)
    commands = eval(example, module.__dict__)

    assert len(commands) == 1
    assert json.loads(commands[0].model_dump_json()) == {"input_schema": {}}
