"""Schema analysis utilities for determining schema types and patterns."""

from typing import Optional

from .utils import get_schema_description

# For backward compatibility, create aliases to the consolidated function
get_any_of_description = get_schema_description
get_one_of_description = get_schema_description


def get_one_of_ref_type(schema: dict) -> str:
    if (
        "type" in schema["properties"]
        and "enum" in schema["properties"]["type"]
        and len(schema["properties"]["type"]["enum"]) == 1
    ):
        t = schema["properties"]["type"]["enum"][0]
        return t

    raise Exception("Cannot get oneOf ref type for schema: ", schema)


def is_nested_object_any_of(schema: dict) -> bool:
    if "anyOf" not in schema:
        return False

    is_nested_object = False
    for any_of in schema["anyOf"]:
        # Check if each are an object w 1 property in it.
        if (
            "type" in any_of
            and any_of["type"] == "object"
            and "properties" in any_of
            and len(any_of["properties"]) == 1
        ):
            for prop_name in any_of["properties"]:
                nested_object = any_of["properties"][prop_name]
                if "type" in nested_object and nested_object["type"] == "object":
                    is_nested_object = True
                else:
                    is_nested_object = False
                    break
        elif (
            "type" in any_of
            and any_of["type"] == "string"
            and "enum" in any_of
            and len(any_of["enum"]) == 1
        ):
            is_nested_object = True
        else:
            is_nested_object = False
            break

    return is_nested_object


def is_nested_object_one_of(schema: dict) -> bool:
    if "oneOf" not in schema:
        return False

    is_nested_object = False
    for one_of in schema["oneOf"]:
        # Check if each are an object w 1 property in it.
        if (
            "type" in one_of
            and one_of["type"] == "object"
            and "properties" in one_of
            and len(one_of["properties"]) == 1
        ):
            for prop_name in one_of["properties"]:
                nested_object = one_of["properties"][prop_name]
                if "type" in nested_object and nested_object["type"] == "object":
                    is_nested_object = True
                else:
                    is_nested_object = False
                    break
        elif (
            "type" in one_of
            and one_of["type"] == "string"
            and "enum" in one_of
            and len(one_of["enum"]) == 1
        ):
            is_nested_object = True
        else:
            is_nested_object = False
            break

    return is_nested_object


def get_tag_any_of(schema: dict) -> Optional[str]:
    tag = None
    for any_of in schema["anyOf"]:
        has_tag = False
        # Check if each are an object w 1 property in it.
        if "type" in any_of and any_of["type"] == "object" and "properties" in any_of:
            for prop_name in any_of["properties"]:
                prop = any_of["properties"][prop_name]
                if (
                    "type" in prop
                    and prop["type"] == "string"
                    and "enum" in prop
                    and len(prop["enum"]) == 1
                ):
                    if tag is not None and tag != prop_name:
                        has_tag = False
                        break
                    else:
                        has_tag = True
                        tag = prop_name

        if has_tag is False:
            tag = None
            break

    return tag


def get_tag_one_of(schema: dict) -> Optional[str]:
    tag = None
    for one_of in schema["oneOf"]:
        has_tag = False
        # Check if each are an object w 1 property in it.
        if one_of["type"] == "object" and "properties" in one_of:
            for prop_name in one_of["properties"]:
                prop = one_of["properties"][prop_name]
                if (
                    "type" in prop
                    and prop["type"] == "string"
                    and "enum" in prop
                    and len(prop["enum"]) == 1
                ):
                    if tag is not None and tag != prop_name:
                        has_tag = False
                        break
                    else:
                        has_tag = True
                        tag = prop_name

        if has_tag is False:
            tag = None
            break

    return tag


def get_content_one_of(schema: dict, tag: Optional[str]) -> Optional[str]:
    if tag is None:
        return None
    content = None
    for one_of in schema["oneOf"]:
        has_content = False
        # Check if each are an object w 1 property in it.
        if one_of["type"] == "object" and "properties" in one_of:
            if len(one_of["properties"]) != 2:
                return None

            for prop_name in one_of["properties"]:
                if prop_name == tag:
                    continue
                if content is not None and content != prop_name:
                    has_content = False
                    break
                else:
                    has_content = True
                    content = prop_name

        if has_content is False:
            content = None
            break

    return content


def is_enum_with_docs_one_of(schema: dict) -> bool:
    if "oneOf" not in schema:
        return False

    is_enum_with_docs = False
    for one_of in schema["oneOf"]:
        if one_of["type"] == "string" and "enum" in one_of and len(one_of["enum"]) == 1:
            is_enum_with_docs = True
        else:
            is_enum_with_docs = False
            break

    return is_enum_with_docs


def is_typed_object_one_of(schema: dict) -> bool:
    if "oneOf" not in schema:
        return False

    is_typed_object = False
    for one_of in schema["oneOf"]:
        if (
            "type" in one_of["properties"]
            and "enum" in one_of["properties"]["type"]
            and len(one_of["properties"]["type"]["enum"]) == 1
        ):
            is_typed_object = True
        else:
            is_typed_object = False
            break

    return is_typed_object


def has_no_content_response(endpoint: dict) -> bool:
    responses = endpoint["responses"]
    for response_code in responses:
        if (
            response_code == "default"
            or response_code == "204"
            or response_code == "302"
        ):
            return True

    return False
