"""Tests for model type generation."""

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
