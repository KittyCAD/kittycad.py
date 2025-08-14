#!/usr/bin/env python3
"""
Utility functions for code generation.
Contains helper functions for string manipulation, import handling, etc.
"""

import logging
import re
import subprocess
from typing import List, Tuple


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
    """Convert CamelCase/PascalCase to snake_case, but only if not already in snake_case."""
    if is_snake_case(name):
        return name
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


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
