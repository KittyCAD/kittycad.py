"""Type generation utilities for generating Python types from API schemas."""

import logging
import os
import random
from typing import Any, List, Optional

from .schema_analysis import (
    get_any_of_description,
    get_content_one_of,
    get_one_of_description,
    get_tag_any_of,
    get_tag_one_of,
    is_enum_with_docs_one_of,
    is_nested_object_any_of,
    is_nested_object_one_of,
)
from .utils import (
    camel_to_screaming_snake,
    camel_to_snake,
    consolidate_imports_in_file,
    get_template,
    randletter,
    render_template_to_file,
    to_pascal_case,
)

# Set random seed for consistent letter generation
random.seed(10)


def generate_types(cwd: str, parser: dict):
    # Make sure we have the directory.
    path = os.path.join(cwd, "kittycad", "models")
    os.makedirs(path, exist_ok=True)

    # Open the __init__.py file.
    file_name = "__init__.py"
    file_path = os.path.join(path, file_name)
    f = open(file_path, "w")
    f.write('""" Contains all the data models used in inputs/outputs """\n')
    f.write("\n")

    # Generate the types.
    data = parser
    schemas = data["components"]["schemas"]
    generated_files = []

    for key in schemas:
        schema = schemas[key]
        logging.info("generating schema: %s", key)
        model_file_path = generate_type(path, key, schema, data)
        if model_file_path:
            generated_files.append(model_file_path)
        f.write("from ." + camel_to_snake(key) + " import " + key + "\n")

    # Add the base model import
    f.write("from .base import KittyCadBaseModel\n")

    # This is a hot fix for the empty type.
    # We likely need a better way to handle this.
    f.write("from .empty import Empty\n")

    # Close the file.
    f.close()

    # Consolidate imports in all generated model files
    for file_path in generated_files:
        if os.path.exists(file_path):
            consolidate_imports_in_file(file_path)


def generate_type(path: str, name: str, schema: dict, data: dict):
    file_path = path
    if path.endswith(".py") is False:
        # Generate the type.
        file_name = camel_to_snake(name) + ".py"
        file_path = os.path.join(path, file_name)

    if "type" in schema:
        type_name = schema["type"]
        if type_name == "object":
            generate_object_type(file_path, name, schema, type_name, data)
        elif type_name == "string" and "enum" in schema and schema["enum"] != [None]:
            generate_enum_type(file_path, name, schema, type_name, [])
        elif type_name == "integer":
            generate_integer_type(file_path, name, schema, type_name)
        elif type_name == "number":
            generate_float_type(file_path, name, schema, type_name)
        elif type_name == "string":
            generate_string_type(file_path, name, schema, type_name)
        else:
            logging.error("unsupported type: %s", type_name)
            raise Exception("unsupported type: ", type_name)
    elif "$ref" in schema:
        # Skip it since we will already have generated it.
        return None
    elif "oneOf" in schema:
        generate_one_of_type(file_path, name, schema, data)
    elif "anyOf" in schema:
        generate_any_of_type(file_path, name, schema, data)
    elif "description" in schema and not any(
        key in schema for key in ["type", "$ref", "oneOf", "anyOf", "allOf"]
    ):
        # This is just a description (possibly with nullable), treat it as Any
        generate_any_type(file_path, name, schema)
    else:
        logging.error("schema: %s", schema)
        logging.error("unsupported type: %s", name)
        raise Exception("unsupported type: ", name)

    return file_path


def generate_primitive_type(path: str, name: str, schema: dict, template_name: str):
    """Generic function to generate primitive types using templates.

    Args:
        path: Output file path
        name: Type name
        schema: Schema dictionary
        template_name: Name of the template file to use (e.g. "str.py.jinja2")
    """
    context = {
        "name": name,
        "description": schema.get("description", ""),
        "minimum": schema.get("minimum"),
        "maximum": schema.get("maximum"),
    }
    render_template_to_file(template_name, context, path)


def generate_string_type(path: str, name: str, schema: dict, type_name: str):
    """Generate a string type using the generic primitive generator."""
    generate_primitive_type(path, name, schema, "str.py.jinja2")


def generate_integer_type(path: str, name: str, schema: dict, type_name: str):
    """Generate an integer type using the generic primitive generator."""
    generate_primitive_type(path, name, schema, "int.py.jinja2")


def generate_float_type(path: str, name: str, schema: dict, type_name: str):
    """Generate a float type using the generic primitive generator."""
    generate_primitive_type(path, name, schema, "float.py.jinja2")


def generate_enum_type(
    path: str,
    name: str,
    schema: dict,
    type_name: str,
    enums: List[str],
):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    enum_code = generate_enum_type_code(name, schema, type_name, enums)
    f.write(enum_code)
    f.close()


def generate_enum_type_code(
    name: str,
    schema: dict,
    type_name: str = "string",
    additional_docs: Optional[List[str]] = None,
) -> str:
    from typing import List, TypedDict

    if additional_docs is None:
        additional_docs = []

    EnumItemType = TypedDict(
        "EnumItemType",
        {
            "name": str,
            "value": str,
            "description": str,
        },
    )

    enum_items: List[EnumItemType] = []

    # Handle oneOf enums with descriptions
    if "oneOf" in schema:
        for num, one_of in enumerate(schema["oneOf"]):
            if "enum" in one_of and len(one_of["enum"]) == 1:
                value = one_of["enum"][0]
                enum_name = camel_to_screaming_snake(value)
                if enum_name == "":
                    enum_name = "EMPTY"
                elif enum_name == "1":
                    enum_name = "ONE"
                elif enum_name == "2":
                    enum_name = "TWO"
                elif enum_name == "3":
                    enum_name = "THREE"
                elif enum_name[0].isdigit():
                    enum_name = "VAL_" + enum_name

                description = ""
                if "description" in one_of:
                    description = one_of["description"]
                elif len(additional_docs) > num and additional_docs[num] != "":
                    description = additional_docs[num]

                enum_items.append(
                    {
                        "name": enum_name,
                        "value": value,
                        "description": description,
                    }
                )
    else:
        # Standard string enum
        if "enum" in schema:
            for num, value in enumerate(schema["enum"], start=0):
                enum_name = camel_to_screaming_snake(value)
                if enum_name == "":
                    enum_name = "EMPTY"
                elif enum_name == "1":
                    enum_name = "ONE"
                elif enum_name == "2":
                    enum_name = "TWO"
                elif enum_name == "3":
                    enum_name = "THREE"
                elif enum_name[0].isdigit():
                    enum_name = "VAL_" + enum_name

                description = ""
                if len(additional_docs) > num and additional_docs[num] != "":
                    description = additional_docs[num]

                enum_items.append(
                    {
                        "name": enum_name,
                        "value": value,
                        "description": description,
                    }
                )

    template = get_template("enum.py.jinja2")
    return template.render(
        name=name, description=schema.get("description", ""), enum_items=enum_items
    )


def generate_any_of_type(path: str, name: str, schema: dict, data: dict):
    logging.info("generating type: %s at: %s", name, path)

    if is_enum_with_docs_one_of(schema):
        additional_docs = []
        enum = []
        # We want to treat this as an enum with additional docs.
        for any_of in schema["anyOf"]:
            enum.append(any_of["enum"][0])
            if "description" in any_of:
                additional_docs.append(any_of["description"])
            else:
                additional_docs.append("")
        # Write the enum.
        schema["enum"] = enum
        schema["type"] = "string"
        generate_enum_type(path, name, schema, "string", additional_docs)
        # return early.
        return

    # Open our file.
    f = open(path, "w")

    # Import the refs if there are any.
    all_options = []
    imported_refs: set[str] = set()  # Track imported refs to avoid duplicates
    for any_of in schema["anyOf"]:
        if "allOf" in any_of:
            for all_of in any_of["allOf"]:
                if "$ref" in all_of:
                    ref = all_of["$ref"]
                    ref_name = ref[ref.rfind("/") + 1 :]
                    f.write(
                        "from ."
                        + camel_to_snake(ref_name)
                        + " import "
                        + ref_name
                        + "\n"
                    )
                    all_options.append(ref_name)
        if "$ref" in any_of:
            ref = any_of["$ref"]
            ref_name = ref[ref.rfind("/") + 1 :]
            f.write("from ." + camel_to_snake(ref_name) + " import " + ref_name + "\n")
            all_options.append(ref_name)

    if is_nested_object_any_of(schema):
        # We want to write each of the nested objects.
        for any_of in schema["anyOf"]:
            # Get the nested object.
            if "properties" in any_of:
                for prop_name in any_of["properties"]:
                    nested_object = any_of["properties"][prop_name]
                    if nested_object == {}:
                        f.write("from typing import Any\n")
                        f.write(prop_name + " = Any\n")
                        f.write("\n")
                        all_options.append(prop_name)
                    elif "$ref" in nested_object:
                        ref = nested_object["$ref"]
                        ref_name = ref[ref.rfind("/") + 1 :]
                        f.write(
                            "from ."
                            + camel_to_snake(ref_name)
                            + " import "
                            + ref_name
                            + "\n"
                        )
                        f.write("\n")
                        if prop_name != ref_name:
                            f.write(prop_name + " = " + ref_name + "\n")
                            f.write("\n")
                        all_options.append(prop_name)
                    else:
                        class_name = to_pascal_case(prop_name)
                        object_code = generate_object_type_code(
                            prop_name,
                            nested_object,
                            "object",
                            data,
                            None,
                            None,
                            False,
                            imported_refs,
                        )
                        f.write(object_code)
                        f.write("\n")
                        all_options.append(class_name)
            elif "type" in any_of and any_of["type"] == "string":
                enum_code = generate_enum_type_code(
                    any_of["enum"][0], any_of, "string", []
                )
                f.write(enum_code)
                f.write("\n")
                all_options.append(any_of["enum"][0])

    # Check if each any_of has the same enum of one.
    tag = get_tag_any_of(schema)

    if tag is not None:
        # Generate each of the options from the tag WITH Option wrappers.
        for any_of in schema["anyOf"]:
            # Get the value of the tag.
            object_name = any_of["properties"][tag]["enum"][0]
            object_code = generate_object_type_code(
                object_name, any_of, "object", data, tag, None, True, imported_refs
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(to_pascal_case("option_" + object_name))
    else:
        # We want to write each of the nested objects WITHOUT Option wrappers.
        for any_of in schema["anyOf"]:
            # Get the nested object.
            if "properties" in any_of:
                for prop_name in any_of["properties"]:
                    nested_object = any_of["properties"][prop_name]
                    if nested_object == {}:
                        f.write("from typing import Any\n")
                        f.write(prop_name + " = Any\n")
                        f.write("\n")
                        all_options.append(prop_name)
                    elif "$ref" in nested_object:
                        ref = nested_object["$ref"]
                        ref_name = ref[ref.rfind("/") + 1 :]
                        f.write(
                            "from ."
                            + camel_to_snake(ref_name)
                            + " import "
                            + ref_name
                            + "\n"
                        )
                        f.write("\n")
                        if prop_name != ref_name:
                            f.write(prop_name + " = " + ref_name + "\n")
                            f.write("\n")
                        all_options.append(prop_name)
                    else:
                        class_name = to_pascal_case(prop_name)
                        object_code = generate_object_type_code(
                            prop_name,
                            nested_object,
                            "object",
                            data,
                            None,
                            None,
                            False,  # No Option wrapper when no tag
                            imported_refs,
                        )
                        f.write(object_code)
                        f.write("\n")
                        all_options.append(class_name)
            elif "type" in any_of and any_of["type"] == "string":
                enum_code = generate_enum_type_code(
                    any_of["enum"][0], any_of, "string", []
                )
                f.write(enum_code)
                f.write("\n")
                all_options.append(any_of["enum"][0])

    # Write the sum type.
    description = get_any_of_description(schema)
    content = generate_original_union_type(all_options, name, description, tag)
    f.write(content)

    # Close the file.
    f.close()


def generate_original_union_type(
    types: List[str], name: str, description: str, tag: Optional[str]
) -> str:
    from typing import TypedDict

    ArgType = TypedDict(
        "ArgType",
        {
            "name": str,
            "var0": str,
            "var1": str,
            "check": str,
            "value": str,
        },
    )
    TemplateType = TypedDict(
        "TemplateType",
        {
            "types": List[ArgType],
            "description": str,
            "name": str,
            "tag": Optional[str],
        },
    )
    template_info: TemplateType = {
        "types": [],
        "description": description,
        "name": name,
        "tag": tag,
    }
    for type in types:
        if type == "SuccessWebSocketResponse":
            template_info["types"].append(
                {
                    "name": type,
                    "var0": randletter(),
                    "var1": randletter(),
                    "check": "success",
                    "value": "True",
                }
            )
        elif type == "FailureWebSocketResponse":
            template_info["types"].append(
                {
                    "name": type,
                    "var0": randletter(),
                    "var1": randletter(),
                    "check": "success",
                    "value": "False",
                }
            )
        else:
            template_info["types"].append(
                {
                    "name": type,
                    "var0": randletter(),
                    "var1": randletter(),
                    "check": "type",
                    "value": '"' + type + '"',
                }
            )

    template = get_template("union-type.py.jinja2")
    content = template.render(**template_info)

    return content


def generate_one_of_type(path: str, name: str, schema: dict, data: dict):
    logging.info("generating type: %s at: %s", name, path)

    if is_enum_with_docs_one_of(schema):
        additional_docs = []
        enum = []
        # We want to treat this as an enum with additional docs.
        for one_of in schema["oneOf"]:
            enum.append(one_of["enum"][0])
            if "description" in one_of:
                additional_docs.append(one_of["description"])
            else:
                additional_docs.append("")
        # Write the enum.
        schema["enum"] = enum
        schema["type"] = "string"
        generate_enum_type(path, name, schema, "string", additional_docs)
        # return early.
        return

    # Open our file.
    f = open(path, "w")

    # Import the refs if there are any.
    all_options = []
    imported_refs: set[str] = set()  # Track imported refs to avoid duplicates
    for one_of in schema["oneOf"]:
        if "$ref" in one_of:
            ref = one_of["$ref"]
            ref_name = ref[ref.rfind("/") + 1 :]
            class_name = to_pascal_case(ref_name)
            # Use class name as the key to avoid importing same class multiple times regardless of path
            if class_name not in imported_refs:
                f.write(
                    "from ." + camel_to_snake(ref_name) + " import " + class_name + "\n"
                )
                imported_refs.add(class_name)
            all_options.append(class_name)

    tag = None
    content = None

    if is_nested_object_one_of(schema):
        alias_imports_needed = False
        for one_of in schema["oneOf"]:
            if "properties" not in one_of:
                continue

            props = list(one_of["properties"].items())
            if len(props) != 1:
                continue

            outer_name, outer_schema = props[0]

            wrap_entire_payload = (
                outer_schema.get("type") == "object" and "properties" in outer_schema
            )

            if wrap_entire_payload:
                inner_properties = outer_schema.get("properties", {})
                required_fields = outer_schema.get("required", [])
            else:
                inner_properties = {outer_name: outer_schema}
                required_fields = [outer_name]

            flattened_schema = {
                "type": "object",
                "description": one_of.get("description", ""),
                "properties": inner_properties,
            }
            if required_fields:
                flattened_schema["required"] = required_fields

            extra_imports = None
            extra_body_lines = []
            wrapped_key = outer_name

            if wrap_entire_payload:
                if not alias_imports_needed:
                    extra_imports = [
                        "from pydantic import model_serializer, model_validator\n"
                    ]
                    alias_imports_needed = True

                extra_body_lines.extend(
                    [
                        '    @model_validator(mode="before")',
                        "    @classmethod",
                        "    def _unwrap(cls, data):",
                        "        if isinstance(data, dict) and '"
                        + wrapped_key
                        + "' in data and isinstance(data['"
                        + wrapped_key
                        + "'], dict):",
                        "            return data['" + wrapped_key + "']",
                        "        return data",
                    ]
                )

                extra_body_lines.extend(
                    [
                        '    @model_serializer(mode="wrap")',
                        "    def _wrap(self, handler, info):",
                        "        payload = handler(self, info)",
                        "        return {'" + wrapped_key + "': payload}",
                    ]
                )

            object_code = generate_object_type_code(
                outer_name,
                flattened_schema,
                "object",
                data,
                None,
                None,
                False,
                imported_refs,
                extra_imports=extra_imports,
                extra_body_lines=extra_body_lines,
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(to_pascal_case(outer_name))
    else:
        # Check if each one_of has the same enum of one.
        tag = get_tag_one_of(schema)
        content = get_content_one_of(schema, tag)

        if tag is not None and content is not None:
            # Generate each of the options from the tag.
            for one_of in schema["oneOf"]:
                # Get the value of the tag.
                object_name = one_of["properties"][tag]["enum"][0]
                # Generate the type for the object.
                content_code = generate_object_type_code(
                    object_name + "_data",
                    one_of["properties"][content],
                    "object",
                    data,
                    None,
                    None,
                    False,
                    imported_refs,
                )
                f.write(content_code)
                f.write("\n")
                object_code = generate_object_type_code(
                    object_name,
                    one_of,
                    "object",
                    data,
                    tag,
                    content,
                    True,
                    imported_refs,
                )
                f.write(object_code)
                f.write("\n")
                all_options.append(to_pascal_case("option_" + object_name))
        elif tag is not None:
            # Generate each of the options from the tag.
            for one_of in schema["oneOf"]:
                # Get the value of the tag.
                object_name = one_of["properties"][tag]["enum"][0]
                object_code = generate_object_type_code(
                    object_name,
                    one_of,
                    "object",
                    data,
                    tag,
                    None,
                    True,
                    imported_refs,
                )
                f.write(object_code)
                f.write("\n")
                all_options.append(to_pascal_case("option_" + object_name))
        elif schema["oneOf"].__len__() == 1:
            description = get_one_of_description(schema)
            object_code = generate_object_type_code(
                name,
                schema["oneOf"][0],
                "object",
                data,
                None,
                None,
                False,
                imported_refs,
            )
            f.write(object_code)
            f.write("\n")
            f.close()
            # return early.
            return
        else:
            # Generate each of the options from the tag.
            i = 0
            for one_of in schema["oneOf"]:
                # Get the value of the tag.
                object_name = camel_to_snake(name) + "_" + str(i)
                object_code = generate_object_type_code(
                    object_name,
                    one_of,
                    "object",
                    data,
                    None,
                    None,
                    False,
                    imported_refs,
                )
                f.write(object_code)
                f.write("\n")
                all_options.append(to_pascal_case(object_name))
                i += 1

    # Write the sum type.
    description = get_one_of_description(schema)
    content = generate_original_union_type(all_options, name, description, tag)
    f.write(content)

    # Close the file.
    f.close()


def generate_object_type_code(
    name: str,
    schema: dict,
    type_name: str,
    data: dict,
    tag: Optional[str],
    content: Optional[str],
    is_option: bool = False,
    imported_refs: Optional[set] = None,
    include_imports: bool = True,
    field_type_overrides: Optional[dict[str, str]] = None,
    extra_imports: Optional[List[str]] = None,
    field_alias_paths: Optional[dict[str, List[str]]] = None,
    extra_body_lines: Optional[List[str]] = None,
) -> str:
    from typing import List, TypedDict

    from .schema_utils import get_refs, get_type_name

    FieldType = TypedDict(
        "FieldType",
        {
            "name": str,
            "type": str,
            "value": str,
        },
    )
    TemplateType = TypedDict(
        "TemplateType",
        {
            "fields": List[FieldType],
            "description": str,
            "name": str,
            "imports": List[str],
            "extra_body_lines": List[str],
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"].replace('"', '\\"')

    imports: List[str] = []
    if extra_imports:
        for extra_import in extra_imports:
            if extra_import not in imports:
                imports.append(extra_import)
    refs = get_refs(schema)
    if imported_refs is None:
        imported_refs = set()
    for ref in refs:
        if ref not in imported_refs:
            imports.append(
                "from ..models." + camel_to_snake(ref) + " import " + ref + "\n"
            )
            imported_refs.add(ref)

    if field_type_overrides is None:
        field_type_overrides = {}
    if field_alias_paths is None:
        field_alias_paths = {}
    if extra_body_lines is None:
        extra_body_lines = []

    def is_default_compatible(base_type_name: str, default_value: Any) -> bool:
        if default_value is None:
            return True

        simple_type_map: dict[str, type | tuple[type, ...]] = {
            "str": str,
            "int": int,
            "float": (int, float),
            "bool": bool,
        }
        if base_type_name in simple_type_map:
            expected_type = simple_type_map[base_type_name]
            return isinstance(default_value, expected_type)

        if base_type_name.startswith("List["):
            return isinstance(default_value, list)

        if base_type_name.startswith("Dict["):
            return isinstance(default_value, dict)

        if base_type_name.startswith("Literal["):
            return True

        if base_type_name == "bytes" and isinstance(default_value, (bytes, bytearray)):
            return True

        return False

    required = []
    if "required" in schema:
        required = schema["required"]

    fields = []
    if "properties" in schema:
        for property_name in schema["properties"]:
            property_schema = schema["properties"][property_name]
            if property_name == tag:
                field0: FieldType = {
                    "name": property_name,
                    "type": "str",
                    "value": '"' + name + '"',
                }
                fields.append(field0)
            elif property_name == content:
                field1: FieldType = {
                    "name": property_name,
                    "type": to_pascal_case(name) + "Data",
                    "value": "",
                }
                fields.append(field1)
            else:
                if property_name in field_type_overrides:
                    base_type = field_type_overrides[property_name]
                else:
                    base_type = get_type_name(property_schema)

                is_required = property_name in required
                has_default = "default" in property_schema
                default_literal = None
                default_value: Any = None
                if has_default:
                    default_value = property_schema["default"]
                    if isinstance(default_value, str):
                        default_literal = f'"{default_value}"'
                    else:
                        default_literal = repr(default_value)

                type_hint = base_type
                if not is_required:
                    if has_default and default_value is not None:
                        # Leave as base type; explicit default handles the missing case.
                        pass
                    else:
                        type_hint = "Optional[" + base_type + "]"
                        if default_literal is None:
                            default_literal = "None"

                elif has_default and default_literal is None:
                    default_literal = "None"

                needs_type_ignore = False
                if has_default:
                    needs_type_ignore = not is_default_compatible(
                        base_type, default_value
                    )

                if property_name in field_alias_paths:
                    alias_parts = ", ".join(
                        ["'" + part + "'" for part in field_alias_paths[property_name]]
                    )
                    alias_expr = "AliasPath(" + alias_parts + ")"
                    field_definition = type_hint + " = Field("
                    field_default = (
                        default_literal if default_literal is not None else "..."
                    )
                    field_definition += "default=" + field_default + ", "
                    field_definition += (
                        "validation_alias="
                        + alias_expr
                        + ", serialization_alias="
                        + alias_expr
                        + ")"
                    )
                else:
                    field_definition = type_hint
                    if default_literal is not None:
                        field_definition += " = " + default_literal

                if needs_type_ignore:
                    field_definition += "  # type: ignore[assignment]"

                field2: FieldType = {
                    "name": property_name,
                    "type": field_definition,
                    "value": "",
                }
                fields.append(field2)

    # Use surgical conversion to handle all naming conventions properly
    name = to_pascal_case(name)
    if is_option:
        name = "Option" + name
    template_info: TemplateType = {
        "fields": fields,
        "description": description,
        "name": name,
        "imports": imports,
        "extra_body_lines": extra_body_lines if extra_body_lines else [],
    }

    # Iterate over the properties.

    if include_imports:
        template_file = "object.py.jinja2"
    else:
        template_file = "object-class-only.py.jinja2"
    template = get_template(template_file)
    content = template.render(**template_info)

    return content


def get_object_type_imports(refs: List[str]) -> List[str]:
    imports = []
    for ref in refs:
        if ref and ref[0].isupper():  # Only PascalCase types
            module_name = camel_to_snake(ref)
            imports.append(f"from .{module_name} import {ref}")
    return sorted(list(set(imports)))


def generate_object_type(
    path: str, name: str, schema: dict, type_name: str, data: dict
):
    logging.info("generating type: %s at: %s", name, path)

    object_code = generate_object_type_code(name, schema, type_name, data, None, None)

    f = open(path, "w")
    f.write(object_code)
    f.close()


def generate_any_type(path: str, name: str, schema: dict):
    """Generate a type alias for Any when schema only has description."""
    logging.info("generating type: %s at: %s", name, path)

    f = open(path, "w")
    f.write("from typing import Any\n")
    f.write("\n")

    description = schema.get("description", "")
    if description:
        f.write(f'"""{description}"""\n')

    f.write(f"{name} = Any\n")
    f.close()
