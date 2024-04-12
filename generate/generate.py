#!/usr/bin/env python3
import io
import json
import logging
import os
import random
import re
from typing import Any, Dict, List, Optional, Tuple, TypedDict

import black
import isort
import jinja2
import jsonpatch
from prance import BaseParser

package_name = "kittycad"

random.seed(10)

examples: List[str] = []


def main():
    cwd = os.getcwd()
    spec_path = os.path.join(cwd, "spec.json")
    logging.info("opening spec file: ", spec_path)
    parser = BaseParser(spec_path)

    # Generate the types.
    generateTypes(cwd, parser.specification)

    # Generate the paths.
    data = generatePaths(cwd, parser.specification)

    # Add the client information to the generation.
    data["info"]["x-python"] = {
        "client": """# Create a client with your token.
from kittycad.client import Client

client = Client(token="$TOKEN")

# - OR -

# Create a new client with your token parsed from the environment variable:
#   `KITTYCAD_API_TOKEN`.
from kittycad.client import ClientFromEnv

client = ClientFromEnv()

# NOTE: The python library additionally implements asyncio, however all the code samples we
# show below use the sync functions for ease of use and understanding.
# Check out the library docs at:
# https://python.api.docs.kittycad.io/_autosummary/kittycad.api.html#module-kittycad.api
# for more details.""",
        "install": "pip install kittycad",
    }

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

    # Rewrite the spec back out.
    patch_file = os.path.join(cwd, "kittycad.py.patch.json")
    f = open(patch_file, "w")
    f.write(json.dumps(new_patch, indent=2))
    f.close()

    # Write all the examples to a file.
    examples_test_path = os.path.join(cwd, "kittycad", "examples_test.py")
    logging.info("opening examples test file: ", spec_path)

    f = open(examples_test_path, "w")
    f.write("import pytest\n\n")
    f.write("\n\n".join(examples))
    f.close()


def generatePaths(cwd: str, parser: dict) -> dict:
    # Make sure we have the directory.
    path = os.path.join(cwd, "kittycad", "api")
    os.makedirs(path, exist_ok=True)

    # Open the __init__.py file.
    file_name = "__init__.py"
    file_path = os.path.join(path, file_name)
    f = open(file_path, "w")
    f.write('""" Contains methods for accessing the API """\n')
    # Close the file.
    f.close()

    # Generate the directory/__init__.py for each of the tags.
    tags = parser["tags"]
    for tag in tags:
        tag_name = tag["name"].replace("-", "_")
        tag_description = tag["description"]
        tag_path = os.path.join(path, tag_name)
        # Esnure the directory exists.
        os.makedirs(tag_path, exist_ok=True)
        # Open the __init__.py file.
        file_name = "__init__.py"
        file_path = os.path.join(tag_path, file_name)
        f = open(file_path, "w")
        f.write(
            '""" Contains methods for accessing the '
            + tag_name
            + " API paths: "
            + tag_description
            + ' """ # noqa: E501\n'
        )
        # Close the file.
        f.close()

    # Generate the paths.
    data = parser
    paths = data["paths"]
    for p in paths:
        # If p starts with /oauth2 we can skip it.
        # We don't care about generating methods for those.
        if p.startswith("/oauth2"):
            continue
        else:
            for method in paths[p]:
                # Skip OPTIONS.
                if method.upper() != "OPTIONS":
                    endpoint = paths[p][method]
                    data = generatePath(path, p, method, endpoint, data)

    return data


def generateTypeAndExamplePython(
    name: str, schema: dict, data: dict, import_path: Optional[str], tag: Optional[str]
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
            items_type, items_example, items_imports = generateTypeAndExamplePython(
                "", schema["items"], data, None, None
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
                    ) = generateTypeAndExamplePython("", prop, data, import_path, tag)
                    example_imports = example_imports + prop_imports
                    parameter_example = parameter_example + (
                        "\n"
                        + clean_parameter_name(property_name)
                        + "="
                        + prop_example
                        + ",\n"
                    )

            parameter_example = parameter_example + ")"
        elif (
            schema["type"] == "object"
            and "additionalProperties" in schema
            and schema["additionalProperties"] is not False
        ):
            items_type, items_example, items_imports = generateTypeAndExamplePython(
                "", schema["additionalProperties"], data, None, None
            )
            example_imports = example_imports + items_imports
            parameter_type = "Dict[str, " + items_type + "]"
            parameter_example = '{"<string>": ' + items_example + "}"
        else:
            logging.error("schema: %s", json.dumps(schema, indent=4))
            raise Exception("Unknown parameter type")
    elif "oneOf" in schema and len(schema["oneOf"]) > 0:
        one_of = schema["oneOf"][0]
        if len(schema["oneOf"]) > 1:
            one_of = schema["oneOf"][1]

        # Check if this is a nested object.
        if isNestedObjectOneOf(schema):
            if "properties" in one_of:
                properties = one_of["properties"]
                for prop in properties:
                    return generateTypeAndExamplePython(
                        prop, properties[prop], data, camel_to_snake(name), None
                    )
                    break
            elif "type" in one_of and one_of["type"] == "string":
                return generateTypeAndExamplePython(
                    name, one_of, data, camel_to_snake(name), None
                )

        tag = getTagOneOf(schema)

        if (
            "properties" in one_of
            and "type" in one_of["properties"]
            and "enum" in one_of["properties"]["type"]
        ):
            return generateTypeAndExamplePython(
                one_of["properties"]["type"]["enum"][0],
                one_of,
                data,
                camel_to_snake(name),
                tag,
            )
        else:
            return generateTypeAndExamplePython(name, one_of, data, None, None)
    elif "allOf" in schema and len(schema["allOf"]) == 1:
        return generateTypeAndExamplePython(name, schema["allOf"][0], data, None, None)
    elif "$ref" in schema:
        parameter_type = schema["$ref"].replace("#/components/schemas/", "")
        # Get the schema for the reference.
        ref_schema = data["components"]["schemas"][parameter_type]

        return generateTypeAndExamplePython(
            parameter_type, ref_schema, data, None, None
        )
    else:
        logging.error("schema: %s", json.dumps(schema, indent=4))
        raise Exception("Unknown parameter type")

    return parameter_type, parameter_example, example_imports


def generatePath(path: str, name: str, method: str, endpoint: dict, data: dict) -> dict:
    # Generate the path.
    fn_name = camel_to_snake(endpoint["operationId"])
    file_name = fn_name + ".py"
    tag_name = ""
    # Add the tag to the path if it exists.
    if "tags" in endpoint:
        tag_name = endpoint["tags"][0].replace("-", "_")
        path = os.path.join(path, tag_name)
    file_path = os.path.join(path, file_name)
    logging.info("generating path functions: ", name, " at: ", file_path)

    endpoint_refs = getEndpointRefs(endpoint, data)
    parameter_refs = getParameterRefs(endpoint)
    request_body_refs = getRequestBodyRefs(endpoint)
    (request_body_type, request_body_schema) = getRequestBodyTypeSchema(endpoint, data)

    success_type = ""
    if len(endpoint_refs) > 0:
        if len(endpoint_refs) > 2:
            er = getEndpointRefs(endpoint, data)
            er.remove("Error")
            success_type = "Union[" + ", ".join(er) + "]"
        else:
            success_type = endpoint_refs[0]

    example_imports = (
        """
from kittycad.client import ClientFromEnv
from kittycad.api."""
        + tag_name
        + """ import """
        + fn_name
        + """
from kittycad.types import Response
"""
    )

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
            ) = generateTypeAndExamplePython("", parameter["schema"], data, None, None)
            example_imports = example_imports + more_example_imports

            if "nullable" in parameter["schema"] and parameter["schema"]["nullable"]:
                parameter_type = "Optional[" + parameter_type + "]"
                optional_args.append(
                    clean_parameter_name(parameter_name)
                    + "= None, # "
                    + parameter_type
                    + "\n"
                )
            else:
                params_str += (
                    clean_parameter_name(parameter_name)
                    + "="
                    + parameter_example
                    + ",\n"
                )

        for optional_arg in optional_args:
            params_str += optional_arg

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
            ) = generateTypeAndExamplePython(request_body_type, rbs, data, None, None)
            body_example = body_ex
            if "x-dropshot-websocket" not in endpoint:
                params_str += "body=" + body_example + ",\n"
            else:
                body_example = request_body_type + "(" + body_example + ")"
                example_imports = (
                    example_imports
                    + "from kittycad.models import "
                    + request_body_type
                    + "\n"
                )
            example_imports = example_imports + more_example_imports

    example_variable = ""
    example_variable_response = ""

    response_type = getFunctionResultType(endpoint, endpoint_refs)
    detailed_response_type = getDetailedFunctionResultType(endpoint, endpoint_refs)
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

        example_variable = "result: " + response_type + " = "

        example_imports = example_imports + "from kittycad.types import Response\n"
        example_imports = example_imports + "from kittycad.models import Error\n"
        example_variable_response = "response: " + detailed_response_type + " = "

    # Add some new lines.
    example_imports = example_imports + "\n\n"

    short_sync_example = (
        """def test_"""
        + fn_name
        + """():
    # Create our client.
    client = ClientFromEnv()

    """
        + example_variable
        + fn_name
        + """.sync(client=client,\n"""
        + params_str
        + """)
"""
    )

    if (
        success_type != "str"
        and success_type != "dict"
        and success_type != "None"
        and success_type != ""
    ):
        example_success_type = success_type

        short_sync_example = short_sync_example + (
            """
    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: """
            + example_success_type
            + """ = result
    print(body)

"""
        )

    long_example = (
        """

    # OR if you need more info (e.g. status_code)
    """
        + example_variable_response
        + fn_name
        + """.sync_detailed(client=client,\n"""
        + params_str
        + """)

# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_"""
        + fn_name
        + """_async():
    # Create our client.
    client = ClientFromEnv()

    """
        + example_variable
        + "await "
        + fn_name
        + """.asyncio(client=client,\n"""
        + params_str
        + """)

    # OR run async with more info
    """
        + example_variable_response
        + "await "
        + fn_name
        + """.asyncio_detailed(client=client,\n"""
        + params_str
        + """)"""
    )

    # Generate the websocket examples.
    if "x-dropshot-websocket" in endpoint:
        if request_body_type is None:
            short_sync_example = (
                """def test_"""
                + fn_name
                + """():
            # Create our client.
            client = ClientFromEnv()

            # Connect to the websocket.
            with """
                + fn_name
                + """.sync(client=client,"""
                + params_str
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
            # Create our client.
            client = ClientFromEnv()

            # Connect to the websocket.
            with """
                + fn_name
                + """.WebSocket(client=client,"""
                + params_str
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
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    websocket = await """
            + fn_name
            + """.asyncio(client=client,"""
            + params_str
            + """)

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)
    """
        )

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
    line_length = 82
    short_sync_example = example_imports + short_sync_example
    cleaned_example = black.format_str(
        isort.api.sort_code_string(
            short_sync_example,
        ),
        mode=black.FileMode(line_length=line_length),
    )

    examples.append(example)

    # Add our example to our json output.
    data["paths"][name][method]["x-python"] = {
        "example": cleaned_example.replace("def test_", "def example_"),
        "libDocsLink": "https://python.api.docs.kittycad.io/_autosummary/kittycad.api."
        + tag_name
        + "."
        + fn_name
        + ".html",
    }

    # Start defining the template info.
    ArgType = TypedDict(
        "ArgType",
        {
            "name": str,
            "type": str,
            "in_url": bool,
            "in_query": bool,
            "is_optional": bool,
        },
    )
    TemplateType = TypedDict(
        "TemplateType",
        {
            "imports": List[str],
            "response_type": str,
            "args": List[ArgType],
            "url_template": str,
            "method": str,
            "docs": str,
            "parse_response": str,
            "has_request_body": bool,
            "request_body_type": str,
        },
    )
    template_info: TemplateType = {
        "imports": [],
        "response_type": response_type,
        "args": [],
        "url_template": "{}" + name,
        "method": method,
        "docs": "",
        "parse_response": "",
        "has_request_body": False,
        "request_body_type": "",
    }

    if len(endpoint_refs) == 0:
        template_info["response_type"] = ""

    if "x-dropshot-websocket" in endpoint:
        template_info["response_type"] = (
            template_info["response_type"].replace("Optional[", "").replace("]", "")
        )

    if "description" in endpoint:
        template_info["docs"] = endpoint["description"]

    # Import our references for responses.
    for ref in endpoint_refs:
        if ref.startswith("List[") and ref.endswith("]"):
            ref = ref.replace("List[", "").replace("]", "")
        if ref != "str" and ref != "dict":
            template_info["imports"].append(
                "from ...models." + camel_to_snake(ref) + " import " + ref
            )
    for ref in parameter_refs:
        template_info["imports"].append(
            "from ...models." + camel_to_snake(ref) + " import " + ref
        )
    for ref in request_body_refs:
        template_info["imports"].append(
            "from ...models." + camel_to_snake(ref) + " import " + ref
        )

    # Iterate over the responses.
    parse_response = io.StringIO()
    if len(endpoint_refs) > 0:
        responses = endpoint["responses"]
        for response_code in responses:
            response = responses[response_code]
            if response_code == "default":
                # This is no content.
                parse_response.write("\treturn None\n")
            elif response_code == "204" or response_code == "302":
                # This is no content.
                parse_response.write("\treturn None\n")
            else:
                parse_response.write(
                    "\tif response.status_code == "
                    + response_code.replace("XX", "00")
                    + ":\n"
                )
                is_one_of = False
                if "content" in response:
                    content = response["content"]
                    for content_type in content:
                        if content_type == "application/json":
                            json = content[content_type]["schema"]
                            if "$ref" in json:
                                ref = json["$ref"].replace("#/components/schemas/", "")
                                schema = data["components"]["schemas"][ref]
                                # Let's check if it is a oneOparse_response.
                                if "oneOf" in schema:
                                    is_one_of = True
                                    # We want to parse each of the possible types.
                                    parse_response.write("\t\tdata = response.json()\n")
                                    for index, one_of in enumerate(schema["oneOf"]):
                                        ref = getOneOfRefType(one_of)
                                        parse_response.write("\t\ttry:\n")
                                        parse_response.write(
                                            "\t\t\tif not isinstance(data, dict):\n"
                                        )
                                        parse_response.write(
                                            "\t\t\t\traise TypeError()\n"
                                        )
                                        option_name = "option_" + camel_to_snake(ref)
                                        parse_response.write(
                                            "\t\t\t"
                                            + option_name
                                            + " = "
                                            + snake_to_title(ref)
                                            + "(**data)\n"
                                        )
                                        parse_response.write(
                                            "\t\t\treturn " + option_name + "\n"
                                        )
                                        parse_response.write("\t\texcept ValueError:\n")
                                        if index == len(schema["oneOf"]) - 1:
                                            # On the last one raise the error.
                                            parse_response.write("\t\t\traise\n")
                                        else:
                                            parse_response.write("\t\t\tpass\n")
                                        parse_response.write("\t\texcept TypeError:\n")
                                        if index == len(schema["oneOf"]) - 1:
                                            # On the last one raise the error.
                                            parse_response.write("\t\t\traise\n")
                                        else:
                                            parse_response.write("\t\t\tpass\n")
                                else:
                                    parse_response.write(
                                        "\t\tresponse_"
                                        + response_code
                                        + " = "
                                        + ref
                                        + "(**response.json())\n"
                                    )
                            elif "type" in json:
                                if json["type"] == "array":
                                    items = json["items"]
                                    if "$ref" in items:
                                        ref = items["$ref"].replace(
                                            "#/components/schemas/", ""
                                        )
                                        parse_response.write(
                                            "\t\tresponse_" + response_code + " = [\n"
                                        )
                                        parse_response.write(
                                            "\t\t\t" + ref + "(**item)\n"
                                        )
                                        parse_response.write(
                                            "\t\t\tfor item in response.json()\n"
                                        )
                                        parse_response.write("\t\t]\n")
                                    elif "type" in items:
                                        if items["type"] == "string":
                                            parse_response.write(
                                                "\t\tresponse_"
                                                + response_code
                                                + " = [\n"
                                            )
                                            parse_response.write("\t\t\tstr(**item)\n")
                                            parse_response.write(
                                                "\t\t\tfor item in response.json()\n"
                                            )
                                            parse_response.write("\t\t]\n")
                                        else:
                                            raise Exception("Unknown array type", items)
                                    else:
                                        raise Exception("Unknown array type")
                                elif json["type"] == "string":
                                    parse_response.write(
                                        "\t\tresponse_"
                                        + response_code
                                        + " = response.text\n"
                                    )
                                elif (
                                    json["type"] == "object"
                                    and "additionalProperties" in json
                                ):
                                    parse_response.write(
                                        "\t\tresponse_"
                                        + response_code
                                        + " = response.json()\n"
                                    )
                                else:
                                    print(json)
                                    raise Exception("Unknown type", json["type"])
                            else:
                                parse_response.write(
                                    "\t\tresponse_"
                                    + response_code
                                    + " = response.json()\n"
                                )

                elif "$ref" in response:
                    schema_name = response["$ref"].replace(
                        "#/components/responses/", ""
                    )
                    schema = data["components"]["responses"][schema_name]
                    if "content" in schema:
                        content = schema["content"]
                        for content_type in content:
                            if content_type == "application/json":
                                json = content[content_type]["schema"]
                                if "$ref" in json:
                                    ref = json["$ref"].replace(
                                        "#/components/schemas/", ""
                                    )
                                    parse_response.write(
                                        "\t\tresponse_"
                                        + response_code
                                        + " = "
                                        + ref
                                        + "(**response.json())\n"
                                    )
                else:
                    print(endpoint)
                    raise Exception("response not supported")

                if not is_one_of:
                    parse_response.write("\t\treturn response_" + response_code + "\n")

        # End the method.
        parse_response.write("\treturn Error(**response.json())\n")
    else:
        parse_response.write("\treturn\n")

    template_info["parse_response"] = parse_response.getvalue()

    # Iterate over the parameters.
    optional_args = []
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
                logging.error("parameter: ", parameter)
                raise Exception("Unknown parameter type")
            if "nullable" in parameter["schema"]:
                if parameter["schema"]["nullable"]:
                    parameter_type = "Optional[" + parameter_type + "] = None"
                    template_info["args"].append(
                        {
                            "name": camel_to_snake(parameter_name),
                            "type": parameter_type,
                            "in_url": "in" in parameter and (parameter["in"] == "path"),
                            "in_query": "in" in parameter
                            and (parameter["in"] == "query"),
                            "is_optional": True,
                        }
                    )
                else:
                    template_info["args"].append(
                        {
                            "name": camel_to_snake(parameter_name),
                            "type": parameter_type,
                            "in_url": "in" in parameter and (parameter["in"] == "path"),
                            "in_query": "in" in parameter
                            and (parameter["in"] == "query"),
                            "is_optional": False,
                        }
                    )
            else:
                template_info["args"].append(
                    {
                        "name": camel_to_snake(parameter_name),
                        "type": parameter_type,
                        "in_url": "in" in parameter and (parameter["in"] == "path"),
                        "in_query": "in" in parameter and (parameter["in"] == "query"),
                        "is_optional": False,
                    }
                )

    if request_body_type:
        template_info["args"].append(
            {
                "name": "body",
                "type": request_body_type,
                "in_url": False,
                "in_query": False,
                "is_optional": False,
            }
        )
        template_info["has_request_body"] = True
        template_info["request_body_type"] = request_body_type

    # Generate the template for the functions.
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("generate/"))
    template_file = "functions.py.jinja2"
    if "x-dropshot-websocket" in endpoint:
        template_file = "functions-ws.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)
    with open(file_path, mode="w", encoding="utf-8") as message:
        message.write(content)
        logging.info(f"... wrote {file_path}")

    return data


def generateTypes(cwd: str, parser: dict):
    # Make sure we have the directory.
    path = os.path.join(cwd, "kittycad", "models")
    os.makedirs(path, exist_ok=True)

    # Open the __init__.py file.
    file_name = "__init__.py"
    file_path = os.path.join(path, file_name)
    f = open(file_path, "w")
    f.write('""" Contains all the data models used in inputs/outputs """\n')
    f.write("\n")

    # Generate the types.
    data = parser
    schemas = data["components"]["schemas"]
    for key in schemas:
        schema = schemas[key]
        logging.info("generating schema: ", key)
        generateType(path, key, schema, data)
        f.write("from ." + camel_to_snake(key) + " import " + key + "\n")

    # This is a hot fix for the empty type.
    # We likely need a better way to handle this.
    f.write("from .empty import Empty\n")

    # Close the file.
    f.close()


def generateType(path: str, name: str, schema: dict, data: dict):
    file_path = path
    if path.endswith(".py") is False:
        # Generate the type.
        file_name = camel_to_snake(name) + ".py"
        file_path = os.path.join(path, file_name)

    if "type" in schema:
        type_name = schema["type"]
        if type_name == "object":
            generateObjectType(file_path, name, schema, type_name, data)
        elif type_name == "string" and "enum" in schema and schema["enum"] != [None]:
            generateEnumType(file_path, name, schema, type_name, [])
        elif type_name == "integer":
            generateIntegerType(file_path, name, schema, type_name)
        elif type_name == "number":
            generateFloatType(file_path, name, schema, type_name)
        elif type_name == "string":
            generateStringType(file_path, name, schema, type_name)
        else:
            logging.error("unsupported type: ", type_name)
            raise Exception("unsupported type: ", type_name)
    elif "$ref" in schema:
        # Skip it since we will already have generated it.
        return
    elif "oneOf" in schema:
        generateOneOfType(file_path, name, schema, data)
    elif "anyOf" in schema:
        generateAnyOfType(file_path, name, schema, data)
    else:
        logging.error("schema: ", [schema])
        logging.error("unsupported type: ", name)
        raise Exception("unsupported type: ", name)


def generateStringType(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: ", name, " at: ", path)
    f = open(path, "w")

    TemplateType = TypedDict(
        "TemplateType",
        {
            "description": str,
            "name": str,
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"]

    template_info: TemplateType = {
        "description": description,
        "name": name,
    }

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("generate/"))
    template_file = "str.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)

    f.write(content)

    # Close the file.
    f.close()


def generateIntegerType(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: ", name, " at: ", path)
    f = open(path, "w")

    TemplateType = TypedDict(
        "TemplateType",
        {
            "description": str,
            "name": str,
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"]

    template_info: TemplateType = {
        "description": description,
        "name": name,
    }

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("generate/"))
    template_file = "int.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)

    f.write(content)

    # Close the file.
    f.close()


def generateFloatType(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: ", name, " at: ", path)
    f = open(path, "w")

    TemplateType = TypedDict(
        "TemplateType",
        {
            "description": str,
            "name": str,
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"]

    template_info: TemplateType = {
        "description": description,
        "name": name,
    }

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("generate/"))
    template_file = "float.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)

    f.write(content)

    # Close the file.
    f.close()


def generateEnumType(
    path: str,
    name: str,
    schema: dict,
    type_name: str,
    additional_docs: List[str],
):
    logging.info("generating type: ", name, " at: ", path)
    f = open(path, "w")

    code = generateEnumTypeCode(name, schema, type_name, additional_docs)
    f.write(code)

    # Close the file.
    f.close()


def generateEnumTypeCode(
    name: str,
    schema: dict,
    type_name: str,
    additional_docs: List[str],
) -> str:
    f = io.StringIO()

    f.write("from enum import Enum\n")
    f.write("\n")
    f.write("class " + name + "(str, Enum):\n")
    if "description" in schema:
        f.write('\t""" ' + schema["description"] + ' """ # noqa: E501\n')
    # Iterate over the properties.
    for num, value in enumerate(schema["enum"], start=0):
        enum_name = camel_to_screaming_snake(value)
        if enum_name == "":
            enum_name = "EMPTY"
        elif enum_name == "1":
            enum_name = "ONE"
        elif enum_name == "2":
            enum_name = "TWO"

        # Write the description if there is one.
        if len(additional_docs) > 0:
            additional_doc = additional_docs[num]
            if additional_doc != "":
                f.write('\t"""# ' + additional_docs[num] + ' """ # noqa: E501\n')
        f.write("\t" + enum_name + " = '" + value + "'\n")

    # close the enum.
    f.write("\n")
    f.write("\tdef __str__(self) -> str:\n")
    f.write("\t\treturn str(self.value)\n")

    value = f.getvalue()

    # Close the file.
    f.close()

    return value


def generateAnyOfType(path: str, name: str, schema: dict, data: dict):
    logging.info("generating type: ", name, " at: ", path)

    if isEnumWithDocsOneOf(schema):
        additional_docs = []
        enum = []
        # We want to treat this as an enum with additional docs.
        for any_of in schema["anyOf"]:
            enum.append(any_of["enum"][0])
            if "description" in any_of:
                additional_docs.append(any_of["description"])
            else:
                additional_docs.append("")
        # Write the enum.
        schema["enum"] = enum
        schema["type"] = "string"
        generateEnumType(path, name, schema, "string", additional_docs)
        # return early.
        return

    # Open our file.
    f = open(path, "w")

    # Import the refs if there are any.
    all_options = []
    for any_of in schema["anyOf"]:
        if "allOf" in any_of:
            for all_of in any_of["allOf"]:
                if "$ref" in all_of:
                    ref = all_of["$ref"]
                    ref_name = ref[ref.rfind("/") + 1 :]
                    f.write(
                        "from ."
                        + camel_to_snake(ref_name)
                        + " import "
                        + ref_name
                        + "\n"
                    )
                    all_options.append(ref_name)
        if "$ref" in any_of:
            ref = any_of["$ref"]
            ref_name = ref[ref.rfind("/") + 1 :]
            f.write("from ." + camel_to_snake(ref_name) + " import " + ref_name + "\n")
            all_options.append(ref_name)

    if isNestedObjectAnyOf(schema):
        # We want to write each of the nested objects.
        for any_of in schema["anyOf"]:
            # Get the nested object.
            if "properties" in any_of:
                for prop_name in any_of["properties"]:
                    nested_object = any_of["properties"][prop_name]
                    if nested_object == {}:
                        f.write("from typing import Any\n")
                        f.write(prop_name + " = Any\n")
                        f.write("\n")
                        all_options.append(prop_name)
                    elif "$ref" in nested_object:
                        ref = nested_object["$ref"]
                        ref_name = ref[ref.rfind("/") + 1 :]
                        f.write(
                            "from ."
                            + camel_to_snake(ref_name)
                            + " import "
                            + ref_name
                            + "\n"
                        )
                        f.write("\n")
                        if prop_name != ref_name:
                            f.write(prop_name + " = " + ref_name + "\n")
                            f.write("\n")
                        all_options.append(prop_name)
                    else:
                        object_code = generateObjectTypeCode(
                            prop_name, nested_object, "object", data, None, None
                        )
                        f.write(object_code)
                        f.write("\n")
                        all_options.append(prop_name)
            elif "type" in any_of and any_of["type"] == "string":
                enum_code = generateEnumTypeCode(
                    any_of["enum"][0], any_of, "string", []
                )
                f.write(enum_code)
                f.write("\n")
                all_options.append(any_of["enum"][0])

    # Check if each any_of has the same enum of one.
    tag = getTagAnyOf(schema)

    if tag is not None:
        # Generate each of the options from the tag.
        for any_of in schema["anyOf"]:
            # Get the value of the tag.
            object_name = any_of["properties"][tag]["enum"][0]
            object_code = generateObjectTypeCode(
                object_name, any_of, "object", data, tag, None
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(object_name)
    else:
        # We want to write each of the nested objects.
        for any_of in schema["anyOf"]:
            # Get the nested object.
            if "properties" in any_of:
                for prop_name in any_of["properties"]:
                    nested_object = any_of["properties"][prop_name]
                    if nested_object == {}:
                        f.write("from typing import Any\n")
                        f.write(prop_name + " = Any\n")
                        f.write("\n")
                        all_options.append(prop_name)
                    elif "$ref" in nested_object:
                        ref = nested_object["$ref"]
                        ref_name = ref[ref.rfind("/") + 1 :]
                        f.write(
                            "from ."
                            + camel_to_snake(ref_name)
                            + " import "
                            + ref_name
                            + "\n"
                        )
                        f.write("\n")
                        if prop_name != ref_name:
                            f.write(prop_name + " = " + ref_name + "\n")
                            f.write("\n")
                        all_options.append(prop_name)
                    else:
                        object_code = generateObjectTypeCode(
                            prop_name, nested_object, "object", data, None, None
                        )
                        f.write(object_code)
                        f.write("\n")
                        all_options.append(prop_name)
            elif "type" in any_of and any_of["type"] == "string":
                enum_code = generateEnumTypeCode(
                    any_of["enum"][0], any_of, "string", []
                )
                f.write(enum_code)
                f.write("\n")
                all_options.append(any_of["enum"][0])

    # Write the sum type.
    description = getAnyOfDescription(schema)
    content = generateUnionType(all_options, name, description, tag)
    f.write(content)

    # Close the file.
    f.close()


def getAnyOfDescription(schema: dict) -> str:
    if "description" in schema:
        return schema["description"]
    else:
        return ""


def generateUnionType(
    types: List[str], name: str, description: str, tag: Optional[str]
) -> str:
    ArgType = TypedDict(
        "ArgType",
        {
            "name": str,
            "var0": str,
            "var1": str,
            "check": str,
            "value": str,
        },
    )
    TemplateType = TypedDict(
        "TemplateType",
        {
            "types": List[ArgType],
            "description": str,
            "name": str,
            "tag": Optional[str],
        },
    )
    template_info: TemplateType = {
        "types": [],
        "description": description,
        "name": name,
        "tag": tag,
    }
    for type in types:
        if type == "SuccessWebSocketResponse":
            template_info["types"].append(
                {
                    "name": type,
                    "var0": randletter(),
                    "var1": randletter(),
                    "check": "success",
                    "value": "True",
                }
            )
        elif type == "FailureWebSocketResponse":
            template_info["types"].append(
                {
                    "name": type,
                    "var0": randletter(),
                    "var1": randletter(),
                    "check": "success",
                    "value": "False",
                }
            )
        else:
            template_info["types"].append(
                {
                    "name": type,
                    "var0": randletter(),
                    "var1": randletter(),
                    "check": "type",
                    "value": '"' + type + '"',
                }
            )

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("generate/"))
    template_file = "union-type.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)

    return content


def generateOneOfType(path: str, name: str, schema: dict, data: dict):
    logging.info("generating type: ", name, " at: ", path)

    if isEnumWithDocsOneOf(schema):
        additional_docs = []
        enum = []
        # We want to treat this as an enum with additional docs.
        for one_of in schema["oneOf"]:
            enum.append(one_of["enum"][0])
            if "description" in one_of:
                additional_docs.append(one_of["description"])
            else:
                additional_docs.append("")
        # Write the enum.
        schema["enum"] = enum
        schema["type"] = "string"
        generateEnumType(path, name, schema, "string", additional_docs)
        # return early.
        return

    # Open our file.
    f = open(path, "w")

    # Import the refs if there are any.
    all_options = []
    for one_of in schema["oneOf"]:
        if "$ref" in one_of:
            ref = one_of["$ref"]
            ref_name = ref[ref.rfind("/") + 1 :]
            f.write(
                "from ."
                + camel_to_snake(ref_name)
                + " import "
                + snake_to_title(ref_name)
                + "\n"
            )
            all_options.append(snake_to_title(ref_name))

    if isNestedObjectOneOf(schema):
        # We want to write each of the nested objects.
        for one_of in schema["oneOf"]:
            # Get the nested object.
            if "properties" in one_of:
                for prop_name in one_of["properties"]:
                    nested_object = one_of["properties"][prop_name]
                    if nested_object == {}:
                        f.write("from typing import Any\n")
                        f.write(prop_name + " = Any\n")
                        f.write("\n")
                        all_options.append(prop_name)
                    elif "$ref" in nested_object:
                        ref = nested_object["$ref"]
                        ref_name = ref[ref.rfind("/") + 1 :]
                        f.write(
                            "from ."
                            + camel_to_snake(ref_name)
                            + " import "
                            + ref_name
                            + "\n"
                        )
                        f.write("\n")
                        if prop_name != ref_name:
                            f.write(prop_name + " = " + ref_name + "\n")
                            f.write("\n")
                        all_options.append(prop_name)
                    else:
                        object_code = generateObjectTypeCode(
                            prop_name, nested_object, "object", data, None, None
                        )
                        f.write(object_code)
                        f.write("\n")
                        all_options.append(prop_name)
            elif "type" in one_of and one_of["type"] == "string":
                enum_code = generateEnumTypeCode(
                    one_of["enum"][0], one_of, "string", []
                )
                f.write(enum_code)
                f.write("\n")
                all_options.append(one_of["enum"][0])

    # Check if each one_of has the same enum of one.
    tag = getTagOneOf(schema)
    content = getContentOneOf(schema, tag)

    if tag is not None and content is not None:
        # Generate each of the options from the tag.
        for one_of in schema["oneOf"]:
            # Get the value of the tag.
            object_name = one_of["properties"][tag]["enum"][0]
            # Generate the type for the object.
            content_code = generateObjectTypeCode(
                snake_to_title(object_name) + "Data",
                one_of["properties"][content],
                "object",
                data,
                None,
                None,
            )
            f.write(content_code)
            f.write("\n")
            object_code = generateObjectTypeCode(
                object_name, one_of, "object", data, tag, content
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(object_name)
    elif tag is not None:
        # Generate each of the options from the tag.
        for one_of in schema["oneOf"]:
            # Get the value of the tag.
            object_name = one_of["properties"][tag]["enum"][0]
            object_code = generateObjectTypeCode(
                object_name,
                one_of,
                "object",
                data,
                tag,
                None,
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(object_name)
    else:
        # Generate each of the options from the tag.
        i = 0
        for one_of in schema["oneOf"]:
            # Get the value of the tag.
            object_name = name + str(i)
            object_code = generateObjectTypeCode(
                object_name,
                one_of,
                "object",
                data,
                None,
                None,
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(object_name)
            i += 1

    # Write the sum type.
    description = getOneOfDescription(schema)
    content = generateUnionType(all_options, name, description, tag)
    f.write(content)

    # Close the file.
    f.close()


def getOneOfDescription(schema: dict) -> str:
    if "description" in schema:
        return schema["description"]
    else:
        return ""


def generateObjectTypeCode(
    name: str,
    schema: dict,
    type_name: str,
    data: dict,
    tag: Optional[str],
    content: Optional[str],
) -> str:
    FieldType = TypedDict(
        "FieldType",
        {
            "name": str,
            "type": str,
            "value": str,
        },
    )
    TemplateType = TypedDict(
        "TemplateType",
        {
            "fields": List[FieldType],
            "description": str,
            "name": str,
            "imports": List[str],
        },
    )

    description = ""
    if "description" in schema:
        description = schema["description"].replace('"', '\\"')

    imports = []
    refs = getRefs(schema)
    for ref in refs:
        imports.append("from ..models." + camel_to_snake(ref) + " import " + ref + "\n")

    required = []
    if "required" in schema:
        required = schema["required"]

    fields = []
    if "properties" in schema:
        for property_name in schema["properties"]:
            property_schema = schema["properties"][property_name]
            if property_name == tag:
                field0: FieldType = {
                    "name": property_name,
                    "type": "str",
                    "value": '"' + name + '"',
                }
                fields.append(field0)
            elif property_name == content:
                field1: FieldType = {
                    "name": property_name,
                    "type": snake_to_title(name) + "Data",
                    "value": "",
                }
                fields.append(field1)
            else:
                field_type = getTypeName(property_schema)
                if property_name not in required:
                    field_type = "Optional[" + field_type + "] = None"
                field2: FieldType = {
                    "name": property_name,
                    "type": field_type,
                    "value": "",
                }
                fields.append(field2)

    template_info: TemplateType = {
        "fields": fields,
        "description": description,
        "name": name,
        "imports": imports,
    }

    # Iterate over the properties.

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("generate/"))
    template_file = "object.py.jinja2"
    template = environment.get_template(template_file)
    content = template.render(**template_info)

    return content


def generateObjectType(path: str, name: str, schema: dict, type_name: str, data: dict):
    logging.info("generating type: ", name, " at: ", path)

    f = open(path, "w")

    code = generateObjectTypeCode(name, schema, type_name, data, None, None)
    f.write(code)

    # Close the file.
    f.close()


def getRefs(schema: dict) -> List[str]:
    refs = []
    if "$ref" in schema:
        refs.append(schema["$ref"].replace("#/components/schemas/", ""))

    else:
        # Generate the type.
        if "type" not in schema:
            if "allOf" in schema:
                for sub_schema in schema["allOf"]:
                    refs.extend(getRefs(sub_schema))
        else:
            type_name = schema["type"]
            if type_name == "object":
                if "properties" in schema:
                    # Iternate over the properties.
                    for property_name in schema["properties"]:
                        property_schema = schema["properties"][property_name]
                        schema_refs = getRefs(property_schema)
                        for ref in schema_refs:
                            if ref not in refs:
                                refs.append(ref)
                elif "additionalProperties" in schema:
                    schema_refs = getRefs(schema["additionalProperties"])
                    for ref in schema_refs:
                        if ref not in refs:
                            refs.append(ref)
                elif schema == {"type": "object"}:
                    # do nothing
                    pass
                else:
                    # This is likely an empty object like above but with a description
                    # so we will just skip it.
                    pass
            elif type_name == "array":
                if "items" in schema:
                    schema_refs = getRefs(schema["items"])
                    for ref in schema_refs:
                        if ref not in refs:
                            refs.append(ref)

    return refs


def getEndpointRefs(endpoint: dict, data: dict) -> List[str]:
    refs = []

    responses = endpoint["responses"]
    for response_code in responses:
        response = responses[response_code]
        if "content" in response:
            content = response["content"]
            for content_type in content:
                if content_type == "application/json":
                    json = content[content_type]["schema"]
                    if "$ref" in json:
                        # If the reference is to a oneOf type, we want to return
                        # all the possible outcomes.
                        ref = json["$ref"].replace("#/components/schemas/", "")
                        schema = data["components"]["schemas"][ref]
                        if isNestedObjectOneOf(schema) or isEnumWithDocsOneOf(schema):
                            if snake_to_title(ref) not in refs:
                                refs.append(snake_to_title(ref))
                        elif isTypedObjectOneOf(schema):
                            for t in schema["oneOf"]:
                                ref = getOneOfRefType(t)
                                if snake_to_title(ref) not in refs:
                                    refs.append(snake_to_title(ref))
                        else:
                            if ref not in refs:
                                refs.append(ref)
                    elif "type" in json:
                        if json["type"] == "array":
                            items = json["items"]
                            if "$ref" in items:
                                ref = items["$ref"].replace("#/components/schemas/", "")
                                refs.append("List[" + ref + "]")
                            elif "type" in items:
                                if items["type"] == "string":
                                    refs.append("List[str]")
                                else:
                                    raise Exception("Unknown array type", items)
                            else:
                                raise Exception("Unknown array type", items)
                        elif json["type"] == "string":
                            refs.append("str")
                        elif (
                            json["type"] == "object" and "additionalProperties" in json
                        ):
                            refs.append("dict")
                        else:
                            print(json)
                            raise Exception("Unknown type ", json["type"])
                    else:
                        refs.append("dict")
                elif content_type == "*/*":
                    s = content[content_type]["schema"]
                    if s == {}:
                        # We don't care it's an empty body.
                        continue
                    else:
                        # Throw an error for an unsupported content type.
                        logging.error("content: ", content)
                        raise Exception("Unsupported content type: ", content_type)
                else:
                    # Throw an error for an unsupported content type.
                    logging.error("content: ", content)
                    raise Exception("Unsupported content type: ", content_type)
        elif "$ref" in response:
            schema_name = response["$ref"].replace("#/components/responses/", "")
            schema = data["components"]["responses"][schema_name]
            if "content" in schema:
                content = schema["content"]
                for content_type in content:
                    if content_type == "application/json":
                        json = content[content_type]["schema"]
                        if "$ref" in json:
                            ref = json["$ref"].replace("#/components/schemas/", "")
                            if snake_to_title(ref) not in refs:
                                refs.append(snake_to_title(ref))

    return refs


def getParameterRefs(endpoint: dict) -> List[str]:
    refs = []

    if "parameters" in endpoint:
        parameters = endpoint["parameters"]
        for parameter in parameters:
            parameter["name"]
            if "$ref" in parameter["schema"]:
                parameter_type = parameter["schema"]["$ref"].replace(
                    "#/components/schemas/", ""
                )
                refs.append(parameter_type)

    return refs


def getRequestBodyRefs(endpoint: dict) -> List[str]:
    refs = []

    if "requestBody" in endpoint:
        requestBody = endpoint["requestBody"]
        if "content" in requestBody:
            content = requestBody["content"]
            for content_type in content:
                if content_type == "application/json":
                    json = content[content_type]["schema"]
                    if "$ref" in json:
                        ref = json["$ref"].replace("#/components/schemas/", "")
                        refs.append(ref)
                elif content_type == "application/octet-stream":
                    # do nothing we dont't care
                    continue
                elif content_type == "application/x-www-form-urlencoded":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = form["$ref"].replace("#/components/schemas/", "")
                        refs.append(ref)
                elif content_type == "multipart/form-data":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = form["$ref"].replace("#/components/schemas/", "")
                        refs.append(ref)
                else:
                    # Throw an error for an unsupported content type.
                    logging.error("content: ", content)
                    raise Exception("Unsupported content type: ", content_type)

    return refs


def getRequestBodyTypeSchema(
    endpoint: dict, data: dict
) -> Tuple[Optional[str], Optional[dict]]:
    if "requestBody" in endpoint:
        requestBody = endpoint["requestBody"]
        if "content" in requestBody:
            content = requestBody["content"]
            for content_type in content:
                if content_type == "application/json":
                    json = content[content_type]["schema"]
                    if "$ref" in json:
                        ref = json["$ref"].replace("#/components/schemas/", "")
                        type_schema = data["components"]["schemas"][ref]
                        return ref, type_schema
                    elif json != {}:
                        logging.error("not a ref: ", json)
                        raise Exception("not a ref")
                elif content_type == "text/plain":
                    return "str", None
                elif content_type == "application/octet-stream":
                    return "bytes", None
                elif content_type == "application/x-www-form-urlencoded":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = form["$ref"].replace("#/components/schemas/", "")
                        type_schema = data["components"]["schemas"][ref]
                        return ref, type_schema
                    elif form != {}:
                        logging.error("not a ref: ", form)
                        raise Exception("not a ref")
                elif content_type == "multipart/form-data":
                    form = content[content_type]["schema"]
                    if "$ref" in form:
                        ref = form["$ref"].replace("#/components/schemas/", "")
                        type_schema = data["components"]["schemas"][ref]
                        return ref, type_schema
                    elif form != {}:
                        type_schema = form
                        return None, type_schema
                else:
                    logging.error("unsupported content type: ", content_type)
                    raise Exception("unsupported content type")

    return None, None


def to_camel_case(s: str):
    s = re.sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return "".join([s[0].lower(), s[1:]])


def clean_parameter_name(name: str):
    return camel_to_snake(name).replace("from", "from_")


def camel_to_snake(name: str):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower().replace("-", "_")


def camel_to_screaming_snake(name: str):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return (
        re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
        .replace(" ", "")
        .upper()
        .replace("-", "_")
        .replace(":", "_")
    )


# Change `file_conversion` to `FileConversion`
def snake_to_title(name: str):
    return name.title().replace("_", "").replace("3D", "3d")


def get_function_parameters(
    endpoint: dict, request_body_type: Optional[str]
) -> List[str]:
    params = []
    if "parameters" in endpoint:
        parameters = endpoint["parameters"]
        for parameter in parameters:
            parameter_name = parameter["name"]
            if "type" in parameter["schema"]:
                (
                    parameter["schema"]["type"]
                    .replace("string", "str")
                    .replace("integer", "int")
                    .replace("number", "float")
                )
            elif "$ref" in parameter["schema"]:
                parameter["schema"]["$ref"].replace("#/components/schemas/", "")
            else:
                logging.error("parameter: ", parameter)
                raise Exception("Unknown parameter type")
            params.append(camel_to_snake(parameter_name))
    if request_body_type:
        params.append("body")
    return params


def getOneOfRefType(schema: dict) -> str:
    if (
        "type" in schema["properties"]
        and "enum" in schema["properties"]["type"]
        and len(schema["properties"]["type"]["enum"]) == 1
    ):
        t = schema["properties"]["type"]["enum"][0]
        return t

    raise Exception("Cannot get oneOf ref type for schema: ", schema)


def isNestedObjectAnyOf(schema: dict) -> bool:
    if "anyOf" not in schema:
        return False

    is_nested_object = False
    for any_of in schema["anyOf"]:
        # Check if each are an object w 1 property in it.
        if (
            "type" in any_of
            and any_of["type"] == "object"
            and "properties" in any_of
            and len(any_of["properties"]) == 1
        ):
            for prop_name in any_of["properties"]:
                nested_object = any_of["properties"][prop_name]
                if "type" in nested_object and nested_object["type"] == "object":
                    is_nested_object = True
                else:
                    is_nested_object = False
                    break
        elif (
            "type" in any_of
            and any_of["type"] == "string"
            and "enum" in any_of
            and len(any_of["enum"]) == 1
        ):
            is_nested_object = True
        else:
            is_nested_object = False
            break

    return is_nested_object


def isNestedObjectOneOf(schema: dict) -> bool:
    if "oneOf" not in schema:
        return False

    is_nested_object = False
    for one_of in schema["oneOf"]:
        # Check if each are an object w 1 property in it.
        if (
            "type" in one_of
            and one_of["type"] == "object"
            and "properties" in one_of
            and len(one_of["properties"]) == 1
        ):
            for prop_name in one_of["properties"]:
                nested_object = one_of["properties"][prop_name]
                if "type" in nested_object and nested_object["type"] == "object":
                    is_nested_object = True
                else:
                    is_nested_object = False
                    break
        elif (
            "type" in one_of
            and one_of["type"] == "string"
            and "enum" in one_of
            and len(one_of["enum"]) == 1
        ):
            is_nested_object = True
        else:
            is_nested_object = False
            break

    return is_nested_object


def getTagAnyOf(schema: dict) -> Optional[str]:
    tag = None
    for any_of in schema["anyOf"]:
        has_tag = False
        # Check if each are an object w 1 property in it.
        if "type" in any_of and any_of["type"] == "object" and "properties" in any_of:
            for prop_name in any_of["properties"]:
                prop = any_of["properties"][prop_name]
                if (
                    "type" in prop
                    and prop["type"] == "string"
                    and "enum" in prop
                    and len(prop["enum"]) == 1
                ):
                    if tag is not None and tag != prop_name:
                        has_tag = False
                        break
                    else:
                        has_tag = True
                        tag = prop_name

        if has_tag is False:
            tag = None
            break

    return tag


def getTagOneOf(schema: dict) -> Optional[str]:
    tag = None
    for one_of in schema["oneOf"]:
        has_tag = False
        # Check if each are an object w 1 property in it.
        if one_of["type"] == "object" and "properties" in one_of:
            for prop_name in one_of["properties"]:
                prop = one_of["properties"][prop_name]
                if (
                    "type" in prop
                    and prop["type"] == "string"
                    and "enum" in prop
                    and len(prop["enum"]) == 1
                ):
                    if tag is not None and tag != prop_name:
                        has_tag = False
                        break
                    else:
                        has_tag = True
                        tag = prop_name

        if has_tag is False:
            tag = None
            break

    return tag


def getContentOneOf(schema: dict, tag: Optional[str]) -> Optional[str]:
    if tag is None:
        return None
    content = None
    for one_of in schema["oneOf"]:
        has_content = False
        # Check if each are an object w 1 property in it.
        if one_of["type"] == "object" and "properties" in one_of:
            if len(one_of["properties"]) != 2:
                return None

            for prop_name in one_of["properties"]:
                if prop_name == tag:
                    continue
                if content is not None and content != prop_name:
                    has_content = False
                    break
                else:
                    has_content = True
                    content = prop_name

        if has_content is False:
            content = None
            break

    return content


def isEnumWithDocsOneOf(schema: dict) -> bool:
    if "oneOf" not in schema:
        return False

    is_enum_with_docs = False
    for one_of in schema["oneOf"]:
        if one_of["type"] == "string" and "enum" in one_of and len(one_of["enum"]) == 1:
            is_enum_with_docs = True
        else:
            is_enum_with_docs = False
            break

    return is_enum_with_docs


def isTypedObjectOneOf(schema: dict) -> bool:
    if "oneOf" not in schema:
        return False

    is_typed_object = False
    for one_of in schema["oneOf"]:
        if (
            "type" in one_of["properties"]
            and "enum" in one_of["properties"]["type"]
            and len(one_of["properties"]["type"]["enum"]) == 1
        ):
            is_typed_object = True
        else:
            is_typed_object = False
            break

    return is_typed_object


def hasNoContentResponse(endpoint: dict) -> bool:
    responses = endpoint["responses"]
    for response_code in responses:
        if (
            response_code == "default"
            or response_code == "204"
            or response_code == "302"
        ):
            return True

    return False


def getFunctionResultType(endpoint: dict, endpoint_refs: List[str]) -> str:
    result = ", ".join(endpoint_refs)
    if len(endpoint_refs) > 1:
        result = "Optional[Union[" + result + "]]"

    if hasNoContentResponse(endpoint):
        result = "Optional[" + result + "]"

    return result


def getDetailedFunctionResultType(endpoint: dict, endpoint_refs: List[str]) -> str:
    return "Response[" + getFunctionResultType(endpoint, endpoint_refs) + "]"


def getTypeName(schema: dict) -> str:
    if "type" in schema:
        if schema["type"] == "string":
            if "format" in schema:
                if (
                    schema["format"] == "date-time"
                    or schema["format"] == "partial-date-time"
                ):
                    return "datetime.datetime"
                elif schema["format"] == "byte":
                    return "Base64Data"
                elif schema["format"] == "uuid":
                    return "str"
                elif schema["format"] == "url":
                    return "AnyUrl"
                elif schema["format"] == "phone":
                    return "str"
            return "str"
        elif schema["type"] == "number":
            return "float"
        elif schema["type"] == "boolean":
            return "bool"
        elif schema["type"] == "integer":
            return "int"
        elif schema["type"] == "array":
            if "items" in schema:
                item_type = getTypeName(schema["items"])
                if "format" in schema["items"] and schema["items"]["format"] == "uint8":
                    return "bytes"
                else:
                    return "List[" + item_type + "]"
        elif "additionalProperties" in schema and schema["type"] == "object":
            item_type = getTypeName(schema["additionalProperties"])
            return "Dict[str, " + item_type + "]"
    elif "$ref" in schema:
        return schema["$ref"].replace("#/components/schemas/", "")
    elif "allOf" in schema and len(schema["allOf"]) == 1:
        return getTypeName(schema["allOf"][0])
    elif "description" in schema:
        return "Any"

    logging.error("schema: ", [schema])
    raise Exception("Unknown schema type")


letters: List[str] = []


# generate a random letter combination in the range A - Z
# do not use O or I.
# make sure we do not use a letter we have already used.
def randletter() -> str:
    letter1 = chr(random.randint(ord("A"), ord("Z")))
    letter2 = chr(random.randint(ord("A"), ord("Z")))
    letter = letter1 + letter2
    while letter in letters:
        return randletter()
    letters.append(letter)
    return letter


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
