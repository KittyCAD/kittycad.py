import json
import os
import time
import uuid
from typing import Optional, Union

import pytest

from .api.ai import create_text_to_cad, get_text_to_cad_model_for_user
from .api.api_tokens import list_api_tokens_for_user
from .api.file import (
    create_file_center_of_mass,
    create_file_conversion,
    create_file_mass,
    create_file_volume,
)
from .api.meta import ping
from .api.modeling import modeling_commands_ws
from .api.users import get_user_self, list_users_extended
from .client import ClientFromEnv
from .models import (
    ApiCallStatus,
    ApiTokenResultsPage,
    Axis,
    AxisDirectionPair,
    CreatedAtSortMode,
    Direction,
    Error,
    ExtendedUserResultsPage,
    FileCenterOfMass,
    FileConversion,
    FileExportFormat,
    FileImportFormat,
    FileMass,
    FileVolume,
    ImageFormat,
    ImportFile,
    InputFormat,
    ModelingCmd,
    ModelingCmdId,
    Pong,
    PostEffectType,
    System,
    TextToCad,
    TextToCadCreateBody,
    UnitDensity,
    UnitLength,
    UnitMass,
    UnitVolume,
    User,
    WebSocketRequest,
    WebSocketResponse,
)
from .models.input_format import obj
from .models.modeling_cmd import (
    default_camera_focus_on,
    import_files,
    start_path,
    take_snapshot,
)
from .models.web_socket_request import modeling_cmd_req
from .types import Unset


def test_get_session():
    # Create our client.
    client = ClientFromEnv()

    # Get the session.
    session: Union[User, Error, None] = get_user_self.sync(client=client)

    assert isinstance(session, User)

    print(f"Session: {session}")


@pytest.mark.asyncio
async def test_get_api_tokens_async():
    # Create our client.
    client = ClientFromEnv()

    # List API tokens.
    fc: Union[ApiTokenResultsPage, Error, None] = list_api_tokens_for_user.sync(
        client=client, sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING
    )

    assert isinstance(fc, ApiTokenResultsPage)

    print(f"fc: {fc}")


@pytest.mark.asyncio
async def test_get_session_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the session.
    session: Union[User, Error, None] = await get_user_self.asyncio(client=client)

    assert isinstance(session, User)

    print(f"Session: {session}")


def test_ping():
    # Create our client.
    client = ClientFromEnv()

    # Get the message.
    message: Union[Pong, Error, None] = ping.sync(client=client)

    assert isinstance(message, Pong)

    print(f"Message: {message}")


@pytest.mark.asyncio
async def test_ping_async():
    # Create our client.
    client = ClientFromEnv()

    # Get the message.
    message: Union[Pong, Error, None] = await ping.asyncio(client=client)

    assert isinstance(message, Pong)

    print(f"Message: {message}")


def test_file_convert_stl():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Optional[Union[FileConversion, Error]] = create_file_conversion.sync(
        client=client,
        body=content,
        src_format=FileImportFormat.STL,
        output_format=FileExportFormat.OBJ,
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    assert fc.status == ApiCallStatus.COMPLETED

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)
    assert fc.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in fc.outputs.items():
        assert len(value.get_decoded()) > 0


@pytest.mark.asyncio
async def test_file_convert_stl_async():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Optional[Union[FileConversion, Error]] = (
        await create_file_conversion.asyncio(
            client=client,
            body=content,
            src_format=FileImportFormat.STL,
            output_format=FileExportFormat.OBJ,
        )
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    assert fc.status == ApiCallStatus.COMPLETED

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)
    assert fc.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in fc.outputs.items():
        assert len(value.get_decoded()) > 0


@pytest.mark.asyncio
async def test_file_convert_obj_async():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/ORIGINALVOXEL-3.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Optional[Union[FileConversion, Error]] = (
        await create_file_conversion.asyncio(
            client=client,
            body=content,
            src_format=FileImportFormat.OBJ,
            output_format=FileExportFormat.STL,
        )
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    assert fc.status == ApiCallStatus.COMPLETED

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)
    assert fc.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in fc.outputs.items():
        assert len(value.get_decoded()) > 0


def test_file_mass():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Union[FileMass, Error, None] = create_file_mass.sync(
        client=client,
        body=content,
        src_format=FileImportFormat.OBJ,
        material_density=1.0,
        material_density_unit=UnitDensity.KG_M3,
        output_unit=UnitMass.G,
    )

    assert isinstance(result, FileMass)

    fm: FileMass = result

    print(f"FileMass: {fm}")

    assert fm.id is not None
    assert fm.mass is not None

    assert fm.model_dump_json() is not None

    assert fm.status == ApiCallStatus.COMPLETED


def test_file_volume():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Union[FileVolume, Error, None] = create_file_volume.sync(
        client=client,
        body=content,
        src_format=FileImportFormat.OBJ,
        output_unit=UnitVolume.CM3,
    )

    assert isinstance(result, FileVolume)

    fv: FileVolume = result

    print(f"FileVolume: {fv}")

    assert fv.id is not None
    assert fv.volume is not None

    assert fv.model_dump_json() is not None

    assert fv.status == ApiCallStatus.COMPLETED


def test_file_center_of_mass():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Union[FileCenterOfMass, Error, None] = create_file_center_of_mass.sync(
        client=client,
        body=content,
        src_format=FileImportFormat.OBJ,
        output_unit=UnitLength.CM,
    )

    assert isinstance(result, FileCenterOfMass)

    fv: FileCenterOfMass = result

    print(f"FileCenterOfMass: {fv}")

    assert fv.id is not None
    assert fv.center_of_mass is not None

    assert fv.model_dump_json() is not None

    assert fv.status == ApiCallStatus.COMPLETED


def test_list_users():
    # Create our client.
    client = ClientFromEnv()

    response: Union[ExtendedUserResultsPage, Error, None] = list_users_extended.sync(
        sort_by=CreatedAtSortMode.CREATED_AT_DESCENDING, client=client, limit=10
    )

    assert isinstance(response, ExtendedUserResultsPage)

    print(f"ExtendedUserResultsPage: {response}")


def test_ws_simple():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    with modeling_commands_ws.WebSocket(
        client=client,
        fps=30,
        show_grid=False,
        post_effect=PostEffectType.NOEFFECT,
        unlocked_framerate=False,
        video_res_height=360,
        video_res_width=480,
        webrtc=False,
    ) as websocket:
        # Send a message.
        id = uuid.uuid4()
        req = WebSocketRequest(
            modeling_cmd_req(cmd=ModelingCmd(start_path()), cmd_id=ModelingCmdId(id))
        )
        websocket.send(req)

        # Get the messages.
        while True:
            message = websocket.recv()
            print(json.dumps(message.model_dump_json()))
            break


def test_ws_import():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    with modeling_commands_ws.WebSocket(
        client=client,
        fps=30,
        post_effect=PostEffectType.NOEFFECT,
        show_grid=False,
        unlocked_framerate=False,
        video_res_height=360,
        video_res_width=480,
        webrtc=False,
    ) as websocket:
        # read the content of the file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = "ORIGINALVOXEL-3.obj"
        file = open(os.path.join(dir_path, "..", "assets", file_name), "rb")
        content = file.read()
        file.close()
        cmd_id = uuid.uuid4()
        ImportFile(data=content, path=file_name)
        # form the request
        req = WebSocketRequest(
            modeling_cmd_req(
                cmd=ModelingCmd(
                    import_files(
                        files=[ImportFile(data=content, path=file_name)],
                        format=InputFormat(
                            obj(
                                units=UnitLength.M,
                                coords=System(
                                    forward=AxisDirectionPair(
                                        axis=Axis.Y, direction=Direction.NEGATIVE
                                    ),
                                    up=AxisDirectionPair(
                                        axis=Axis.Z, direction=Direction.POSITIVE
                                    ),
                                ),
                            )
                        ),
                    )
                ),
                cmd_id=ModelingCmdId(cmd_id),
            )
        )
        # Import files request must be sent as binary, because the file contents might be binary.
        websocket.send_binary(req)

        # Get the success message.
        object_id = ""
        for message in websocket:
            message_dict = message.model_dump()
            if message_dict["success"] is not True:
                raise Exception(message_dict)
            elif message_dict["resp"]["type"] != "modeling":
                continue
            elif (
                message_dict["resp"]["data"]["modeling_response"]["type"]
                != "import_files"
            ):
                # We have a modeling command response.
                # Make sure its the import files response.
                raise Exception(message_dict)
            else:
                # Okay we have the import files response.
                # Break since now we know it was a success.
                object_id = str(
                    message_dict["resp"]["data"]["modeling_response"]["data"][
                        "object_id"
                    ]
                )
                break

        # Now we want to focus on the object.
        cmd_id = uuid.uuid4()
        # form the request
        req = WebSocketRequest(
            modeling_cmd_req(
                cmd=ModelingCmd(default_camera_focus_on(uuid=object_id)),
                cmd_id=ModelingCmdId(cmd_id),
            )
        )
        websocket.send(req)

        # Get the success message.
        for message in websocket:
            message_dict = message.model_dump()
            if message_dict["success"] is not True:
                raise Exception(message_dict)
            elif message_dict["resp"]["type"] != "modeling":
                continue
            elif message_dict["request_id"] == str(cmd_id):
                # We got a success response for our cmd.
                break
            else:
                raise Exception(message_dict)

        # Now we want to snapshot as a png.
        cmd_id = uuid.uuid4()
        # form the request
        # form the request
        req = WebSocketRequest(
            modeling_cmd_req(
                cmd=ModelingCmd(take_snapshot(format=ImageFormat.PNG)),
                cmd_id=ModelingCmdId(cmd_id),
            )
        )
        websocket.send(req)

        # Get the success message.
        png_contents = b""
        for message in websocket:
            message_dict = message.model_dump()
            if message_dict["success"] is not True:
                raise Exception(message_dict)
            elif message_dict["resp"]["type"] != "modeling":
                continue
            elif (
                message_dict["resp"]["data"]["modeling_response"]["type"]
                != "take_snapshot"
            ):
                # Make sure its the correct response.
                raise Exception(message_dict)
            else:
                # Okay we have the snapshot response.
                # Break since now we know it was a success.
                png_contents = message_dict["resp"]["data"]["modeling_response"][
                    "data"
                ]["contents"].get_decoded()
                break

        # Save the contents to a file.
        png_path = os.path.join(dir_path, "..", "assets", "snapshot.png")
        with open(png_path, "wb") as f:
            f.write(png_contents)

        # Ensure the file is not empty.
        assert len(png_contents) > 0

        # Ensure the file exists.
        assert os.path.exists(png_path)


def test_serialize_deserialize():
    json_str = """{"success":true,"request_id":"16a06065-6ca3-4a96-a042-d0bec6b161a6","resp":{"type":"modeling","data":{"modeling_response":{"type":"import_files","data":{"object_id":"f61ac02e-77bd-468f-858f-fd4141a26acd"}}}}}"""
    d = json.loads(json_str)
    print(d)
    message = WebSocketResponse(**d)
    model_dump = message.model_dump()
    print(model_dump)
    assert model_dump["success"] is True  # type: ignore
    assert model_dump["request_id"] == "16a06065-6ca3-4a96-a042-d0bec6b161a6"  # type: ignore
    assert model_dump["resp"]["type"] == "modeling"  # type: ignore
    assert model_dump["resp"]["data"]["modeling_response"]["type"] == "import_files"  # type: ignore
    assert model_dump["resp"]["data"]["modeling_response"]["data"]["object_id"] == "f61ac02e-77bd-468f-858f-fd4141a26acd"  # type: ignore


def test_text_to_cad():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[TextToCad, Error]] = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.STEP,
        body=TextToCadCreateBody(
            prompt="a 2x4 lego",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: TextToCad = result

    # Poll the api until the status is completed.
    # Timeout after some seconds.
    start_time = time.time()
    while (
        body.status == ApiCallStatus.IN_PROGRESS or body.status == ApiCallStatus.QUEUED
    ) and time.time() - start_time < 120:
        result_status: Optional[Union[TextToCad, Error]] = (
            get_text_to_cad_model_for_user.sync(
                client=client,
                id=body.id,
            )
        )

        if isinstance(result_status, Error) or result_status is None:
            print(result_status)
            raise Exception("Error in response")

        body = result_status

    assert body.status == ApiCallStatus.COMPLETED
