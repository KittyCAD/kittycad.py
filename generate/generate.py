#!/usr/bin/env python3
from prance import BaseParser
import jsonpatch

import json
import os
import re

package_name = 'kittycad'


def main():
    cwd = os.getcwd()
    spec_path = os.path.join(cwd, 'spec.json')
    print("opening spec file: ", spec_path)
    parser = BaseParser(spec_path)

    # Generate the types.
    generateTypes(cwd, parser.specification)

    # Generate the paths.
    data = generatePaths(cwd, parser.specification)

    # Add the client information to the generation.
    data['info']['x-python'] = {
        'client': """# Create a client with your token.
from kittycad import Client

client = Client(token="$TOKEN")

# - OR -

# Create a new client with your token parsed from the environment variable:
#   `KITTYCAD_API_TOKEN`.
from kittycad import ClientFromEnv

client = ClientFromEnv()""",
        'install': 'pip install kittycad',
    }

    # Read the original spec file as a dict.
    spec = open(spec_path, 'r')
    original = json.load(spec)
    # Create the json patch document.
    patch = jsonpatch.make_patch(original, data)

    # Rewrite the spec back out.
    patch_file = os.path.join(cwd, 'kittycad.py.patch.json')
    f = open(patch_file, 'w')
    f.write(patch.to_string())
    f.close()


def generatePaths(cwd: str, parser: dict) -> dict:
    # Make sure we have the directory.
    path = os.path.join(cwd, 'kittycad', 'api')
    os.makedirs(path, exist_ok=True)

    # Open the __init__.py file.
    file_name = '__init__.py'
    file_path = os.path.join(path, file_name)
    f = open(file_path, 'w')
    f.write("\"\"\" Contains methods for accessing the API \"\"\"\n")
    # Close the file.
    f.close()

    # Generate the directory/__init__.py for each of the tags.
    tags = parser['tags']
    for tag in tags:
        tag_name = tag['name'].replace('-', '_')
        tag_description = tag['description']
        tag_path = os.path.join(path, tag_name)
        # Esnure the directory exists.
        os.makedirs(tag_path, exist_ok=True)
        # Open the __init__.py file.
        file_name = '__init__.py'
        file_path = os.path.join(tag_path, file_name)
        f = open(file_path, 'w')
        f.write(
            "\"\"\" Contains methods for accessing the " +
            tag_name +
            " API paths: " +
            tag_description +
            " \"\"\"\n")
        # Close the file.
        f.close()

    # Generate the paths.
    data = parser
    paths = data['paths']
    for p in paths:
        # If p starts with /oauth2 we can skip it.
        # We don't care about generating methods for those.
        if p.startswith('/oauth2'):
            continue
        else:
            for method in paths[p]:
                print('METHOD: ', method.upper())
                # Skip OPTIONS.
                if method.upper() != 'OPTIONS':
                    endpoint = paths[p][method]
                    data = generatePath(path, p, method, endpoint, data)

    return data


def generatePath(
        path: str,
        name: str,
        method: str,
        endpoint: dict,
        data: dict) -> dict:
    # Generate the path.
    fn_name = camel_to_snake(endpoint['operationId'])
    file_name = fn_name + '.py'
    tag_name = ''
    # Add the tag to the path if it exists.
    if 'tags' in endpoint:
        tag_name = endpoint['tags'][0].replace('-', '_')
        path = os.path.join(path, tag_name)
    file_path = os.path.join(path, file_name)
    print("generating type: ", name, " at: ", file_path)
    print("  endpoint: ", [endpoint])
    f = open(file_path, "w")

    endpoint_refs = getEndpointRefs(endpoint, data)
    parameter_refs = getParameterRefs(endpoint)
    request_body_refs = getRequestBodyRefs(endpoint)
    request_body_type = getRequestBodyType(endpoint)

    success_type = ""
    if len(endpoint_refs) > 0:
        success_type = endpoint_refs[0]

    if fn_name == 'get_file_conversion' or fn_name == 'create_file_conversion':
        fn_name += '_with_base64_helper'

    # Iterate over the parameters.
    params_str = ''
    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            parameter_type = ''
            if 'type' in parameter['schema']:
                if 'format' in parameter['schema']:
                    if parameter['schema']['format'] == 'uuid':
                        parameter_type = "\"<uuid>\""
                    else:
                        parameter_type = "\"<string>\""
            elif '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
            else:
                print("  parameter: ", parameter)
                raise Exception("Unknown parameter type")
            params_str += ', ' + \
                camel_to_snake(parameter_name) + '=' + parameter_type

    if request_body_type:
        params_str += ', body=' + request_body_type

    example = """from kittycad.models import """ + success_type + """
from kittycad.api.""" + tag_name + """ import """ + fn_name + """
from kittycad.types import Response

fc: """ + success_type + """ = """ + fn_name + """.sync(client=client""" + params_str + """)

# OR if you need more info (e.g. status_code)
response: Response[""" + success_type + """] = """ + fn_name + """.sync_detailed(client=client""" + params_str + """)

# OR run async
fc: """ + success_type + """ = await """ + fn_name + """.asyncio(client=client""" + params_str + """)

# OR run async with more info
response: Response[""" + success_type + """] = await """ + fn_name + """.asyncio_detailed(client=client""" + params_str + """)"""

    # Add our example to our json output.
    data['paths'][name][method]['x-python'] = {
        'example': example,
        'libDocsLink': 'https://python.api.docs.kittycad.io/modules/kittycad.api.' + tag_name + '.' + fn_name + '.html',
    }

    # Add our imports.
    f.write("from typing import Any, Dict, Optional, Union, cast\n")
    f.write("\n")
    f.write("import httpx\n")
    f.write("\n")
    f.write("from ...client import Client\n")
    # Import our references for responses.
    for ref in endpoint_refs:
        if ref.startswith('[') and ref.endswith(']'):
            ref = ref.replace('[', '').replace(']', '')
        f.write(
            "from ...models." +
            camel_to_snake(ref) +
            " import " +
            ref +
            "\n")
    for ref in parameter_refs:
        f.write(
            "from ...models." +
            camel_to_snake(ref) +
            " import " +
            ref +
            "\n")
    for ref in request_body_refs:
        f.write(
            "from ...models." +
            camel_to_snake(ref) +
            " import " +
            ref +
            "\n")
    f.write("from ...types import Response\n")
    f.write("\n")

    # Define the method.
    f.write("def _get_kwargs(\n")
    # Iterate over the parameters.
    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            if 'type' in parameter['schema']:
                parameter_type = parameter['schema']['type'].replace(
                    'string', 'str').replace(
                    'integer', 'int').replace(
                    'number', 'float')
            elif '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
            else:
                print("  parameter: ", parameter)
                raise Exception("Unknown parameter type")
            f.write(
                "\t" +
                camel_to_snake(parameter_name) +
                ": " +
                parameter_type +
                ",\n")
    if request_body_type:
        f.write(
            "\tbody: " +
            request_body_type +
            ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    f.write(") -> Dict[str, Any]:\n")
    templateUrl = "{}" + name
    formatTemplate = ".format(client.base_url"
    queryTemplate = ""
    # Iterate over the parameters.
    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            if 'type' in parameter['schema']:
                parameter_type = parameter['schema']['type'].replace(
                    'string', 'str')
            elif '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
            else:
                print("  parameter: ", parameter)
                raise Exception("Unknown parameter type")
            if parameter['in'] == 'path':
                formatTemplate = formatTemplate + ", " + \
                    parameter_name + "=" + camel_to_snake(parameter_name)
            elif parameter['in'] == 'query':
                formatTemplate = formatTemplate + ", " + \
                    parameter_name + "=" + camel_to_snake(parameter_name)
                queryTemplate = queryTemplate + "&" + \
                    camel_to_snake(parameter_name) + "=" + "{" + camel_to_snake(parameter_name) + "}"
    if queryTemplate[1:].__len__() > 0:
        f.write("\turl = \"" + templateUrl + "?" +
                queryTemplate[1:] + "\"" + formatTemplate + ")\n")
    else:
        f.write("\turl = \"" + templateUrl + "\"" + formatTemplate + ")\n")

    f.write("\n")
    f.write("\theaders: Dict[str, Any] = client.get_headers()\n")
    f.write("\tcookies: Dict[str, Any] = client.get_cookies()\n")
    f.write("\n")

    f.write("\treturn {\n")
    f.write("\t\t\"url\": url,\n")
    f.write("\t\t\"headers\": headers,\n")
    f.write("\t\t\"cookies\": cookies,\n")
    f.write("\t\t\"timeout\": client.get_timeout(),\n")
    if request_body_type:
        f.write("\t\t\"content\": body,\n")
    f.write("\t}\n")

    # Define the parse reponse.
    f.write("\n")
    f.write("\n")

    f.write(
        "def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, " +
        ", ".join(endpoint_refs) +
        "]]:\n")
    # Iterate over the responses.
    responses = endpoint['responses']
    for response_code in responses:
        response = responses[response_code]
        f.write(
            "\tif response.status_code == " +
            response_code.replace(
                "XX",
                "00") +
            ":\n")
        is_one_of = False
        if 'content' in response:
            content = response['content']
            for content_type in content:
                if content_type == 'application/json':
                    json = content[content_type]['schema']
                    if '$ref' in json:
                        ref = json['$ref'].replace('#/components/schemas/', '')
                        schema = data['components']['schemas'][ref]
                        # Let's check if it is a oneOf.
                        if 'oneOf' in schema:
                            is_one_of = True
                            # We want to parse each of the possible types.
                            f.write("\t\tdata = response.json()\n")
                            for index, one_of in enumerate(schema['oneOf']):
                                ref = getOneOfRefType(one_of)
                                f.write("\t\ttry:\n")
                                f.write(
                                    "\t\t\tif not isinstance(data, dict):\n")
                                f.write("\t\t\t\traise TypeError()\n")
                                f.write(
                                    "\t\t\toption = " + ref + ".from_dict(data)\n")
                                f.write("\t\t\treturn option\n")
                                f.write("\t\texcept:\n")
                                if index == len(schema['oneOf']) - 1:
                                    # On the last one raise the error.
                                    f.write("\t\t\traise\n")
                                else:
                                    f.write("\t\t\tpass\n")
                        else:
                            f.write(
                                "\t\tresponse_" +
                                response_code +
                                " = " +
                                ref +
                                ".from_dict(response.json())\n")
                    elif 'type' in json:
                        if json['type'] == 'array':
                            items = json['items']
                            if '$ref' in items:
                                ref = items['$ref'].replace(
                                    '#/components/schemas/', '')
                                f.write(
                                    "\t\tresponse_" +
                                    response_code +
                                    " = [\n")
                                f.write(
                                    "\t\t\t" +
                                    ref +
                                    ".from_dict(item)\n")
                                f.write(
                                    "\t\t\tfor item in response.json()\n")
                                f.write("\t\t]\n")
                            else:
                                raise Exception("Unknown array type")
                        elif json['type'] == 'string':
                            f.write(
                                "\t\tresponse_" +
                                response_code +
                                " = response.text\n")
                        else:
                            raise Exception("Unknown type", json['type'])
                    else:
                        f.write(
                            "\t\tresponse_" +
                            response_code +
                            " = response.json()\n")

        elif '$ref' in response:
            schema_name = response['$ref'].replace(
                '#/components/responses/', '')
            schema = data['components']['responses'][schema_name]
            if 'content' in schema:
                content = schema['content']
                for content_type in content:
                    if content_type == 'application/json':
                        json = content[content_type]['schema']
                        if '$ref' in json:
                            ref = json['$ref'].replace(
                                '#/components/schemas/', '')
                            f.write(
                                "\t\tresponse_" +
                                response_code +
                                " = " +
                                ref +
                                ".from_dict(response.json())\n")
        else:
            f.write("\t\tresponse_" + response_code + " = None\n")

        if not is_one_of:
            f.write(
                "\t\treturn response_" +
                response_code +
                "\n")

    # End the method.
    f.write("\treturn None\n")

    # Define the build response method.
    f.write("\n")
    f.write("\n")
    f.write(
        "def _build_response(*, response: httpx.Response) -> Response[Union[Any, " +
        ", ".join(endpoint_refs) +
        "]]:\n")
    f.write("\treturn Response(\n")
    f.write("\t\tstatus_code=response.status_code,\n")
    f.write("\t\tcontent=response.content,\n")
    f.write("\t\theaders=response.headers,\n")
    f.write("\t\tparsed=_parse_response(response=response),\n")
    f.write("\t)\n")

    # Define the sync_detailed method.
    f.write("\n")
    f.write("\n")
    f.write(
        "def sync_detailed(\n")
    # Iterate over the parameters.
    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            if 'type' in parameter['schema']:
                parameter_type = parameter['schema']['type'].replace(
                    'string', 'str').replace(
                    'integer', 'int').replace(
                    'number', 'float')
            elif '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
            else:
                print("  parameter: ", parameter)
                raise Exception("Unknown parameter type")
            f.write(
                "\t" +
                camel_to_snake(parameter_name) +
                ": " +
                parameter_type +
                ",\n")
    if request_body_type:
        f.write(
            "\tbody: " +
            request_body_type +
            ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    f.write(") -> Response[Union[Any, " +
            ", ".join(endpoint_refs) +
            "]]:\n")
    f.write("\tkwargs = _get_kwargs(\n")
    params = get_function_parameters(endpoint, request_body_type)
    for param in params:
        f.write(
            "\t\t" + param + "=" + param + ",\n")
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
    f.write(
        "def sync(\n")
    # Iterate over the parameters.
    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            if 'type' in parameter['schema']:
                parameter_type = parameter['schema']['type'].replace(
                    'string', 'str').replace(
                    'integer', 'int').replace(
                    'number', 'float')
            elif '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
            else:
                print("  parameter: ", parameter)
                raise Exception("Unknown parameter type")
            f.write(
                "\t" +
                camel_to_snake(parameter_name) +
                ": " +
                parameter_type +
                ",\n")
    if request_body_type:
        f.write(
            "\tbody: " +
            request_body_type +
            ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    f.write(") -> Optional[Union[Any, " +
            ", ".join(endpoint_refs) +
            "]]:\n")
    if 'description' in endpoint:
        f.write("\t\"\"\" " + endpoint['description'] + " \"\"\"\n")
    f.write("\n")
    f.write("\treturn sync_detailed(\n")
    params = get_function_parameters(endpoint, request_body_type)
    for param in params:
        f.write(
            "\t\t" + param + "=" + param + ",\n")
    f.write("\t\tclient=client,\n")
    f.write("\t).parsed\n")

    # Define the asyncio_detailed method.
    f.write("\n")
    f.write("\n")
    f.write(
        "async def asyncio_detailed(\n")
    # Iterate over the parameters.
    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            if 'type' in parameter['schema']:
                parameter_type = parameter['schema']['type'].replace(
                    'string', 'str').replace(
                    'integer', 'int').replace(
                    'number', 'float')
            elif '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
            else:
                print("  parameter: ", parameter)
                raise Exception("Unknown parameter type")
            f.write(
                "\t" +
                camel_to_snake(parameter_name) +
                ": " +
                parameter_type +
                ",\n")
    if request_body_type:
        f.write(
            "\tbody: " +
            request_body_type +
            ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    f.write(") -> Response[Union[Any, " +
            ", ".join(endpoint_refs) +
            "]]:\n")
    f.write("\tkwargs = _get_kwargs(\n")
    params = get_function_parameters(endpoint, request_body_type)
    for param in params:
        f.write(
            "\t\t" + param + "=" + param + ",\n")
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
    f.write(
        "async def asyncio(\n")
    # Iterate over the parameters.
    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            if 'type' in parameter['schema']:
                parameter_type = parameter['schema']['type'].replace(
                    'string', 'str').replace(
                    'integer', 'int').replace(
                    'number', 'float')
            elif '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
            else:
                print("  parameter: ", parameter)
                raise Exception("Unknown parameter type")
            f.write(
                "\t" +
                camel_to_snake(parameter_name) +
                ": " +
                parameter_type +
                ",\n")
    if request_body_type:
        f.write(
            "\tbody: " +
            request_body_type +
            ",\n")
    f.write("\t*,\n")
    f.write("\tclient: Client,\n")
    f.write(") -> Optional[Union[Any, " +
            ", ".join(endpoint_refs) +
            "]]:\n")
    if 'description' in endpoint:
        f.write("\t\"\"\" " + endpoint['description'] + " \"\"\"\n")
    f.write("\n")
    f.write("\treturn (\n")
    f.write("\t\tawait asyncio_detailed(\n")
    params = get_function_parameters(endpoint, request_body_type)
    for param in params:
        f.write(
            "\t\t" + param + "=" + param + ",\n")
    f.write("\t\t\tclient=client,\n")
    f.write("\t\t)\n")
    f.write("\t).parsed\n")

    # Close the file.
    f.close()

    return data


def generateTypes(cwd: str, parser: dict):
    # Make sure we have the directory.
    path = os.path.join(cwd, 'kittycad', 'models')
    os.makedirs(path, exist_ok=True)

    # Open the __init__.py file.
    file_name = '__init__.py'
    file_path = os.path.join(path, file_name)
    f = open(file_path, 'w')
    f.write("\"\"\" Contains all the data models used in inputs/outputs \"\"\"\n")
    f.write("\n")

    # Generate the types.
    data = parser
    schemas = data['components']['schemas']
    for key in schemas:
        schema = schemas[key]
        print("generating schema: ", key)
        generateType(path, key, schema, data)
        if 'oneOf' not in schema:
            f.write("from ." + camel_to_snake(key) + " import " + key + "\n")

    # Close the file.
    f.close()


def generateType(path: str, name: str, schema: dict, data: dict):
    file_path = path
    if path.endswith(".py") is False:
        # Generate the type.
        file_name = camel_to_snake(name) + '.py'
        file_path = os.path.join(path, file_name)

    if 'type' in schema:
        type_name = schema['type']
        if type_name == 'object':
            generateObjectType(file_path, name, schema, type_name, data)
        elif type_name == 'string' and 'enum' in schema and schema['enum'] != [None]:
            generateEnumType(file_path, name, schema, type_name)
        elif type_name == 'integer':
            generateIntegerType(file_path, name, schema, type_name)
        elif type_name == 'number':
            generateIntegerType(file_path, name, schema, type_name)
        elif type_name == 'string':
            generateStringType(file_path, name, schema, type_name)
        else:
            print("  unsupported type: ", type_name)
            raise Exception("  unsupported type: ", type_name)
    elif '$ref' in schema:
        # Skip it since we will already have generated it.
        return
    elif 'oneOf' in schema:
        # Skip it since we will already have generated it.
        return
    else:
        print("  schema: ", [schema])
        print("  unsupported type: ", name)
        raise Exception("  unsupported type: ", name)


def generateStringType(path: str, name: str, schema: dict, type_name: str):
    print("generating type: ", name, " at: ", path)
    print("  schema: ", [schema])
    f = open(path, "w")

    f.write("class " + name + "(str):\n")
    f.write("\n")
    f.write("\tdef __str__(self) -> str:\n")
    f.write("\t\treturn self\n")

    # Close the file.
    f.close()


def generateIntegerType(path: str, name: str, schema: dict, type_name: str):
    print("generating type: ", name, " at: ", path)
    print("  schema: ", [schema])
    f = open(path, "w")

    f.write("class " + name + "(int):\n")
    f.write("\n")
    f.write("\tdef __int__(self) -> int:\n")
    f.write("\t\treturn self\n")

    # Close the file.
    f.close()


def generateFloatType(path: str, name: str, schema: dict, type_name: str):
    print("generating type: ", name, " at: ", path)
    print("  schema: ", [schema])
    f = open(path, "w")

    f.write("class " + name + "(float):\n")
    f.write("\n")
    f.write("\tdef __float__(self) -> float:\n")
    f.write("\t\treturn self\n")

    # Close the file.
    f.close()


def generateEnumType(path: str, name: str, schema: dict, type_name: str):
    print("generating type: ", name, " at: ", path)
    print("  schema: ", [schema])
    f = open(path, "w")

    f.write("from enum import Enum\n")
    f.write("\n")
    f.write("class " + name + "(str, Enum):\n")
    # Iterate over the properties.
    for value in schema['enum']:
        enum_name = camel_to_screaming_snake(value)
        if enum_name == '':
            enum_name = 'EMPTY'
        elif enum_name == '1':
            enum_name = 'ONE'
        elif enum_name == '2':
            enum_name = 'TWO'

        f.write(
            "\t" +
            enum_name +
            " = '" +
            value +
            "'\n")

    # close the enum.
    f.write("\n")
    f.write("\tdef __str__(self) -> str:\n")
    f.write("\t\treturn str(self.value)\n")

    # Close the file.
    f.close()


def generateObjectType(
        path: str,
        name: str,
        schema: dict,
        type_name: str,
        data: dict):
    print("generating type: ", name, " at: ", path)
    print("  schema: ", [schema])
    f = open(path, "w")

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
        print("  ref: ", ref, "schema: ", [schema])
        f.write(
            "from ..models." +
            camel_to_snake(ref) +
            " import " +
            ref +
            "\n")

    f.write("from ..types import UNSET, Unset\n")
    f.write("\n")
    f.write("T = TypeVar(\"T\", bound=\"" + name + "\")\n")
    f.write("\n")
    f.write("@attr.s(auto_attribs=True)\n")
    f.write("class " + name + ":\n")
    # Write the description.
    f.write("\t\"\"\" \"\"\"\n")
    # Iterate over the properties.
    for property_name in schema['properties']:
        property_schema = schema['properties'][property_name]
        renderTypeInit(f, path, property_name, property_schema, data)

    # Finish writing the class.
    f.write("\n")
    f.write(
        "\tadditional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)\n")

    # Now let's write the to_dict method.
    f.write("\n")
    f.write("\tdef to_dict(self) -> Dict[str, Any]:\n")
    # Iternate over the properties.
    for property_name in schema['properties']:
        property_schema = schema['properties'][property_name]
        renderTypeToDict(f, property_name, property_schema, data)

    # Finish writing the to_dict method.
    f.write("\n")
    f.write("\t\tfield_dict: Dict[str, Any] = {}\n")
    f.write("\t\tfield_dict.update(self.additional_properties)\n")
    f.write("\t\tfield_dict.update({})\n")

    # Iternate over the properties.
    for property_name in schema['properties']:
        # Write the property.
        f.write("\t\tif " + property_name + " is not UNSET:\n")
        f.write(
            "\t\t\tfield_dict['" +
            property_name +
            "'] = " +
            property_name +
            "\n")

    f.write("\n")
    f.write("\t\treturn field_dict\n")

    # Now let's write the from_dict method.
    f.write("\n")
    f.write("\t@classmethod\n")
    f.write(
        "\tdef from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:\n")
    f.write("\t\td = src_dict.copy()\n")

    # Iternate over the properties.
    for property_name in schema['properties']:
        property_schema = schema['properties'][property_name]
        renderTypeFromDict(f, property_name, property_schema, data)

    # Finish writing the from_dict method.
    f.write("\n")
    f.write("\t\t" + camel_to_snake(name) + " = cls(\n")
    # Iternate over the properties.
    for property_name in schema['properties']:
        # Write the property.
        f.write("\t\t\t" + property_name + "= " + property_name + ",\n")

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

    # Close the file.
    f.close()


def renderTypeToDict(
        f,
        property_name: str,
        property_schema: dict,
        data: dict):
    if 'type' in property_schema:
        property_type = property_schema['type']

        # Write the property.
        if property_type == 'string':
            if 'format' in property_schema:
                if property_schema['format'] == 'date-time' or property_schema['format'] == 'partial-date-time':
                    f.write(
                        "\t\t" +
                        property_name +
                        ": Union[Unset, str] = UNSET\n")
                    f.write(
                        "\t\tif not isinstance(self." +
                        property_name +
                        ", Unset):\n")
                    f.write(
                        "\t\t\t" +
                        property_name +
                        " = self." +
                        property_name +
                        ".isoformat()\n")
                    # return early
                    return

            f.write(
                "\t\t" +
                property_name +
                " = self." +
                property_name +
                "\n")
        elif property_type == 'integer':
            f.write(
                "\t\t" +
                property_name +
                " = self." +
                property_name +
                "\n")
        elif property_type == 'number':
            f.write(
                "\t\t" +
                property_name +
                " = self." +
                property_name +
                "\n")
        elif property_type == 'boolean':
            f.write(
                "\t\t" +
                property_name +
                " = self." +
                property_name +
                "\n")
        elif property_type == 'array':
            if 'items' in property_schema:
                if '$ref' in property_schema['items']:
                    property_type = property_schema['items']['$ref']
                    property_type = property_type.replace(
                        '#/components/schemas/', '')
                    f.write(
                        "\t\tfrom ..models." +
                        camel_to_snake(property_type) +
                        " import " +
                        property_type +
                        "\n")
                elif 'type' in property_schema['items']:
                    if property_schema['items']['type'] == 'string':
                        property_type = 'str'
                    elif property_schema['items']['type'] == 'number':
                        property_type = 'float'
                    elif property_schema['items']['type'] == 'array':
                        if 'items' in property_schema['items']:
                            if property_schema['items']['items']['type'] == 'string':
                                property_type = 'List[str]'
                            elif property_schema['items']['items']['type'] == 'number':
                                property_type = 'List[float]'
                            else:
                                print("  property: ", property_schema)
                                raise Exception("Unknown property type")
                        else:
                            print("  property: ", property_schema)
                            raise Exception("Unknown property type")
                    else:
                        print("  property: ", property_schema)
                        raise Exception("Unknown property type")
                else:
                    print("  array: ", [property_schema])
                    print("  array: ", [property_schema['items']])
                    raise Exception("Unknown array type")

            f.write(
                "\t\t" +
                property_name +
                ": Union[Unset, List[" +
                property_type +
                "]] = UNSET\n")
            f.write(
                "\t\tif not isinstance(self." +
                property_name +
                ", Unset):\n")
            f.write(
                "\t\t\t" +
                property_name +
                " = self." +
                property_name +
                "\n")
        else:
            f.write(
                "\t\t" +
                property_name +
                " = self." +
                property_name +
                "\n")
    elif '$ref' in property_schema:
        ref = property_schema['$ref'].replace(
            '#/components/schemas/', '')
        f.write(
            "\t\t" +
            property_name +
            ": Union[Unset, str] = UNSET\n")
        f.write(
            "\t\tif not isinstance(self." +
            property_name +
            ", Unset):\n")
        f.write(
            "\t\t\t" +
            property_name +
            " = self." +
            property_name +
            ".value\n")
    elif 'allOf' in property_schema:
        thing = property_schema['allOf'][0]
        if '$ref' in thing:
            ref = thing['$ref'].replace(
                '#/components/schemas/', '')
            if ref == "Uuid":
                return renderTypeToDict(
                    f, property_name, data['components']['schemas'][ref], data)
            f.write(
                "\t\t" +
                property_name +
                ": Union[Unset, str] = UNSET\n")
            f.write(
                "\t\tif not isinstance(self." +
                property_name +
                ", Unset):\n")
            f.write(
                "\t\t\t" +
                property_name +
                " = self." +
                property_name +
                ".value\n")
        else:
            raise Exception("  unknown allOf type: ", property_schema)
    else:
        f.write(
            "\t\t" +
            property_name +
            " = self." +
            property_name +
            "\n")


def renderTypeInit(
        f,
    path: str,
        property_name: str,
        property_schema: dict,
        data: dict):
    if 'type' in property_schema:
        property_type = property_schema['type']

        # Write the property.
        if property_type == 'string':
            if 'format' in property_schema:
                if property_schema['format'] == 'date-time' or property_schema['format'] == 'partial-date-time':
                    f.write(
                        "\t" +
                        property_name +
                        ": Union[Unset, datetime.datetime] = UNSET\n")
                    # Return early.
                    return

            f.write(
                "\t" +
                property_name +
                ": Union[Unset, str] = UNSET\n")
        elif property_type == 'object':
            f.write(
                "\t" +
                property_name +
                ": Union[Unset, Any] = UNSET\n")
        elif property_type == 'integer':
            f.write(
                "\t" +
                property_name +
                ":  Union[Unset, int] = UNSET\n")
        elif property_type == 'number':
            f.write(
                "\t" +
                property_name +
                ":  Union[Unset, float] = UNSET\n")
        elif property_type == 'boolean':
            f.write(
                "\t" +
                property_name +
                ": Union[Unset, bool] = False\n")
        elif property_type == 'array':
            if 'items' in property_schema:
                if '$ref' in property_schema['items']:
                    property_type = property_schema['items']['$ref']
                    property_type = property_type.replace(
                        '#/components/schemas/', '')
                    f.write(
                        "\tfrom ..models." +
                        camel_to_snake(property_type) +
                        " import " +
                        property_type +
                        "\n")
                elif 'type' in property_schema['items']:
                    if property_schema['items']['type'] == 'string':
                        property_type = 'str'
                    elif property_schema['items']['type'] == 'number':
                        property_type = 'float'
                    elif property_schema['items']['type'] == 'array':
                        if 'items' in property_schema['items']:
                            if property_schema['items']['items']['type'] == 'string':
                                property_type = 'List[str]'
                            elif property_schema['items']['items']['type'] == 'number':
                                property_type = 'List[float]'
                            else:
                                print("  property: ", property_schema)
                                raise Exception("Unknown property type")
                        else:
                            print("  property: ", property_schema)
                            raise Exception("Unknown property type")
                    else:
                        print("  property: ", property_schema)
                        raise Exception("Unknown property type")
                else:
                    print("  array: ", [property_schema])
                    print("  array: ", [property_schema['items']])
                    raise Exception("Unknown array type")

                f.write(
                    "\t" +
                    property_name +
                    ": Union[Unset, List[" +
                    property_type +
                    "]] = UNSET\n")
            else:
                raise Exception("Unknown array type")
        else:
            print("  property type: ", property_type)
            raise Exception("  unknown type: ", property_type)
    elif '$ref' in property_schema:
        ref = property_schema['$ref'].replace(
            '#/components/schemas/', '')
        f.write(
            "\t" +
            property_name +
            ": Union[Unset, " +
            ref +
            "] = UNSET\n")
    elif 'allOf' in property_schema:
        thing = property_schema['allOf'][0]
        if '$ref' in thing:
            ref = thing['$ref'].replace(
                '#/components/schemas/', '')
            if ref == "Uuid":
                return renderTypeInit(
                    f,
                    path,
                    property_name,
                    data['components']['schemas'][ref],
                    data)
            f.write(
                "\t" +
                property_name +
                ": Union[Unset, " +
                ref +
                "] = UNSET\n")
        else:
            raise Exception("  unknown allOf type: ", property_schema)
    else:
        f.write(
            "\t" +
            property_name +
            ": Union[Unset, Any] = UNSET\n")


def renderTypeFromDict(
        f,
        property_name: str,
        property_schema: dict,
        data: dict):
    if 'type' in property_schema:
        property_type = property_schema['type']

        # Write the property.
        if property_type == 'string':
            if 'format' in property_schema:
                if property_schema['format'] == 'date-time' or property_schema['format'] == 'partial-date-time':
                    f.write(
                        "\t\t_" +
                        property_name +
                        " = d.pop(\"" +
                        property_name +
                        "\", UNSET)\n")
                    f.write(
                        "\t\t" +
                        property_name +
                        ": Union[Unset, datetime.datetime]\n")
                    f.write(
                        "\t\tif isinstance(_" + property_name + ", Unset):\n")
                    f.write("\t\t\t" + property_name + " = UNSET\n")
                    f.write("\t\telse:\n")
                    f.write("\t\t\t" + property_name +
                            " = isoparse(_" + property_name + ")\n")
                    f.write("\n")
                    # Return early.
                    return

            f.write(
                "\t\t" +
                property_name +
                " = d.pop(\"" +
                property_name +
                "\", UNSET)\n")
            f.write("\n")
        elif property_type == 'integer':
            f.write(
                "\t\t" +
                property_name +
                " = d.pop(\"" +
                property_name +
                "\", UNSET)\n")
            f.write("\n")
        elif property_type == 'number':
            f.write(
                "\t\t" +
                property_name +
                " = d.pop(\"" +
                property_name +
                "\", UNSET)\n")
            f.write("\n")
        elif property_type == 'boolean':
            f.write(
                "\t\t" +
                property_name +
                " = d.pop(\"" +
                property_name +
                "\", UNSET)\n")
            f.write("\n")
        elif property_type == 'array':
            if 'items' in property_schema:
                if '$ref' in property_schema['items']:
                    property_type = property_schema['items']['$ref']
                    property_type = property_type.replace(
                        '#/components/schemas/', '')
                    f.write(
                        "\t\tfrom ..models." +
                        camel_to_snake(property_type) +
                        " import " +
                        property_type +
                        "\n")
                elif 'type' in property_schema['items']:
                    if property_schema['items']['type'] == 'string':
                        property_type = 'str'
                    elif property_schema['items']['type'] == 'number':
                        property_type = 'float'
                    elif property_schema['items']['type'] == 'array':
                        if 'items' in property_schema['items']:
                            if property_schema['items']['items']['type'] == 'string':
                                property_type = 'List[str]'
                            elif property_schema['items']['items']['type'] == 'number':
                                property_type = 'List[float]'
                            else:
                                print("  property: ", property_schema)
                                raise Exception("Unknown property type")
                        else:
                            print("  property: ", property_schema)
                            raise Exception("Unknown property type")
                    else:
                        raise Exception(
                            "  unknown array type: ",
                            property_schema['items']['type'])
                else:
                    print("  array: ", [property_schema])
                    print("  array: ", [property_schema['items']])
                    raise Exception("Unknown array type")

            f.write(
                "\t\t" +
                property_name +
                " = cast(List[" + property_type + "], d.pop(\"" +
                property_name +
                "\", UNSET))\n")
            f.write("\n")
        else:
            f.write(
                "\t\t" +
                property_name +
                " = d.pop(\"" +
                property_name +
                "\", UNSET)\n")
    elif '$ref' in property_schema:
        ref = property_schema['$ref'].replace(
            '#/components/schemas/', '')
        f.write(
            "\t\t_" +
            property_name +
            " = d.pop(\"" +
            property_name +
            "\", UNSET)\n")
        f.write("\t\t" + property_name +
                ": Union[Unset, " + ref + "]\n")
        f.write(
            "\t\tif isinstance(_" +
            property_name +
            ", Unset):\n")
        f.write("\t\t\t" + property_name + " = UNSET\n")
        f.write("\t\telse:\n")
        f.write("\t\t\t" + property_name + " = " +
                ref + "(_" + property_name + ")\n")
        f.write("\n")
    elif 'allOf' in property_schema:
        thing = property_schema['allOf'][0]
        if '$ref' in thing:
            ref = thing['$ref'].replace(
                '#/components/schemas/', '')
            if ref == "Uuid":
                return renderTypeFromDict(
                    f, property_name, data['components']['schemas'][ref], data)
            f.write(
                "\t\t_" +
                property_name +
                " = d.pop(\"" +
                property_name +
                "\", UNSET)\n")
            f.write("\t\t" + property_name +
                    ": Union[Unset, " + ref + "]\n")
            f.write(
                "\t\tif isinstance(_" +
                property_name +
                ", Unset):\n")
            f.write("\t\t\t" + property_name + " = UNSET\n")
            f.write("\t\telse:\n")
            f.write("\t\t\t" + property_name + " = " +
                    ref + "(_" + property_name + ")\n")
            f.write("\n")
        else:
            raise Exception("  unknown allOf type: ", property_schema)
    else:
        f.write(
            "\t\t" +
            property_name +
            " = d.pop(\"" +
            property_name +
            "\", UNSET)\n")


def hasDateTime(schema: dict) -> bool:
    # Generate the type.
    if 'type' in schema:
        type_name = schema['type']
        if type_name == 'object':
            # Iternate over the properties.
            if 'properties' in schema:
                for property_name in schema['properties']:
                    property_schema = schema['properties'][property_name]
                    has_date_time = hasDateTime(property_schema)
                    if has_date_time:
                        return True
        elif type_name == 'string' and 'format' in schema:
            if schema['format'] == 'date-time' or schema['format'] == 'partial-date-time':
                return True

    return False


def getRefs(schema: dict) -> [str]:
    refs = []
    if '$ref' in schema:
        refs.append(schema['$ref'].replace('#/components/schemas/', ''))

    else:
        # Generate the type.
        if 'type' not in schema:
            if 'allOf' in schema:
                for sub_schema in schema['allOf']:
                    refs.extend(getRefs(sub_schema))
        else:
            type_name = schema['type']
            if type_name == 'object':
                if 'properties' in schema:
                    # Iternate over the properties.
                    for property_name in schema['properties']:
                        property_schema = schema['properties'][property_name]
                        schema_refs = getRefs(property_schema)
                        for ref in schema_refs:
                            if ref not in refs:
                                refs.append(ref)
                elif 'additionalProperties' in schema:
                    schema_refs = getRefs(schema['additionalProperties'])
                    for ref in schema_refs:
                        if ref not in refs:
                            refs.append(ref)
                else:
                    print("  unsupported type: ", schema)
                    raise Exception("  unsupported type: ", schema)

    return refs


def getEndpointRefs(endpoint: dict, data: dict) -> [str]:
    refs = []

    responses = endpoint['responses']
    for response_code in responses:
        response = responses[response_code]
        if 'content' in response:
            content = response['content']
            for content_type in content:
                if content_type == 'application/json':
                    json = content[content_type]['schema']
                    if '$ref' in json:
                        # If the reference is to a oneOf type, we want to return
                        # all the possible outcomes.
                        ref = json['$ref'].replace(
                            '#/components/schemas/', '')
                        schema = data['components']['schemas'][ref]
                        if 'oneOf' in schema:
                            for t in schema['oneOf']:
                                ref = getOneOfRefType(t)
                                if ref not in refs:
                                    refs.append(ref)
                        else:
                            if ref not in refs:
                                refs.append(ref)
                    elif 'type' in json:
                        if json['type'] == 'array':
                            items = json['items']
                            if '$ref' in items:
                                ref = items['$ref'].replace(
                                    '#/components/schemas/', '')
                                refs.append('[' + ref + ']')
                            else:
                                raise Exception("Unknown array type")
                        elif json['type'] == 'string':
                            refs.append('str')
                        else:
                            raise Exception("Unknown type ", json['type'])
                    else:
                        refs.append('dict')
                elif content_type == '*/*':
                    s = content[content_type]['schema']
                    if s == {}:
                        # We don't care it's an empty body.
                        continue
                    else:
                        # Throw an error for an unsupported content type.
                        print("content: ", content)
                        raise Exception(
                            "Unsupported content type: ", content_type)
                else:
                    # Throw an error for an unsupported content type.
                    print("content: ", content)
                    raise Exception("Unsupported content type: ", content_type)
        elif '$ref' in response:
            schema_name = response['$ref'].replace(
                '#/components/responses/', '')
            schema = data['components']['responses'][schema_name]
            if 'content' in schema:
                content = schema['content']
                for content_type in content:
                    if content_type == 'application/json':
                        json = content[content_type]['schema']
                        if '$ref' in json:
                            ref = json['$ref'].replace(
                                '#/components/schemas/', '')
                            if ref not in refs:
                                refs.append(ref)

    return refs


def getParameterRefs(endpoint: dict) -> [str]:
    refs = []

    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            if '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
                refs.append(parameter_type)

    return refs


def getRequestBodyRefs(endpoint: dict) -> [str]:
    refs = []

    if 'requestBody' in endpoint:
        requestBody = endpoint['requestBody']
        if 'content' in requestBody:
            content = requestBody['content']
            for content_type in content:
                if content_type == 'application/json':
                    json = content[content_type]['schema']
                    if '$ref' in json:
                        ref = json['$ref'].replace('#/components/schemas/', '')
                        refs.append(ref)
                elif content_type == 'application/octet-stream':
                    # do nothing we dont't care
                    continue
                elif content_type == 'application/x-www-form-urlencoded':
                    form = content[content_type]['schema']
                    if '$ref' in form:
                        ref = form['$ref'].replace('#/components/schemas/', '')
                        refs.append(ref)
                else:
                    # Throw an error for an unsupported content type.
                    print("content: ", content)
                    raise Exception("Unsupported content type: ", content_type)

    return refs


def getRequestBodyType(endpoint: dict) -> str:
    type_name = None

    if 'requestBody' in endpoint:
        requestBody = endpoint['requestBody']
        if 'content' in requestBody:
            content = requestBody['content']
            for content_type in content:
                if content_type == 'application/json':
                    json = content[content_type]['schema']
                    if '$ref' in json:
                        ref = json['$ref'].replace('#/components/schemas/', '')
                        return ref
                elif content_type == 'text/plain':
                    return 'bytes'
                elif content_type == 'application/octet-stream':
                    return 'bytes'
                elif content_type == 'application/x-www-form-urlencoded':
                    json = content[content_type]['schema']
                    if '$ref' in json:
                        ref = json['$ref'].replace('#/components/schemas/', '')
                        return ref
                else:
                    print("  unsupported content type: ", content_type)
                    raise Exception("unsupported content type")

    return type_name


def camel_to_snake(name: str):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(
        '([a-z0-9])([A-Z])',
        r'\1_\2',
        name).lower().replace(
        '-',
        '_')


def camel_to_screaming_snake(name: str):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(
        '([a-z0-9])([A-Z])',
        r'\1_\2',
        name).replace(
        ' ',
        '').upper().replace(
            '-',
        '_').replace(
            ':',
        '_')


def get_function_parameters(endpoint: dict, request_body_type: bool) -> [str]:
    params = []
    if 'parameters' in endpoint:
        parameters = endpoint['parameters']
        for parameter in parameters:
            parameter_name = parameter['name']
            if 'type' in parameter['schema']:
                parameter_type = parameter['schema']['type'].replace(
                    'string', 'str').replace(
                    'integer', 'int').replace(
                    'number', 'float')
            elif '$ref' in parameter['schema']:
                parameter_type = parameter['schema']['$ref'].replace(
                    '#/components/schemas/', '')
            else:
                print("  parameter: ", parameter)
                raise Exception("Unknown parameter type")
            params.append(camel_to_snake(parameter_name))
    if request_body_type:
        params.append("body")
    return params


def getOneOfRefType(schema: dict) -> str:
    if 'type' in schema['properties']:
        t = schema['properties']['type']['enum'][0]
        return t

    raise Exception("Cannot get oneOf ref type for schema: ", schema)


if (__name__ == '__main__'):
    exit_code = main()
    exit(exit_code)
