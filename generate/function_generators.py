"""Function generation utilities for API endpoints and WebSocket connections."""

from .utils import (
    camel_to_snake,
    get_template,
    get_template_environment,
    process_endpoint_parameters,
    to_pascal_case,
)


def _generate_docstring_with_examples(
    endpoint: dict, file_info: dict, request_body_type: str
) -> str:
    """Generate docstring with usage examples for endpoints."""
    base_docs = endpoint.get("description", endpoint.get("summary", ""))

    # Add examples for JSON + multipart endpoints
    if file_info.get("has_json_body_multipart", False):
        examples = f"""

Examples:
    Basic usage with file attachments:
    
    ```python
    from pathlib import Path
    from kittycad.models.{camel_to_snake(request_body_type) if request_body_type else "text_to_cad_multi_file_iteration_body"} import {request_body_type or "TextToCadMultiFileIterationBody"}
    
    # Create the request body
    body = {request_body_type or "TextToCadMultiFileIterationBody"}(
        # Add your parameters here
    )
    
    # Prepare file attachments
    file_attachments = {{
        "main.kcl": Path("path/to/main.kcl"),
        "helper.kcl": Path("path/to/helper.kcl"),
    }}
    
    # Make the request
    result = client.{camel_to_snake(endpoint.get("operationId", ""))}(
        body=body,
        file_attachments=file_attachments,
    )
    ```
    
    Using different file types:
    
    ```python
    from io import BytesIO
    
    # Mix of file paths and file-like objects
    file_attachments = {{
        "main.kcl": Path("main.kcl"),
        "config.kcl": BytesIO(b"// KCL configuration"),
        "data.json": "path/to/data.json",
    }}
    
    result = client.{camel_to_snake(endpoint.get("operationId", ""))}(
        body=body,
        file_attachments=file_attachments,
    )
    ```
    """
        return base_docs + examples

    return base_docs


def generate_sync_function(path: str, method: str, endpoint: dict, data: dict) -> str:
    """Generate a sync function implementation using the sync_function template"""

    env = get_template_environment()

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

    # Process parameters using consolidated utility
    args = process_endpoint_parameters(endpoint, data, is_websocket=False)

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
                "type": "Dict[str, SyncUpload]",
                "is_optional": False,
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
        "docs": _generate_docstring_with_examples(
            endpoint, file_info, request_body_type
        ),
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

    env = get_template_environment()

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

    # Process parameters using consolidated utility
    args = process_endpoint_parameters(endpoint, data, is_websocket=False)

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
                "type": "Dict[str, SyncUpload]",
                "is_optional": False,
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
        "docs": _generate_docstring_with_examples(
            endpoint, file_info, request_body_type
        ),
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
    # Process parameters using consolidated utility
    args = process_endpoint_parameters(endpoint, data, is_websocket=True)

    # For WebSocket endpoints, we don't include the body in the main method signature
    # The body is only used in the low-level connection methods

    # Use WebSocket template
    template = get_template("websocket_sync_function.py.jinja2")
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
    # Process parameters using consolidated utility
    args = process_endpoint_parameters(endpoint, data, is_websocket=True)

    # For WebSocket endpoints, we don't include the body in the main method signature
    # The body is only used in the low-level connection methods

    # Use WebSocket async template
    template = get_template("websocket_async_function.py.jinja2")
    return template.render(
        function_name=operation_id,
        args=args,
        url_template=path,
        docs=endpoint.get("summary", "").replace('"', '\\"'),
    )
