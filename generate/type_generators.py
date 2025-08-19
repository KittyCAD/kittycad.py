"""Type generation utilities for generating Python types from API schemas."""

import logging
import os
import random
from typing import List, Optional

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


def generate_string_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    template = get_template("str.py.jinja2")
    description = schema.get("description", "")
    f.write(template.render(name=name, description=description))
    f.close()


def generate_integer_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    template = get_template("int.py.jinja2")
    description = schema.get("description", "")
    minimum = schema.get("minimum")
    maximum = schema.get("maximum")

    f.write(
        template.render(
            name=name, description=description, minimum=minimum, maximum=maximum
        )
    )
    f.close()


def generate_float_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    template = get_template("float.py.jinja2")
    description = schema.get("description", "")
    minimum = schema.get("minimum")
    maximum = schema.get("maximum")

    f.write(
        template.render(
            name=name, description=description, minimum=minimum, maximum=maximum
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

    enum_code = generate_enum_type_code(name, schema, type_name, enums)
    f.write(enum_code)
    f.close()


def generate_enum_type_code(
    name: str,
    schema: dict,
    type_name: str = "string",
    additional_docs: Optional[List[str]] = None,
) -> str:
    import io

    if additional_docs is None:
        additional_docs = []

    f = io.StringIO()

    f.write("from enum import Enum\n")
    f.write("\n")
    f.write("class " + name + "(str, Enum):\n")
    if "description" in schema:
        f.write('\t""" ' + schema["description"] + ' """ # noqa: E501\n')

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

                # Write the description if there is one.
                if "description" in one_of:
                    f.write('\t"""# ' + one_of["description"] + ' """ # noqa: E501\n')
                elif len(additional_docs) > num and additional_docs[num] != "":
                    f.write('\t"""# ' + additional_docs[num] + ' """ # noqa: E501\n')

                f.write("\t" + enum_name + " = '" + value + "'\n")
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

                # Write the description if there is one.
                if len(additional_docs) > num and additional_docs[num] != "":
                    f.write('\t"""# ' + additional_docs[num] + ' """ # noqa: E501\n')

                f.write("\t" + enum_name + " = '" + value + "'\n")

    # close the enum.
    f.write("\n")
    f.write("\tdef __str__(self) -> str:\n")
    f.write("\t\treturn str(self.value)\n")

    value = f.getvalue()

    # Close the file.
    f.close()

    return value


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

    if is_nested_object_one_of(schema):
        # We want to write each of the nested objects.
        for one_of in schema["oneOf"]:
            # Get the nested object.
            if "properties" in one_of:
                for prop_name in one_of["properties"]:
                    nested_object = one_of["properties"][prop_name]
                    if nested_object == {}:
                        f.write("from typing import Any\n")
                        f.write(prop_name + " = Any\n")
                        f.write("\n")
                        all_options.append(prop_name)
                    elif "$ref" in nested_object:
                        ref = nested_object["$ref"]
                        ref_name = ref[ref.rfind("/") + 1 :]
                        class_name = to_pascal_case(ref_name)
                        # Use class name as the key to avoid importing same class multiple times regardless of path
                        if class_name not in imported_refs:
                            f.write(
                                "from ."
                                + camel_to_snake(ref_name)
                                + " import "
                                + class_name
                                + "\n"
                            )
                            imported_refs.add(class_name)
                        f.write("\n")
                        if prop_name != ref_name:
                            f.write(prop_name + " = " + class_name + "\n")
                            f.write("\n")
                        all_options.append(class_name)
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
            elif "type" in one_of and one_of["type"] == "string":
                enum_code = generate_enum_type_code(
                    one_of["enum"][0], one_of, "string", []
                )
                f.write(enum_code)
                f.write("\n")
                all_options.append(one_of["enum"][0])

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
                object_name, one_of, "object", data, tag, content, True, imported_refs
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
                object_name, one_of, "object", data, tag, None, True, imported_refs
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
