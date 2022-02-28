#!/usr/bin/env python3
from openapi_parser.parser.loader import OpenApiParser

import os

package_name = 'kittycad'

def main():
    cwd = os.getcwd()
    path = os.path.join(cwd, 'spec.json')
    print("opening spec file: ", path)
    parser = OpenApiParser.open(path)
    # Ignore the security definitions.
    parser.load_metadata()
    parser.load_schemas()
    parser.load_path_items()

    # Generate the types.
    generateTypes(cwd, parser)

    print([parser])

def generateTypes(cwd: str, parser: OpenApiParser):
    # Make sure we have the directory.
    path = os.path.join(cwd, 'kittycad', 'models')
    os.makedirs(path, exist_ok=True)

    # Generate the types.
    data = parser.data
    schemas = data['components']['schemas']
    for key in schemas:
        schema = schemas[key]
        print(key)


if (__name__ == '__main__'):
    exit_code = main()
    exit(exit_code)
