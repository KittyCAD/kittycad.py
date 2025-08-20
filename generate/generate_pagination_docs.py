#!/usr/bin/env python3
"""
Automatic Pagination Documentation Generator

This script automatically generates comprehensive documentation for all pagination
features in the KittyCAD Python SDK by analyzing the OpenAPI specification and
generating examples for each paginated endpoint.

Run this script to generate docs/pagination.rst automatically.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def load_openapi_spec() -> dict:
    """Load the OpenAPI specification."""
    # The spec is in the root directory as spec.json
    openapi_path = Path(__file__).parent.parent / "spec.json"
    with open(openapi_path, "r") as f:
        return json.load(f)


def find_paginated_endpoints(spec: dict) -> List[Dict]:
    """Find all endpoints with x-dropshot-pagination."""
    paginated_endpoints = []

    for path, path_data in spec.get("paths", {}).items():
        for method, endpoint in path_data.items():
            if method.lower() in ["get", "post", "put", "delete", "patch"]:
                if "x-dropshot-pagination" in endpoint:
                    paginated_endpoints.append(
                        {
                            "path": path,
                            "method": method.upper(),
                            "operation_id": endpoint.get("operationId", ""),
                            "summary": endpoint.get("summary", ""),
                            "description": endpoint.get("description", ""),
                            "tags": endpoint.get("tags", []),
                            "parameters": endpoint.get("parameters", []),
                            "responses": endpoint.get("responses", {}),
                        }
                    )

    return paginated_endpoints


def get_response_type_and_item_type(
    endpoint: Dict, spec: dict
) -> Tuple[Optional[str], Optional[str]]:
    """Extract response type and item type from endpoint."""
    responses = endpoint.get("responses", {})
    success_response = responses.get("200", {})

    if "content" not in success_response:
        return None, None

    json_content = success_response["content"].get("application/json", {})
    if "schema" not in json_content:
        return None, None

    schema = json_content["schema"]

    # Handle $ref
    if "$ref" in schema:
        ref_path = schema["$ref"].replace("#/", "").split("/")
        ref_schema = spec
        for part in ref_path:
            ref_schema = ref_schema.get(part, {})

        response_type = ref_path[-1]  # Last part is the type name

        # Extract item type from ResultsPage
        if response_type.endswith("ResultsPage"):
            item_type = response_type.replace("ResultsPage", "")
            return response_type, item_type

    return None, None


def operation_id_to_function_name(operation_id: str) -> str:
    """Convert operationId to Python function name."""
    # Most operation IDs are already snake_case, but some might be camelCase
    # Convert camelCase to snake_case if needed
    import re

    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", operation_id).lower()


def get_api_section_from_tags(tags: List[str]) -> str:
    """Get API section from tags."""
    if not tags:
        return "api"
    return tags[0].replace("-", "_")


def generate_pagination_rst(paginated_endpoints: List[Dict], spec: dict) -> str:
    """Generate the pagination.rst documentation."""

    rst_content = """
Pagination
==========

The KittyCAD Python SDK provides automatic pagination support for list endpoints that return large datasets. Instead of manually handling page tokens and making multiple requests, you can simply iterate over all results using Python's standard iteration patterns.

Features
--------

* **Automatic Pagination**: Seamlessly iterate through all pages of results
* **Memory Efficient**: Uses generators to yield results as they're fetched (O(1) memory usage)
* **Type Safe**: Full type annotations and IDE support
* **Both Sync & Async**: Works with both ``KittyCAD`` and ``AsyncKittyCAD`` clients
* **OpenAI-Style API**: Familiar pagination patterns inspired by the OpenAI Python SDK

Quick Start
-----------

**Sync Example:**

.. code-block:: python

    from kittycad import KittyCAD
    
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable
    
    # Iterate through all API calls automatically
    for api_call in client.api_calls.list_api_calls():
        print(f"API Call: {api_call}")
        # No manual pagination needed!

**Async Example:**

.. code-block:: python

    import asyncio
    from kittycad import AsyncKittyCAD
    
    async def main():
        client = AsyncKittyCAD()
        
        # Iterate through all results asynchronously
        async for api_call in client.api_calls.list_api_calls():
            print(f"API Call: {api_call}")
            
        await client.aclose()
    
    asyncio.run(main())

How It Works
------------

The pagination system automatically:

1. **Detects Paginated Endpoints**: Uses the ``x-dropshot-pagination`` OpenAPI extension
2. **Returns Iterators**: Instead of page objects, returns ``SyncPageIterator`` or ``AsyncPageIterator``
3. **Handles Page Tokens**: Automatically manages ``page_token`` and ``limit`` parameters
4. **Yields Individual Items**: You get the actual items, not page wrappers
5. **Preserves Parameters**: All your query parameters are maintained across pages

Available Paginated Endpoints
-----------------------------

The following endpoints support automatic pagination:

"""

    # Group endpoints by API section
    endpoints_by_section: Dict[str, List[Dict]] = {}
    for endpoint in paginated_endpoints:
        section = get_api_section_from_tags(endpoint["tags"])
        if section not in endpoints_by_section:
            endpoints_by_section[section] = []
        endpoints_by_section[section].append(endpoint)

    # Generate documentation for each section
    for section_name in sorted(endpoints_by_section.keys()):
        section_endpoints = endpoints_by_section[section_name]

        rst_content += f"""
{section_name.replace("_", " ").title()} API
{"-" * (len(section_name) + 4)}

"""

        for endpoint in section_endpoints:
            func_name = operation_id_to_function_name(endpoint["operation_id"])
            response_type, item_type = get_response_type_and_item_type(endpoint, spec)

            # Create a clean summary
            summary = endpoint.get("summary", "").replace("Returns a list of", "List")
            if not summary:
                summary = f"List {func_name.replace('_', ' ')}"

            rst_content += f"""**{func_name}**
    {summary}
    
    Returns: ``{"SyncPageIterator" if item_type else "Iterator"}[{item_type or "Any"}]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.{section_name}.{func_name}():
            print(item)
            
        # Async  
        async for item in client.{section_name}.{func_name}():
            print(item)

"""

    rst_content += """
Advanced Usage
--------------

Controlling Page Size
~~~~~~~~~~~~~~~~~~~~

You can control the page size using the ``limit`` parameter:

.. code-block:: python

    # Fetch 50 items per page instead of the default
    for item in client.api_calls.list_api_calls(limit=50):
        print(item)

Starting from a Specific Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can start pagination from a specific page token:

.. code-block:: python

    # Start from a specific page
    for item in client.api_calls.list_api_calls(page_token="your_token_here"):
        print(item)

Early Termination
~~~~~~~~~~~~~~~~

You can break out of the iteration at any time:

.. code-block:: python

    # Only process the first 100 items
    count = 0
    for item in client.api_calls.list_api_calls():
        print(item)
        count += 1
        if count >= 100:
            break

Memory Efficiency
~~~~~~~~~~~~~~~~

The pagination system uses generators for memory efficiency:

.. code-block:: python

    # This uses O(1) memory regardless of total result count
    # Items are fetched and yielded as needed
    for item in client.api_calls.list_api_calls():
        process_large_item(item)  # Memory usage stays constant

Error Handling
~~~~~~~~~~~~~

Handle API errors during pagination:

.. code-block:: python

    try:
        for item in client.api_calls.list_api_calls():
            print(item)
    except Exception as e:
        print(f"Pagination failed: {e}")

Multiple Iterations
~~~~~~~~~~~~~~~~~~

You can iterate over the same paginator multiple times:

.. code-block:: python

    paginator = client.api_calls.list_api_calls()
    
    # First iteration
    for item in paginator:
        print(f"First pass: {item}")
        
    # Second iteration (starts fresh)
    for item in paginator:
        print(f"Second pass: {item}")

Type Safety
----------

All paginated endpoints return properly typed iterators:

.. code-block:: python

    from kittycad.models import ApiCallWithPrice
    
    # Full type safety and IDE support
    item: ApiCallWithPrice
    for item in client.api_calls.list_api_calls():
        # IDE knows 'item' is ApiCallWithPrice
        print(item.id)  # Autocomplete works!
        print(item.created_at)  # Type checking works!

Implementation Details
---------------------

The pagination system is built on top of:

* **SyncPageIterator**: For synchronous pagination
* **AsyncPageIterator**: For asynchronous pagination  
* **Dropshot Pagination**: Uses the industry-standard Dropshot pagination protocol
* **Type Inference**: Automatically extracts item types from ``*ResultsPage`` response types

The iterators implement Python's standard iteration protocols, so they work seamlessly with:

* ``for`` loops
* ``list()`` comprehensions  
* ``async for`` loops
* ``itertools`` functions
* Any code that expects iterables

Contributing
-----------

This documentation is automatically generated from the OpenAPI specification. 
To update it, run:

.. code-block:: bash

    python generate/generate_pagination_docs.py

The pagination implementation can be found in ``kittycad/pagination.py``.
"""

    return rst_content.strip()


def main():
    """Generate pagination documentation."""
    logging.basicConfig(level=logging.INFO)

    # Load OpenAPI spec
    logging.info("Loading OpenAPI specification...")
    spec = load_openapi_spec()

    # Find paginated endpoints
    logging.info("Finding paginated endpoints...")
    paginated_endpoints = find_paginated_endpoints(spec)
    logging.info(f"Found {len(paginated_endpoints)} paginated endpoints")

    # Generate RST content
    logging.info("Generating pagination documentation...")
    rst_content = generate_pagination_rst(paginated_endpoints, spec)

    # Write to file
    docs_dir = Path(__file__).parent.parent / "docs"
    pagination_rst_path = docs_dir / "pagination.rst"

    with open(pagination_rst_path, "w") as f:
        f.write(rst_content)

    logging.info(f"Generated pagination documentation: {pagination_rst_path}")

    # Also suggest updating index.rst
    index_rst_path = docs_dir / "index.rst"
    logging.info(
        f"\nTo include pagination docs in your main documentation, add this line to {index_rst_path}:"
    )
    logging.info("   kittycad.pagination")
    logging.info("\nOr add a manual entry in the toctree.")


if __name__ == "__main__":
    main()
