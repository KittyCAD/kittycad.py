#!/usr/bin/env python3
import io
import json
import logging
import os
import random
from typing import Any, Dict, List, Optional, Tuple, TypedDict

import jinja2
from prance import BaseParser

from .post_processing import generate_examples_tests, generate_patch_json

# Import utilities
from .utils import (
    camel_to_screaming_snake,
    camel_to_snake,
    clean_parameter_name,
    consolidate_imports_in_file,
    deduplicate_imports,
    to_pascal_case,
)

package_name = "kittycad"

random.seed(10)

examples: List[str] = []


def generate_sync_function(path: str, method: str, endpoint: dict, data: dict) -> str:
    """Generate a sync function implementation using the sync_function template"""

    import os

    from jinja2 import Environment, FileSystemLoader

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))

    # Add custom filters using existing utility functions
    env.filters["to_pascal_case"] = to_pascal_case
    env.filters["pascal_to_snake"] = camel_to_snake

    # Check if this endpoint uses pagination
    is_paginated = "x-dropshot-pagination" in endpoint
    template_name = (
        "sync_paginated_function.py.jinja2"
        if is_paginated
        else "sync_function.py.jinja2"
    )

    template = env.get_template(template_name)

    # Build context exactly like the working functions.py template
    fn_name = camel_to_snake(endpoint["operationId"])
    endpoint_refs = get_endpoint_refs(endpoint, data)
    (request_body_type, request_body_schema) = get_request_body_type_schema(
        endpoint, data
    )

    # Get response type
    response_type = ""
    if len(endpoint_refs) > 0:
        er = [ref for ref in endpoint_refs if ref != "Error"]
        if len(er) > 1:
            pascal_er = [to_pascal_case(ref) for ref in er]
            response_type = "Union[" + ", ".join(pascal_er) + "]"
        elif len(er) == 1:
            response_type = to_pascal_case(er[0])

    # Process parameters exactly like the working template
    args = []
    if "parameters" in endpoint:
        for param in endpoint["parameters"]:
            param_schema = param.get("schema", {})
            arg_type, _, _ = generate_type_and_example_python(
                "", param_schema, data, None, None
            )

            # Mark optional parameters
            # For query parameters, default to optional (required=False) if not specified
            # For path parameters, default to required (required=True) if not specified
            default_required = param.get("in") == "path"
            is_optional = not param.get(
                "required", default_required
            ) or param_schema.get("nullable", False)
            if is_optional and not arg_type.startswith("Optional["):
                arg_type = f"Optional[{arg_type}]"

            args.append(
                {
                    "name": clean_parameter_name(param["name"]),
                    "type": arg_type,
                    "is_optional": is_optional,
                    "in_url": param.get("in") == "path",
                    "in_query": param.get("in") == "query",
                }
            )

    # Add request body parameter if it exists
    if request_body_type:
        args.append(
            {
                "name": "body",
                "type": request_body_type,
                "is_optional": False,
                "in_url": False,
                "in_query": False,
            }
        )

    # Check if there's actually a body parameter in the args
    has_body_param = any(arg.get("name") == "body" for arg in args)

    # Create context for template with all required variables
    context = {
        "func_name": fn_name,
        "method": method.lower(),
        "response_type": response_type,
        "url_template": "{}" + path,
        "has_request_body": has_body_param,
        "request_body_type": request_body_type,
        "args": args,
        "docs": endpoint.get("description", endpoint.get("summary", "")),
    }

    # Add pagination-specific context if needed
    if is_paginated and response_type:
        # Extract item type from response type (e.g., "ApiCallWithPriceResultsPage" -> "ApiCallWithPrice")
        item_type = response_type.replace("ResultsPage", "")
        context["item_type"] = item_type
        context["api_section"] = (
            path.split("/")[1] if len(path.split("/")) > 1 else "api"
        )

    return template.render(context)


def generate_async_function(path: str, method: str, endpoint: dict, data: dict) -> str:
    """Generate an async function implementation using the async_function template"""

    import os

    from jinja2 import Environment, FileSystemLoader

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))

    # Add custom filters using existing utility functions
    env.filters["to_pascal_case"] = to_pascal_case
    env.filters["pascal_to_snake"] = camel_to_snake

    # Check if this endpoint uses pagination
    is_paginated = "x-dropshot-pagination" in endpoint
    template_name = (
        "async_paginated_function.py.jinja2"
        if is_paginated
        else "async_function.py.jinja2"
    )
    template = env.get_template(template_name)

    # Build context exactly like the sync function
    fn_name = camel_to_snake(endpoint["operationId"])
    endpoint_refs = get_endpoint_refs(endpoint, data)
    (request_body_type, request_body_schema) = get_request_body_type_schema(
        endpoint, data
    )

    # Get response type
    response_type = ""
    if len(endpoint_refs) > 0:
        er = [ref for ref in endpoint_refs if ref != "Error"]
        if len(er) > 1:
            pascal_er = [to_pascal_case(ref) for ref in er]
            response_type = "Union[" + ", ".join(pascal_er) + "]"
        elif len(er) == 1:
            response_type = to_pascal_case(er[0])

    # Process parameters exactly like the working template
    args = []
    if "parameters" in endpoint:
        for param in endpoint["parameters"]:
            param_schema = param.get("schema", {})
            arg_type, _, _ = generate_type_and_example_python(
                "", param_schema, data, None, None
            )

            # Mark optional parameters
            # For query parameters, default to optional (required=False) if not specified
            # For path parameters, default to required (required=True) if not specified
            default_required = param.get("in") == "path"
            is_optional = not param.get(
                "required", default_required
            ) or param_schema.get("nullable", False)
            if is_optional and not arg_type.startswith("Optional["):
                arg_type = f"Optional[{arg_type}]"

            args.append(
                {
                    "name": clean_parameter_name(param["name"]),
                    "type": arg_type,
                    "is_optional": is_optional,
                    "in_url": param.get("in") == "path",
                    "in_query": param.get("in") == "query",
                }
            )

    # Add request body parameter if it exists
    if request_body_type:
        args.append(
            {
                "name": "body",
                "type": request_body_type,
                "is_optional": False,
                "in_url": False,
                "in_query": False,
            }
        )

    # Check if there's actually a body parameter in the args
    has_body_param = any(arg.get("name") == "body" for arg in args)

    # Create context for template with all required variables
    context = {
        "func_name": fn_name,
        "method": method.lower(),
        "response_type": response_type,
        "url_template": "{}" + path,
        "has_request_body": has_body_param,
        "request_body_type": request_body_type,
        "args": args,
        "docs": endpoint.get("description", endpoint.get("summary", "")),
    }

    # Add pagination-specific context if needed
    if is_paginated and response_type:
        # Extract item type from response type (e.g., "ApiCallWithPriceResultsPage" -> "ApiCallWithPrice")
        item_type = response_type.replace("ResultsPage", "")
        context["item_type"] = item_type
        context["api_section"] = (
            path.split("/")[1] if len(path.split("/")) > 1 else "api"
        )

    return template.render(context)


def generate_client_classes(cwd: str, data: dict):
    """Generate the KittyCAD and AsyncKittyCAD client classes with embedded endpoint logic"""

    # Collect all endpoints by tag with full implementation details
    endpoints_by_tag: Dict[str, Dict[str, Any]] = {}
    all_imports = set()
    has_websockets = False

    # Process each path and method to collect endpoint info
    for path, path_data in data.get("paths", {}).items():
        for method, endpoint_data in path_data.items():
            if method not in ["get", "post", "put", "delete", "patch"]:
                continue

            if "tags" not in endpoint_data:
                continue

            tag = endpoint_data["tags"][0].replace("-", "_")
            operation_id = endpoint_data.get("operationId", "")

            if tag not in endpoints_by_tag:
                endpoints_by_tag[tag] = {}

            # Check if this is a WebSocket endpoint
            is_websocket = "x-dropshot-websocket" in endpoint_data
            if is_websocket:
                has_websockets = True

            # Generate everything directly from the OpenAPI spec
            implementation_code = ""
            parameters = ""
            call_args = ""
            return_type = "Any"
            parse_response = "response.json()" if method.lower() == "get" else "None"
            has_websocket_class = False

            # Enable WebSocket wrapper classes for endpoints with request bodies
            # These need wrapper classes for methods like send_binary(), __enter__, __exit__
            has_websocket_class = is_websocket

            # Generate sync and async implementations for all endpoints
            sync_implementation = ""
            async_implementation = ""
            try:
                if is_websocket:
                    # Generate WebSocket-specific implementations
                    sync_implementation = generate_websocket_sync_function(
                        operation_id, path, method, endpoint_data, data
                    )
                    async_implementation = generate_websocket_async_function(
                        operation_id, path, method, endpoint_data, data
                    )
                else:
                    sync_implementation = generate_sync_function(
                        path, method, endpoint_data, data
                    )
                    async_implementation = generate_async_function(
                        path, method, endpoint_data, data
                    )

                # Collect imports from response types for all endpoints
                endpoint_refs = get_endpoint_refs(endpoint_data, data)
                for ref in endpoint_refs:
                    # Extract inner types from List, Union, Dict, Optional wrappers
                    inner_types = []
                    if ref.startswith("List[") and ref.endswith("]"):
                        inner_type = ref[5:-1]  # Extract "Type" from "List[Type]"
                        inner_types.append(inner_type)
                    elif ref.startswith("Union[") and ref.endswith("]"):
                        # Extract types from "Union[Type1, Type2]" - for now just skip complex unions
                        pass
                    elif ref.startswith("Dict[") and ref.endswith("]"):
                        # Extract types from "Dict[Key, Value]" - for now just skip
                        pass
                    elif ref.startswith("Optional[") and ref.endswith("]"):
                        inner_type = ref[9:-1]  # Extract "Type" from "Optional[Type]"
                        inner_types.append(inner_type)
                    else:
                        inner_types.append(ref)

                    for inner_type in inner_types:
                        if (
                            inner_type != "Error"
                            and inner_type != "str"
                            and inner_type != "int"
                            and inner_type != "float"
                            and inner_type != "bool"
                            and inner_type != "dict"
                            and inner_type
                            and inner_type[0].isupper()  # Only PascalCase class names
                        ):
                            module_name = camel_to_snake(inner_type)
                            all_imports.add(
                                f"from .models.{module_name} import {inner_type}"
                            )

                # Also collect imports from request body types for all endpoints
                (request_body_type, _) = get_request_body_type_schema(
                    endpoint_data, data
                )
                if (
                    request_body_type
                    and request_body_type != "str"
                    and request_body_type != "bytes"
                ):
                    module_name = camel_to_snake(request_body_type)
                    all_imports.add(
                        f"from .models.{module_name} import {request_body_type}"
                    )

                # Also collect imports from parameter types
                if "parameters" in endpoint_data:
                    parameters = endpoint_data["parameters"]
                    for parameter in parameters:
                        param_schema = parameter.get("schema", {})
                        if "$ref" in param_schema:
                            param_type = param_schema["$ref"].replace(
                                "#/components/schemas/", ""
                            )
                            if param_type and param_type[0].isupper():
                                module_name = camel_to_snake(param_type)
                                all_imports.add(
                                    f"from .models.{module_name} import {param_type}"
                                )
                        elif (
                            param_schema.get("type") == "array"
                            and "items" in param_schema
                        ):
                            items = param_schema["items"]
                            if "$ref" in items:
                                param_type = items["$ref"].replace(
                                    "#/components/schemas/", ""
                                )
                                if param_type and param_type[0].isupper():
                                    module_name = camel_to_snake(param_type)
                                    all_imports.add(
                                        f"from .models.{module_name} import {param_type}"
                                    )

            except Exception as e:
                # Fallback to empty implementations if generation fails
                sync_implementation = (
                    f"    # Error generating implementation: {e}\n    pass"
                )
                async_implementation = (
                    f"    # Error generating implementation: {e}\n    pass"
                )

            # Generate formatted parameter strings for WebSocket wrapper classes
            websocket_params = ""
            websocket_call_args = ""

            if is_websocket and has_websocket_class and "parameters" in endpoint_data:
                required_params = []
                optional_params = []
                call_arg_parts = []

                for param in endpoint_data["parameters"]:
                    param_name = camel_to_snake(param["name"])
                    param_schema = param.get("schema", {})

                    # Generate type
                    if "type" in param_schema:
                        param_type = (
                            param_schema["type"]
                            .replace("string", "str")
                            .replace("integer", "int")
                            .replace("number", "float")
                            .replace("boolean", "bool")
                        )
                    elif "$ref" in param_schema:
                        param_type = param_schema["$ref"].replace(
                            "#/components/schemas/", ""
                        )
                    else:
                        param_type = "Any"

                    # Handle optional parameters
                    # For query parameters, default to optional (required=False) if not specified
                    # For path parameters, default to required (required=True) if not specified
                    default_required = param.get("in") == "path"
                    is_required = param.get("required", default_required)
                    if not is_required or param_schema.get("nullable", False):
                        if not param_type.startswith("Optional["):
                            param_type = f"Optional[{param_type}]"
                        optional_params.append(f"{param_name}: {param_type} = None")
                    else:
                        required_params.append(f"{param_name}: {param_type}")

                    call_arg_parts.append(f"{param_name}={param_name}")

                # WebSocket endpoints don't need body parameters for connection
                # The body is for messages sent through the WebSocket after connection
                # So we skip adding the body parameter for WebSocket wrapper classes

                # Combine parameters: required first, then optional
                all_params = required_params + optional_params
                if all_params:
                    websocket_params = ", " + ", ".join(all_params)
                    websocket_call_args = ", ".join(call_arg_parts)

            endpoints_by_tag[tag][operation_id] = {
                "name": operation_id,
                "is_websocket": is_websocket,
                "has_websocket_class": has_websocket_class,
                "description": endpoint_data.get("summary", "").replace('"', '\\"'),
                "return_type": return_type,
                "path": path,
                "method": method.lower(),
                "parameters": parameters,
                "websocket_params": websocket_params,
                "websocket_call_args": websocket_call_args,
                "call_args": call_args,
                "implementation": implementation_code,
                "parse_response": parse_response,
                "sync_implementation": sync_implementation,
                "async_implementation": async_implementation,
            }

    # Load and render the template
    from jinja2 import Environment, FileSystemLoader

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))

    # Add custom filters using existing utility functions
    env.filters["to_pascal_case"] = to_pascal_case
    env.filters["pascal_to_snake"] = camel_to_snake

    template = env.get_template("__init__.py.jinja2")

    # Render the template
    rendered_content = template.render(
        endpoints_by_tag=endpoints_by_tag,
        all_imports=sorted(all_imports),
        has_websockets=has_websockets,
    )

    # Write to the __init__.py file
    init_path = os.path.join(cwd, "kittycad", "__init__.py")

    with open(init_path, "w") as f:
        f.write(rendered_content)

    # Generate examples tests and patch json files
    generate_examples_tests(cwd, examples)

    # Add the client information to the generation.
    data["info"]["x-python"] = {
        "client": """# Setup your client with your token
from kittycad import KittyCAD

client = KittyCAD(token="$TOKEN")

# - OR -

# Create a new client with your token parsed from the environment variable:
# `KITTYCAD_API_TOKEN` or `ZOO_API_TOKEN`.
# Optionally, you can pass in `ZOO_HOST` to specify the host. But this only
# works if you are using the `ZOO_API_TOKEN` environment variable.
from kittycad import KittyCAD

client = KittyCAD()

# NOTE: The python library additionally implements asyncio, however all the code samples we
# show below use the sync functions for ease of use and understanding.
# Check out the library docs at:
# https://python.api.docs.zoo.dev
# for more details.""",
        "install": "pip install kittycad",
    }

    spec_path = os.path.join(cwd, "spec.json")
    generate_patch_json(cwd, spec_path, data)


def main():
    cwd = os.getcwd()
    spec_path = os.path.join(cwd, "spec.json")
    logging.info("opening spec file: %s", spec_path)
    parser = BaseParser(spec_path)

    # Generate the types.
    generate_types(cwd, parser.specification)

    # Generate the paths.
    data = generate_paths(cwd, parser.specification)

    # Generate the client classes
    generate_client_classes(cwd, data)


def generate_paths(cwd: str, parser: dict) -> dict:
    # Generate the paths without creating individual API files.
    data = parser
    paths = data["paths"]
    # Sort paths to ensure consistent processing order
    for p in sorted(paths.keys()):
        # If p starts with /oauth2 we can skip it.
        # We don't care about generating methods for those.
        if p.startswith("/oauth2"):
            continue
        else:
            # Sort methods for consistent order
            for method in sorted(paths[p].keys()):
                # Skip OPTIONS.
                if method.upper() != "OPTIONS":
                    endpoint = paths[p][method]
                    data = generate_path_data(p, method, endpoint, data)

    return data


def generate_type_and_example_python(
    name: str,
    schema: dict,
    data: dict,
    import_path: Optional[str],
    tag: Optional[str],
    wrapper: Optional[str] = None,
) -> Tuple[str, str, str]:
    parameter_type = ""
    parameter_example = ""
    example_imports = ""
    ip: str = ""
    if import_path is not None:
        ip = import_path
    if "type" in schema:
        if "format" in schema and schema["format"] == "uuid":
            if name != "":
                parameter_type = name
                if import_path is None:
                    example_imports = example_imports + (
                        "from kittycad.models."
                        + camel_to_snake(parameter_type)
                        + " import "
                        + parameter_type
                        + "\n"
                    )
                else:
                    example_imports = example_imports + (
                        "from kittycad.models."
                        + ip
                        + " import "
                        + parameter_type
                        + "\n"
                    )

                parameter_example = parameter_type + '("<uuid>")'
            else:
                parameter_type = "str"
                parameter_example = '"<uuid>"'
        if "format" in schema and schema["format"] == "date-time":
            if name != "":
                parameter_type = name
                if import_path is None:
                    example_imports = example_imports + (
                        "from kittycad.models."
                        + camel_to_snake(parameter_type)
                        + " import "
                        + parameter_type
                        + "\n"
                    )
                else:
                    example_imports = example_imports + (
                        "from kittycad.models."
                        + ip
                        + " import "
                        + parameter_type
                        + "\n"
                    )

                parameter_example = parameter_type + "(datetime.datetime.now())"
            else:
                parameter_type = "datetime"
                parameter_example = "datetime.datetime.now()"
        elif "format" in schema and schema["format"] == "byte":
            if name != "":
                parameter_type = name
                if import_path is None:
                    example_imports = example_imports + (
                        "from kittycad.models."
                        + camel_to_snake(parameter_type)
                        + " import "
                        + parameter_type
                        + "\n"
                    )
                else:
                    example_imports = example_imports + (
                        "from kittycad.models."
                        + ip
                        + " import "
                        + parameter_type
                        + "\n"
                    )

                example_imports = (
                    example_imports
                    + "from kittycad.models.base64data import Base64Data\n"
                )

                parameter_example = parameter_type + 'Base64Data(b"<bytes>")'
            else:
                example_imports = (
                    example_imports
                    + "from kittycad.models.base64data import Base64Data\n"
                )
                parameter_type = "Base64Data"
                parameter_example = 'Base64Data(b"<bytes>")'

        elif (
            schema["type"] == "string" and "enum" in schema and len(schema["enum"]) > 0
        ):
            if name == "":
                if len(schema["enum"]) == 1:
                    name = schema["enum"][0]
                else:
                    logging.error("schema: %s", json.dumps(schema, indent=4))
                    raise Exception("Unknown type name for enum")

            parameter_type = name

            if import_path is None:
                example_imports = example_imports + (
                    "from kittycad.models."
                    + camel_to_snake(parameter_type)
                    + " import "
                    + parameter_type
                    + "\n"
                )
            else:
                example_imports = example_imports + (
                    "from kittycad.models." + ip + " import " + parameter_type + "\n"
                )

            parameter_example = (
                parameter_type + "." + camel_to_screaming_snake(schema["enum"][0])
            )
        elif schema["type"] == "string":
            if name != "":
                parameter_type = name
                if import_path is None:
                    example_imports = example_imports + (
                        "from kittycad.models."
                        + camel_to_snake(parameter_type)
                        + " import "
                        + parameter_type
                        + "\n"
                    )
                else:
                    example_imports = example_imports + (
                        "from kittycad.models."
                        + ip
                        + " import "
                        + parameter_type
                        + "\n"
                    )
                parameter_example = parameter_type + '("<string>")'
            else:
                parameter_type = "str"
                parameter_example = '"<string>"'
        elif schema["type"] == "integer":
            parameter_type = "int"
            parameter_example = "10"
        elif schema["type"] == "boolean":
            parameter_type = "bool"
            parameter_example = "False"
        elif (
            schema["type"] == "number"
            and "format" in schema
            and (
                schema["format"] == "float"
                or schema["format"] == "double"
                or schema["format"] == "money-usd"
            )
        ):
            parameter_type = "float"
            parameter_example = "3.14"
        elif schema["type"] == "array" and "items" in schema:
            # Special case for uint8 arrays which represent bytes in Python
            if "format" in schema["items"] and schema["items"]["format"] == "uint8":
                parameter_type = "bytes"
                parameter_example = 'b"<bytes>"'
            else:
                items_type, items_example, items_imports = (
                    generate_type_and_example_python(
                        "", schema["items"], data, None, None
                    )
                )
                example_imports = example_imports + items_imports
                parameter_type = "List[" + items_type + "]"
                if "minItems" in schema and schema["minItems"] > 1:
                    parameter_example = "["
                    for i in range(schema["minItems"] - 1):
                        parameter_example = parameter_example + items_example + ", "
                    parameter_example = parameter_example + "]"
                else:
                    parameter_example = "[" + items_example + "]"

                example_imports = example_imports + ("from typing import List\n")
        elif schema["type"] == "object" and "properties" in schema:
            if name == "":
                logging.error("schema: %s", json.dumps(schema, indent=4))
                raise Exception("Unknown type name for object")

            parameter_type = name

            if import_path is None:
                example_imports = example_imports + (
                    "from kittycad.models."
                    + camel_to_snake(parameter_type)
                    + " import "
                    + parameter_type
                    + "\n"
                )
            else:
                example_imports = example_imports + (
                    "from kittycad.models." + ip + " import " + parameter_type + "\n"
                )
            parameter_example = name + "("
            for property_name in schema["properties"]:
                prop = schema["properties"][property_name]
                if "nullable" in prop:
                    # We don't care if it's nullable
                    continue
                elif property_name == tag:
                    # We don't care if it's the tag, since we already have it.
                    continue
                else:
                    (
                        prop_type,
                        prop_example,
                        prop_imports,
                    ) = generate_type_and_example_python(
                        "", prop, data, import_path, tag
                    )
                    example_imports = example_imports + prop_imports
                    parameter_example = parameter_example + (
                        "\n"
                        + clean_parameter_name(property_name)
                        + "="
                        + prop_example
                        + ",\n"
                    )

            parameter_example = parameter_example + ")"

            if wrapper is not None:
                if wrapper != "WebSocketRequest":
                    example_imports = example_imports + (
                        "from kittycad.models." + ip + " import " + wrapper + "\n"
                    )
                    parameter_example = wrapper + "(" + parameter_example + ")"
        elif (
            schema["type"] == "object"
            and "additionalProperties" in schema
            and schema["additionalProperties"] is not False
        ):
            items_type, items_example, items_imports = generate_type_and_example_python(
                "", schema["additionalProperties"], data, None, None
            )
            example_imports = example_imports + items_imports
            parameter_type = "Dict[str, " + items_type + "]"
            parameter_example = '{"<string>": ' + items_example + "}"
        else:
            logging.error("schema: %s", json.dumps(schema, indent=4))
            raise Exception("Unknown parameter type")
    elif "oneOf" in schema and len(schema["oneOf"]) > 0:
        # Choose a random one.
        index = random.randint(0, len(schema["oneOf"]) - 1)
        one_of = schema["oneOf"][index]

        # Check if this is a nested object.
        if is_nested_object_one_of(schema):
            if "properties" in one_of:
                properties = one_of["properties"]
                for prop in properties:
                    return generate_type_and_example_python(
                        prop, properties[prop], data, camel_to_snake(name), None
                    )
                    break
            elif "type" in one_of and one_of["type"] == "string":
                return generate_type_and_example_python(
                    name, one_of, data, camel_to_snake(name), None
                )

        tag = get_tag_one_of(schema)

        if (
            "properties" in one_of
            and "type" in one_of["properties"]
            and "enum" in one_of["properties"]["type"]
        ):
            return generate_type_and_example_python(
                to_pascal_case("option_" + one_of["properties"]["type"]["enum"][0]),
                one_of,
                data,
                camel_to_snake(name),
                tag,
                name,
            )
        else:
            return generate_type_and_example_python(name, one_of, data, None, None)
    elif "allOf" in schema and len(schema["allOf"]) == 1:
        return generate_type_and_example_python(
            name, schema["allOf"][0], data, None, None
        )
    elif "$ref" in schema:
        parameter_type = schema["$ref"].replace("#/components/schemas/", "")
        # Get the schema for the reference.
        ref_schema = data["components"]["schemas"][parameter_type]

        return generate_type_and_example_python(
            parameter_type, ref_schema, data, None, None
        )
    else:
        logging.error("schema: %s", json.dumps(schema, indent=4))
        raise Exception("Unknown parameter type")

    return parameter_type, parameter_example, example_imports


def generate_path_data(name: str, method: str, endpoint: dict, data: dict) -> dict:
    # Generate the path data (without creating individual files).
    fn_name = camel_to_snake(endpoint["operationId"])
    tag_name = ""
    # Get the tag name if it exists.
    if "tags" in endpoint:
        tag_name = endpoint["tags"][0].replace("-", "_")
    logging.info("processing path: %s", name)

    # Get endpoint refs for the example generation
    endpoint_refs = get_endpoint_refs(endpoint, data)
    (request_body_type, request_body_schema) = get_request_body_type_schema(
        endpoint, data
    )

    success_type = ""
    if len(endpoint_refs) > 0:
        # Always filter out Error from endpoint_refs for examples
        er = [ref for ref in endpoint_refs if ref != "Error"]
        if len(er) > 1:
            # Ensure all refs are PascalCase for the example type
            pascal_er = [to_pascal_case(ref) for ref in er]
            success_type = "Union[" + ", ".join(pascal_er) + "]"
        elif len(er) == 1:
            # Ensure single ref is PascalCase for the example type
            success_type = to_pascal_case(er[0])
        # If no non-Error refs, success_type stays empty

    example_imports = ""

    # Iterate over the parameters.
    params_str = ""
    if "parameters" in endpoint:
        parameters = endpoint["parameters"]
        optional_args = []
        for parameter in parameters:
            parameter_name = parameter["name"]
            (
                parameter_type,
                parameter_example,
                more_example_imports,
            ) = generate_type_and_example_python(
                "", parameter["schema"], data, None, None
            )
            example_imports = example_imports + more_example_imports

            if "nullable" in parameter["schema"] and parameter["schema"]["nullable"]:
                parameter_type = "Optional[" + parameter_type + "]"
                optional_args.append(clean_parameter_name(parameter_name) + "=None,\n")
            else:
                params_str += (
                    clean_parameter_name(parameter_name)
                    + "="
                    + parameter_example
                    + ",\n"
                )

        for optional_arg in optional_args:
            params_str += optional_arg

    body_example = "{}"
    if request_body_type:
        if request_body_type == "str":
            params_str += "body='<string>',\n"
        elif request_body_type == "bytes":
            params_str += "body=bytes('some bytes', 'utf-8'),\n"
        elif request_body_schema:
            # Generate an example for the schema.
            rbs: Dict[Any, Any] = request_body_schema
            (
                body_type,
                body_ex,
                more_example_imports,
            ) = generate_type_and_example_python(
                request_body_type, rbs, data, None, None
            )
            body_example = body_ex
            if "x-dropshot-websocket" not in endpoint:
                params_str += "body=" + body_example + ",\n"
            else:
                # For websockets, body_example should be wrapped with the request body type
                # but not double-wrapped if it's already wrapped
                if not body_example.startswith(request_body_type + "("):
                    body_example = request_body_type + "(" + body_example + ")"
                example_imports = (
                    example_imports
                    + "from kittycad.models import "
                    + request_body_type
                    + "\n"
                )
            example_imports = example_imports + more_example_imports

    example_variable = ""

    response_type = get_function_result_type(endpoint, endpoint_refs, data)
    if (
        success_type != "str"
        and success_type != "dict"
        and success_type != "None"
        and success_type != ""
    ):
        for endpoint_ref in endpoint_refs:
            if endpoint_ref == "Error":
                continue
            # For some reason, PrivacySettings is showing up twice so we want to skip
            # it here. Obviously this is a hack and we should fix the root cause.
            # When this happens again with another struct there might be a more obvious
            # solution, but alas, I am lazy.
            if endpoint_ref != "PrivacySettings" and endpoint_ref != "List[str]":
                example_imports = example_imports + (
                    """from kittycad.models import """
                    + endpoint_ref.replace("List[", "").replace("]", "")
                    + "\n"
                )
        example_imports = (
            example_imports + "from typing import Union, Any, Optional, List, Tuple\n"
        )

        if response_type and response_type != "None":
            example_variable = "result: " + response_type + " = "
        else:
            example_variable = "result = "

        example_imports = example_imports + "from kittycad.types import Response\n"

    # Add some new lines.
    example_imports = example_imports + "\n\n"

    # Clean up params_str for use in examples (no client parameter needed)
    # For WebSocket examples, we need to properly format parameters
    no_client_params = params_str.strip()
    if no_client_params.endswith(",\n"):
        no_client_params = no_client_params[:-2]
    elif no_client_params.endswith(","):
        no_client_params = no_client_params[:-1]

    # If we have parameters, format them properly with proper indentation for multiline calls
    if no_client_params:
        # Split into lines and properly indent each parameter line
        param_lines = no_client_params.split("\n")
        formatted_lines = []
        for i, line in enumerate(param_lines):
            if line.strip():  # Skip empty lines
                if i == 0:
                    # First parameter line goes on same line as function call
                    formatted_lines.append(line.strip())
                else:
                    # Subsequent lines need proper indentation
                    formatted_lines.append("        " + line.strip())
        no_client_params = "\n".join(formatted_lines)

    short_sync_example = (
        """def test_"""
        + fn_name
        + """():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    """
        + example_variable
        + "client."
        + tag_name
        + "."
        + fn_name
        + """("""
        + no_client_params
        + """)

"""
    )

    if (
        success_type != "str"
        and success_type != "dict"
        and success_type != "None"
        and success_type != ""
    ):
        example_success_type = response_type

        if (
            example_success_type != "str"
            and example_success_type != "dict"
            and example_success_type != "None"
            and example_success_type != ""
        ):
            short_sync_example = short_sync_example + (
                """
    body: """
                + example_success_type
                + """ = result
    print(body)

"""
            )
        else:
            short_sync_example = short_sync_example + (
                """
    print(result)

"""
            )

    long_example = (
        """

# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_"""
        + fn_name
        + """_async():
    from kittycad import AsyncKittyCAD
    
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    """
        + example_variable
        + "await client."
        + tag_name
        + "."
        + fn_name
        + """("""
        + no_client_params
        + """)

"""
    )

    # Generate the websocket examples.
    if "x-dropshot-websocket" in endpoint:
        if request_body_type is None:
            short_sync_example = (
                """def test_"""
                + fn_name
                + """():
            client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

            # Connect to the websocket.
            with client."""
                + tag_name
                + """."""
                + fn_name
                + """("""
                + no_client_params
                + """) as websocket:

                # Send a message.
                websocket.send("{}")

                # Get the messages.
                for message in websocket:
                    print(message)

        """
            )
        else:
            short_sync_example = (
                """def test_"""
                + fn_name
                + """():
            client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

            # Connect to the websocket.
            with client."""
                + tag_name
                + """."""
                + fn_name
                + """("""
                + no_client_params
                + """) as websocket:

                # Send a message.
                websocket.send("""
                + body_example
                + """)

                # Get a message.
                message = websocket.recv()
                print(message)

        """
            )

        long_example = (
            """

# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_"""
            + fn_name
            + """_async():
    from kittycad import AsyncKittyCAD
    
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client."""
            + tag_name
            + """."""
            + fn_name
            + """("""
            + no_client_params
            + """)

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)
    """
        )
    # Generate pagination examples for endpoints with x-dropshot-pagination
    elif "x-dropshot-pagination" in endpoint:
        # Extract item type from ResultsPage response type
        item_type = "Any"
        if success_type and success_type.endswith("ResultsPage"):
            # Extract item type by removing "ResultsPage" suffix
            # E.g., "ApiCallWithPriceResultsPage" -> "ApiCallWithPrice"
            item_type = success_type.replace("ResultsPage", "")

        # Add import for the item type if it's not Any
        if item_type != "Any":
            example_imports = (
                example_imports + f"from kittycad.models import {item_type}\n"
            )

        # Create pagination-focused examples
        short_sync_example = (
            """def test_"""
            + fn_name
            + """():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: """
            + item_type
            + """
    for item in client."""
            + tag_name
            + """."""
            + fn_name
            + """("""
            + no_client_params
            + """):
        print(item)

"""
        )

        long_example = (
            """

# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_"""
            + fn_name
            + """_async():
    from kittycad import AsyncKittyCAD
    
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically  
    iterator = client."""
            + tag_name
            + """."""
            + fn_name
            + """("""
            + no_client_params
            + """)
    item: """
            + item_type
            + """
    async for item in iterator:
        print(item)
    """
        )

    # Deduplicate imports before creating examples
    example_imports = deduplicate_imports(example_imports)

    # This longer example we use for generating tests.
    # We only show the short example in the docs since it is much more intuitive to MEs
    example = (
        example_imports
        + """

@pytest.mark.skip
"""
        + short_sync_example
        + long_example
    )

    # Make pretty.
    short_sync_example = example_imports + short_sync_example

    # Don't format individual examples - we'll format the consolidated file later
    cleaned_example = short_sync_example

    examples.append(example)

    # Add our example to our json output.
    data["paths"][name][method]["x-python"] = {
        "example": cleaned_example.replace("def test_", "def example_"),
        "libDocsLink": "https://python.api.docs.zoo.dev/_autosummary/kittycad.KittyCAD.html#kittycad.KittyCAD."
        + fn_name,
    }

    return data


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
    else:
        logging.error("schema: %s", schema)
        logging.error("unsupported type: %s", name)
        raise Exception("unsupported type: ", name)

    return file_path


def generate_string_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    TemplateType = TypedDict(
        "TemplateType",
        {
            "description": str,
            "name": str,
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"]

    template_info: TemplateType = {
        "description": description,
        "name": name,
    }

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("generate/templates/")
    )
    template_file = "str.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)

    f.write(content)

    # Close the file.
    f.close()


def generate_integer_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    TemplateType = TypedDict(
        "TemplateType",
        {
            "description": str,
            "name": str,
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"]

    template_info: TemplateType = {
        "description": description,
        "name": name,
    }

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("generate/templates/")
    )
    template_file = "int.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)

    f.write(content)

    # Close the file.
    f.close()


def generate_float_type(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    TemplateType = TypedDict(
        "TemplateType",
        {
            "description": str,
            "name": str,
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"]

    template_info: TemplateType = {
        "description": description,
        "name": name,
    }

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("generate/templates/")
    )
    template_file = "float.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)

    f.write(content)

    # Close the file.
    f.close()


def generate_enum_type(
    path: str,
    name: str,
    schema: dict,
    type_name: str,
    additional_docs: List[str],
):
    logging.info("generating type: %s at: %s", name, path)
    f = open(path, "w")

    code = generate_enum_type_code(name, schema, type_name, additional_docs)
    f.write(code)

    # Close the file.
    f.close()


def generate_enum_type_code(
    name: str,
    schema: dict,
    type_name: str,
    additional_docs: List[str],
) -> str:
    f = io.StringIO()

    f.write("from enum import Enum\n")
    f.write("\n")
    f.write("class " + name + "(str, Enum):\n")
    if "description" in schema:
        f.write('\t""" ' + schema["description"] + ' """ # noqa: E501\n')
    # Iterate over the properties.
    for num, value in enumerate(schema["enum"], start=0):
        enum_name = camel_to_screaming_snake(value)
        if enum_name == "":
            enum_name = "EMPTY"
        elif enum_name == "1":
            enum_name = "ONE"
        elif enum_name == "2":
            enum_name = "TWO"

        # Write the description if there is one.
        if len(additional_docs) > 0:
            additional_doc = additional_docs[num]
            if additional_doc != "":
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
        # Generate each of the options from the tag.
        for any_of in schema["anyOf"]:
            # Get the value of the tag.
            object_name = any_of["properties"][tag]["enum"][0]
            object_code = generate_object_type_code(
                object_name, any_of, "object", data, tag, None
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(object_name)
    else:
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

    # Write the sum type.
    description = get_any_of_description(schema)
    content = generate_union_type(all_options, name, description, tag)
    f.write(content)

    # Close the file.
    f.close()


def get_any_of_description(schema: dict) -> str:
    if "description" in schema:
        return schema["description"]
    else:
        return ""


def generate_union_type(
    types: List[str], name: str, description: str, tag: Optional[str]
) -> str:
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

    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("generate/templates/")
    )
    template_file = "union-type.py.jinja2"
    template = environment.get_template(template_file)
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
                        # Use class name as the key to avoid importing same class multiple times regardless of path
                        if ref_name not in imported_refs:
                            f.write(
                                "from ."
                                + camel_to_snake(ref_name)
                                + " import "
                                + ref_name
                                + "\n"
                            )
                            f.write("\n")
                            imported_refs.add(ref_name)
                        if prop_name != ref_name:
                            f.write(prop_name + " = " + ref_name + "\n")
                            f.write("\n")
                        all_options.append(ref_name)
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
    content = generate_union_type(all_options, name, description, tag)
    f.write(content)

    # Close the file.
    f.close()


def get_one_of_description(schema: dict) -> str:
    if "description" in schema:
        return schema["description"]
    else:
        return ""


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


def get_object_type_imports(
    name: str,
    schema: dict,
    type_name: str,
    data: dict,
    tag: Optional[str],
    content: Optional[str],
    is_option: bool = False,
    imported_refs: Optional[set] = None,
) -> List[str]:
    """Get the imports needed for an object type."""
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
    return imports


def generate_object_type(
    path: str, name: str, schema: dict, type_name: str, data: dict
):
    logging.info("generating type: %s at: %s", name, path)

    f = open(path, "w")

    code = generate_object_type_code(name, schema, type_name, data, None, None)
    f.write(code)

    # Close the file.
    f.close()


def get_refs(schema: dict) -> List[str]:
    refs = []
    if "$ref" in schema:
        refs.append(schema["$ref"].replace("#/components/schemas/", ""))

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
                        ref = json["$ref"].replace("#/components/schemas/", "")
                        schema = data["components"]["schemas"][ref]
                        if is_nested_object_one_of(schema) or is_enum_with_docs_one_of(
                            schema
                        ):
                            if ref not in refs:
                                refs.append(ref)
                        elif is_typed_object_one_of(schema):
                            for t in schema["oneOf"]:
                                ref = get_one_of_ref_type(t)
                                if ref not in refs:
                                    refs.append(ref)
                        else:
                            if ref not in refs:
                                refs.append(ref)
                    elif "type" in json:
                        if json["type"] == "array":
                            items = json["items"]
                            if "$ref" in items:
                                ref = items["$ref"].replace("#/components/schemas/", "")
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
                            print(json)
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
                            ref = json["$ref"].replace("#/components/schemas/", "")
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
                parameter_type = parameter["schema"]["$ref"].replace(
                    "#/components/schemas/", ""
                )
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
                        ref = json["$ref"].replace("#/components/schemas/", "")
                        refs.append(ref)
                elif content_type == "application/octet-stream":
                    # do nothing we dont't care
                    continue
                elif content_type == "application/x-www-form-urlencoded":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = form["$ref"].replace("#/components/schemas/", "")
                        refs.append(ref)
                elif content_type == "multipart/form-data":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = form["$ref"].replace("#/components/schemas/", "")
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
                        ref = json["$ref"].replace("#/components/schemas/", "")
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
                        ref = form["$ref"].replace("#/components/schemas/", "")
                        type_schema = data["components"]["schemas"][ref]
                        return ref, type_schema
                    elif form != {}:
                        logging.error("not a ref: %s", form)
                        raise Exception("not a ref")
                elif content_type == "multipart/form-data":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = form["$ref"].replace("#/components/schemas/", "")
                        type_schema = data["components"]["schemas"][ref]
                        return ref, type_schema
                    elif form != {}:
                        type_schema = form
                        return None, type_schema
                else:
                    logging.error("unsupported content type: %s", content_type)
                    raise Exception("unsupported content type")

    return None, None


def rename_if_keyword(name: str):
    """Rename a name if it is also a Python keyword."""
    KEYWORDS = ["global"]  # there are more, but this is the only one we overlap now
    if name in KEYWORDS:
        return name + "_"
    return name


# Change `file_conversion` to `FileConversion`


def get_function_parameters(
    endpoint: dict, request_body_type: Optional[str]
) -> List[str]:
    params = []
    if "parameters" in endpoint:
        parameters = endpoint["parameters"]
        for parameter in parameters:
            parameter_name = parameter["name"]
            if "type" in parameter["schema"]:
                (
                    parameter["schema"]["type"]
                    .replace("string", "str")
                    .replace("integer", "int")
                    .replace("number", "float")
                )
            elif "$ref" in parameter["schema"]:
                parameter["schema"]["$ref"].replace("#/components/schemas/", "")
            else:
                logging.error("parameter: %s", parameter)
                raise Exception("Unknown parameter type")
            params.append(camel_to_snake(parameter_name))
    if request_body_type:
        params.append("body")
    return params


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


def get_success_endpoint_refs(endpoint: dict, data: dict) -> List[str]:
    """Get references from successful response codes only (2xx), excluding errors."""
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
                        ref = json["$ref"].replace("#/components/schemas/", "")
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
                            for t in schema["oneOf"]:
                                ref = get_one_of_ref_type(t)
                                if ref != "Error" and ref not in refs:
                                    refs.append(ref)
                        else:
                            if ref not in refs:
                                refs.append(ref)
                    elif "type" in json:
                        if json["type"] == "array":
                            items = json["items"]
                            if "$ref" in items:
                                ref = items["$ref"].replace("#/components/schemas/", "")
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
        return schema["$ref"].replace("#/components/schemas/", "")
    elif "allOf" in schema and len(schema["allOf"]) == 1:
        return get_type_name(schema["allOf"][0])
    elif "description" in schema:
        return "Any"

    logging.error("schema: %s", schema)
    raise Exception("Unknown schema type")


def generate_websocket_sync_function(
    operation_id: str, path: str, method: str, endpoint: dict, data: dict
) -> str:
    """Generate a sync WebSocket function implementation."""
    from jinja2 import Environment, FileSystemLoader

    # Build template context
    args = []

    # Handle parameters
    if "parameters" in endpoint:
        parameters = endpoint["parameters"]
        for parameter in parameters:
            parameter_name = parameter["name"]
            if "type" in parameter["schema"]:
                parameter_type = (
                    parameter["schema"]["type"]
                    .replace("string", "str")
                    .replace("integer", "int")
                    .replace("number", "float")
                    .replace("boolean", "bool")
                )
            elif "$ref" in parameter["schema"]:
                parameter_type = parameter["schema"]["$ref"].replace(
                    "#/components/schemas/", ""
                )
            else:
                parameter_type = "Any"

            if "nullable" in parameter["schema"] and parameter["schema"]["nullable"]:
                parameter_type = f"Optional[{parameter_type}]"
                is_optional = True
            else:
                is_optional = False

            args.append(
                {
                    "name": camel_to_snake(parameter_name),
                    "type": parameter_type,
                    "in_url": "in" in parameter and parameter["in"] == "path",
                    "in_query": "in" in parameter and parameter["in"] == "query",
                    "is_optional": is_optional,
                }
            )

    # Handle request body for WebSocket endpoints
    (request_body_type, _) = get_request_body_type_schema(endpoint, data)
    if request_body_type:
        args.append(
            {
                "name": "body",
                "type": request_body_type,
                "in_url": False,
                "in_query": False,
                "is_optional": False,
            }
        )

    # Use WebSocket template
    environment = Environment(loader=FileSystemLoader("generate/templates/"))
    template = environment.get_template("websocket_sync_function.py.jinja2")
    return template.render(
        function_name=operation_id,
        args=args,
        url_template=path,
        docs=endpoint.get("summary", "").replace('"', '\\"'),
    )


def generate_websocket_async_function(
    operation_id: str, path: str, method: str, endpoint: dict, data: dict
) -> str:
    """Generate an async WebSocket function implementation."""
    from jinja2 import Environment, FileSystemLoader

    # Build template context (same as sync)
    args = []

    # Handle parameters
    if "parameters" in endpoint:
        parameters = endpoint["parameters"]
        for parameter in parameters:
            parameter_name = parameter["name"]
            if "type" in parameter["schema"]:
                parameter_type = (
                    parameter["schema"]["type"]
                    .replace("string", "str")
                    .replace("integer", "int")
                    .replace("number", "float")
                    .replace("boolean", "bool")
                )
            elif "$ref" in parameter["schema"]:
                parameter_type = parameter["schema"]["$ref"].replace(
                    "#/components/schemas/", ""
                )
            else:
                parameter_type = "Any"

            if "nullable" in parameter["schema"] and parameter["schema"]["nullable"]:
                parameter_type = f"Optional[{parameter_type}]"
                is_optional = True
            else:
                is_optional = False

            args.append(
                {
                    "name": camel_to_snake(parameter_name),
                    "type": parameter_type,
                    "in_url": "in" in parameter and parameter["in"] == "path",
                    "in_query": "in" in parameter and parameter["in"] == "query",
                    "is_optional": is_optional,
                }
            )

    # Handle request body
    (request_body_type, _) = get_request_body_type_schema(endpoint, data)
    if request_body_type:
        args.append(
            {
                "name": "body",
                "type": request_body_type,
                "in_url": False,
                "in_query": False,
                "is_optional": False,
            }
        )

    # Use WebSocket async template
    environment = Environment(loader=FileSystemLoader("generate/templates/"))
    template = environment.get_template("websocket_async_function.py.jinja2")
    return template.render(
        function_name=operation_id,
        args=args,
        url_template=path,
        docs=endpoint.get("summary", "").replace('"', '\\"'),
    )


letters: List[str] = []


# generate a random letter combination in the range A - Z
# do not use O or I.
# make sure we do not use a letter we have already used.
def randletter() -> str:
    letter1 = chr(random.randint(ord("A"), ord("Z")))
    letter2 = chr(random.randint(ord("A"), ord("Z")))
    letter3 = chr(random.randint(ord("A"), ord("Z")))
    letter = letter1 + letter2 + letter3
    while letter in letters:
        return randletter()
    letters.append(letter)
    return letter


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
