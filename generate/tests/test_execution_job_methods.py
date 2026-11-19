"""Exercise the generated execution methods against the HTTP contract."""

import json
from datetime import datetime, timezone
from uuid import uuid4

import httpx
import pytest

from kittycad import AsyncKittyCAD, KittyCAD
from kittycad.exceptions import KittyCADClientError
from kittycad.models import (
    ExecutionInputArtifact,
    ExecutionInputBatch,
    ExecutionJobCreateRequest,
    ExecutionJobResponse,
    Uuid,
)

ID = Uuid(str(uuid4()))
NOW = "2026-11-17T00:00:00Z"
JOB = dict(
    id=ID,
    status="queued",
    runtime_id="cad",
    compute_profile_id="cpu",
    timeout_seconds=60,
    state_version=0,
    active_attempt=0,
    created_at=NOW,
    updated_at=NOW,
)
INPUT = {"id": ID, "byte_length": 4, "sha256": "0" * 64}
BODY = ExecutionJobCreateRequest(
    command=["tool"], compute_profile_id="cpu", runtime_id="cad", timeout_seconds=60
)


def handle(request: httpx.Request) -> httpx.Response:
    assert request.headers["Authorization"] == "Bearer caller"
    path = request.url.path
    if path == "/execution/jobs" and request.method == "POST":
        assert request.headers.get_list("Idempotency-Key") == ["original"]
        assert request.headers["Content-Type"] == "application/json"
        assert json.loads(request.content)["command"] == ["tool"]
        return httpx.Response(201, json=JOB)
    if path == "/execution/jobs":
        if "created_after" in request.url.params:
            assert request.url.params["created_after"] == "2026-11-17T00:00:00+00:00"
        token = request.url.params.get("page_token")
        if token is not None:
            assert token == "a+/=&b"
        items = [] if token else [JOB]
        return httpx.Response(
            200, json={"items": items, "next_page": "a+/=&b" if items else None}
        )
    if path == "/execution/inputs":
        if request.headers["Content-Type"].startswith("multipart/form-data;"):
            assert b'filename="dir/model.step"' in request.content
            return httpx.Response(201, json={"artifacts": [INPUT]})
        assert request.headers["Content-Type"] == "application/octet-stream"
        assert request.content == b"part"
        return httpx.Response(201, json=INPUT)
    if path.endswith("/artifacts"):
        return httpx.Response(
            200,
            json={
                "state": "pending",
                "failure_code": None,
                "artifacts": {"items": [], "next_page": "a+/=&b"},
            },
        )
    if path.endswith(f"/artifacts/{ID}"):
        return httpx.Response(200, stream=httpx.ByteStream(b"\x00\xff"))
    return httpx.Response(
        404, json={"message": "Artifact expired", "request_id": "req-7"}
    )


def test_sync_execution_methods():
    with KittyCAD(
        token="caller",
        headers={"idempotency-key": "default"},
        http_client=httpx.Client(transport=httpx.MockTransport(handle)),
    ) as sdk:
        api = sdk.executor
        assert api.create_execution_job(idempotency_key="original", body=BODY).id == ID
        job: ExecutionJobResponse
        ids: list[Uuid] = []
        for job in api.list_execution_jobs():
            ids.append(job.id)
        assert ids == [ID]
        assert (
            api.list_execution_jobs_page(
                created_after=datetime(2026, 11, 17, tzinfo=timezone.utc)
            ).next_page
            == "a+/=&b"
        )
        assert api.list_execution_job_artifacts(ID).artifacts.next_page == "a+/=&b"
        assert isinstance(
            api.upload_execution_input(iter([b"pa", b"rt"])).root,
            ExecutionInputArtifact,
        )
        assert isinstance(
            api.upload_execution_input({"dir/model.step": b"part"}).root,
            ExecutionInputBatch,
        )
        with api.download_execution_job_artifact(ID, ID) as response:
            assert not response.is_stream_consumed
            assert b"".join(response.iter_bytes()) == b"\x00\xff"
        assert response.is_closed
        with (
            pytest.raises(KittyCADClientError, match="Artifact expired"),
            api.download_execution_job_artifact(ID, Uuid(str(uuid4()))),
        ):
            pytest.fail("an error body must not be yielded as artifact bytes")


@pytest.mark.asyncio
async def test_async_execution_methods():
    async def chunks():
        yield b"pa"
        yield b"rt"

    async with AsyncKittyCAD(
        token="caller",
        headers={"idempotency-key": "default"},
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)),
    ) as sdk:
        api = sdk.executor
        assert (
            await api.create_execution_job(idempotency_key="original", body=BODY)
        ).id == ID
        job: ExecutionJobResponse
        ids: list[Uuid] = []
        async for job in api.list_execution_jobs():
            ids.append(job.id)
        assert ids == [ID]
        assert (await api.list_execution_jobs_page()).next_page == "a+/=&b"
        assert (await api.list_execution_job_artifacts(ID)).state == "pending"
        assert isinstance(
            (await api.upload_execution_input(chunks())).root, ExecutionInputArtifact
        )
        assert isinstance(
            (await api.upload_execution_input({"dir/model.step": b"part"})).root,
            ExecutionInputBatch,
        )
        async with api.download_execution_job_artifact(ID, ID) as response:
            assert not response.is_stream_consumed
            assert (
                b"".join([chunk async for chunk in response.aiter_bytes()])
                == b"\x00\xff"
            )
        assert response.is_closed
        with pytest.raises(KittyCADClientError, match="Artifact expired"):
            async with api.download_execution_job_artifact(ID, Uuid(str(uuid4()))):
                pytest.fail("an error body must not be yielded as artifact bytes")
