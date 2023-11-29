import json
import os
import uuid
from typing import Optional, Union, cast

import pytest

from .api.api_tokens import list_api_tokens_for_user
from .api.file import create_file_conversion, create_file_mass, create_file_volume
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
    FailureWebSocketResponse,
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
    SuccessWebSocketResponse,
    System,
    UnitDensity,
    UnitLength,
    UnitMass,
    UnitVolume,
    User,
    WebSocketRequest,
)
from .models.input_format import obj
from .models.modeling_cmd import (
    default_camera_focus_on,
    import_files,
    start_path,
    take_snapshot,
)
from .models.ok_web_socket_response_data import modeling
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
        assert len(value) > 0


@pytest.mark.asyncio
async def test_file_convert_stl_async():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Optional[
        Union[FileConversion, Error]
    ] = await create_file_conversion.asyncio(
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
        assert len(value) > 0


@pytest.mark.asyncio
async def test_file_convert_obj_async():
    # Create our client.
    client = ClientFromEnv()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../assets/ORIGINALVOXEL-3.obj"), "rb")
    content = file.read()
    file.close()

    # Get the fc.
    result: Optional[
        Union[FileConversion, Error]
    ] = await create_file_conversion.asyncio(
        client=client,
        body=content,
        src_format=FileImportFormat.OBJ,
        output_format=FileExportFormat.STL,
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
        assert len(value) > 0


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


def test_list_users():
    # Create our client.
    client = ClientFromEnv()

    response: Union[ExtendedUserResultsPage, Error, None] = list_users_extended.sync(
        sort_by=CreatedAtSortMode.CREATED_AT_DESCENDING, client=client, limit=10
    )

    assert isinstance(response, ExtendedUserResultsPage)

    print(f"ExtendedUserResultsPage: {response}")


def test_ws():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    with modeling_commands_ws.WebSocket(
        client=client,
        fps=30,
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
                                units=UnitLength.MM,
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
        message = websocket.recv()
        if isinstance(message, FailureWebSocketResponse):
            raise Exception(message)
        elif isinstance(message, SuccessWebSocketResponse):
            response = cast(SuccessWebSocketResponse, message)
            resp = cast(modeling, response.resp)
            print(json.dumps(resp.model_dump_json()))
        # Get the object id from the response.
        # TODO: FIX
        object_id = uuid.uuid4()

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
        message = websocket.recv()
        print(json.dumps(message.model_dump_json()))

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
