"""Post-processing functions for generating examples tests and patch JSON files."""

import json
import logging
import os
import re
from typing import List

import jsonpatch

from .utils import extract_imports_from_examples, format_file_with_ruff


def generate_examples_tests(cwd: str, examples: List[str]):
    """Generate the examples test file."""
    examples_test_path = os.path.join(cwd, "kittycad", "tests", "test_examples.py")
    logging.info("opening examples test file: %s", examples_test_path)

    # Extract and consolidate imports from all examples
    consolidated_imports, examples_without_imports = extract_imports_from_examples(
        examples
    )

    # Write all the examples to a file.
    f = open(examples_test_path, "w")

    # Write base imports first
    f.write("import pytest\n")
    f.write("import datetime\n")
    f.write("from typing import Dict, Optional, Union\n")
    f.write("from kittycad import KittyCAD\n\n")

    # Write consolidated imports from examples
    if consolidated_imports:
        f.write("\n".join(consolidated_imports))
        f.write("\n\n")

    # Write examples without their individual imports
    f.write("\n\n".join(examples_without_imports))
    f.close()

    _alias_conflicting_option_headers(examples_test_path)

    # Post-process with ruff to clean up imports and formatting
    format_file_with_ruff(examples_test_path)


def _alias_conflicting_option_headers(examples_test_path: str) -> None:
    """Alias clashing OptionHeaders imports so tests stay lint-clean."""

    with open(examples_test_path, "r") as file:
        content = file.read()

    original_import = "from kittycad.models.web_socket_request import OptionHeaders"
    alias_import = (
        "from kittycad.models.web_socket_request import OptionHeaders as "
        "WebSocketRequestOptionHeaders"
    )

    if original_import not in content:
        return

    # Alias the import line for the websocket variant
    content = content.replace(original_import, alias_import, 1)

    # Update usages to reference the aliased name while preserving whitespace
    content = re.sub(
        r"WebSocketRequest\((\s*)OptionHeaders",
        r"WebSocketRequest(\1WebSocketRequestOptionHeaders",
        content,
    )

    with open(examples_test_path, "w") as file:
        file.write(content)


def generate_patch_json(cwd: str, spec_path: str, data: dict):
    """Generate the kittycad.py.patch.json file."""
    # Read the original spec file as a dict.
    spec = open(spec_path, "r")
    original = json.load(spec)
    # Create the json patch document.
    patch = jsonpatch.make_patch(original, data)

    # Convert this to a dict.
    patch = json.loads(patch.to_string())

    new_patch = []
    # Make sure we aren't changing any components/schemas.
    for index, p in enumerate(patch):
        if not p["path"].startswith("/components"):
            new_patch.append(p)

    # Sort patch operations by path and operation to ensure consistent output
    new_patch.sort(
        key=lambda x: (x.get("path", ""), x.get("op", ""), str(x.get("value", "")))
    )

    # Rewrite the spec back out.
    patch_file = os.path.join(cwd, "kittycad.py.patch.json")

    # Check if the content is actually different before writing
    new_content = json.dumps(new_patch, indent=2)
    current_content = ""
    if os.path.exists(patch_file):
        with open(patch_file, "r") as f:
            current_content = f.read()

    if new_content != current_content:
        with open(patch_file, "w") as f:
            f.write(new_content)
