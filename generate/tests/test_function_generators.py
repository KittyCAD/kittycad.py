"""Tests for endpoint function generation."""

import ast
import warnings
from collections.abc import Callable

import pytest

from generate.function_generators import generate_async_function, generate_sync_function


@pytest.mark.parametrize(
    "generate_function", [generate_sync_function, generate_async_function]
)
@pytest.mark.parametrize("paginated", [False, True])
@pytest.mark.parametrize("doc_field", ["description", "summary"])
@pytest.mark.parametrize(
    "docs",
    [
        r'Example request (curl): ``` curl -X POST https://api.zoo.dev/user/factory/jobs \   -H "Authorization: Bearer $ZOO_API_TOKEN" ```',
        r"Literal escapes: \n, \t, \u1234, and \\",
        "Trailing backslash: \\",
    ],
)
def test_docstring_backslashes_are_preserved(
    generate_function: Callable[[str, str, dict, dict], str],
    paginated: bool,
    doc_field: str,
    docs: str,
) -> None:
    endpoint: dict = {
        "operationId": "get_test",
        doc_field: docs,
        "responses": {
            "200": {
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/TestResultsPage"}
                    }
                }
            }
        },
    }
    if paginated:
        endpoint["x-dropshot-pagination"] = {}

    data = {
        "components": {
            "schemas": {"TestResultsPage": {"type": "object", "properties": {}}}
        }
    }
    source = "class Example:\n" + generate_function("/test", "get", endpoint, data)
    with warnings.catch_warnings():
        warnings.simplefilter("error", SyntaxWarning)
        warnings.simplefilter("error", DeprecationWarning)
        tree = ast.parse(source)

    cls = tree.body[0]
    assert isinstance(cls, ast.ClassDef)
    method = cls.body[0]
    assert isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef))
    docstring = ast.get_docstring(method)
    assert docstring is not None
    assert docstring.split("\n\n", 1)[0] == docs
