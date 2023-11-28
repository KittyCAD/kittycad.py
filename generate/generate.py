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
            and (schema["format"] == "float" or schema["format"] == "double")
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

    if request_body_type and "x-dropshot-websocket" not in endpoint:
        if request_body_type == "str":
            params_str += "body='<string>',\n"
        elif request_body_type == "bytes":
            params_str += "body=bytes('some bytes', 'utf-8'),\n"
        elif request_body_schema:
            # Generate an example for the schema.
            rbs: Dict[Any, Any] = request_body_schema
            (
                body_type,
                body_example,
                more_example_imports,
            ) = generateTypeAndExamplePython(request_body_type, rbs, data, None, None)
            params_str += "body=" + body_example + ",\n"
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
    if isinstance(result, Error) or result == None:
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
        short_sync_example = (
            """def test_"""
            + fn_name
            + """():
        # Create our client.
        client = ClientFromEnv()

        # Connect to the websocket.
        websocket = """
            + fn_name
            + """.sync(client=client,"""
            + params_str
            + """)

        # Send a message.
        websocket.send("{}")

        # Get the messages.
        for message in websocket:
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
                                            + ".from_dict(data)\n"
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
                                        + ".from_dict(response.json())\n"
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
                                            "\t\t\t" + ref + ".from_dict(item)\n"
                                        )
                                        parse_response.write(
                                            "\t\t\tfor item in response.json()\n"
                                        )
                                        parse_response.write("\t\t]\n")
                                    else:
                                        raise Exception("Unknown array type")
                                elif json["type"] == "string":
                                    parse_response.write(
                                        "\t\tresponse_"
                                        + response_code
                                        + " = response.text\n"
                                    )
                                else:
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
                                        + ".from_dict(response.json())\n"
                                    )
                else:
                    print(endpoint)
                    raise Exception("response not supported")

                if not is_one_of:
                    parse_response.write("\t\treturn response_" + response_code + "\n")

        # End the method.
        parse_response.write("\treturn Error.from_dict(response.json())\n")
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

    # Add the Base64Data type.
    f.write("from .base64data import Base64Data\n")

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
            generateIntegerType(file_path, name, schema, type_name)
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

    f.write("class " + name + "(str):\n")
    f.write("\n")
    f.write("\tdef __str__(self) -> str:\n")
    f.write("\t\treturn self\n")

    # Close the file.
    f.close()


def generateIntegerType(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: ", name, " at: ", path)
    f = open(path, "w")

    f.write("class " + name + "(int):\n")
    f.write("\n")
    f.write("\tdef __int__(self) -> int:\n")
    f.write("\t\treturn self\n")

    # Close the file.
    f.close()


def generateFloatType(path: str, name: str, schema: dict, type_name: str):
    logging.info("generating type: ", name, " at: ", path)
    f = open(path, "w")

    f.write("class " + name + "(float):\n")
    f.write("\n")
    f.write("\tdef __float__(self) -> float:\n")
    f.write("\t\treturn self\n")

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

    if isNestedObjectOneOf(schema):
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
                            prop_name, nested_object, "object", data, None
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
                object_name, any_of, "object", data, tag
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(object_name)

    # Write the sum type.
    description = getAnyOfDescription(schema)
    content = generateUnionType(all_options, name, description)
    f.write(content)

    # Close the file.
    f.close()


def getAnyOfDescription(schema: dict) -> str:
    if "description" in schema:
        return schema["description"]
    else:
        return ""


def generateUnionType(types: List[str], name: str, description: str) -> str:
    ArgType = TypedDict(
        "ArgType",
        {
            "name": str,
        },
    )
    TemplateType = TypedDict(
        "TemplateType",
        {
            "types": List[ArgType],
            "description": str,
            "name": str,
        },
    )
    template_info: TemplateType = {
        "types": [],
        "description": description,
        "name": name,
    }
    for type in types:
        template_info["types"].append({"name": type})

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
                            prop_name, nested_object, "object", data, None
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

    if tag is not None:
        # Generate each of the options from the tag.
        for one_of in schema["oneOf"]:
            # Get the value of the tag.
            object_name = one_of["properties"][tag]["enum"][0]
            object_code = generateObjectTypeCode(
                object_name, one_of, "object", data, tag
            )
            f.write(object_code)
            f.write("\n")
            all_options.append(object_name)

    # Write the sum type.
    if name == "SnakeCaseResult":
        f.write("from typing import Any\n")
        f.write(name + " = Any")
    else:
        description = getOneOfDescription(schema)
        content = generateUnionType(all_options, name, description)
        f.write(content)

    # Close the file.
    f.close()


def getOneOfDescription(schema: dict) -> str:
    if "description" in schema:
        return schema["description"]
    else:
        return ""


def generateObjectTypeCode(
    name: str, schema: dict, type_name: str, data: dict, tag: Optional[str]
) -> str:
    f = io.StringIO()

    has_date_time = hasDateTime(schema)
    has_base_64 = hasBase64(schema)
    if has_date_time:
        f.write("import datetime\n")
    if has_base_64:
        f.write("from ..models.base64data import Base64Data\n")
    f.write(
        "from typing import Any, Dict, List, Type, TypeVar, Union, cast, deprecated\n"
    )
    f.write("\n")
    f.write("import attr\n")
    if has_date_time:
        f.write("from dateutil.parser import isoparse\n")
    f.write("\n")

    refs = getRefs(schema)
    for ref in refs:
        f.write("from ..models." + camel_to_snake(ref) + " import " + ref + "\n")

    f.write("from ..types import UNSET, Unset\n")
    f.write("\n")

    type_letter = randletter()
    f.write(type_letter + ' = TypeVar("' + type_letter + '", bound="' + name + '")\n')
    f.write("\n")
    f.write("@attr.s(auto_attribs=True)\n")
    f.write("class " + name + ":\n")
    # Write the description.
    if "description" in schema:
        f.write('\t""" ' + schema["description"] + ' """ # noqa: E501\n')
    # Iterate over the properties.
    for property_name in schema["properties"]:
        property_schema = schema["properties"][property_name]
        if property_name == tag:
            f.write("\t" + property_name + ': str = "' + name + '"\n')
        else:
            renderTypeInit(f, property_name, property_schema, data)

    # Finish writing the class.
    f.write("\n")
    f.write(
        "\tadditional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)\n"
    )

    # Now let's write the to_dict method.
    f.write("\n")
    f.write("\tdef to_dict(self) -> Dict[str, Any]:\n")
    # Iternate over the properties.
    for property_name in schema["properties"]:
        property_schema = schema["properties"][property_name]
        if property_name == tag:
            renderTypeToDict(f, property_name, property_schema, data)
        else:
            renderTypeToDict(f, property_name, property_schema, data)

    # Finish writing the to_dict method.
    f.write("\n")
    f.write("\t\tfield_dict: Dict[str, Any] = {}\n")
    f.write("\t\tfield_dict.update(self.additional_properties)\n")
    f.write("\t\tfield_dict.update({})\n")

    # Iternate over the properties.
    for property_name in schema["properties"]:
        property_schema = schema["properties"][property_name]
        if "allOf" in property_schema and len(property_schema["allOf"]) == 1:
            property_schema = property_schema["allOf"][0]
        if property_name == tag:
            f.write(
                "\t\tfield_dict['"
                + property_name
                + "'] = "
                + clean_parameter_name(property_name)
                + "\n"
            )
        else:
            # Write the property.
            f.write(
                "\t\tif " + clean_parameter_name(property_name) + " is not UNSET:\n"
            )
            # We only want .to_dict on nested objects.
            if "$ref" in property_schema:
                actual_schema = data["components"]["schemas"][
                    property_schema["$ref"].replace("#/components/schemas/", "")
                ]
                is_enum = isEnumWithDocsOneOf(actual_schema)
                if (
                    "properties" in actual_schema
                    or "oneOf" in actual_schema
                    or "anyOf" in actual_schema
                    or "allOf" in actual_schema
                ) and not is_enum:
                    f.write(
                        "\t\t\tfield_dict['"
                        + property_name
                        + "'] = "
                        + clean_parameter_name(property_name)
                        + ".to_dict()\n"
                    )
                else:
                    f.write(
                        "\t\t\tfield_dict['"
                        + property_name
                        + "'] = "
                        + clean_parameter_name(property_name)
                        + "\n"
                    )
            else:
                f.write(
                    "\t\t\tfield_dict['"
                    + property_name
                    + "'] = "
                    + clean_parameter_name(property_name)
                    + "\n"
                )

    f.write("\n")
    f.write("\t\treturn field_dict\n")

    # Now let's write the from_dict method.
    f.write("\n")
    f.write("\t@classmethod\n")
    f.write(
        "\tdef from_dict(cls: Type["
        + type_letter
        + "], src_dict: Dict[str, Any]) -> "
        + type_letter
        + ":\n"
    )
    f.write("\t\td = src_dict.copy()\n")

    # Iternate over the properties.
    for property_name in schema["properties"]:
        property_schema = schema["properties"][property_name]
        renderTypeFromDict(f, property_name, property_schema, data)

    # Finish writing the from_dict method.
    f.write("\n")
    f.write("\t\t" + camel_to_snake(name) + " = cls(\n")
    # Iternate over the properties.
    for property_name in schema["properties"]:
        # Write the property.
        f.write(
            "\t\t\t"
            + clean_parameter_name(property_name)
            + "= "
            + clean_parameter_name(property_name)
            + ",\n"
        )

    # Close the class.
    f.write("\t\t)\n")
    f.write("\n")
    f.write("\t\t" + camel_to_snake(name) + ".additional_properties = d\n")
    f.write("\t\treturn " + camel_to_snake(name) + "\n")

    # write the rest of the class.
    f.write("\n")
    f.write("\t@property\n")
    f.write("\tdef additional_keys(self) -> List[str]:\n")
    f.write("\t\treturn list(self.additional_properties.keys())\n")

    f.write("\n")
    f.write("\tdef __getitem__(self, key: str) -> Any:\n")
    f.write("\t\treturn self.additional_properties[key]\n")

    f.write("\n")
    f.write("\tdef __setitem__(self, key: str, value: Any) -> None:\n")
    f.write("\t\tself.additional_properties[key] = value\n")

    f.write("\n")
    f.write("\tdef __delitem__(self, key: str) -> None:\n")
    f.write("\t\tdel self.additional_properties[key]\n")

    f.write("\n")
    f.write("\tdef __contains__(self, key: str) -> bool:\n")
    f.write("\t\treturn key in self.additional_properties\n")

    value = f.getvalue()

    # Close the file.
    f.close()

    return value


def generateObjectType(path: str, name: str, schema: dict, type_name: str, data: dict):
    logging.info("generating type: ", name, " at: ", path)

    f = open(path, "w")

    code = generateObjectTypeCode(name, schema, type_name, data, None)
    f.write(code)

    # Close the file.
    f.close()


def renderTypeToDict(f, property_name: str, property_schema: dict, data: dict):
    if "type" in property_schema:
        property_type = property_schema["type"]

        # Write the property.
        if property_type == "string":
            if "format" in property_schema:
                if (
                    property_schema["format"] == "date-time"
                    or property_schema["format"] == "partial-date-time"
                ):
                    f.write("\t\t" + property_name + ": Union[Unset, str] = UNSET\n")
                    f.write(
                        "\t\tif not isinstance(self."
                        + clean_parameter_name(property_name)
                        + ", Unset):\n"
                    )
                    f.write(
                        "\t\t\t"
                        + clean_parameter_name(property_name)
                        + " = self."
                        + clean_parameter_name(property_name)
                        + ".isoformat()\n"
                    )
                    # return early
                    return
                elif property_schema["format"] == "byte":
                    f.write("\t\t" + property_name + ": Union[Unset, str] = UNSET\n")
                    f.write(
                        "\t\tif not isinstance(self."
                        + clean_parameter_name(property_name)
                        + ", Unset):\n"
                    )
                    f.write(
                        "\t\t\t"
                        + clean_parameter_name(property_name)
                        + " = self."
                        + clean_parameter_name(property_name)
                        + ".get_encoded()\n"
                    )
                    # return early
                    return

            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + " = self."
                + clean_parameter_name(property_name)
                + "\n"
            )
        elif property_type == "integer":
            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + " = self."
                + clean_parameter_name(property_name)
                + "\n"
            )
        elif property_type == "number":
            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + " = self."
                + clean_parameter_name(property_name)
                + "\n"
            )
        elif property_type == "boolean":
            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + " = self."
                + clean_parameter_name(property_name)
                + "\n"
            )
        elif "additionalProperties" in property_schema and property_type == "object":
            if "$ref" in property_schema["additionalProperties"]:
                ref = property_schema["additionalProperties"]["$ref"].replace(
                    "#/components/schemas/", ""
                )
                f.write(
                    "\t\t" + property_name + ": Union[Unset, Dict[str, Any]] = UNSET\n"
                )
                f.write(
                    "\t\tif not isinstance(self."
                    + clean_parameter_name(property_name)
                    + ", Unset):\n"
                )
                f.write("\t\t\tnew_dict: Dict[str, Any] = {}\n")
                f.write(
                    "\t\t\tfor key, value in self."
                    + clean_parameter_name(property_name)
                    + ".items():\n"
                )
                f.write("\t\t\t\tnew_dict[key] = value.to_dict()\n")
                f.write(
                    "\t\t\t" + clean_parameter_name(property_name) + " = new_dict\n"
                )
            elif (
                "type" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["type"] == "integer"
            ):
                f.write(
                    "\t\t"
                    + clean_parameter_name(property_name)
                    + " = self."
                    + clean_parameter_name(property_name)
                    + "\n"
                )
                f.write("\n")
            elif (
                "format" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["format"] == "byte"
            ):
                f.write(
                    "\t\t" + property_name + ": Union[Unset, Dict[str, str]] = UNSET\n"
                )
                f.write(
                    "\t\tif not isinstance(self."
                    + clean_parameter_name(property_name)
                    + ", Unset):\n"
                )
                f.write("\t\t\tnew_dict: Dict[str, str] = {}\n")
                f.write(
                    "\t\t\tfor key, value in self."
                    + clean_parameter_name(property_name)
                    + ".items():\n"
                )
                f.write("\t\t\t\tnew_dict[key] = value.get_encoded()\n")
                f.write(
                    "\t\t\t" + clean_parameter_name(property_name) + " = new_dict\n"
                )
            elif (
                "type" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["type"] == "string"
            ):
                f.write(
                    "\t\t"
                    + clean_parameter_name(property_name)
                    + " = self."
                    + clean_parameter_name(property_name)
                    + "\n"
                )
                f.write("\n")
            else:
                # Throw an error.
                print("property: ", property_schema)
                raise Exception("Unknown property type")
        elif property_type == "array":
            if "items" in property_schema:
                if "$ref" in property_schema["items"]:
                    property_type = property_schema["items"]["$ref"]
                    property_type = property_type.replace("#/components/schemas/", "")
                    f.write(
                        "\t\tfrom ..models."
                        + camel_to_snake(property_type)
                        + " import "
                        + property_type
                        + "\n"
                    )
                elif "type" in property_schema["items"]:
                    if property_schema["items"]["type"] == "string":
                        property_type = "str"
                    elif property_schema["items"]["type"] == "integer":
                        property_type = "int"
                    elif property_schema["items"]["type"] == "number":
                        property_type = "float"
                    elif property_schema["items"]["type"] == "array":
                        if "items" in property_schema["items"]:
                            if property_schema["items"]["items"]["type"] == "string":
                                property_type = "List[str]"
                            elif property_schema["items"]["items"]["type"] == "number":
                                property_type = "List[float]"
                            else:
                                logging.error("property: ", property_schema)
                                raise Exception("Unknown property type")
                        else:
                            logging.error("property: ", property_schema)
                            raise Exception("Unknown property type")
                    else:
                        print("property: ", property_schema)
                        raise Exception("Unknown property type")
                else:
                    logging.error("array: ", [property_schema])
                    logging.error("array: ", [property_schema["items"]])
                    raise Exception("Unknown array type")

            f.write(
                "\t\t"
                + property_name
                + ": Union[Unset, List["
                + property_type
                + "]] = UNSET\n"
            )
            f.write(
                "\t\tif not isinstance(self."
                + clean_parameter_name(property_name)
                + ", Unset):\n"
            )
            f.write(
                "\t\t\t"
                + clean_parameter_name(property_name)
                + " = self."
                + clean_parameter_name(property_name)
                + "\n"
            )
        else:
            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + " = self."
                + clean_parameter_name(property_name)
                + "\n"
            )
    elif "$ref" in property_schema:
        ref = property_schema["$ref"].replace("#/components/schemas/", "")
        f.write(
            "\t\tif not isinstance(self."
            + clean_parameter_name(property_name)
            + ", Unset):\n"
        )
        f.write(
            "\t\t\t"
            + clean_parameter_name(property_name)
            + " = self."
            + clean_parameter_name(property_name)
            + "\n"
        )
    elif "allOf" in property_schema:
        thing = property_schema["allOf"][0]
        if "$ref" in thing:
            ref = thing["$ref"].replace("#/components/schemas/", "")
            if ref == "Uuid":
                return renderTypeToDict(
                    f, property_name, data["components"]["schemas"][ref], data
                )
            f.write(
                "\t\tif not isinstance(self."
                + clean_parameter_name(property_name)
                + ", Unset):\n"
            )
            f.write(
                "\t\t\t"
                + clean_parameter_name(property_name)
                + " = self."
                + clean_parameter_name(property_name)
                + "\n"
            )
        else:
            raise Exception("unknown allOf type: ", property_schema)
    else:
        f.write(
            "\t\t"
            + clean_parameter_name(property_name)
            + " = self."
            + clean_parameter_name(property_name)
            + "\n"
        )


def renderTypeInit(f, property_name: str, property_schema: dict, data: dict):
    property_name = clean_parameter_name(property_name)
    # if "deprecated" in property_schema and property_schema["deprecated"]:
    # TODO some properties are deprecated, but we still need to support them
    # we should show some kind of warning here
    if "type" in property_schema:
        property_type = property_schema["type"]

        # Write the property.
        if property_type == "string":
            if "format" in property_schema:
                if (
                    property_schema["format"] == "date-time"
                    or property_schema["format"] == "partial-date-time"
                ):
                    f.write(
                        "\t"
                        + property_name
                        + ": Union[Unset, datetime.datetime] = UNSET\n"
                    )
                    # Return early.
                    return
                elif property_schema["format"] == "byte":
                    f.write(
                        "\t" + property_name + ": Union[Unset, Base64Data] = UNSET\n"
                    )
                    # Return early.
                    return

            f.write("\t" + property_name + ": Union[Unset, str] = UNSET\n")
        elif "additionalProperties" in property_schema and property_type == "object":
            if "$ref" in property_schema["additionalProperties"]:
                ref = property_schema["additionalProperties"]["$ref"].replace(
                    "#/components/schemas/", ""
                )
                # Make sure we import the model.
                f.write(
                    "\tfrom ..models." + camel_to_snake(ref) + " import " + ref + "\n"
                )
                f.write(
                    "\t"
                    + property_name
                    + ": Union[Unset, Dict[str, "
                    + ref
                    + "]] = UNSET\n"
                )
            elif (
                "type" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["type"] == "integer"
            ):
                f.write(
                    "\t" + property_name + ": Union[Unset, Dict[str, int]] = UNSET\n"
                )
            elif (
                "format" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["format"] == "byte"
            ):
                f.write(
                    "\t"
                    + property_name
                    + ": Union[Unset, Dict[str, Base64Data]] = UNSET\n"
                )
            elif (
                "type" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["type"] == "string"
            ):
                f.write(
                    "\t" + property_name + ": Union[Unset, Dict[str, str]] = UNSET\n"
                )
            else:
                # Throw an error.
                print("property: ", property_schema)
                raise Exception("Unknown property type")
        elif property_type == "object":
            # TODO: we need to get the name of the object
            f.write("\t" + property_name + ": Union[Unset, Any] = UNSET\n")
        elif property_type == "integer":
            f.write("\t" + property_name + ":  Union[Unset, int] = UNSET\n")
        elif property_type == "number":
            f.write("\t" + property_name + ":  Union[Unset, float] = UNSET\n")
        elif property_type == "boolean":
            f.write("\t" + property_name + ": Union[Unset, bool] = False\n")
        elif property_type == "array":
            if "items" in property_schema:
                if "$ref" in property_schema["items"]:
                    property_type = property_schema["items"]["$ref"]
                    property_type = property_type.replace("#/components/schemas/", "")
                    f.write(
                        "\tfrom ..models."
                        + camel_to_snake(property_type)
                        + " import "
                        + property_type
                        + "\n"
                    )
                elif "type" in property_schema["items"]:
                    if property_schema["items"]["type"] == "string":
                        property_type = "str"
                    elif property_schema["items"]["type"] == "number":
                        property_type = "float"
                    elif property_schema["items"]["type"] == "integer":
                        property_type = "int"
                    elif property_schema["items"]["type"] == "array":
                        if "items" in property_schema["items"]:
                            if property_schema["items"]["items"]["type"] == "string":
                                property_type = "List[str]"
                            elif property_schema["items"]["items"]["type"] == "number":
                                property_type = "List[float]"
                            else:
                                logging.error("property: ", property_schema)
                                raise Exception("Unknown property type")
                        else:
                            logging.error("property: ", property_schema)
                            raise Exception("Unknown property type")
                    else:
                        print("property: ", property_schema)
                        raise Exception("Unknown property type")
                else:
                    logging.error("array: ", [property_schema])
                    logging.error("array: ", [property_schema["items"]])
                    raise Exception("Unknown array type")

                f.write(
                    "\t"
                    + property_name
                    + ": Union[Unset, List["
                    + property_type
                    + "]] = UNSET\n"
                )
            else:
                raise Exception("Unknown array type")
        else:
            logging.error("property type: ", property_schema)
            raise Exception("unknown type: ", property_type)
    elif "$ref" in property_schema:
        ref = property_schema["$ref"].replace("#/components/schemas/", "")
        f.write("\t" + property_name + ": Union[Unset, " + ref + "] = UNSET\n")
    elif "allOf" in property_schema:
        thing = property_schema["allOf"][0]
        if "$ref" in thing:
            ref = thing["$ref"].replace("#/components/schemas/", "")
            if ref == "Uuid":
                return renderTypeInit(
                    f, property_name, data["components"]["schemas"][ref], data
                )
            f.write("\t" + property_name + ": Union[Unset, " + ref + "] = UNSET\n")
        else:
            raise Exception("unknown allOf type: ", property_schema)
    else:
        f.write("\t" + property_name + ": Union[Unset, Any] = UNSET\n")


def renderTypeFromDict(f, property_name: str, property_schema: dict, data: dict):
    if "type" in property_schema:
        property_type = property_schema["type"]

        # Write the property.
        if property_type == "string":
            if "format" in property_schema:
                if (
                    property_schema["format"] == "date-time"
                    or property_schema["format"] == "partial-date-time"
                ):
                    f.write(
                        "\t\t_"
                        + clean_parameter_name(property_name)
                        + ' = d.pop("'
                        + property_name
                        + '", UNSET)\n'
                    )
                    f.write(
                        "\t\t"
                        + clean_parameter_name(property_name)
                        + ": Union[Unset, datetime.datetime]\n"
                    )
                    f.write(
                        "\t\tif isinstance(_"
                        + clean_parameter_name(property_name)
                        + ", Unset):\n"
                    )
                    f.write(
                        "\t\t\t" + clean_parameter_name(property_name) + " = UNSET\n"
                    )
                    f.write("\t\telse:\n")
                    f.write(
                        "\t\t\t"
                        + clean_parameter_name(property_name)
                        + " = isoparse(_"
                        + clean_parameter_name(property_name)
                        + ")\n"
                    )
                    f.write("\n")
                    # Return early.
                    return
                elif property_schema["format"] == "byte":
                    f.write(
                        "\t\t_"
                        + clean_parameter_name(property_name)
                        + ' = d.pop("'
                        + property_name
                        + '", UNSET)\n'
                    )
                    f.write(
                        "\t\t"
                        + clean_parameter_name(property_name)
                        + ": Union[Unset, Base64Data]\n"
                    )
                    f.write(
                        "\t\tif isinstance(_"
                        + clean_parameter_name(property_name)
                        + ", Unset):\n"
                    )
                    f.write(
                        "\t\t\t" + clean_parameter_name(property_name) + " = UNSET\n"
                    )
                    f.write("\t\telse:\n")
                    f.write(
                        "\t\t\t"
                        + clean_parameter_name(property_name)
                        + " = Base64Data(bytes(_"
                        + clean_parameter_name(property_name)
                        + ", 'utf-8'))\n"
                    )
                    f.write("\n")
                    # Return early.
                    return

            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + ' = d.pop("'
                + property_name
                + '", UNSET)\n'
            )
            f.write("\n")
        elif property_type == "integer":
            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + ' = d.pop("'
                + property_name
                + '", UNSET)\n'
            )
            f.write("\n")
        elif property_type == "number":
            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + ' = d.pop("'
                + property_name
                + '", UNSET)\n'
            )
            f.write("\n")
        elif property_type == "boolean":
            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + ' = d.pop("'
                + property_name
                + '", UNSET)\n'
            )
            f.write("\n")
        elif "additionalProperties" in property_schema and property_type == "object":
            if "$ref" in property_schema["additionalProperties"]:
                ref = property_schema["additionalProperties"]["$ref"].replace(
                    "#/components/schemas/", ""
                )
                f.write(
                    "\t\t_"
                    + clean_parameter_name(property_name)
                    + ' = d.pop("'
                    + property_name
                    + '", UNSET)\n'
                )
                f.write(
                    "\t\tif isinstance(_"
                    + clean_parameter_name(property_name)
                    + ", Unset):\n"
                )
                f.write("\t\t\t" + clean_parameter_name(property_name) + " = UNSET\n")
                f.write("\t\telse:\n")
                f.write(
                    "\t\t\tnew_map: Dict[str, "
                    + ref
                    + "] = {}\n\t\t\tfor k, v in _"
                    + clean_parameter_name(property_name)
                    + ".items():\n\t\t\t\tnew_map[k] = "
                    + ref
                    + ".from_dict(v) # type: ignore\n\t\t\t"
                    + clean_parameter_name(property_name)
                    + " = new_map # type: ignore\n"
                )
                f.write("\n")
            elif (
                "type" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["type"] == "integer"
            ):
                f.write(
                    "\t\t"
                    + clean_parameter_name(property_name)
                    + ' = d.pop("'
                    + property_name
                    + '", UNSET)\n'
                )
                f.write("\n")
            elif (
                "format" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["format"] == "byte"
            ):
                f.write(
                    "\t\t_"
                    + clean_parameter_name(property_name)
                    + ' = d.pop("'
                    + property_name
                    + '", UNSET)\n'
                )
                f.write(
                    "\t\tif isinstance(_"
                    + clean_parameter_name(property_name)
                    + ", Unset):\n"
                )
                f.write("\t\t\t" + clean_parameter_name(property_name) + " = UNSET\n")
                f.write(
                    "\t\telse:\n\t\t\tnew_map: Dict[str, Base64Data] = {}\n\t\t\tfor k, v in _"
                    + clean_parameter_name(property_name)
                    + ".items():\n\t\t\t\tnew_map[k] = Base64Data(bytes(v, 'utf-8'))\n\t\t\t"
                    + clean_parameter_name(property_name)
                    + " = new_map # type: ignore\n"
                )
                f.write("\n")
            elif (
                "type" in property_schema["additionalProperties"]
                and property_schema["additionalProperties"]["type"] == "string"
            ):
                f.write(
                    "\t\t"
                    + clean_parameter_name(property_name)
                    + ' = d.pop("'
                    + property_name
                    + '", UNSET)\n'
                )
                f.write("\n")
            else:
                # Throw an error.
                print("property: ", property_schema)
                raise Exception("Unknown property type")
        elif property_type == "array":
            if "items" in property_schema:
                if "$ref" in property_schema["items"]:
                    property_type = property_schema["items"]["$ref"]
                    property_type = property_type.replace("#/components/schemas/", "")
                    f.write(
                        "\t\tfrom ..models."
                        + camel_to_snake(property_type)
                        + " import "
                        + property_type
                        + "\n"
                    )
                elif "type" in property_schema["items"]:
                    if property_schema["items"]["type"] == "string":
                        property_type = "str"
                    elif property_schema["items"]["type"] == "number":
                        property_type = "float"
                    elif property_schema["items"]["type"] == "integer":
                        property_type = "int"
                    elif property_schema["items"]["type"] == "array":
                        if "items" in property_schema["items"]:
                            if property_schema["items"]["items"]["type"] == "string":
                                property_type = "List[str]"
                            elif property_schema["items"]["items"]["type"] == "number":
                                property_type = "List[float]"
                            else:
                                logging.error("property: ", property_schema)
                                raise Exception("Unknown property type")
                        else:
                            logging.error("property: ", property_schema)
                            raise Exception("Unknown property type")
                    else:
                        raise Exception(
                            "  unknown array type: ",
                            property_schema["items"]["type"],
                        )
                else:
                    logging.error("array: ", [property_schema])
                    logging.error("array: ", [property_schema["items"]])
                    raise Exception("Unknown array type")

            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + " = cast(List["
                + property_type
                + '], d.pop("'
                + property_name
                + '", UNSET))\n'
            )
            f.write("\n")
        else:
            f.write(
                "\t\t"
                + clean_parameter_name(property_name)
                + ' = d.pop("'
                + property_name
                + '", UNSET)\n'
            )
    elif "$ref" in property_schema:
        ref = property_schema["$ref"].replace("#/components/schemas/", "")
        # Get the type for the reference.
        data["components"]["schemas"][ref]

        f.write(
            "\t\t_"
            + clean_parameter_name(property_name)
            + ' = d.pop("'
            + property_name
            + '", UNSET)\n'
        )
        f.write(
            "\t\t"
            + clean_parameter_name(property_name)
            + ": Union[Unset, "
            + ref
            + "]\n"
        )
        f.write(
            "\t\tif isinstance(_" + clean_parameter_name(property_name) + ", Unset):\n"
        )
        f.write("\t\t\t" + clean_parameter_name(property_name) + " = UNSET\n")
        f.write("\t\telse:\n")

        f.write(
            "\t\t\t"
            + clean_parameter_name(property_name)
            + " = _"
            + clean_parameter_name(property_name)
            + " # type: ignore[arg-type]\n"
        )

        f.write("\n")
    elif "allOf" in property_schema:
        if len(property_schema["allOf"]) != 1:
            print(property_schema)
            raise Exception("Unknown allOf")
        thing = property_schema["allOf"][0]
        renderTypeFromDict(f, property_name, thing, data)
    else:
        f.write(
            "\t\t"
            + clean_parameter_name(property_name)
            + ' = d.pop("'
            + property_name
            + '", UNSET)\n'
        )


def hasDateTime(schema: dict) -> bool:
    # Generate the type.
    if "type" in schema:
        type_name = schema["type"]
        if type_name == "object":
            # Iternate over the properties.
            if "properties" in schema:
                for property_name in schema["properties"]:
                    property_schema = schema["properties"][property_name]
                    has_date_time = hasDateTime(property_schema)
                    if has_date_time:
                        return True
        elif type_name == "string" and "format" in schema:
            if (
                schema["format"] == "date-time"
                or schema["format"] == "partial-date-time"
            ):
                return True

    return False


def hasBase64(schema: dict) -> bool:
    # Generate the type.
    if "type" in schema:
        type_name = schema["type"]
        if type_name == "object":
            if "additionalProperties" in schema:
                return hasBase64(schema["additionalProperties"])
            # Iternate over the properties.
            if "properties" in schema:
                for property_name in schema["properties"]:
                    property_schema = schema["properties"][property_name]
                    has_base64 = hasBase64(property_schema)
                    if has_base64:
                        return True
        elif type_name == "string" and "format" in schema:
            if schema["format"] == "byte":
                return True

    return False


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
                    logging.error("unsupported type: ", schema)
                    raise Exception("unsupported type: ", schema)

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
                            else:
                                raise Exception("Unknown array type")
                        elif json["type"] == "string":
                            refs.append("str")
                        else:
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


def isNestedObjectOneOf(schema: dict) -> bool:
    if "oneOf" not in schema:
        return False

    is_nested_object = False
    for one_of in schema["oneOf"]:
        # Check if each are an object w 1 property in it.
        if (
            one_of["type"] == "object"
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
            one_of["type"] == "string" and "enum" in one_of and len(one_of["enum"]) == 1
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
