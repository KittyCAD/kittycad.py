"""Type generation utilities for generating Python types from API schemas."""

import logging
import os
from typing import List, Optional

from jinja2 import Environment, FileSystemLoader

from .schema_analysis import (
    get_any_of_description,
    get_one_of_description,
    get_tag_any_of,
    get_tag_one_of,
    is_nested_object_any_of,
    is_nested_object_one_of,
)
from .utils import (
    camel_to_screaming_snake,
    camel_to_snake,
    consolidate_imports_in_file,
    to_pascal_case,
)


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


def generate_string_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("str.py.jinja2")

    description = schema.get("description", "")
    f.write(template.render(class_name=name, description=description))
    f.close()


def generate_integer_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("int.py.jinja2")

    description = schema.get("description", "")
    minimum = schema.get("minimum")
    maximum = schema.get("maximum")

    f.write(
        template.render(
            class_name=name, description=description, minimum=minimum, maximum=maximum
        )
    )
    f.close()


def generate_float_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("float.py.jinja2")

    description = schema.get("description", "")
    minimum = schema.get("minimum")
    maximum = schema.get("maximum")

    f.write(
        template.render(
            class_name=name, description=description, minimum=minimum, maximum=maximum
        )
    )
    f.close()


def generate_enum_type(
    path: str,
    name: str,
    schema: dict,
    type_name: str,
    enums: List[str],
):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    enum_code = generate_enum_type_code(name, schema)
    f.write(enum_code)
    f.close()


def generate_enum_type_code(
    name: str,
    schema: dict,
) -> str:
    import io

    f = io.StringIO()

    f.write("from enum import Enum\n")
    f.write("\n")
    f.write("class " + name + "(str, Enum):\n")
    if "description" in schema:
        f.write('\t""" ' + schema["description"] + ' """ # noqa: E501\n')

    # Handle oneOf enums with descriptions
    if "oneOf" in schema:
        for one_of in schema["oneOf"]:
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

                f.write("\t" + enum_name + ' = "' + value + '"\n')
                if "description" in one_of:
                    f.write('\t""" ' + one_of["description"] + ' """\n')
    else:
        # Standard string enum
        if "enum" in schema:
            for value in schema["enum"]:
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

                f.write("\t" + enum_name + ' = "' + value + '"\n')

    return f.getvalue()


def generate_any_of_type(path: str, name: str, schema: dict, data: dict):
    logging.info("generating type: %s at: %s", name, path)

    description = get_any_of_description(schema)

    # Let's see what types of any of we have
    types = []
    nested_objects = []
    for any_of in schema["anyOf"]:
        if "type" in any_of:
            if any_of["type"] == "object":
                # This is a nested object.
                if "properties" in any_of and len(any_of["properties"]) == 1:
                    # This is a property
                    property_name = ""
                    for prop_name in any_of["properties"]:
                        property_name = prop_name
                    nested_objects.append(property_name)
                else:
                    # This is just another object.
                    nested_objects.append("object")
            else:
                types.append(any_of["type"])
        elif "$ref" in any_of:
            # This is another type.
            ref = any_of["$ref"].replace("#/components/schemas/", "")
            types.append(ref)

    if is_nested_object_any_of(schema):
        # Generate a union type
        tag = get_tag_any_of(schema)
        types_str = generate_union_type(nested_objects, name, description, tag)

        f = open(path, "w")
        f.write(types_str)
        f.close()
    else:
        # Generate a regular Union type
        union_types = []
        for t in types:
            if t in ["string", "number", "integer", "boolean"]:
                python_type = (
                    t.replace("string", "str")
                    .replace("integer", "int")
                    .replace("number", "float")
                    .replace("boolean", "bool")
                )
                union_types.append(python_type)
            else:
                union_types.append(t)

        template_dir = os.path.join(os.path.dirname(__file__), "templates")
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("union-type.py.jinja2")

        f = open(path, "w")
        f.write(
            template.render(class_name=name, description=description, types=union_types)
        )
        f.close()


def generate_union_type(
    types: List[str], name: str, description: str, tag: Optional[str]
) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("union-type.py.jinja2")

    return template.render(
        class_name=name,
        description=description,
        types=[to_pascal_case(t) for t in types],
        tag=tag,
    )


def generate_one_of_type(path: str, name: str, schema: dict, data: dict):
    logging.info("generating type: %s at: %s", name, path)

    description = get_one_of_description(schema)

    # Let's see what types of oneOf we have
    types = []
    nested_objects = []
    for one_of in schema["oneOf"]:
        if "type" in one_of:
            if one_of["type"] == "object":
                # This is a nested object.
                if "properties" in one_of and len(one_of["properties"]) == 1:
                    # This is a property
                    property_name = ""
                    for prop_name in one_of["properties"]:
                        property_name = prop_name
                    nested_objects.append(property_name)
                else:
                    # This is just another object.
                    nested_objects.append("object")
            elif one_of["type"] == "string" and "enum" in one_of:
                # This is a string enum
                if len(one_of["enum"]) == 1:
                    types.append(one_of["enum"][0])
                else:
                    types.extend(one_of["enum"])
        elif "$ref" in one_of:
            # This is another type.
            ref = one_of["$ref"].replace("#/components/schemas/", "")
            types.append(ref)

    if is_nested_object_one_of(schema):
        # Generate a union type
        tag = get_tag_one_of(schema)
        types_str = generate_union_type(nested_objects, name, description, tag)

        f = open(path, "w")
        f.write(types_str)
        f.close()
    else:
        # Generate a regular Union or enum type
        if all(isinstance(t, str) and not t[0].isupper() for t in types):
            # Generate an enum
            enum_values = []
            for i, one_of in enumerate(schema["oneOf"]):
                if "enum" in one_of and len(one_of["enum"]) == 1:
                    value = one_of["enum"][0]
                    desc = one_of.get("description", "")
                    enum_values.append(
                        {"name": value, "value": value, "description": desc}
                    )

            enum_code = generate_enum_type_code(
                name, {"oneOf": schema["oneOf"], "description": description}
            )
            f = open(path, "w")
            f.write(enum_code)
            f.close()
        else:
            # Generate a Union type
            union_types = []
            for t in types:
                if t in ["string", "number", "integer", "boolean"]:
                    python_type = (
                        t.replace("string", "str")
                        .replace("integer", "int")
                        .replace("number", "float")
                        .replace("boolean", "bool")
                    )
                    union_types.append(python_type)
                else:
                    union_types.append(t)

            template_dir = os.path.join(os.path.dirname(__file__), "templates")
            env = Environment(loader=FileSystemLoader(template_dir))
            template = env.get_template("union-type.py.jinja2")

            f = open(path, "w")
            f.write(
                template.render(
                    class_name=name, description=description, types=union_types
                )
            )
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
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"].replace('"', '\\"')

    imports = []
    refs = get_refs(schema)
    if imported_refs is None:
        imported_refs = set()
    for ref in refs:
        if ref not in imported_refs:
            imports.append(
                "from ..models." + camel_to_snake(ref) + " import " + ref + "\n"
            )
            imported_refs.add(ref)

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
                field_type = get_type_name(property_schema)
                if property_name not in required:
                    if "default" in property_schema:
                        if field_type == "str":
                            field_type += ' = "' + property_schema["default"] + '"'
                        elif isinstance(property_schema["default"], str):
                            field_type += (
                                ' = "' + property_schema["default"] + '" # type: ignore'
                            )
                        elif "allOf" in property_schema:
                            field_type += (
                                " = "
                                + str(property_schema["default"])
                                + " # type: ignore"
                            )
                        else:
                            field_type += " = " + str(property_schema["default"])
                    else:
                        field_type = "Optional[" + field_type + "] = None"
                field2: FieldType = {
                    "name": property_name,
                    "type": field_type,
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
    }

    # Iterate over the properties.

    import jinja2

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("generate/templates/")
    )
    if include_imports:
        template_file = "object.py.jinja2"
    else:
        template_file = "object-class-only.py.jinja2"
    template = environment.get_template(template_file)
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
