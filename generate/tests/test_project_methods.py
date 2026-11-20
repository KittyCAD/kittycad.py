"""Exercise generated project uploads and downloads against the HTTP contract."""

import json
from email import policy
from email.parser import BytesParser
from io import BytesIO
from pathlib import Path
from typing import Any

import httpx
import pytest

from kittycad import AsyncKittyCAD, KittyCAD, _multipart as multipart_helpers
from kittycad.exceptions import (
    KittyCADAPIError,
    KittyCADClientError,
    KittyCADServerError,
)
from kittycad.models import (
    CreateProjectRequest,
    CreateProjectVersionRequest,
    ProjectArchiveFormat,
    UpdateProjectRequest,
    Uuid,
)

ID = Uuid("00000000-0000-4000-8000-000000000001")
VERSION = Uuid("00000000-0000-4000-8000-000000000002")
FILE_IDS = [str(ID), str(VERSION)]
UPLOADS = ["create_project", "update_project", "create_project_version"]
DOWNLOADS = [
    ("projects", "download_project", (ID,), f"/user/projects/{ID}/download"),
    (
        "projects",
        "download_project_version",
        (ID, VERSION),
        f"/user/projects/{ID}/versions/{VERSION}/download",
    ),
    ("projects", "download_public_project", (ID,), f"/projects/public/{ID}/download"),
    (
        "hidden",
        "download_shared_project",
        ("share-key",),
        "/projects/shared/share-key/download",
    ),
]
PROJECT = {
    "id": str(ID),
    "title": "Bracket",
    "description": "",
    "entrypoint_path": "main.kcl",
    "project_toml_path": "project.toml",
    "category_ids": [],
    "files": [],
    "revision": str(VERSION),
    "metadata_revision": "metadata-1",
    "preview_status": "pending",
    "publication_status": "private",
    "publication": {"has_unpublished_changes": False},
    "access": {
        "can_delete": True,
        "can_edit": True,
        "can_manage_organization": False,
        "scope": "personal",
    },
    "created_at": "2026-11-20T00:00:00Z",
    "updated_at": "2026-11-20T00:00:00Z",
}


def upload_arguments(operation: str, files: dict) -> dict[str, Any]:
    if operation == "create_project_version":
        return {
            "id": ID,
            "body": CreateProjectVersionRequest(
                title="Bracket", parent_version_id=VERSION
            ),
            "file_attachments": files,
            "idempotency_key": "save-1",
        }
    body = (
        CreateProjectRequest(title="Bracket")
        if operation == "create_project"
        else UpdateProjectRequest(
            title="Bracket", expected_revision=str(VERSION), deleted_paths=[]
        )
    )
    return {
        **({"id": ID} if operation == "update_project" else {}),
        "body": body,
        "file_attachments": files,
    }


@pytest.fixture
def prepared_files(monkeypatch):
    opened = []
    original = multipart_helpers.prepare_upload_input

    def prepare(*args, **kwargs):
        result = original(*args, **kwargs)
        opened.append((result[0], result[1]))
        return result

    monkeypatch.setattr(multipart_helpers, "prepare_upload_input", prepare)
    return opened


@pytest.mark.parametrize("operation", UPLOADS)
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_project_upload(
    operation: str, asynchronous: bool, tmp_path: Path, prepared_files
):
    disk_file = tmp_path / "original.kcl"
    disk_file.write_bytes(b"// disk file")
    stream = BytesIO(b"// stream file")
    contents = {
        "main.kcl": b"// main",
        "parts/helper.kcl": b"// stream file",
        'renamed"file.kcl': b"// disk file",
        "body": b"// file named body",
        "event": b"// file named event",
        'part"v1.kcl': b"// quoted filename",
        "part%22v1.kcl": b"// literal percent filename",
        "零件/café.kcl": b"// unicode filename",
        'parts/quoted";file.kcl': b"// nested quoted filename",
    }
    files: dict[str, Any] = dict(contents)
    files["parts/helper.kcl"] = stream
    files['renamed"file.kcl'] = disk_file
    arguments = upload_arguments(operation, files)
    calls = []

    def handle(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        assert request.method == ("PUT" if operation == "update_project" else "POST")
        expected_path = "/user/projects"
        if operation != "create_project":
            expected_path += f"/{ID}"
        if operation == "create_project_version":
            expected_path += "/versions"
            assert request.headers.get_list("Idempotency-Key") == ["save-1"]
        assert request.url.path == expected_path
        assert request.headers["Authorization"] == "Bearer caller"
        assert request.headers["Content-Type"].startswith(
            "multipart/form-data; boundary="
        )
        message = BytesParser(policy=policy.default).parsebytes(
            b"Content-Type: "
            + request.headers["Content-Type"].encode()
            + b"\r\n\r\n"
            + request.content
        )
        parts = list(message.iter_parts())
        assert parts[0].get_param("name", header="Content-Disposition") == "body"
        assert parts[0].get_filename() is None
        assert parts[0].get_content_type() == "application/json"
        metadata = parts[0].get_payload(decode=True)
        assert isinstance(metadata, bytes)
        assert json.loads(metadata) == arguments["body"].to_dict()
        assert len(parts) == len(contents) + 1
        assert all(
            p.get_param("name", header="Content-Disposition") == "files"
            for p in parts[1:]
        )
        assert {
            p.get_filename(): p.get_payload(decode=True) for p in parts[1:]
        } == contents
        assert b'filename="part\\"v1.kcl"\r\n' in request.content
        assert b'filename="part%22v1.kcl"\r\n' in request.content
        if operation == "create_project_version":
            return httpx.Response(
                200, json={"version_id": VERSION, "current_version_id": ID}
            )
        return httpx.Response(
            201 if operation == "create_project" else 200, json=PROJECT
        )

    options: dict[str, Any] = {
        "token": "caller",
        "headers": {"content-type": "application/json", "idempotency-key": "default"},
    }
    transport = httpx.MockTransport(handle)
    sdk: Any
    if asynchronous:
        async with AsyncKittyCAD(
            **options, http_client=httpx.AsyncClient(transport=transport)
        ) as sdk:
            result = await getattr(sdk.projects, operation)(**arguments)
    else:
        with KittyCAD(**options, http_client=httpx.Client(transport=transport)) as sdk:
            result = getattr(sdk.projects, operation)(**arguments)
    assert len(calls) == 1
    assert (
        result.version_id if operation == "create_project_version" else result.id
    ) == (VERSION if operation == "create_project_version" else ID)
    assert not stream.closed
    assert all(file.closed for file, owned in prepared_files if owned)


@pytest.mark.parametrize("operation", UPLOADS)
@pytest.mark.parametrize(
    "files,message",
    [
        ({}, "At least one file attachment"),
        ({"bad\r\nname.kcl": b"bad"}, "control characters"),
        ({"bad\x00name.kcl": b"bad"}, "control characters"),
        ({"bad\x7fname.kcl": b"bad"}, "control characters"),
    ],
)
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_project_upload_rejects_invalid_attachments(
    operation, files, message, asynchronous, prepared_files
):
    def handle(request):
        pytest.fail("Invalid attachments should fail before an HTTP request")

    arguments = upload_arguments(operation, files)
    transport = httpx.MockTransport(handle)
    sdk: Any
    if asynchronous:
        async with AsyncKittyCAD(
            token="caller", http_client=httpx.AsyncClient(transport=transport)
        ) as sdk:
            with pytest.raises(ValueError, match=message):
                await getattr(sdk.projects, operation)(**arguments)
    else:
        with KittyCAD(
            token="caller", http_client=httpx.Client(transport=transport)
        ) as sdk:
            with pytest.raises(ValueError, match=message):
                getattr(sdk.projects, operation)(**arguments)
    assert not prepared_files


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_project_upload_cleans_up_on_transport_error(
    asynchronous, tmp_path, prepared_files
):
    path = tmp_path / "main.kcl"
    path.write_bytes(b"// main")
    stream = BytesIO(b"// borrowed stream")
    arguments = upload_arguments("update_project", {"main.kcl": path, "body": stream})

    def handle(request):
        raise httpx.WriteError("Upload interrupted", request=request)

    transport = httpx.MockTransport(handle)
    sdk: Any
    if asynchronous:
        async with AsyncKittyCAD(
            token="caller", http_client=httpx.AsyncClient(transport=transport)
        ) as sdk:
            with pytest.raises(httpx.WriteError, match="Upload interrupted"):
                await sdk.projects.update_project(**arguments)
    else:
        with KittyCAD(
            token="caller", http_client=httpx.Client(transport=transport)
        ) as sdk:
            with pytest.raises(httpx.WriteError, match="Upload interrupted"):
                sdk.projects.update_project(**arguments)
    assert any(owned for _, owned in prepared_files)
    assert all(file.closed for file, owned in prepared_files if owned)
    assert not stream.closed


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_project_upload_streams_large_files(asynchronous):
    content = b"x" * (3 * 64 * 1024 + 17)
    reads = []

    class TrackedFile(BytesIO):
        def read(self, size=-1):
            assert 0 < size <= 64 * 1024
            reads.append(size)
            return super().read(size)

    stream = TrackedFile(content)
    chunks = []

    class Transport(httpx.BaseTransport, httpx.AsyncBaseTransport):
        def handle_request(self, request):
            assert reads == [512]  # MIME sniffing is the only read before sending.
            assert request.headers["Transfer-Encoding"] == "chunked"
            assert "Content-Length" not in request.headers
            chunks.extend(request.stream)
            return httpx.Response(200, json=PROJECT)

        async def handle_async_request(self, request):
            assert reads == [512]
            assert request.headers["Transfer-Encoding"] == "chunked"
            assert "Content-Length" not in request.headers
            async for chunk in request.stream:
                chunks.append(chunk)
            return httpx.Response(200, json=PROJECT)

    arguments = upload_arguments("update_project", {'large"file.kcl': stream})
    sdk: Any
    if asynchronous:
        async with AsyncKittyCAD(
            token="caller", http_client=httpx.AsyncClient(transport=Transport())
        ) as sdk:
            await sdk.projects.update_project(**arguments)
    else:
        with KittyCAD(
            token="caller", http_client=httpx.Client(transport=Transport())
        ) as sdk:
            sdk.projects.update_project(**arguments)
    assert chunks.count(b"x" * (64 * 1024)) == 3
    assert b"x" * 17 in chunks
    assert len(b"".join(chunks)) > len(content)
    assert not stream.closed


@pytest.mark.parametrize("group,operation,arguments,path", DOWNLOADS)
@pytest.mark.parametrize(
    "archive_format", [ProjectArchiveFormat.TAR, ProjectArchiveFormat.ZIP]
)
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_project_download(
    group, operation, arguments, path, archive_format, asynchronous
):
    content = b"\x00\xffarchive contents"

    def handle(request):
        assert request.method == "GET"
        assert request.url.path == path
        assert request.url.params["format"] == archive_format.value
        assert request.url.params.get_list("file_ids") == [",".join(FILE_IDS)]
        assert request.headers["Authorization"] == "Bearer caller"
        return httpx.Response(
            200,
            headers={
                "Content-Type": "application/x-tar"
                if archive_format == ProjectArchiveFormat.TAR
                else "application/zip",
                "Content-Disposition": f'attachment; filename="project.{archive_format.value}"',
                "X-Api-Call-Id": "download-1",
            },
            stream=httpx.ByteStream(content),
        )

    transport = httpx.MockTransport(handle)
    sdk: Any
    if asynchronous:
        async with AsyncKittyCAD(
            token="caller", http_client=httpx.AsyncClient(transport=transport)
        ) as sdk:
            download = getattr(getattr(sdk, group), operation)
            async with download(
                *arguments, format=archive_format, file_ids=FILE_IDS
            ) as response:
                assert not response.is_stream_consumed
                assert (
                    b"".join([chunk async for chunk in response.aiter_bytes()])
                    == content
                )
                assert response.headers["X-Api-Call-Id"] == "download-1"
                assert response.headers["Content-Disposition"].endswith(
                    f'.{archive_format.value}"'
                )
    else:
        with KittyCAD(
            token="caller", http_client=httpx.Client(transport=transport)
        ) as sdk:
            download = getattr(getattr(sdk, group), operation)
            with download(
                *arguments, format=archive_format, file_ids=FILE_IDS
            ) as response:
                assert not response.is_stream_consumed
                assert b"".join(response.iter_bytes()) == content
                assert response.headers["X-Api-Call-Id"] == "download-1"
                assert response.headers["Content-Disposition"].endswith(
                    f'.{archive_format.value}"'
                )
    assert response.is_closed


@pytest.mark.parametrize("group,operation,arguments,path", DOWNLOADS)
@pytest.mark.parametrize("status", [400, 404, 500])
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_project_download_errors(
    group, operation, arguments, path, status, asynchronous
):
    responses = []

    def handle(request):
        assert not request.url.params
        response = httpx.Response(
            status,
            headers={"Content-Type": "application/json"},
            stream=httpx.ByteStream(
                json.dumps(
                    {
                        "message": "Selected files unavailable",
                        "error_code": "InvalidProjectFileSelection",
                        "missing_file_ids": FILE_IDS,
                    }
                ).encode()
            ),
        )
        responses.append(response)
        return response

    transport = httpx.MockTransport(handle)
    sdk: Any
    if asynchronous:
        async with AsyncKittyCAD(
            token="caller", http_client=httpx.AsyncClient(transport=transport)
        ) as sdk:
            download = getattr(getattr(sdk, group), operation)
            with pytest.raises(
                KittyCADAPIError, match="Selected files unavailable"
            ) as error:
                async with download(*arguments):
                    pytest.fail("Error responses must not be yielded as archive bytes")
    else:
        with KittyCAD(
            token="caller", http_client=httpx.Client(transport=transport)
        ) as sdk:
            download = getattr(getattr(sdk, group), operation)
            with pytest.raises(
                KittyCADAPIError, match="Selected files unavailable"
            ) as error:
                with download(*arguments):
                    pytest.fail("Error responses must not be yielded as archive bytes")
    assert error.value.status_code == status
    assert isinstance(
        error.value, KittyCADServerError if status >= 500 else KittyCADClientError
    )
    assert error.value.error_code == "InvalidProjectFileSelection"
    assert responses[0].is_closed
