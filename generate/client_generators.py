"""Client class generation for KittyCAD and AsyncKittyCAD."""

import os
from typing import Any, Dict

from .file_operation_detection import get_required_file_imports
from .function_generators import (
    generate_async_function,
    generate_sync_function,
    generate_websocket_async_function,
    generate_websocket_sync_function,
)
from .post_processing import generate_examples_tests
from .schema_utils import get_endpoint_refs, get_request_body_type_schema
from .utils import camel_to_snake, get_template_environment


def generate_client_classes(cwd: str, data: dict, examples: list):
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

                # Collect file operation imports if needed
                file_imports = get_required_file_imports(endpoint_data)
                for import_stmt in file_imports:
                    # Extract the module and class names from import statement
                    # e.g., "from kittycad._io_types import SyncUpload, ProgressCallback"
                    if " import " in import_stmt:
                        module_part, imports_part = import_stmt.split(" import ", 1)
                        module_name = module_part.replace("from ", "")
                        for imported_name in imports_part.split(", "):
                            all_imports.add(
                                f"from {module_name} import {imported_name.strip()}"
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

                    # Handle optional parameters - query params are optional by default
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
    env = get_template_environment()
    template = env.get_template("__init__.py.jinja2")

    # Use the examples passed as parameter

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
    from .post_processing import generate_patch_json

    generate_patch_json(cwd, spec_path, data)
