"""Schema and reference utilities for API specification processing."""

import logging
from typing import List, Optional, Tuple

from .utils import resolve_schema_ref, to_pascal_case


def get_refs(schema: dict) -> List[str]:
    refs = []
    if "$ref" in schema:
        refs.append(resolve_schema_ref(schema["$ref"]))

    else:
        # Generate the type.
        if "type" not in schema:
            if "allOf" in schema:
                for sub_schema in schema["allOf"]:
                    refs.extend(get_refs(sub_schema))
        else:
            type_name = schema["type"]
            if type_name == "object":
                if "properties" in schema:
                    # Iternate over the properties.
                    for property_name in schema["properties"]:
                        property_schema = schema["properties"][property_name]
                        schema_refs = get_refs(property_schema)
                        for ref in schema_refs:
                            if ref not in refs:
                                refs.append(ref)
                elif "additionalProperties" in schema:
                    schema_refs = get_refs(schema["additionalProperties"])
                    for ref in schema_refs:
                        if ref not in refs:
                            refs.append(ref)
                elif schema == {"type": "object"}:
                    # do nothing
                    pass
                else:
                    # This is likely an empty object like above but with a description
                    # so we will just skip it.
                    pass
            elif type_name == "array":
                if "items" in schema:
                    schema_refs = get_refs(schema["items"])
                    for ref in schema_refs:
                        if ref not in refs:
                            refs.append(ref)

    return refs


def get_endpoint_refs(endpoint: dict, data: dict) -> List[str]:
    # Import here to avoid circular imports
    from .schema_analysis import (
        is_enum_with_docs_one_of,
        is_nested_object_one_of,
        is_typed_object_one_of,
    )

    refs = []

    responses = endpoint["responses"]
    for response_code in responses:
        response = responses[response_code]
        if "content" in response:
            content = response["content"]
            for content_type in content:
                if content_type == "application/json":
                    json = content[content_type]["schema"]
                    if "$ref" in json:
                        # If the reference is to a oneOf type, we want to return
                        # all the possible outcomes.
                        ref = resolve_schema_ref(json["$ref"])
                        schema = data["components"]["schemas"][ref]
                        if is_nested_object_one_of(schema) or is_enum_with_docs_one_of(
                            schema
                        ):
                            if ref not in refs:
                                refs.append(ref)
                        elif is_typed_object_one_of(schema):
                            # For typed (discriminated) oneOf, prefer the wrapper type
                            # (e.g., TextToCadResponse) instead of expanding to inner variants.
                            if ref not in refs:
                                refs.append(ref)
                        else:
                            if ref not in refs:
                                refs.append(ref)
                    elif "type" in json:
                        if json["type"] == "array":
                            items = json["items"]
                            if "$ref" in items:
                                ref = resolve_schema_ref(items["$ref"])
                                refs.append("List[" + ref + "]")
                            elif "type" in items:
                                if items["type"] == "string":
                                    refs.append("List[str]")
                                else:
                                    raise Exception("Unknown array type", items)
                            else:
                                raise Exception("Unknown array type", items)
                        elif json["type"] == "string":
                            refs.append("str")
                        elif (
                            json["type"] == "object" and "additionalProperties" in json
                        ):
                            refs.append("dict")
                        else:
                            logging.error("Unknown type: %s", json["type"])
                            raise Exception("Unknown type ", json["type"])
                    else:
                        refs.append("dict")
                elif content_type == "*/*":
                    s = content[content_type]["schema"]
                    if s == {}:
                        # We don't care it's an empty body.
                        continue
                    else:
                        # Throw an error for an unsupported content type.
                        logging.error("content: %s", content)
                        raise Exception("Unsupported content type: ", content_type)
                else:
                    # Throw an error for an unsupported content type.
                    logging.error("content: %s", content)
                    raise Exception("Unsupported content type: ", content_type)
        elif "$ref" in response:
            schema_name = response["$ref"].replace("#/components/responses/", "")
            schema = data["components"]["responses"][schema_name]
            if "content" in schema:
                content = schema["content"]
                for content_type in content:
                    if content_type == "application/json":
                        json = content[content_type]["schema"]
                        if "$ref" in json:
                            ref = resolve_schema_ref(json["$ref"])
                            if ref not in refs:
                                refs.append(ref)

    return refs


def get_parameter_refs(endpoint: dict) -> List[str]:
    refs = []

    if "parameters" in endpoint:
        parameters = endpoint["parameters"]
        for parameter in parameters:
            parameter["name"]
            if "$ref" in parameter["schema"]:
                parameter_type = resolve_schema_ref(parameter["schema"]["$ref"])
                refs.append(parameter_type)

    return refs


def get_request_body_refs(endpoint: dict) -> List[str]:
    refs = []

    if "requestBody" in endpoint:
        requestBody = endpoint["requestBody"]
        if "content" in requestBody:
            content = requestBody["content"]
            for content_type in content:
                if content_type == "application/json":
                    json = content[content_type]["schema"]
                    if "$ref" in json:
                        ref = resolve_schema_ref(json["$ref"])
                        refs.append(ref)
                elif content_type == "application/octet-stream":
                    # do nothing we dont't care
                    continue
                elif content_type == "application/x-www-form-urlencoded":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = resolve_schema_ref(form["$ref"])
                        refs.append(ref)
                elif content_type == "multipart/form-data":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = resolve_schema_ref(form["$ref"])
                        refs.append(ref)
                else:
                    # Throw an error for an unsupported content type.
                    logging.error("content: %s", content)
                    raise Exception("Unsupported content type: ", content_type)

    return refs


def get_request_body_type_schema(
    endpoint: dict, data: dict
) -> Tuple[Optional[str], Optional[dict]]:
    if "requestBody" in endpoint:
        requestBody = endpoint["requestBody"]
        if "content" in requestBody:
            content = requestBody["content"]
            for content_type in content:
                if content_type == "application/json":
                    json = content[content_type]["schema"]
                    if "$ref" in json:
                        ref = resolve_schema_ref(json["$ref"])
                        type_schema = data["components"]["schemas"][ref]
                        return ref, type_schema
                    elif json != {}:
                        logging.error("not a ref: %s", json)
                        raise Exception("not a ref")
                elif content_type == "text/plain":
                    return "str", None
                elif content_type == "application/octet-stream":
                    return "bytes", None
                elif content_type == "application/x-www-form-urlencoded":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = resolve_schema_ref(form["$ref"])
                        type_schema = data["components"]["schemas"][ref]
                        return ref, type_schema
                    elif form != {}:
                        logging.error("not a ref: %s", form)
                        raise Exception("not a ref")
                elif content_type == "multipart/form-data":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = resolve_schema_ref(form["$ref"])
                        type_schema = data["components"]["schemas"][ref]
                        return ref, type_schema
                    elif form != {}:
                        type_schema = form
                        return None, type_schema
                else:
                    logging.error("unsupported content type: %s", content_type)
                    raise Exception("unsupported content type")

    return None, None


def get_success_endpoint_refs(endpoint: dict, data: dict) -> List[str]:
    """Get references from successful response codes only (2xx), excluding errors."""
    # Import here to avoid circular imports
    from .schema_analysis import (
        is_enum_with_docs_one_of,
        is_nested_object_one_of,
        is_typed_object_one_of,
    )

    refs = []

    responses = endpoint["responses"]
    for response_code in responses:
        # For WebSocket endpoints, "default" is the success response
        is_websocket = "x-dropshot-websocket" in endpoint

        # Only include successful response codes (2xx) or default for WebSockets
        if not (
            response_code.startswith("2")
            or response_code == "200"
            or response_code == "201"
            or response_code == "204"
            or (is_websocket and response_code == "default")
        ):
            continue

        response = responses[response_code]
        if "content" in response:
            content = response["content"]
            for content_type in content:
                if content_type == "application/json":
                    json = content[content_type]["schema"]
                    if "$ref" in json:
                        ref = resolve_schema_ref(json["$ref"])
                        # Skip Error types explicitly
                        if ref == "Error":
                            continue
                        schema = data["components"]["schemas"][ref]
                        if is_nested_object_one_of(schema) or is_enum_with_docs_one_of(
                            schema
                        ):
                            if ref not in refs:
                                refs.append(ref)
                        elif is_typed_object_one_of(schema):
                            # For typed (discriminated) oneOf, prefer the wrapper type
                            # so callers can use RootModel wrappers for validation.
                            if ref not in refs and ref != "Error":
                                refs.append(ref)
                        else:
                            if ref not in refs:
                                refs.append(ref)
                    elif "type" in json:
                        if json["type"] == "array":
                            items = json["items"]
                            if "$ref" in items:
                                ref = resolve_schema_ref(items["$ref"])
                                if ref != "Error":
                                    refs.append("List[" + ref + "]")
                            elif "type" in items:
                                if items["type"] == "string":
                                    refs.append("List[str]")
                                else:
                                    raise Exception("Unknown array type", items)
                        elif json["type"] == "string":
                            refs.append("str")
                        elif (
                            json["type"] == "object" and "additionalProperties" in json
                        ):
                            refs.append("dict")

    return refs


def get_function_result_type(
    endpoint: dict, endpoint_refs: List[str], data: Optional[dict] = None
) -> str:
    # Import here to avoid circular imports
    from .schema_analysis import has_no_content_response

    # Use success-only refs to avoid including Error types in return signatures
    if data:
        success_refs = get_success_endpoint_refs(endpoint, data)
    else:
        # Fallback to filtering existing endpoint_refs to remove Error types
        success_refs = [ref for ref in endpoint_refs if ref != "Error"]

    # Ensure all refs are in PascalCase for return types
    pascal_refs = [to_pascal_case(ref) for ref in success_refs]
    result = ", ".join(pascal_refs) if pascal_refs else ""

    if len(success_refs) > 1:
        result = "Optional[Union[" + result + "]]"
    elif len(success_refs) == 1:
        result = pascal_refs[0]

    if has_no_content_response(endpoint):
        result = "Optional[" + result + "]" if result else ""

    return result


def get_type_name(schema: dict) -> str:
    if "type" in schema:
        if schema["type"] == "string":
            if "format" in schema:
                if (
                    schema["format"] == "date-time"
                    or schema["format"] == "partial-date-time"
                ):
                    return "datetime.datetime"
                elif schema["format"] == "byte":
                    return "Base64Data"
                elif schema["format"] == "uuid":
                    return "str"
                elif schema["format"] == "url":
                    return "AnyUrl"
                elif schema["format"] == "phone":
                    return "str"
            return "str"
        elif schema["type"] == "number":
            return "float"
        elif schema["type"] == "boolean":
            return "bool"
        elif schema["type"] == "integer":
            return "int"
        elif schema["type"] == "array":
            if "items" in schema:
                item_type = get_type_name(schema["items"])
                if "format" in schema["items"] and schema["items"]["format"] == "uint8":
                    return "bytes"
                else:
                    return "List[" + item_type + "]"
        elif schema["type"] == "object":
            if "additionalProperties" in schema:
                item_type = get_type_name(schema["additionalProperties"])
                return "Dict[str, " + item_type + "]"
            elif "properties" in schema:
                return "Dict[str, Any]"
            else:
                return "Dict[str, Any]"
    elif "$ref" in schema:
        return resolve_schema_ref(schema["$ref"])
    elif "allOf" in schema and len(schema["allOf"]) == 1:
        return get_type_name(schema["allOf"][0])
    elif "description" in schema:
        return "Any"

    logging.error("schema: %s", schema)
    raise Exception("Unknown schema type")
