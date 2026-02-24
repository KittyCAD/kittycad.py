"""Post-processing functions for generating examples tests and patch JSON files."""

import json
import logging
import os
import re
from typing import Dict, List, Tuple, TypedDict

import jsonpatch

try:
    from .utils import (
        extract_imports_from_examples,
        format_file_with_ruff,
        to_pascal_case,
    )
except ImportError:
    from utils import (
        extract_imports_from_examples,
        format_file_with_ruff,
        to_pascal_case,
    )


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

    _alias_conflicting_model_imports(examples_test_path)

    # Post-process with ruff to clean up imports and formatting
    format_file_with_ruff(examples_test_path)


_MODEL_IMPORT_PATTERN = re.compile(
    r"^from kittycad\.models\.(?P<module>[a-z0-9_]+) import (?P<imports>.+)$"
)


class _ParsedImportLine(TypedDict):
    module_name: str
    imported_names: List[str]


def _parse_import_name(import_name: str) -> Tuple[str, str]:
    """Split an import segment into (name, alias)."""

    name, alias_separator, alias = import_name.partition(" as ")
    if not alias_separator:
        return import_name.strip(), ""
    return name.strip(), alias.strip()


def _alias_conflicting_model_imports(examples_test_path: str) -> None:
    """Alias clashing model imports in generated examples tests.

    Some schema unions define the same option class name in different modules
    (e.g. input_format3d.OptionPly vs output_format3d.OptionPly). Ruff flags this
    as F811, so alias all but the first import and update the matching wrapper
    constructor usage to point at the alias.
    """

    with open(examples_test_path, "r") as file:
        content = file.read()

    lines = content.splitlines()
    parsed_model_import_lines: Dict[int, _ParsedImportLine] = {}
    imported_name_occurrences: Dict[str, List[Tuple[int, str]]] = {}

    for index, line in enumerate(lines):
        stripped_line = line.strip()
        match = _MODEL_IMPORT_PATTERN.match(stripped_line)
        if match is None:
            continue

        module_name = match.group("module")
        imported_names = [name.strip() for name in match.group("imports").split(",")]
        parsed_model_import_lines[index] = {
            "module_name": module_name,
            "imported_names": imported_names,
        }

        for import_name in imported_names:
            symbol_name, _ = _parse_import_name(import_name)
            imported_name_occurrences.setdefault(symbol_name, []).append(
                (index, module_name)
            )

    # Tracks which wrapper constructors should swap Symbol -> AliasedSymbol.
    # Tuple format: (wrapper_class_name, symbol_name, alias_name)
    replacement_rules: List[Tuple[str, str, str]] = []

    for symbol_name, occurrences in imported_name_occurrences.items():
        if len(occurrences) < 2:
            continue

        for occurrence_index, (line_index, module_name) in enumerate(occurrences):
            if occurrence_index == 0:
                continue

            wrapper_class_name = to_pascal_case(module_name)
            alias_name = f"{wrapper_class_name}{symbol_name}"

            parsed_line = parsed_model_import_lines[line_index]
            aliased_import_names: List[str] = []
            for import_name in parsed_line["imported_names"]:
                imported_symbol_name, _ = _parse_import_name(import_name)
                if imported_symbol_name == symbol_name:
                    aliased_import_names.append(f"{symbol_name} as {alias_name}")
                else:
                    aliased_import_names.append(import_name)

            parsed_line["imported_names"] = aliased_import_names
            replacement_rules.append((wrapper_class_name, symbol_name, alias_name))

    for line_index, parsed_line in parsed_model_import_lines.items():
        module_name = parsed_line["module_name"]
        imported_names = parsed_line["imported_names"]
        lines[line_index] = (
            f"from kittycad.models.{module_name} import {', '.join(imported_names)}"
        )

    content = "\n".join(lines)

    for wrapper_class_name, symbol_name, alias_name in replacement_rules:
        content = re.sub(
            rf"({wrapper_class_name}\(\s*){symbol_name}\b",
            rf"\1{alias_name}",
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
