#!/usr/bin/env python3
import json
import logging
import os
import random
from typing import Any, Dict, List, Optional, Tuple

from prance import BaseParser

# Import specialized modules instead of duplicating functions
from .client_generators import generate_client_classes

# Import function generators from dedicated module
from .schema_analysis import get_tag_one_of, is_nested_object_one_of
from .schema_utils import (
    get_endpoint_refs,
    get_function_result_type,
    get_request_body_type_schema,
)
from .type_generators import generate_types

# Import utilities
from .utils import (
    camel_to_screaming_snake,
    camel_to_snake,
    clean_parameter_name,
    deduplicate_imports,
    to_pascal_case,
)

package_name = "kittycad"

random.seed(10)

examples: List[str] = []


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
    generate_client_classes(cwd, data, examples)


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

    # Detect multipart/file operation endpoints
    from .file_operation_detection import extract_file_parameter_info

    file_info = extract_file_parameter_info(endpoint, data)

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

    # Add file_attachments parameter for multipart endpoints that use JSON body + files pattern
    if file_info.get("has_json_body_multipart", False):
        # Add the necessary imports for file operations
        example_imports = example_imports + (
            "from pathlib import Path\n"
            "from typing import Dict\n"
            "from kittycad._io_types import SyncUpload\n"
        )
        # Add file_attachments parameter with example values
        params_str += "file_attachments={\n"
        params_str += '        "main.kcl": Path("path/to/main.kcl"),\n'
        params_str += '        "helper.kcl": Path("path/to/helper.kcl"),\n'
        params_str += "    },\n"

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
    # Generate the correct documentation link
    # All API methods are documented on the main KittyCAD class page with the structure: client.{tag}.{method}()
    if tag_name:
        docs_link = f"https://python.api.docs.zoo.dev/_autosummary/kittycad.KittyCAD.html#kittycad.KittyCAD.{tag_name}"
    else:
        docs_link = f"https://python.api.docs.zoo.dev/_autosummary/kittycad.KittyCAD.html#kittycad.KittyCAD.{fn_name}"

    data["paths"][name][method]["x-python"] = {
        "example": cleaned_example.replace("def test_", "def example_"),
        "libDocsLink": docs_link,
    }

    return data


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
