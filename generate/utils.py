#!/usr/bin/env python3
"""
Utility functions for code generation.
Contains helper functions for string manipulation, import handling, etc.
"""

import logging
import os
import random
import re
import subprocess
from typing import List, Optional, Tuple

from jinja2 import Environment, FileSystemLoader

# Global list to track used letter combinations
_letters: List[str] = []


def randletter() -> str:
    """Generate a random 3-letter combination that hasn't been used before."""
    letter1 = chr(random.randint(ord("A"), ord("Z")))
    letter2 = chr(random.randint(ord("A"), ord("Z")))
    letter3 = chr(random.randint(ord("A"), ord("Z")))
    letter = letter1 + letter2 + letter3
    while letter in _letters:
        return randletter()
    _letters.append(letter)
    return letter


def is_snake_case(name: str) -> bool:
    """Check if string is in snake_case format."""
    return (
        "_" in name
        and name.islower()
        and not name.startswith("_")
        and not name.endswith("_")
    )


def is_camel_case(name: str) -> bool:
    """Check if string is in camelCase format (starts lowercase)."""
    return name[0].islower() and any(c.isupper() for c in name[1:]) and "_" not in name


def is_pascal_case(name: str) -> bool:
    """Check if string is in PascalCase format (starts uppercase)."""
    return name[0].isupper() and any(c.isupper() for c in name[1:]) and "_" not in name


def camel_to_snake(name: str) -> str:
    """Convert CamelCase/PascalCase to snake_case, but only if not already in snake_case.

    Handles most acronyms properly: XMLHttpRequest -> xml_http_request, APIKey -> api_key.
    Special hardcoded fixes for common problematic cases.
    """
    if is_snake_case(name):
        return name

    # Hardcoded fixes for specific problematic cases
    hardcoded_fixes = {
        "OAuth2ClientInfo": "oauth2_client_info",
        "OAuth2GrantType": "oauth2_grant_type",
    }

    if name in hardcoded_fixes:
        return hardcoded_fixes[name]

    # Insert underscore between lower/digit and upper
    s1 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)

    # Handle sequences of uppercase letters followed by lowercase
    # Keep acronyms together until they hit a lowercase letter
    s2 = re.sub("([A-Z]+)([A-Z][a-z])", r"\1_\2", s1)

    return s2.lower()


def to_pascal_case(name: str) -> str:
    """Convert any naming convention to PascalCase intelligently."""
    # Already PascalCase? Return as-is
    if is_pascal_case(name):
        return name

    # snake_case? Convert it
    if is_snake_case(name):
        return "".join(word.capitalize() for word in name.split("_"))

    # camelCase? Just capitalize first letter
    if is_camel_case(name):
        return name[0].upper() + name[1:]

    # All lowercase single word? Capitalize it
    if name.islower() and "_" not in name:
        return name.capitalize()

    # Has underscores but not clean snake_case? Split and capitalize
    if "_" in name:
        return "".join(word.capitalize() for word in name.split("_"))

    # Default: return as-is
    return name


def camel_to_screaming_snake(name: str) -> str:
    """Convert CamelCase to SCREAMING_SNAKE_CASE."""
    # Replace colons and other problematic characters with underscores
    name = name.replace(":", "_").replace("-", "_").replace(".", "_")
    return camel_to_snake(name).upper()


def clean_parameter_name(name: str) -> str:
    """Clean parameter names to be valid Python identifiers."""
    # Replace common problematic characters
    name = name.replace("-", "_")
    name = name.replace(".", "_")
    name = name.replace(" ", "_")

    # Handle Python keywords
    if name in [
        "type",
        "from",
        "import",
        "class",
        "def",
        "return",
        "if",
        "else",
        "for",
        "while",
    ]:
        name = name + "_"

    return name


def deduplicate_imports(imports_string: str) -> str:
    """Deduplicate imports, prioritizing bulk imports over specific imports."""
    if not imports_string.strip():
        return imports_string

    # Preserve original format characteristics
    has_trailing_newline = imports_string.endswith("\n")
    lines = imports_string.strip().split("\n")

    deduplicated_lines = []
    bulk_imports = set()
    i = 0

    # First pass: identify bulk imports from kittycad.models
    for line in lines:
        line_stripped = line.strip()
        if (
            line_stripped.startswith("from kittycad.models import ")
            and "(" not in line_stripped
        ):
            # Extract imported class names
            imports_part = line_stripped.split(" import ", 1)[1]
            # Split by comma and clean up names
            imported_names = [name.strip() for name in imports_part.split(",")]
            bulk_imports.update(imported_names)

    # Second pass: filter out redundant imports
    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()

        # Handle multi-line imports from kittycad.models.*
        if (
            line_stripped.startswith("from kittycad.models.")
            and " import " in line_stripped
            and "(" in line_stripped
            and ")" not in line_stripped
        ):
            # Collect the entire multi-line import block
            import_block = [line]
            i += 1
            while i < len(lines) and ")" not in lines[i]:
                import_block.append(lines[i])
                i += 1
            # Add the closing line
            if i < len(lines):
                import_block.append(lines[i])
                i += 1
            else:
                i += 1
                break

            # Check if any imported class name from this block conflicts with bulk imports
            has_conflict = False
            full_text = " ".join(import_block)

            for bulk_import in bulk_imports:
                # Look for the bulk import name as a standalone word in the import block
                if bulk_import in full_text:
                    has_conflict = True
                    break

            # If no conflicts, keep the entire import block
            if not has_conflict:
                deduplicated_lines.extend(import_block)

        # Handle single-line imports from kittycad.models.*
        elif (
            line_stripped.startswith("from kittycad.models.")
            and " import " in line_stripped
            and "(" not in line_stripped
        ):
            # Extract the imported class name
            import_name = line_stripped.split(" import ")[-1].strip()
            # If we have a bulk import for this, skip the specific import
            if import_name not in bulk_imports:
                deduplicated_lines.append(line)
            i += 1
        else:
            # Regular line, just add it
            deduplicated_lines.append(line)
            i += 1

    result = "\n".join(deduplicated_lines)

    # Preserve trailing newline if original had one
    if has_trailing_newline:
        result += "\n"

    return result


def consolidate_imports_in_file(file_path: str) -> None:
    """Consolidate imports at the top of a Python file."""
    with open(file_path, "r") as f:
        content = f.read()

    lines = content.split("\n")

    # Collect all import lines
    all_imports = set()
    non_import_lines = []

    for line in lines:
        stripped = line.strip()

        # Check if this line is an import (but not in a multi-line string or comment)
        if (
            stripped.startswith("from ") or stripped.startswith("import ")
        ) and "(" not in stripped:
            all_imports.add(stripped)
        else:
            non_import_lines.append(line)

    # Sort imports for consistency - standard library first, then third-party, then local
    standard_imports = []
    third_party_imports = []
    local_imports = []

    for imp in sorted(all_imports):
        if (
            imp.startswith("import datetime")
            or imp.startswith("import json")
            or imp.startswith("from typing")
        ):
            standard_imports.append(imp)
        elif (
            imp.startswith("from pydantic")
            or imp.startswith("from uuid")
            or "pydantic_extra_types" in imp
            or "typing_extensions" in imp
        ):
            third_party_imports.append(imp)
        elif imp.startswith("from .") or imp.startswith("from .."):
            local_imports.append(imp)
        else:
            # Default to third-party
            third_party_imports.append(imp)

    # Write the consolidated file
    with open(file_path, "w") as f:
        # Write standard library imports
        if standard_imports:
            f.write("\n".join(standard_imports))
            f.write("\n\n")

        # Write third-party imports
        if third_party_imports:
            f.write("\n".join(third_party_imports))
            f.write("\n\n")

        # Write local imports
        if local_imports:
            f.write("\n".join(local_imports))
            f.write("\n\n")

        # Write the rest of the content
        f.write("\n".join(non_import_lines))


def format_file_with_ruff(file_path: str) -> None:
    """Format a Python file in-place using ruff."""
    try:
        # First consolidate imports to fix E402 errors
        consolidate_imports_in_file(file_path)

        subprocess.run(
            ["python", "-m", "ruff", "check", "--fix", file_path],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["python", "-m", "ruff", "format", file_path],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        logging.error("Failed to format file with ruff: %s", file_path)
        logging.error("Ruff error details: %s", e)
        # Hard fail on ruff errors
        raise


def extract_imports_from_examples(examples: List[str]) -> Tuple[List[str], List[str]]:
    """Extract and consolidate imports from examples, returning (imports, examples_without_imports)."""
    all_imports = set()
    examples_without_imports = []

    for example in examples:
        lines = example.split("\n")
        import_lines = []
        code_lines = []
        in_import_section = True

        for line in lines:
            stripped = line.strip()

            # Check if this line is an import
            if (
                stripped.startswith("from ") or stripped.startswith("import ")
            ) and "(" not in stripped:
                if in_import_section:
                    import_lines.append(line)
                    all_imports.add(stripped)
                else:
                    # Import found after code started - this is the E402 issue
                    all_imports.add(stripped)
            else:
                # Not an import line
                if stripped and not stripped.startswith("#"):
                    in_import_section = False
                code_lines.append(line)

        # Join the code lines back together
        examples_without_imports.append("\n".join(code_lines))

    # Sort imports for consistency
    consolidated_imports = sorted(list(all_imports))

    return consolidated_imports, examples_without_imports


# Shared template environment instance
_template_env = None


def get_template_environment() -> Environment:
    """Get a shared Jinja2 template environment with standard filters."""
    global _template_env
    if _template_env is None:
        template_dir = os.path.join(os.path.dirname(__file__), "templates")
        _template_env = Environment(loader=FileSystemLoader(template_dir))
        # Add standard filters that are used across the codebase
        _template_env.filters["to_pascal_case"] = to_pascal_case
        _template_env.filters["pascal_to_snake"] = camel_to_snake
        _template_env.filters["camel_to_snake"] = camel_to_snake
        _template_env.filters["camel_to_screaming_snake"] = camel_to_screaming_snake
    return _template_env


def get_template(template_name: str):
    """Get a template from the shared environment."""
    env = get_template_environment()
    return env.get_template(template_name)


def render_template_to_file(template_name: str, context: dict, output_path: str):
    """Helper function to render a template and write it to a file.

    Args:
        template_name: Name of the Jinja2 template file
        context: Dictionary of variables to pass to the template
        output_path: Path where the rendered output should be written
    """
    import logging

    template = get_template(template_name)
    content = template.render(**context)

    with open(output_path, "w") as f:
        f.write(content)

    logging.info("Generated file: %s using template: %s", output_path, template_name)


def render_function_with_unified_template(
    context: dict, output_path: str, is_async: bool = False
):
    """Render a function using the unified template that handles both sync and async.

    Args:
        context: Dictionary of variables to pass to the template
        output_path: Path where the rendered output should be written
        is_async: Whether to generate async function (default: False for sync)
    """
    # Add the is_async flag to context
    context = context.copy()
    context["is_async"] = is_async

    render_template_to_file("unified_function.py.jinja2", context, output_path)


def prepare_function_context(
    func_name: str,
    endpoint: dict,
    args: list,
    response_type: str,
    is_async: bool = False,
    is_paginated: bool = False,
    is_websocket: bool = False,
    **kwargs,
) -> dict:
    """Prepare comprehensive context for universal function template.

    This function moves business logic out of templates and pre-computes
    all the boolean flags and processed data that templates need.

    Args:
        func_name: Name of the function to generate
        endpoint: OpenAPI endpoint specification
        args: Processed list of function arguments
        response_type: Return type annotation
        is_async: Generate async function
        is_paginated: Generate paginated function
        is_websocket: Generate WebSocket function
        **kwargs: Additional context variables

    Returns:
        Complete context dictionary for template rendering
    """
    # Base context
    context = {
        "func_name": func_name,
        "args": args,
        "response_type": response_type,
        "is_async": is_async,
        "is_paginated": is_paginated,
        "is_websocket": is_websocket,
        # Endpoint information
        "method": endpoint.get("method", "get").lower(),
        "url_template": endpoint.get("url", ""),
        "docs": endpoint.get("description", endpoint.get("summary", "")),
        # Request/response flags (pre-computed business logic)
        "has_request_body": "requestBody" in endpoint,
        "request_body_type": kwargs.get("request_body_type", ""),
        # File upload information
        "file_info": kwargs.get("file_info", {}),
        # API section for documentation
        "api_section": kwargs.get("api_section", ""),
        # Function type (computed from booleans for template clarity)
        "function_type": (
            "websocket" if is_websocket else "paginated" if is_paginated else "regular"
        ),
    }

    # Add any additional context
    context.update(kwargs)

    return context


def render_universal_function(
    func_name: str,
    endpoint: dict,
    args: list,
    response_type: str,
    output_path: str,
    **kwargs,
) -> None:
    """Render a function using the universal template.

    This is a convenience function that prepares context and renders
    the universal function template.
    """
    context = prepare_function_context(
        func_name=func_name,
        endpoint=endpoint,
        args=args,
        response_type=response_type,
        **kwargs,
    )

    render_template_to_file("universal_function.py.jinja2", context, output_path)


def process_endpoint_parameters(
    endpoint: dict, data: dict, is_websocket: bool = False
) -> List[dict]:
    """Process endpoint parameters into a standardized format.

    Args:
        endpoint: The endpoint definition from OpenAPI spec
        data: The full OpenAPI specification data
        is_websocket: Whether this is a WebSocket endpoint (affects parameter handling)

    Returns:
        List of parameter dictionaries with keys: name, type, is_optional, in_url, in_query
    """
    from .generate import generate_type_and_example_python

    args: List[dict] = []
    if "parameters" not in endpoint:
        return args

    for param in endpoint["parameters"]:
        param_schema = param.get("schema", {})
        arg_type, _, _ = generate_type_and_example_python(
            "", param_schema, data, None, None
        )

        # For WebSocket endpoints, make all query parameters optional with defaults
        # For regular endpoints, path params are required by default, query params are optional
        if is_websocket and param.get("in") == "query":
            is_optional = True
            if not arg_type.startswith("Optional["):
                arg_type = f"Optional[{arg_type}]"
        else:
            # Regular parameter handling
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

    return args


def resolve_schema_ref(ref: str) -> str:
    """Resolve a schema $ref to just the schema name.

    Args:
        ref: Full $ref string like "#/components/schemas/MyType"

    Returns:
        Schema name like "MyType"
    """
    return ref.replace("#/components/schemas/", "")


def get_schema_description(schema: dict) -> str:
    """Get description from a schema, returning empty string if not present.

    Args:
        schema: Schema dictionary

    Returns:
        Description string or empty string
    """
    return schema.get("description", "")


def process_response_content_types(
    response: dict, allowed_types: Optional[set] = None
) -> List[str]:
    """Process response content types, filtering to allowed types if specified.

    Args:
        response: Response definition from OpenAPI spec
        allowed_types: Set of allowed content types to filter to (optional)

    Returns:
        List of content types found
    """
    if "content" not in response:
        return []

    content_types = list(response["content"].keys())

    if allowed_types:
        content_types = [ct for ct in content_types if ct in allowed_types]

    return content_types


# Common content type sets for reuse
FILE_UPLOAD_CONTENT_TYPES = {
    "multipart/form-data",
    "application/octet-stream",
    "image/*",
    "video/*",
    "audio/*",
    "application/pdf",
    "application/zip",
    "text/plain",
}

FILE_DOWNLOAD_CONTENT_TYPES = {
    "application/octet-stream",
    "image/*",
    "video/*",
    "audio/*",
    "application/pdf",
    "application/zip",
    "text/plain",
    "text/csv",
}
