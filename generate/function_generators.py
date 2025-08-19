"""Function generation utilities for API endpoints and WebSocket connections."""

import os

from jinja2 import Environment, FileSystemLoader

from .utils import camel_to_snake, clean_parameter_name, to_pascal_case


def generate_sync_function(path: str, method: str, endpoint: dict, data: dict) -> str:
    """Generate a sync function implementation using the sync_function template"""

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

    # Import these here to avoid circular imports
    from .file_operation_detection import extract_file_parameter_info
    from .generate import generate_type_and_example_python
    from .schema_utils import get_endpoint_refs, get_request_body_type_schema

    # Build context exactly like the working functions.py template
    fn_name = camel_to_snake(endpoint["operationId"])
    endpoint_refs = get_endpoint_refs(endpoint, data)
    (request_body_type, request_body_schema) = get_request_body_type_schema(
        endpoint, data
    )

    # Extract file operation information
    file_info = extract_file_parameter_info(endpoint, data)

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

    # Add request body parameter(s) based on endpoint type
    if file_info.get("has_json_body_multipart", False):
        # For JSON + multipart endpoints, add both JSON body and file attachments
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
        args.append(
            {
                "name": "file_attachments",
                "type": "Optional[Dict[str, SyncUpload]]",
                "is_optional": True,
                "in_url": False,
                "in_query": False,
            }
        )
    elif request_body_type:
        # Regular request body handling
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
        "file_info": file_info,  # Add file operation info to context
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

    # Import these here to avoid circular imports
    from .file_operation_detection import extract_file_parameter_info
    from .generate import generate_type_and_example_python
    from .schema_utils import get_endpoint_refs, get_request_body_type_schema

    # Build context exactly like the sync function
    fn_name = camel_to_snake(endpoint["operationId"])
    endpoint_refs = get_endpoint_refs(endpoint, data)
    (request_body_type, request_body_schema) = get_request_body_type_schema(
        endpoint, data
    )

    # Extract file operation information
    file_info = extract_file_parameter_info(endpoint, data)

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

    # Add request body parameter(s) based on endpoint type
    if file_info.get("has_json_body_multipart", False):
        # For JSON + multipart endpoints, add both JSON body and file attachments
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
        args.append(
            {
                "name": "file_attachments",
                "type": "Optional[Dict[str, SyncUpload]]",
                "is_optional": True,
                "in_url": False,
                "in_query": False,
            }
        )
    elif request_body_type:
        # Regular request body handling
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
        "file_info": file_info,  # Add file operation info to context
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


def generate_websocket_sync_function(
    operation_id: str, path: str, method: str, endpoint: dict, data: dict
) -> str:
    """Generate a sync WebSocket function implementation."""
    from jinja2 import Environment, FileSystemLoader

    # Import here to avoid circular imports
    from .schema_utils import get_request_body_type_schema

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

    # Import here to avoid circular imports
    from .schema_utils import get_request_body_type_schema

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
