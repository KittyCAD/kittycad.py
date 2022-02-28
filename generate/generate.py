#!/usr/bin/env python3
from openapi_parser.parser.loader import OpenApiParser

import os
import re

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

    # Generate the paths.

def generateTypes(cwd: str, parser: OpenApiParser):
    # Make sure we have the directory.
    path = os.path.join(cwd, 'kittycad', 'models')
    os.makedirs(path, exist_ok=True)

    # Generate the types.
    data = parser.data
    schemas = data['components']['schemas']
    for key in schemas:
        schema = schemas[key]
        generateType(path, key, schema)

def generateType(path: str, name: str, schema: dict):
    # Generate the type.
    file_name = camel_to_snake(name) + '.py'
    file_path = os.path.join(path, file_name)
    type_name = schema['type']
    print("generating type: ", name, " at: ", file_path)
    print("  schema: ", [schema])
    f = open(file_path, "w")
    if type_name == 'object':
        has_date_time = hasDateTime(schema)
        if has_date_time:
            f.write("import datetime\n")
        f.write("from typing import Any, Dict, List, Type, TypeVar, Union\n")
        f.write("\n")
        f.write("import attr\n")
        if has_date_time:
            f.write("from dateutil.parser import isoparse\n")
        f.write("\n")

        refs = getRefs(schema)
        for ref in refs:
            f.write("from ..models."+camel_to_snake(ref)+" import "+ref+"\n")

        f.write("from ..types import UNSET, Unset\n")
        f.write("\n")
        f.write("T = TypeVar(\"T\", bound=\""+name+"\")\n")
        f.write("\n")
        f.write("@attr.s(auto_attribs=True)\n")
        f.write("class "+name+":\n")
        # Write the description.
        f.write("\t\"\"\" \"\"\"\n")
        # Iterate over the properties.
        for property_name in schema['properties']:
            property_schema = schema['properties'][property_name]
            if 'type' in property_schema:
                property_type = property_schema['type']

                # Write the property.
                if property_type == 'string':
                    if 'format' in property_schema:
                        if property_schema['format'] == 'date-time':
                            f.write("\t"+property_name+": Union[Unset, datetime.datetime] = UNSET\n")
                            continue

                    f.write("\t"+property_name+": Union[Unset, str] = UNSET\n")
                elif property_type == 'integer':
                    f.write("\t"+property_name+":  Union[Unset, int] = UNSET\n")
                elif property_type == 'number':
                    f.write("\t"+property_name+":  Union[Unset, float] = UNSET\n")
                elif property_type == 'boolean':
                    f.write("\t"+property_name+": Union[Unset, bool] = False\n")
                else:
                    print("  unknown type: ", property_type)
            elif '$ref' in property_schema:
                ref = property_schema['$ref'].replace('#/components/schemas/', '')
                f.write("\t"+property_name+": Union[Unset, "+ref+"] = UNSET\n")
            else:
                print("  unknown schema: ", property_schema)

        # Finish writing the class.
        f.write("\n")
        f.write("\tadditional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)\n")

        # Now let's write the to_dict method.
        f.write("\n")
        f.write("\tdef to_dict(self) -> Dict[str, Any]:\n")
        # Iternate over the properties.
        for property_name in schema['properties']:
            property_schema = schema['properties'][property_name]
            if 'type' in property_schema:
                property_type = property_schema['type']

                # Write the property.
                if property_type == 'string':
                    if 'format' in property_schema:
                        if property_schema['format'] == 'date-time':
                            f.write("\t\t"+property_name+": Union[Unset, str] = UNSET\n")
                            f.write("\t\tif not isinstance(self."+property_name+", Unset):\n")
                            f.write("\t\t\t"+property_name+" = self."+property_name+".isoformat()\n")
                            continue

                    f.write("\t"+property_name+" = self."+property_name+"\n")
                elif property_type == 'integer':
                    f.write("\t"+property_name+" = self."+property_name+"\n")
                elif property_type == 'number':
                    f.write("\t"+property_name+" = self."+property_name+"\n")
                elif property_type == 'boolean':
                    f.write("\t"+property_name+" = self."+property_name+"\n")
                else:
                    print("  unknown type: ", property_type)
            elif '$ref' in property_schema:
                ref = property_schema['$ref'].replace('#/components/schemas/', '')
                f.write("\t\t"+property_name+": Union[Unset, str] = UNSET\n")
                f.write("\t\tif not isinstance(self."+property_name+", Unset):\n")
                f.write("\t\t\t"+property_name+" = self."+property_name+".value\n")
            else:
                print("  unknown schema: ", property_schema)

        # Finish writing the to_dict method.
        f.write("\n")
        f.write("\t\tfield_dict: Dict[str, Any] = {}\n")
        f.write("\t\tfield_dict.update(self.additional_properties)\n")
        f.write("\t\tfield_dict.update({})\n")


        # Iternate over the properties.
        for property_name in schema['properties']:
            # Write the property.
            f.write("\t\tif "+property_name+" is not UNSET:\n")
            f.write("\t\t\tfield_dict['"+property_name+"'] = "+property_name+"\n")

        f.write("\n")
        f.write("\t\treturn field_dict\n")

        # Now let's write the from_dict method.
        f.write("\n")
        f.write("\t@classmethod\n")
        f.write("\tdef from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:\n")
        f.write("\t\td = src_dict.copy()\n")

        # Iternate over the properties.
        for property_name in schema['properties']:
            property_schema = schema['properties'][property_name]
            if 'type' in property_schema:
                property_type = property_schema['type']

                # Write the property.
                if property_type == 'string':
                    if 'format' in property_schema:
                        if property_schema['format'] == 'date-time':
                            f.write("\t\t_"+property_name+" = d.pop(\"" +property_name+"\", UNSET)\n")
                            f.write("\t\t"+property_name+": Union[Unset, datetime.datetime]\n")
                            f.write("\t\tif not isinstance(_"+property_name+", Unset):\n")
                            f.write("\t\t\t"+property_name+" = UNSET\n")
                            f.write("\t\telse:\n")
                            f.write("\t\t\t"+property_name+" = isoparse(_"+property_name+")\n")
                            f.write("\n")
                            continue

                    f.write("\t"+property_name+" = d.pop(\"" +property_name+"\", UNSET)\n")
                    f.write("\n")
                elif property_type == 'integer':
                    f.write("\t"+property_name+" = d.pop(\"" +property_name+"\", UNSET)\n")
                    f.write("\n")
                elif property_type == 'number':
                    f.write("\t"+property_name+" = d.pop(\"" +property_name+"\", UNSET)\n")
                    f.write("\n")
                elif property_type == 'boolean':
                    f.write("\t"+property_name+" = d.pop(\"" +property_name+"\", UNSET)\n")
                    f.write("\n")
                else:
                    print("  unknown type: ", property_type)
            elif '$ref' in property_schema:
                ref = property_schema['$ref'].replace('#/components/schemas/', '')
                f.write("\t\t_"+property_name+" = d.pop(\"" +property_name+"\", UNSET)\n")
                f.write("\t\t"+property_name+": Union[Unset, "+ref+"]\n")
                f.write("\t\tif not isinstance(_"+property_name+", Unset):\n")
                f.write("\t\t\t"+property_name+" = UNSET\n")
                f.write("\t\telse:\n")
                f.write("\t\t\t"+property_name+" = "+ref+"(_"+property_name+")\n")
                f.write("\n")
            else:
                print("  unknown schema: ", property_schema)

        # Finish writing the from_dict method.
        f.write("\n")
        f.write("\t\t"+camel_to_snake(name)+" = cls(\n")
        # Iternate over the properties.
        for property_name in schema['properties']:
            # Write the property.
            f.write("\t\t\t"+property_name+"= "+property_name+",\n")

        # Close the class.
        f.write("\t\t)\n")
        f.write("\n")
        f.write("\t\t"+camel_to_snake(name)+".additional_properties = d\n")
        f.write("return "+camel_to_snake(name)+"\n")

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
    elif type_name == 'string' and 'enum' in schema:
        f.write("from enum import Enum\n")
        f.write("\n")
        f.write("class "+name+"(str, Enum):\n")
        # Iterate over the properties.
        for value in schema['enum']:
            f.write("\t"+camel_to_screaming_snake(value)+" = '"+value+"'\n")

        # close the enum.
        f.write("\n")
        f.write("\tdef __str__(self) -> str:\n")
        f.write("\t\treturn str(self.value)\n")
    else:
        print("  unsupported type: ", type_name)
        return

def hasDateTime(schema: dict) -> bool:
    # Generate the type.
    if 'type' in schema:
        type_name = schema['type']
        if type_name == 'object':
            # Iternate over the properties.
            for property_name in schema['properties']:
                property_schema = schema['properties'][property_name]
                has_date_time = hasDateTime(property_schema)
                if has_date_time:
                    return True
        elif type_name == 'string' and 'format' in schema:
            if schema['format'] == 'date-time':
                return True

    return False

def getRefs(schema: dict) -> [str]:
    refs = []
    if '$ref' in schema:
        refs.append(schema['$ref'].replace('#/components/schemas/', ''))

    else:
        # Generate the type.
        type_name = schema['type']
        if type_name == 'object':
            # Iternate over the properties.
            for property_name in schema['properties']:
                property_schema = schema['properties'][property_name]
                schema_refs = getRefs(property_schema)
                for ref in schema_refs:
                    if ref not in refs:
                        refs.append(ref)

    return refs


def camel_to_snake(name: str):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def camel_to_screaming_snake(name: str):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).upper()

if (__name__ == '__main__'):
    exit_code = main()
    exit(exit_code)
