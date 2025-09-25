import json
import os
import time
import uuid

import pytest
from websockets.exceptions import ConnectionClosedError

from kittycad import KittyCAD
from kittycad.models import (
    ApiCallStatus,
    Axis,
    AxisDirectionPair,
    ConversionParams,
    CreatedAtSortMode,
    Direction,
    FileCenterOfMass,
    FileConversion,
    FileExportFormat,
    FileImportFormat,
    FileMass,
    FileVolume,
    ImageFormat,
    ImportFile,
    InputFormat3d,
    ModelingCmd,
    ModelingCmdId,
    OutputFormat3d,
    Pong,
    PostEffectType,
    System,
    TextToCadCreateBody,
    UnitDensity,
    UnitLength,
    UnitMass,
    UnitVolume,
    User,
    WebSocketRequest,
    WebSocketResponse,
)
from kittycad.models.input_format3d import OptionObj, OptionStl
from kittycad.models.modeling_cmd import (
    OptionDefaultCameraFocusOn,
    OptionImportFiles,
    OptionStartPath,
    OptionTakeSnapshot,
)
from kittycad.models.output_format3d import OptionObj as OutputOptionObj
from kittycad.models.web_socket_request import OptionModelingCmdReq
from kittycad.types import Unset


def _poll_for_completion(
    client, fc: FileConversion, timeout_seconds: int = 60
) -> FileConversion:
    """Poll for file conversion completion.

    Args:
        client: KittyCAD client (sync or async)
        fc: Initial FileConversion object
        timeout_seconds: Maximum time to wait for completion

    Returns:
        Completed FileConversion object
    """
    import time

    start_time = time.time()

    # Handle both completed and in-progress cases
    if fc.status == ApiCallStatus.COMPLETED:
        # Already completed, no need to poll
        return fc

    # Need to poll for completion
    current_status: ApiCallStatus = fc.status
    body = fc

    while (
        current_status == ApiCallStatus.IN_PROGRESS
        or current_status == ApiCallStatus.QUEUED
        or current_status == ApiCallStatus.UPLOADED
    ) and time.time() - start_time < timeout_seconds:
        time.sleep(2)  # Wait 2 seconds between polls
        result_status = client.api_calls.get_async_operation(id=fc.id)

        # Handle response from get_async_operation
        if isinstance(result_status, dict):
            status_str = result_status.get("status", "unknown")
            print(f"FileConversion status: {status_str}")
            # Convert string status to ApiCallStatus
            if status_str == "completed":
                current_status = ApiCallStatus.COMPLETED
            elif status_str == "failed":
                current_status = ApiCallStatus.FAILED
            elif status_str == "in_progress":
                current_status = ApiCallStatus.IN_PROGRESS
            elif status_str == "queued":
                current_status = ApiCallStatus.QUEUED
            elif status_str == "uploaded":
                current_status = ApiCallStatus.UPLOADED
            else:
                current_status = ApiCallStatus.FAILED  # Default for unknown

            if current_status in [ApiCallStatus.COMPLETED, ApiCallStatus.FAILED]:
                break
        else:
            if hasattr(result_status, "status"):
                current_status = result_status.status
                body = result_status
                print(f"FileConversion status: {current_status}")

    # If we exited the loop due to completion, get the final FileConversion object
    if current_status == ApiCallStatus.COMPLETED:
        # Get the final state of the FileConversion object
        final_result = client.api_calls.get_async_operation(id=fc.id)
        if not isinstance(final_result, dict):
            body = final_result

    return body


async def _poll_for_completion_async(
    client, fc: FileConversion, timeout_seconds: int = 60
) -> FileConversion:
    """Async version of poll for file conversion completion.

    Args:
        client: AsyncKittyCAD client
        fc: Initial FileConversion object
        timeout_seconds: Maximum time to wait for completion

    Returns:
        Completed FileConversion object
    """
    import time

    start_time = time.time()

    # Handle both completed and in-progress cases
    if fc.status == ApiCallStatus.COMPLETED:
        # Already completed, no need to poll
        return fc

    # Need to poll for completion
    current_status: ApiCallStatus = fc.status
    body = fc

    while (
        current_status == ApiCallStatus.IN_PROGRESS
        or current_status == ApiCallStatus.QUEUED
        or current_status == ApiCallStatus.UPLOADED
    ) and time.time() - start_time < timeout_seconds:
        time.sleep(2)  # Wait 2 seconds between polls
        result_status = await client.api_calls.get_async_operation(id=fc.id)

        # Handle response from get_async_operation
        if isinstance(result_status, dict):
            status_str = result_status.get("status", "unknown")
            print(f"FileConversion status: {status_str}")
            # Convert string status to ApiCallStatus
            if status_str == "completed":
                current_status = ApiCallStatus.COMPLETED
            elif status_str == "failed":
                current_status = ApiCallStatus.FAILED
            elif status_str == "in_progress":
                current_status = ApiCallStatus.IN_PROGRESS
            elif status_str == "queued":
                current_status = ApiCallStatus.QUEUED
            elif status_str == "uploaded":
                current_status = ApiCallStatus.UPLOADED
            else:
                current_status = ApiCallStatus.FAILED  # Default for unknown

            if current_status in [ApiCallStatus.COMPLETED, ApiCallStatus.FAILED]:
                break
        else:
            if hasattr(result_status, "status"):
                current_status = result_status.status
                body = result_status
                print(f"FileConversion status: {current_status}")

    # If we exited the loop due to completion, get the final FileConversion object
    if current_status == ApiCallStatus.COMPLETED:
        # Get the final state of the FileConversion object
        final_result = await client.api_calls.get_async_operation(id=fc.id)
        if not isinstance(final_result, dict):
            body = final_result

    return body


def test_get_session():
    # Create our client
    client = KittyCAD()

    # Get the session using modern pattern
    session = client.users.get_user_self()

    assert isinstance(session, User)

    print(f"Session: {session}")


@pytest.mark.asyncio
async def test_get_api_tokens_async():
    # Create our client
    client = KittyCAD()

    # List API tokens using modern pattern
    fc = client.api_tokens.list_api_tokens_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING
    )

    # Now returns SyncPageIterator instead of ApiTokenResultsPage
    from kittycad.pagination import SyncPageIterator

    assert isinstance(fc, SyncPageIterator)

    print(f"fc: {fc}")


@pytest.mark.asyncio
async def test_get_session_async():
    from kittycad import AsyncKittyCAD

    # Create our async client
    client = AsyncKittyCAD()

    # Get the session using new async pattern
    session = await client.users.get_user_self()

    assert isinstance(session, User)

    print(f"Session: {session}")


def test_ping():
    # Create our client
    client = KittyCAD()

    # Get the message using modern pattern (no .api layer)
    message = client.meta.ping()

    assert isinstance(message, Pong)

    print(f"Message: {message}")


@pytest.mark.asyncio
async def test_ping_async():
    from kittycad import AsyncKittyCAD

    # Create our async client
    client = AsyncKittyCAD()

    # Get the message using new async pattern (no .api layer)
    message = await client.meta.ping()

    assert isinstance(message, Pong)

    print(f"Message: {message}")


def test_file_convert_stl():
    # Create our client
    client = KittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the file conversion using modern pattern
    fc = client.file.create_file_conversion(
        body=content,
        src_format=FileImportFormat.STL,
        output_format=FileExportFormat.OBJ,
    )

    assert isinstance(fc, FileConversion)

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    # File conversion might complete immediately or be uploaded for async processing
    assert fc.status in [ApiCallStatus.UPLOADED, ApiCallStatus.COMPLETED]

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)
    assert fc.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in fc.outputs.items():
        assert len(value) > 0


@pytest.mark.asyncio
async def test_file_convert_stl_async():
    from kittycad import AsyncKittyCAD

    # Create our async client
    client = AsyncKittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../../assets/testing.stl"), "rb")
    content = file.read()
    file.close()

    # Get the file conversion using new async pattern
    result = await client.file.create_file_conversion(
        body=content,
        src_format=FileImportFormat.STL,
        output_format=FileExportFormat.OBJ,
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    # File conversion might complete immediately or be uploaded for async processing
    assert fc.status in [ApiCallStatus.UPLOADED, ApiCallStatus.COMPLETED]

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)
    assert fc.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in fc.outputs.items():
        assert len(value) > 0


@pytest.mark.asyncio
async def test_file_convert_obj_async():
    from kittycad import AsyncKittyCAD

    # Create our async client
    client = AsyncKittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../../assets/ORIGINALVOXEL-3.obj"), "rb")
    content = file.read()
    file.close()

    # Get the file conversion using new async pattern
    result = await client.file.create_file_conversion(
        body=content,
        src_format=FileImportFormat.OBJ,
        output_format=FileExportFormat.STL,
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion: {fc}")

    assert fc.id is not None
    # File conversion might complete immediately or be uploaded for async processing
    assert fc.status in [ApiCallStatus.UPLOADED, ApiCallStatus.COMPLETED]

    print(f"FileConversion: {fc}")

    assert not isinstance(fc.outputs, Unset)
    assert fc.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in fc.outputs.items():
        assert len(value) > 0


def test_file_conversion_options_stl():
    # Create our client
    client = KittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "../../assets/testing.stl")

    # Test create_file_conversion_options with the same input file as create_file_conversion
    fc = client.file.create_file_conversion_options(
        body=ConversionParams(
            src_format=InputFormat3d(
                OptionStl(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.NEGATIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Z,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    units=UnitLength.MM,
                )
            ),
            output_format=OutputFormat3d(
                OutputOptionObj(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Z,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    units=UnitLength.MM,
                )
            ),
        ),
        file_attachments={"input.stl": file_path},
    )

    assert isinstance(fc, FileConversion)

    print(f"FileConversion initial: {fc}")

    assert fc.id is not None
    # File conversion might complete immediately or be uploaded for async processing
    assert fc.status in [ApiCallStatus.UPLOADED, ApiCallStatus.COMPLETED]

    # Poll for completion (max 60 seconds)
    body = _poll_for_completion(client, fc, timeout_seconds=60)

    # Check final status
    assert body.status == ApiCallStatus.COMPLETED
    print(f"FileConversion completed: {body}")

    assert not isinstance(body.outputs, Unset)
    assert body.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in body.outputs.items():
        assert len(value) > 0


@pytest.mark.asyncio
async def test_file_conversion_options_stl_async():
    from kittycad import AsyncKittyCAD

    # Create our async client
    client = AsyncKittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "../../assets/testing.stl")

    # Test async create_file_conversion_options with the same input file
    result = await client.file.create_file_conversion_options(
        body=ConversionParams(
            src_format=InputFormat3d(
                OptionStl(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.NEGATIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Z,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    units=UnitLength.MM,
                )
            ),
            output_format=OutputFormat3d(
                OutputOptionObj(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Z,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    units=UnitLength.MM,
                )
            ),
        ),
        file_attachments={"input.stl": file_path},
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion initial: {fc}")

    assert fc.id is not None
    # File conversion might complete immediately or be uploaded for async processing
    assert fc.status in [ApiCallStatus.UPLOADED, ApiCallStatus.COMPLETED]

    # Poll for completion (max 60 seconds)
    body = await _poll_for_completion_async(client, fc, timeout_seconds=60)

    # Check final status
    assert body.status == ApiCallStatus.COMPLETED
    print(f"FileConversion completed: {body}")

    assert not isinstance(body.outputs, Unset)
    assert body.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in body.outputs.items():
        assert len(value) > 0


@pytest.mark.asyncio
async def test_file_conversion_options_obj_async():
    from kittycad import AsyncKittyCAD

    # Create our async client
    client = AsyncKittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "../../assets/ORIGINALVOXEL-3.obj")

    # Test async create_file_conversion_options with OBJ input
    result = await client.file.create_file_conversion_options(
        body=ConversionParams(
            src_format=InputFormat3d(
                OptionObj(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.NEGATIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Z,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    units=UnitLength.M,
                )
            ),
            output_format=OutputFormat3d(
                OutputOptionObj(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Z,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    units=UnitLength.MM,
                )
            ),
        ),
        file_attachments={"input.obj": file_path},
    )

    assert isinstance(result, FileConversion)

    fc: FileConversion = result

    print(f"FileConversion initial: {fc}")

    assert fc.id is not None
    # File conversion might complete immediately or be uploaded for async processing
    assert fc.status in [ApiCallStatus.UPLOADED, ApiCallStatus.COMPLETED]

    # Poll for completion (max 60 seconds)
    body = await _poll_for_completion_async(client, fc, timeout_seconds=60)

    # Check final status
    assert body.status == ApiCallStatus.COMPLETED
    print(f"FileConversion completed: {body}")

    assert not isinstance(body.outputs, Unset)
    assert body.outputs is not None

    # Make sure the bytes are not empty.
    for key, value in body.outputs.items():
        assert len(value) > 0


def test_file_mass():
    # Create our client
    client = KittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the file mass using modern pattern
    fm = client.file.create_file_mass(
        body=content,
        src_format=FileImportFormat.OBJ,
        material_density=1.0,
        material_density_unit=UnitDensity.KG_M3,
        output_unit=UnitMass.G,
    )

    assert isinstance(fm, FileMass)

    print(f"FileMass: {fm}")

    assert fm.id is not None
    assert fm.mass is not None

    assert fm.model_dump_json() is not None

    assert fm.status == ApiCallStatus.COMPLETED


def test_file_volume():
    # Create our client
    client = KittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the file volume using modern pattern
    fv = client.file.create_file_volume(
        body=content,
        src_format=FileImportFormat.OBJ,
        output_unit=UnitVolume.CM3,
    )

    assert isinstance(fv, FileVolume)

    print(f"FileVolume: {fv}")

    assert fv.id is not None
    assert fv.volume is not None

    assert fv.model_dump_json() is not None

    assert fv.status == ApiCallStatus.COMPLETED


def test_file_center_of_mass():
    # Create our client
    client = KittyCAD()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(dir_path, "../../assets/testing.obj"), "rb")
    content = file.read()
    file.close()

    # Get the file center of mass using modern pattern
    fv = client.file.create_file_center_of_mass(
        body=content,
        src_format=FileImportFormat.OBJ,
        output_unit=UnitLength.CM,
    )

    assert isinstance(fv, FileCenterOfMass)

    print(f"FileCenterOfMass: {fv}")

    assert fv.id is not None
    assert fv.center_of_mass is not None

    assert fv.model_dump_json() is not None

    assert fv.status == ApiCallStatus.COMPLETED


def test_list_users():
    # Create our client
    client = KittyCAD()

    # List users using modern pattern
    response = client.users.list_users_extended(
        sort_by=CreatedAtSortMode.CREATED_AT_DESCENDING, limit=10
    )

    # Now returns SyncPageIterator instead of ExtendedUserResultsPage
    from kittycad.pagination import SyncPageIterator

    assert isinstance(response, SyncPageIterator)

    print(f"ExtendedUserResultsPage: {response}")


def test_websocket_recv_timeout_defaults_and_override():
    recorded_connections = []

    class RecordingWS:
        def __init__(self):
            self.recv_calls = []

        def recv(self, timeout=None):
            self.recv_calls.append(timeout)
            return "{}"

        def __iter__(self):
            return iter([])

        def send(self, *_args, **_kwargs):
            return None

        def send_binary(self, *_args, **_kwargs):
            return None

        def close(self):
            return None

    def fake_ws_connect(*_args, **_kwargs):
        ws = RecordingWS()
        recorded_connections.append(ws)
        return ws

    client = KittyCAD(
        token="fake-token",
        base_url="https://example.com",
        websocket_recv_timeout=45.0,
    )

    connection = client.executor.create_executor_term(ws_factory=fake_ws_connect)
    connection.recv()
    assert recorded_connections[-1].recv_calls == [45.0]
    connection.close()

    connection_override = client.executor.create_executor_term(
        recv_timeout=120.0, ws_factory=fake_ws_connect
    )
    connection_override.recv()
    assert recorded_connections[-1].recv_calls == [120.0]
    connection_override.close()


def test_ws_simple():
    # Create our client
    client = KittyCAD()

    # WebSocket uses direct pattern
    with client.modeling.modeling_commands_ws(
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
            OptionModelingCmdReq(
                cmd=ModelingCmd(OptionStartPath()), cmd_id=ModelingCmdId(id)
            )
        )
        websocket.send(req)

        # Get the messages.
        while True:
            message = websocket.recv()
            print(json.dumps(message.model_dump_json()))
            break


def test_ws_import():
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            # Create our client
            client = KittyCAD()

            # WebSocket uses direct pattern
            with client.modeling.modeling_commands_ws(
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
                file_path = os.path.join(dir_path, "../..", "assets", file_name)
                with open(file_path, "rb") as file:
                    content = file.read()
                cmd_id = uuid.uuid4()
                ImportFile(data=content, path=file_name)
                # form the request
                req = WebSocketRequest(
                    OptionModelingCmdReq(
                        cmd=ModelingCmd(
                            OptionImportFiles(
                                files=[ImportFile(data=content, path=file_name)],
                                format=InputFormat3d(
                                    OptionObj(
                                        units=UnitLength.M,
                                        coords=System(
                                            forward=AxisDirectionPair(
                                                axis=Axis.Y,
                                                direction=Direction.NEGATIVE,
                                            ),
                                            up=AxisDirectionPair(
                                                axis=Axis.Z,
                                                direction=Direction.POSITIVE,
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
                    OptionModelingCmdReq(
                        cmd=ModelingCmd(OptionDefaultCameraFocusOn(uuid=object_id)),
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
                req = WebSocketRequest(
                    OptionModelingCmdReq(
                        cmd=ModelingCmd(OptionTakeSnapshot(format=ImageFormat.PNG)),
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
                    elif (
                        message_dict["resp"]["data"]["modeling_response"]["type"]
                        != "take_snapshot"
                    ):
                        # Make sure its the correct response.
                        raise Exception(message_dict)
                    else:
                        # Okay we have the snapshot response.
                        # Break since now we know it was a success.
                        png_contents = message_dict["resp"]["data"][
                            "modeling_response"
                        ]["data"]["contents"]
                        break

                # Save the contents to a file.
                png_path = os.path.join(dir_path, "../..", "assets", "snapshot.png")
                with open(png_path, "wb") as f:
                    f.write(png_contents)

                # Ensure the file is not empty.
                assert len(png_contents) > 0

                # Ensure the file exists.
                assert os.path.exists(png_path)

            # Exit the retry loop on success
            break

        except ConnectionClosedError:
            if attempt < max_retries:
                print(
                    f"ConnectionClosedError encountered on attempt {attempt}/{max_retries}. Retrying..."
                )
            else:
                # After max retries, re-raise the exception to fail the test
                print(
                    f"ConnectionClosedError encountered on attempt {attempt}/{max_retries}. No more retries left."
                )
                raise


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
    assert (
        model_dump["resp"]["data"]["modeling_response"]["data"]["object_id"]
        == "f61ac02e-77bd-468f-858f-fd4141a26acd"
    )  # type: ignore


def test_deserialize_null_request_id():
    json_str = """{"success":true,"request_id":null,"resp":{"type":"modeling_session_data","data":{"session":{"api_call_id":"91f7fd17-8846-4593-97ff-6400a81b8cdd"}}}}"""
    d = json.loads(json_str)
    print(d)
    message = WebSocketResponse(**d)
    model_dump = message.model_dump()
    print(model_dump)
    assert model_dump["success"] is True  # type: ignore
    assert model_dump["success"] is True  # type: ignore
    assert model_dump["request_id"] is None  # type: ignore
    assert model_dump["resp"]["type"] == "modeling_session_data"  # type: ignore
    assert (
        model_dump["resp"]["data"]["session"]["api_call_id"]
        == "91f7fd17-8846-4593-97ff-6400a81b8cdd"
    )  # type: ignore


def test_text_to_cad():
    # Test the modern client.api pattern
    client = KittyCAD()

    # Modern way: client.ml.create_text_to_cad()
    result = client.ml.create_text_to_cad(
        output_format=FileExportFormat.STEP,
        body=TextToCadCreateBody(
            prompt="a 2x4 lego",
        ),
    )
    print(f"Modern result: {result}")

    # Poll the api until the status is completed.
    # Timeout after some seconds.
    start_time = time.time()
    body = result
    while (
        body.status == ApiCallStatus.IN_PROGRESS or body.status == ApiCallStatus.QUEUED
    ) and time.time() - start_time < 120:
        result_status = client.ml.get_text_to_cad_part_for_user(
            id=body.id,
        )

        body = result_status.root  # type: ignore

    assert body.status == ApiCallStatus.COMPLETED
