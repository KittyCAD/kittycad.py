"""Tests for model type generation."""

import json
import subprocess
import sys
import warnings
from types import ModuleType

import pytest
from pydantic import ValidationError

from generate.generate import generate_type_and_example_python
from generate.type_generators import generate_object_type_code


def test_omissible_fields_default_to_none():
    schema = {
        "type": "object",
        "properties": {
            "required_name": {"type": "string"},
            "required_nullable_note": {"type": "string", "nullable": True},
            "optional_label": {"type": "string"},
            "optional_nullable_description": {"type": "string", "nullable": True},
        },
        "required": ["required_name", "required_nullable_note"],
    }

    generated = generate_object_type_code(
        "ExamplePayload", schema, "object", {}, None, None
    )

    assert "required_name: str" in generated
    assert "required_nullable_note: Optional[str]\n" in generated
    assert "required_nullable_note: Optional[str] = None" not in generated
    assert "optional_label: Optional[str] = None" in generated
    assert "optional_nullable_description: Optional[str] = None" in generated


def test_ref_matching_generated_class_name_is_aliased():
    schema = {
        "type": "object",
        "properties": {
            "entity_reference": {
                "nullable": True,
                "allOf": [{"$ref": "#/components/schemas/EntityReference"}],
            },
        },
    }

    generated = generate_object_type_code(
        "EntityReference", schema, "object", {}, None, None
    )

    assert (
        "from ..models.entity_reference import EntityReference as EntityReferenceModel"
        in generated
    )
    assert "class EntityReference(KittyCadBaseModel):" in generated
    assert "entity_reference: Optional[EntityReferenceModel] = None" in generated


@pytest.mark.parametrize(
    ("required", "field_schema", "default"),
    [
        (True, {"type": "string"}, None),
        (False, {"type": "string"}, None),
        (False, {"type": "string", "default": "ap242"}, "ap242"),
    ],
)
def test_schema_field_alias_preserves_input_and_output(required, field_schema, default):
    schema = {
        "type": "object",
        "properties": {"schema": field_schema},
        "required": ["schema"] if required else [],
    }
    generated = generate_object_type_code(
        "ExamplePayload", schema, "object", {}, None, None
    )
    module = ModuleType("kittycad.models.generated_example_payload")
    module.__package__ = "kittycad.models"
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "error", message='Field name "schema"', category=UserWarning
        )
        exec(generated, module.__dict__)
    model = module.ExamplePayload

    for field_name in ("schema", "schema_"):
        instance = model.model_validate({field_name: "ap203"})
        assert instance.schema_ == "ap203"
        assert instance.to_dict() == {"schema": "ap203"}
        assert json.loads(instance.to_json()) == {"schema": "ap203"}

    if required:
        with pytest.raises(ValidationError):
            model()
    else:
        assert model().schema_ == default

    _, example, _ = generate_type_and_example_python(
        "ExamplePayload", schema, {}, None, None
    )
    assert eval(example, module.__dict__).schema_ is not None


def test_step_schema_alias_preserves_nested_request_payload():
    from kittycad.models.output_format3d import OptionStep, OutputFormat3d
    from kittycad.models.step_schema import StepSchema
    from kittycad.types import serialize_request_body

    assert OptionStep().schema_ == "ap242"
    for field_name in ("schema", "schema_"):
        step = OptionStep.model_validate({field_name: "ap203", "coords": None})
        assert step.schema_ == "ap203"
        step.schema_ = StepSchema.AP214
        payload = json.loads(serialize_request_body(OutputFormat3d(step)))
        assert payload["schema"] == "ap214"
        assert "schema_" not in payload

    step = OptionStep(schema=None, coords=None)
    payload = json.loads(serialize_request_body(OutputFormat3d(step)))
    assert "schema" in payload
    assert payload["schema"] is None


def test_sdk_import_has_no_schema_shadowing_warning():
    subprocess.run(
        [sys.executable, "-W", "error::UserWarning", "-c", "import kittycad"],
        check=True,
        capture_output=True,
        text=True,
    )
