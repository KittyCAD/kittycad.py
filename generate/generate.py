#!/usr/bin/env python3
import io
import json
import logging
import os
import random
import re
from typing import Any, Dict, List, Optional, Tuple

import black
import isort
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
from kittycad import Client

client = Client(token="$TOKEN")

# - OR -

# Create a new client with your token parsed from the environment variable:
#   `KITTYCAD_API_TOKEN`.
from kittycad import ClientFromEnv

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

    # Rewrite the spec back out.
    patch_file = os.path.join(cwd, "kittycad.py.patch.json")
    f = open(patch_file, "w")
    f.write(patch.to_string())
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
    name: str, schema: dict, data: dict, import_path: Optional[str]
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
        elif (
            schema["type"] == "number"
            and "format" in schema
            and (schema["format"] == "float" or schema["format"] == "double")
        ):
            parameter_type = "float"
            parameter_example = "3.14"
        elif schema["type"] == "array" and "items" in schema:
            items_type, items_example, items_imports = generateTypeAndExamplePython(
                "", schema["items"], data, None
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
                else:
                    (
                        prop_type,
                        prop_example,
                        prop_imports,
                    ) = generateTypeAndExamplePython("", prop, data, None)
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
                "", schema["additionalProperties"], data, None
            )
            example_imports = example_imports + items_imports
            parameter_type = "Dict[str, " + items_type + "]"
            parameter_example = '{"<string>": ' + items_example + "}"
        else:
            logging.error("schema: %s", json.dumps(schema, indent=4))
            raise Exception("Unknown parameter type")
    elif "oneOf" in schema and len(schema["oneOf"]) > 0:
        one_of = schema["oneOf"][0]
        # Check if each of these only has a object w 1 property.
        if isNestedObjectOneOf(schema):
            if "properties" in one_of:
                properties = one_of["properties"]
                for prop in properties:
                    return generateTypeAndExamplePython(
                        prop, properties[prop], data, camel_to_snake(name)
                    )
                    break
            elif "type" in one_of and one_of["type"] == "string":
                return generateTypeAndExamplePython(
                    name, one_of, data, camel_to_snake(name)
                )

        return generateTypeAndExamplePython(name, schema["oneOf"][0], data, None)
    elif "allOf" in schema and len(schema["allOf"]) == 1:
        return generateTypeAndExamplePython(name, schema["allOf"][0], data, None)
    elif "$ref" in schema:
        parameter_type = schema["$ref"].replace("#/components/schemas/", "")
        # Get the schema for the reference.
        ref_schema = data["components"]["schemas"][parameter_type]

        return generateTypeAndExamplePython(parameter_type, ref_schema, data, None)
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
    logging.info("generating type: ", name, " at: ", file_path)
    f = open(file_path, "w")

    f.write("from typing import List\n\n")

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

    if fn_name == "get_file_conversion" or fn_name == "create_file_conversion":
        fn_name += "_with_base64_helper"

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

    if fn_name.endswith("_with_base64_helper"):
        example_imports += (
            """from kittycad.api."""
            + tag_name
            + """ import """
            + fn_name.replace("_with_base64_helper", "")
            + "\n"
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
            ) = generateTypeAndExamplePython("", parameter["schema"], data, None)
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
                body_example,
                more_example_imports,
            ) = generateTypeAndExamplePython(request_body_type, rbs, data, None)
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
            example_imports + "from typing import Union, Any, Optional, List\n"
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
        short_sync_example = short_sync_example + (
            """
    if isinstance(result, Error) or result == None:
        print(result)
        raise Exception("Error in response")

    body: """
            + success_type
            + """ = result
    print(body)

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
        + """

    # OR if you need more info (e.g. status_code)
    """
        + example_variable_response
        + fn_name.replace("_with_base64_helper", "")
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
        + fn_name.replace("_with_base64_helper", "")
        + """.asyncio_detailed(client=client,\n"""
        + params_str
        + """)"""
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

    # Add our imports.
    f.write("from typing import Any, Dict, Optional, Union, cast\n")
    f.write("\n")
    f.write("import httpx\n")
    f.write("\n")
    f.write("from ...client import Client\n")
    # Import our references for responses.
    for ref in endpoint_refs:
        if ref.startswith("List[") and ref.endswith("]"):
            ref = ref.replace("List[", "").replace("]", "")
        if ref != "str" and ref != "dict":
            f.write("from ...models." + camel_to_snake(ref) + " import " + ref + "\n")
    for ref in parameter_refs:
        f.write("from ...models." + camel_to_snake(ref) + " import " + ref + "\n")
    for ref in request_body_refs:
        f.write("from ...models." + camel_to_snake(ref) + " import " + ref + "\n")
    f.write("from ...types import Response\n")
    f.write("\n")

    # Define the method.
    f.write("def _get_kwargs(\n")
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
                    optional_args.append(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
                else:
                    f.write(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
            else:
                f.write(
                    "\t"
                    + camel_to_snake(parameter_name)
                    + ": "
                    + parameter_type
                    + ",\n"
                )
    if request_body_type:
        f.write("\tbody: " + request_body_type + ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    for optional_arg in optional_args:
        f.write(optional_arg)
    f.write(") -> Dict[str, Any]:\n")
    templateUrl = "{}" + name
    formatTemplate = ".format(client.base_url"
    query_params: List[str] = []
    # Iterate over the parameters.
    if "parameters" in endpoint:
        parameters = endpoint["parameters"]
        for parameter in parameters:
            parameter_name = parameter["name"]
            if "type" in parameter["schema"]:
                parameter_type = parameter["schema"]["type"].replace("string", "str")
            elif "$ref" in parameter["schema"]:
                parameter_type = parameter["schema"]["$ref"].replace(
                    "#/components/schemas/", ""
                )
            else:
                logging.error("parameter: ", parameter)
                raise Exception("Unknown parameter type")
            if parameter["in"] == "path":
                formatTemplate = (
                    formatTemplate
                    + ", "
                    + clean_parameter_name(parameter_name)
                    + "="
                    + camel_to_snake(parameter_name)
                )
            elif parameter["in"] == "query":
                query_params.append(parameter_name)

    f.write('\turl = "' + templateUrl + '"' + formatTemplate + ") # noqa: E501\n")
    for query_param in query_params:
        f.write("\tif " + query_param + " is not None:\n")
        f.write("\t\tif '?' in url:\n")
        f.write("\t\t\turl = url + '&" + query_param + "='+str(" + query_param + ")\n")
        f.write("\t\telse:\n")
        f.write("\t\t\turl = url + '?" + query_param + "='+str(" + query_param + ")\n")

    f.write("\n")
    f.write("\theaders: Dict[str, Any] = client.get_headers()\n")
    f.write("\tcookies: Dict[str, Any] = client.get_cookies()\n")
    f.write("\n")

    f.write("\treturn {\n")
    f.write('\t\t"url": url,\n')
    f.write('\t\t"headers": headers,\n')
    f.write('\t\t"cookies": cookies,\n')
    f.write('\t\t"timeout": client.get_timeout(),\n')
    if request_body_type:
        f.write('\t\t"content": body,\n')
    f.write("\t}\n")

    # Define the parse reponse.
    f.write("\n")
    f.write("\n")

    if len(endpoint_refs) > 0:
        f.write(
            "def _parse_response(*, response: httpx.Response) -> "
            + response_type
            + ":\n"
        )
    else:
        f.write("def _parse_response(*, response: httpx.Response):\n")

    # Iterate over the responses.
    if len(endpoint_refs) > 0:
        responses = endpoint["responses"]
        for response_code in responses:
            response = responses[response_code]
            if response_code == "default":
                # This is no content.
                f.write("\treturn None\n")
            elif response_code == "204" or response_code == "302":
                # This is no content.
                f.write("\treturn None\n")
            else:
                f.write(
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
                                # Let's check if it is a oneOf.
                                if "oneOf" in schema:
                                    is_one_of = True
                                    # We want to parse each of the possible types.
                                    f.write("\t\tdata = response.json()\n")
                                    for index, one_of in enumerate(schema["oneOf"]):
                                        ref = getOneOfRefType(one_of)
                                        f.write("\t\ttry:\n")
                                        f.write(
                                            "\t\t\tif not isinstance(data, dict):\n"
                                        )
                                        f.write("\t\t\t\traise TypeError()\n")
                                        option_name = "option_" + camel_to_snake(ref)
                                        f.write(
                                            "\t\t\t"
                                            + option_name
                                            + " = "
                                            + ref
                                            + ".from_dict(data)\n"
                                        )
                                        f.write("\t\t\treturn " + option_name + "\n")
                                        f.write("\t\texcept ValueError:\n")
                                        if index == len(schema["oneOf"]) - 1:
                                            # On the last one raise the error.
                                            f.write("\t\t\traise\n")
                                        else:
                                            f.write("\t\t\tpass\n")
                                        f.write("\t\texcept TypeError:\n")
                                        if index == len(schema["oneOf"]) - 1:
                                            # On the last one raise the error.
                                            f.write("\t\t\traise\n")
                                        else:
                                            f.write("\t\t\tpass\n")
                                else:
                                    f.write(
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
                                        f.write(
                                            "\t\tresponse_" + response_code + " = [\n"
                                        )
                                        f.write("\t\t\t" + ref + ".from_dict(item)\n")
                                        f.write("\t\t\tfor item in response.json()\n")
                                        f.write("\t\t]\n")
                                    else:
                                        raise Exception("Unknown array type")
                                elif json["type"] == "string":
                                    f.write(
                                        "\t\tresponse_"
                                        + response_code
                                        + " = response.text\n"
                                    )
                                else:
                                    raise Exception("Unknown type", json["type"])
                            else:
                                f.write(
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
                                    f.write(
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
                    f.write("\t\treturn response_" + response_code + "\n")

        # End the method.
        f.write("\treturn Error.from_dict(response.json())\n")
    else:
        f.write("\treturn\n")

    # Define the build response method.
    f.write("\n")
    f.write("\n")
    if len(endpoint_refs) > 0:
        f.write(
            "def _build_response(*, response: httpx.Response) -> "
            + detailed_response_type
            + ":\n"
        )
    else:
        f.write("def _build_response(*, response: httpx.Response) -> Response[Any]:\n")

    f.write("\treturn Response(\n")
    f.write("\t\tstatus_code=response.status_code,\n")
    f.write("\t\tcontent=response.content,\n")
    f.write("\t\theaders=response.headers,\n")
    f.write("\t\tparsed=_parse_response(response=response),\n")
    f.write("\t)\n")

    # Define the sync_detailed method.
    f.write("\n")
    f.write("\n")
    f.write("def sync_detailed(\n")
    optional_args = []
    # Iterate over the parameters.
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
                    optional_args.append(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
                else:
                    f.write(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
            else:
                f.write(
                    "\t"
                    + camel_to_snake(parameter_name)
                    + ": "
                    + parameter_type
                    + ",\n"
                )
    if request_body_type:
        f.write("\tbody: " + request_body_type + ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    for optional_arg in optional_args:
        f.write(optional_arg)

    if len(endpoint_refs) > 0:
        f.write(") -> " + detailed_response_type + ":\n")
    else:
        f.write(") -> Response[Any]:\n")

    f.write("\tkwargs = _get_kwargs(\n")
    params = get_function_parameters(endpoint, request_body_type)
    for param in params:
        f.write("\t\t" + clean_parameter_name(param) + "=" + param + ",\n")
    f.write("\t\tclient=client,\n")
    f.write("\t)\n")
    f.write("\n")
    f.write("\tresponse = httpx." + method + "(\n")
    f.write("\t\tverify=client.verify_ssl,\n")
    f.write("\t\t**kwargs,\n")
    f.write("\t)\n")
    f.write("\n")
    f.write("\treturn _build_response(response=response)\n")

    # Define the sync method.
    f.write("\n")
    f.write("\n")
    f.write("def sync(\n")
    optional_args = []
    # Iterate over the parameters.
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
                    optional_args.append(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
                else:
                    f.write(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
            else:
                f.write(
                    "\t"
                    + camel_to_snake(parameter_name)
                    + ": "
                    + parameter_type
                    + ",\n"
                )
    if request_body_type:
        f.write("\tbody: " + request_body_type + ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    for optional_arg in optional_args:
        f.write(optional_arg)

    if len(endpoint_refs) > 0:
        f.write(") -> " + response_type + ":\n")
    else:
        f.write("):\n")

    if "description" in endpoint:
        f.write('\t""" ' + endpoint["description"] + ' """ # noqa: E501\n')
    f.write("\n")
    f.write("\treturn sync_detailed(\n")
    params = get_function_parameters(endpoint, request_body_type)
    for param in params:
        f.write("\t\t" + clean_parameter_name(param) + "=" + param + ",\n")
    f.write("\t\tclient=client,\n")
    f.write("\t).parsed\n")

    # Define the asyncio_detailed method.
    f.write("\n")
    f.write("\n")
    f.write("async def asyncio_detailed(\n")
    optional_args = []
    # Iterate over the parameters.
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
                    optional_args.append(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
                else:
                    f.write(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
            else:
                f.write(
                    "\t"
                    + camel_to_snake(parameter_name)
                    + ": "
                    + parameter_type
                    + ",\n"
                )
    if request_body_type is not None:
        f.write("\tbody: " + request_body_type + ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    for optional_arg in optional_args:
        f.write(optional_arg)

    if len(endpoint_refs) > 0:
        f.write(") -> " + detailed_response_type + ":\n")
    else:
        f.write(") -> Response[Any]:\n")

    f.write("\tkwargs = _get_kwargs(\n")
    params = get_function_parameters(endpoint, request_body_type)
    for param in params:
        f.write("\t\t" + clean_parameter_name(param) + "=" + param + ",\n")
    f.write("\t\tclient=client,\n")
    f.write("\t)\n")
    f.write("\n")
    f.write("\tasync with httpx.AsyncClient(verify=client.verify_ssl) as _client:\n")
    f.write("\t\tresponse = await _client." + method + "(**kwargs)\n")
    f.write("\n")
    f.write("\treturn _build_response(response=response)\n")

    # Define the asyncio method.
    f.write("\n")
    f.write("\n")
    f.write("async def asyncio(\n")
    optional_args = []
    # Iterate over the parameters.
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
                    optional_args.append(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
                else:
                    f.write(
                        "\t"
                        + camel_to_snake(parameter_name)
                        + ": "
                        + parameter_type
                        + ",\n"
                    )
            else:
                f.write(
                    "\t"
                    + camel_to_snake(parameter_name)
                    + ": "
                    + parameter_type
                    + ",\n"
                )
    if request_body_type:
        f.write("\tbody: " + request_body_type + ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    for optional_arg in optional_args:
        f.write(optional_arg)

    if len(endpoint_refs) > 0:
        f.write(") -> " + response_type + ":\n")
    else:
        f.write("):\n")

    if "description" in endpoint:
        f.write('\t""" ' + endpoint["description"] + ' """ # noqa: E501\n')
    f.write("\n")
    f.write("\treturn (\n")
    f.write("\t\tawait asyncio_detailed(\n")
    params = get_function_parameters(endpoint, request_body_type)
    for param in params:
        f.write("\t\t" + clean_parameter_name(param) + "=" + param + ",\n")
    f.write("\t\t\tclient=client,\n")
    f.write("\t\t)\n")
    f.write("\t).parsed\n")

    # Close the file.
    f.close()

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
            f.write("from ." + camel_to_snake(ref_name) + " import " + ref_name + "\n")
            all_options.append(ref_name)

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
                            prop_name, nested_object, "object", data
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

    if tag is not None:
        # Generate each of the options from the tag.
        for one_of in schema["oneOf"]:
            # Get the value of the tag.
            object_name = one_of["properties"][tag]["enum"][0]
            object_code = generateObjectTypeCode(object_name, one_of, "object", data)
            f.write(object_code)
            f.write("\n")
            all_options.append(object_name)

    # Write the sum type.
    f.write(name + " = Union[")
    for num, option in enumerate(all_options, start=0):
        if num == 0:
            f.write(option)
        else:
            f.write(", " + option + "")
    f.write("]\n")

    # Close the file.
    f.close()


def generateObjectTypeCode(name: str, schema: dict, type_name: str, data: dict) -> str:
    f = io.StringIO()

    has_date_time = hasDateTime(schema)
    if has_date_time:
        f.write("import datetime\n")
    f.write("from typing import Any, Dict, List, Type, TypeVar, Union, cast\n")
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
        renderTypeToDict(f, property_name, property_schema, data)

    # Finish writing the to_dict method.
    f.write("\n")
    f.write("\t\tfield_dict: Dict[str, Any] = {}\n")
    f.write("\t\tfield_dict.update(self.additional_properties)\n")
    f.write("\t\tfield_dict.update({})\n")

    # Iternate over the properties.
    for property_name in schema["properties"]:
        # Write the property.
        f.write("\t\tif " + clean_parameter_name(property_name) + " is not UNSET:\n")
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

    code = generateObjectTypeCode(name, schema, type_name, data)
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
                        logging.error("property: ", property_schema)
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

            f.write("\t" + property_name + ": Union[Unset, str] = UNSET\n")
        elif property_type == "object":
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
                        logging.error("property: ", property_schema)
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
            logging.error("property type: ", property_type)
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

        # if isNestedObjectOneOf(ref_schema):
        f.write(
            "\t\t\t"
            + clean_parameter_name(property_name)
            + " = _"
            + clean_parameter_name(property_name)
            + " # type: ignore[arg-type]\n"
        )
        # else:
        #    f.write(
        #        "\t\t\t"
        #        + clean_parameter_name(property_name)
        #        + " = "
        #        + ref
        #       + "(_"
        #        + clean_parameter_name(property_name)
        #        + ")\n"
        #     )
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
                            if ref not in refs:
                                refs.append(ref)
                        elif isTypedObjectOneOf(schema):
                            for t in schema["oneOf"]:
                                ref = getOneOfRefType(t)
                                if ref not in refs:
                                    refs.append(ref)
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
                            if ref not in refs:
                                refs.append(ref)

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
