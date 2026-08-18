# Changelog

All notable changes to the KittyCAD Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v1.5.0

Regenerated the SDK against the latest API spec.

### Added

- **Factory API** — a new `client.factory` group:
  - `POST /user/factory/jobs` (`create_user_factory_job`) returning `FactoryJobResponse` — submit a part for manufacturing.
  - `GET /user/factory/materials` (`get_user_factory_materials`) and `GET /user/factory/finishes` (`get_user_factory_finishes`), both returning `List[FactoryCustomerCatalogOption]`.
- **Pay-as-you-go collection thresholds** on `client.payments`:
  - `get_user_usage_collection_threshold` / `set_user_usage_collection_threshold` / `reset_user_usage_collection_threshold` (`GET`/`PUT`/`DELETE /user/billing/usage-collection-threshold`).
  - `get_org_usage_collection_threshold` / `set_org_usage_collection_threshold` / `reset_org_usage_collection_threshold` (`GET`/`PUT`/`DELETE /org/billing/usage-collection-threshold`).
  - All six return `AggregateUsageCollectionThresholdView`; `set_*` takes an `AggregateUsageCollectionThresholdSet` body and `reset_*` takes `expected_version`. New supporting models: `AggregateUsageCollectionThresholdBounds` and `AggregateUsageCollectionThresholdSource`.
- **Modeling commands & responses**:
  - `begin_execution` / `end_execution` — tell the engine to render in reduced detail while a batch of commands streams in, then restore high quality (`BeginExecution` / `EndExecution`).
  - `create_planar_surface` — build a planar surface bounded by a set of curves (`CreatePlanarSurface`).
  - `sketch_get_info` — sketch debug info (`SketchGetInfo`, plus the new `CurveDebug` / `CurveTypeDebug` models).
- **Edge references in modeling**: `extrude` gained `direction_reference` and `target_reference`, `extrude_to_reference` gained `target_reference`, `sweep` gained `projected_axis`, and `MirrorAcross` gained an `edge_reference` variant — all keyed off `EdgeSpecifier`.
- **STEP import representation**: the `step` variant of `InputFormat3d` gained `target_representation` (`StepImportTargetRepresentation`: `mesh` or `brep`, defaulting to `brep`).
- **ML Copilot**:
  - `MlCopilotMode` gained `zookeeper_pro` and `zookeeper_ultra`.
  - `MlCopilotServerMessage` gained the backend-only variants `ZookeeperOpenAiResponseCheckpoint`, `ZookeeperTurnUsage`, and `ZookeeperRecoveryToolOutput` — these are persisted and replayed only to the text-to-CAD backend, never forwarded to browser clients. New models: `ZookeeperTurnUsage`, `ZookeeperTurnUsageModel`, `ZookeeperTurnUsageStage`.
  - The `User` variant of `MlCopilotClientMessage` gained `correlation_id` and `engine_api_call_id`.
  - `ReasoningMessage` gained `created_project_file`, `updated_project_file`, and `deleted_project_file` for non-KCL project files.
- **Billing & users**:
  - `allow_pay_as_you_go` on `UserResponse`, `ExtendedUser`, and `UpdateUser`.
  - `BlockReason` gained `billing_threshold_reached`, `pay_as_you_go_disabled`, and `admin`.
  - `CustomerBalance` gained `monthly_api_credits_refresh_at`.
  - `ZooProductSubscriptionsUserRequest` gained `downgrade_reason` (`ZooProductSubscriptionDowngradeReason`) and `downgrade_reason_text`.
- **Org datasets**: `list_org_datasets` gained a `lookup_enabled` filter, `list_org_dataset_conversions` gained `q` and `phase`, and `search_org_dataset_conversions` gained `filter` and `phase`. `ConversionSortMode` gained `phase_ascending` / `phase_descending`, `OrgDatasetStatus` gained `paused`, and `OrgDatasetFileConversionStatus` gained `error_execution` / `error_connection`.
- `Feature` — a single enum of environment/rule/override-driven feature switches, replacing `UserFeature`.
- `OAuth2Scope` gained `user:read`.
- `AdjacencyInfo` gained `previous_adjacent_info`.

### Changed

- `UserFeatureEntry.id` is now typed as `Feature` instead of `UserFeature`.
- `OrgDataset` now includes a required `lookup_enabled: bool`.
- Several modeling-command fields are now optional: `target` on `extrude` and `extrude_to_reference` (supply `target_reference` instead), and `edge_id` on `solid3d_get_extrusion_face_info` and `solid3d_get_adjacency_info`.

### Removed

- **The text-to-CAD generation endpoints have been removed**: `create_text_to_cad` (`POST /ai/text-to-cad/{output_format}`), `create_text_to_cad_iteration` (`POST /ml/text-to-cad/iteration`), and `create_text_to_cad_multi_file_iteration` (`POST /ml/text-to-cad/multi-file/iteration`), along with the `TextToCad`, `TextToCadIteration`, and `TextToCadMultiFileIteration` models.
- **`UserFeature` has been removed** in favor of `Feature`.
- **The `enable_dry_run` / `disable_dry_run` modeling commands and their `EnableDryRun` / `DisableDryRun` models have been removed.**
- **`KittyCAD.wait_for_async_operation(...)` and `AsyncKittyCAD.wait_for_async_operation(...)` have been removed.** These were announced in the v1.4.0 notes but were still present in the v1.4.0 code; the removal actually lands here.

### Migration

- **Text-to-CAD generation**: `create_text_to_cad`, `create_text_to_cad_iteration`, and `create_text_to_cad_multi_file_iteration` no longer exist. Generation now runs over the ML Copilot websocket (`client.ml.ml_copilot_ws`); the read-side endpoints (`list_text_to_cad_parts_for_user`, `get_text_to_cad_part_for_user`, `create_text_to_cad_part_feedback`) are unchanged. `TextToCadMultiFileIterationBody` is still exported but no longer has an endpoint that accepts it.
- **Feature flags**: replace `UserFeature` with `Feature`. Member names carry over for the overlapping values (e.g. `PLUGINS`, `MODELING_DIALOGS`, `WEB_APP_FILE_BROWSER`), but `BODIES_PANE` is gone and many new switches were added.
- **Dry-run commands**: remove any `enable_dry_run` / `disable_dry_run` modeling commands; consider `begin_execution` / `end_execution` if you were using them to reduce render cost during bulk execution.
- **Async-operation polling**: replace `wait_for_async_operation(...)` with polling through `client.api_calls.get_async_operation(id=operation_id)`.
- **Constructing `OrgDataset` directly** (e.g. in tests): set `lookup_enabled`. Reading dataset responses from the API requires no change.
- **Known limitation**: `create_user_factory_job` is generated without a body parameter, so it cannot yet send the required `multipart/form-data` payload. Call `POST /user/factory/jobs` directly until the generator supports it.
- All other changes are additive — no action required.

## v1.4.0

Regenerated the SDK against the latest API spec.

### Added

- **Organization skills**: `GET /org/skills` (`list_org_skills`) returning `OrgSkillResponse` — the public skill context available to the caller's organization.
- **Announcements**: `GET /announcements` (`get_announcements`) returning `AnnouncementList` / `Announcement` for announcements broadcast to all clients.
- **ML Copilot attachment-loading flow** (WebSocket):
  - `MlCopilotServerMessage` now includes `RequestAttachments` (backend request for the API to reload client attachments from storage) and `AttachmentsLoaded` (notification that all attachments for a conversation finished loading).
  - `MlCopilotClientMessage` now includes `AttachmentResponse` (`type="attachment_response"`), carrying the attachments returned in response to a `RequestAttachments` message.
- **ML Copilot Zookeeper editing**: `ZookeeperAutoRouterMetadata` (on `MlCopilotServerMessage`) and `ZookeeperEditPatch` / `ZookeeperEditPatchFile` (on `MlToolResult`) for project-edit replay data.
- **Modeling commands & responses**:
  - New `OkModelingCmdResponse` variants: `EdgeGetLength`, `ObjectSetName`, and `RegionGetResolvableIntersectionInfo`.
  - `extrude` now accepts a `DirectionType`, and the edge-cut commands (`solid3d_fillet_edge`, `solid3d_cut_edge_references`, `solid3d_cut_edges`) accept an `EdgeCutVersion` (edge-cut algorithm version).
- **Edge-aware annotations**: `AnnotationBasicDimension`, `AnnotationFeatureControl`, and `AnnotationFeatureTag` can now target edges via `edge_reference` / `from_edge_reference` / `to_edge_reference`, and `AnnotationOptions` gained a `units` field.
- `MlCopilotModeOption` gained a `disabled` field.
- `ProjectPublicationInfoResponse` gained a `feedback` field.

### Changed

- **`create_api_token_for_user` (`POST /user/api-tokens`) now returns `ApiTokenWithFullToken`** instead of `ApiToken`. The new model is a superset that additionally exposes the full, unobfuscated token value.
- `OrgDataset` now includes a required `require_raw_kcl_similarity_score_for_success: bool`; `CreateOrgDataset` and `UpdateOrgDataset` accept it as an optional field.
- `ProjectResponse` and `ProjectSummaryResponse` now include a required `revision` field.
- Annotation models no longer require `entity_id` / `from_entity_id` / `to_entity_id`, now that edges can be referenced instead.

### Removed

- **`GET /orgs/{id}/admin/details` (`org_admin_details_get`) and the `OrgAddress` / `OrgAdminDetails` models have been removed.**
- `KittyCAD.wait_for_async_operation(...)` and `AsyncKittyCAD.wait_for_async_operation(...)` have been removed.

### Migration

- **API tokens**: `create_api_token_for_user` now returns `ApiTokenWithFullToken`. Attribute access is compatible because it is a superset of the old `ApiToken`, but update any explicit `ApiToken` type annotations on the return value.
- **Org admin details**: remove any calls to `org_admin_details_get` and any references to `OrgAddress` / `OrgAdminDetails`; the endpoint and models no longer exist.
- **Async-operation polling**: replace `wait_for_async_operation(...)` with polling through `client.api_calls.get_async_operation(id=operation_id)`.
- **Constructing `OrgDataset` directly** (e.g. in tests): set `require_raw_kcl_similarity_score_for_success`. Reading dataset responses from the API requires no change.
- All other changes are additive — no action required.

## v1.3.2

### Added

- Added ergonomic async-operation polling helpers on the client:
  - `KittyCAD.wait_for_async_operation(operation_id, timeout_seconds=..., poll_interval_seconds=...)`
  - `await AsyncKittyCAD.wait_for_async_operation(operation_id, timeout_seconds=..., poll_interval_seconds=...)`
- These helpers unwrap operation payloads for you and normalize status handling, so callers no longer need to inspect internal `RootModel` wrappers while waiting for completion.

### Fixed

- Fixed async file-conversion test behavior to use a valid conversion pair (`obj` -> `stl`) and stable fixture input.
- Fixed polling behavior in tests to correctly handle `/async/operations/{id}` responses that return wrapped payload models.

### Migration

- No action required. If you currently poll async operation status manually, you can simplify your code by switching to `wait_for_async_operation(...)`.

## v1.2.5

### Added

- WebSocket wrappers now honor configurable receive timeouts. Set a client-wide default with `KittyCAD(..., websocket_recv_timeout=120)` or override per connection via `client.modeling.modeling_commands_ws(recv_timeout=300)`. Existing code keeps the previous 60 second timeout without changes.

### Migration

- No action required unless you wish to change the timeout. If you relied on the old hardcoded 60 second timeout, explicitly pass `recv_timeout=60` to preserve that behavior when using a client configured with a different default.

## v1.1.2

### Changed - WebSocket message typing

- WebSocket wrapper classes now use request/response models from the OpenAPI spec:
  - `ml_copilot_ws` sends `MlCopilotClientMessage` and yields/returns `MlCopilotServerMessage`.
  - `modeling_commands_ws` continues to use `WebSocketRequest`/`WebSocketResponse` per spec.
  - Endpoints without explicit schemas (e.g. `/ws/executor/term`) now default to `Dict[str, Any]`.

### Fixed

- WebSocket wrapper URLs now correctly interpolate path params and append query params (e.g. `ml_reasoning_ws(id=...)`).

### Migration

- If you previously typed your WebSocket code against `WebSocketRequest`/`WebSocketResponse` for ML copilot streams, update to the spec types:
  - `ws.send(MlCopilotClientMessage(...))`
  - `msg: MlCopilotServerMessage = ws.recv()`
  - `for msg in ws: ...` (now yields `MlCopilotServerMessage`)

## v1.1.0

### Added - Enhanced Pydantic Models & Developer Experience 🎨

**New Common BaseModel**: All generated models now inherit from `KittyCadBaseModel`, providing enhanced functionality and better developer experience:

- **User-friendly string representation**: Models now display key fields in `__repr__()` for easier debugging
- **Convenience methods**: Added `to_dict()`, `to_json()`, `from_dict()`, and `from_json()` factory methods
- **Stricter validation**: Enhanced Pydantic configuration with `extra='forbid'` to catch unexpected fields
- **Better serialization**: Improved JSON serialization with `use_enum_values=True` and `exclude_none=True`

```python
# Enhanced model usage
from kittycad.models import User

# Clean string representation
user = User(id="123", name="John Doe", email="john@example.com")
print(user)  # User(id='123', name='John Doe', email='john@example.com')

# Convenient serialization/deserialization
user_dict = user.to_dict()
user_json = user.to_json()
new_user = User.from_dict({"id": "456", "name": "Jane"})
```

**Improved Acronym Handling**: Fixed code generation to handle acronyms more naturally in module names:

- **Better file naming**: `OAuth2ClientInfo` now generates `oauth2_client_info.py` instead of `o_auth2_client_info.py`
- **Cleaner imports**: `from kittycad.models.oauth2_client_info import OAuth2ClientInfo` (previously required `o_auth2_client_info`)
- **Consistent patterns**: XML, API, HTML, JSON, HTTPS, and other acronyms are handled properly
- **Hardcoded fixes**: Special handling for complex cases like OAuth2 that don't fit general patterns

**Enhanced Code Generation Tests**: Added comprehensive test suite for code generation utilities:

- **Acronym handling verification**: Tests ensure proper conversion of camelCase to snake_case
- **Regression prevention**: Automated tests prevent future acronym handling regressions
- **Integration with pytest**: Tests are discoverable and run with the main test suite
- **Coverage verification**: Tests cover edge cases and common acronym patterns

### Technical Improvements

**BaseModel Configuration**:

```python
model_config = ConfigDict(
    protected_namespaces=(),     # Avoid namespace warnings
    populate_by_name=True,       # Enable alias usage for API compatibility
    extra='forbid',              # Prevent typos and unexpected fields
    use_enum_values=True,        # Clean enum serialization
)
```

**Updated Code Generation**:

- Templates now use `KittyCadBaseModel` instead of direct Pydantic `BaseModel`
- Removed duplicate `ConfigDict` declarations from generated models
- Added base model import to generated `__init__.py` files

**Test Infrastructure**:

- New test directory: `generate/tests/` for code generation utilities
- Pytest-compatible test structure with proper parametrization
- Tests verify both current behavior and improvements

### Added - Comprehensive HTTPX Exception Wrapping 🛡️

**Uniform Error Model**: All network and HTTP errors are now wrapped in custom KittyCAD exception types, providing consistent error handling across the SDK.

**Enhanced Exception Attributes**: All exceptions now include comprehensive context for debugging:

```python
try:
    user = client.users.get_user(id="123")
except KittyCADAPIError as e:
    print(f"HTTP {e.status_code}: {e.message}")
    print(f"Error code: {e.error_code}")
    print(f"Request ID: {e.request_id}")
    print(f"Request: {e.request_method} {e.request_url}")
except KittyCADConnectionError as e:
    print(f"Connection failed: {e.message}")
    print(f"Original error: {e.original_error}")
except KittyCADTimeoutError as e:
    print(f"Request timed out: {e.message}")
    print(f"Timeout: {e.timeout_seconds}s")
```

**Complete HTTPX Integration**: Previously, raw HTTPX exceptions (timeouts, connection errors) could surface to users. Now all exceptions are wrapped:

- **`KittyCADConnectionError`**: Network errors, DNS failures, connection refused
- **`KittyCADTimeoutError`**: Connection and read timeouts with timeout duration
- **`KittyCADClientError`**: Enhanced 4xx errors with request context
- **`KittyCADServerError`**: Enhanced 5xx errors with request context

**Rich Debugging Context**: Exception attributes now include:

- `request_method` and `request_url` for all HTTP-related errors
- `original_error` for network errors to access underlying HTTPX exceptions
- `timeout_seconds` for timeout errors
- `headers` dictionary for all API errors
- Enhanced error messages with full request context

**Automatic Error Handling**: All HTTPX exceptions are now automatically wrapped without any user intervention required - users simply get consistent KittyCAD exceptions regardless of the underlying failure type.

### Added - Enhanced JSON + Multipart Form Data Support 🔧

**Comprehensive Function Examples**: All JSON + multipart endpoints now include detailed usage examples in their generated docstrings, showing how to use both the JSON body and file attachments parameters effectively.

**Required File Attachments**: File attachments are now required (not optional) for multipart endpoints, ensuring consistent API usage and preventing incomplete requests.

**Complete Test Coverage**: Added real API tests for `create_file_conversion_options` endpoint using the same input files as existing `create_file_conversion` tests, covering both sync and async patterns:

```python
# Sync version with STL input
def test_file_conversion_options_stl():
    fc = client.file.create_file_conversion_options(
        body=ConversionParams(
            src_format=InputFormat3d(InputOptionStep(split_closed_faces=False)),
            output_format=OutputFormat3d(OutputOptionObj(...))
        ),
        file_attachments={"input.stl": file_path}
    )

# Async version with STL input  
async def test_file_conversion_options_stl_async():
    result = await client.file.create_file_conversion_options(
        body=ConversionParams(...),
        file_attachments={"input.stl": file_path}
    )

# Async version with OBJ input
async def test_file_conversion_options_obj_async():
    result = await client.file.create_file_conversion_options(
        body=ConversionParams(...),
        file_attachments={"input.obj": file_path}
    )
```

**Improved Code Generation**: Enhanced function generation to properly handle multipart endpoints with comprehensive examples and correct parameter signatures that mirror the robust file handling patterns from the Rust SDK.

### Added - Comprehensive Pythonic File Handling System 📁

**OpenAI-Level Ergonomic File Operations**: The SDK now provides a comprehensive file handling system that feels as intuitive as popular libraries like OpenAI, Stripe, and Boto3, with support for flexible input types, automatic content detection, progress tracking, and streaming operations.

**Flexible Input Types**: File operations accept multiple input types seamlessly:

```python
# File paths (str or pathlib.Path)
client.upload_file("/path/to/document.pdf")
client.upload_file(Path("/path/to/document.pdf"))

# File objects (any IO[bytes])
with open("/path/to/file.pdf", "rb") as f:
    client.upload_file(f)

file_obj = io.BytesIO(b"content")
client.upload_file(file_obj)

# Raw bytes/bytearray/memoryview
client.upload_file(b"raw file content")
client.upload_file(bytearray(b"content"))

# Streaming iterators for large files
def file_chunks():
    with open("/path/to/large_file.bin", "rb") as f:
        while chunk := f.read(8192):
            yield chunk

client.upload_file(file_chunks())
```

**Automatic Content Detection and Upload Method Selection**:

- **Content-Type Detection**: From filename extensions, file content magic bytes, or explicit override
- **Smart Upload Method**: Automatically chooses between `multipart/form-data` and `application/octet-stream`
- **Filename Handling**: Extracted from paths or file object names, with sensible defaults

```python
# Content type auto-detected as image/png
client.upload_file("/path/to/image.png")

# Multipart used automatically (has filename)
client.upload_file("/path/to/document.pdf")

# Binary used automatically (raw bytes)
client.upload_file(b"raw binary data")

# Explicit overrides supported
client.upload_file(
    "/path/to/file.bin",
    content_type="application/custom-binary",
    force_multipart=True
)
```

**Comprehensive Progress Tracking**: All file operations support optional progress callbacks with built-in console display utilities:

```python
def progress_callback(bytes_transferred, total_bytes):
    if total_bytes:
        percentage = (bytes_transferred / total_bytes) * 100
        print(f"Progress: {percentage:.1f}% ({bytes_transferred}/{total_bytes})")

# Upload with progress
client.upload_file("/path/to/file.pdf", progress_callback=progress_callback)

# Built-in console progress display
from kittycad._progress import create_progress_callback
progress = create_progress_callback("Uploading", show_percentage=True, show_speed=True)
client.upload_file("/path/to/file.pdf", progress_callback=progress)
# Output: Uploading: 1,234,567/2,000,000 bytes (61.7%) [1.2 MB/s]
```

**Streaming Operations for Large Files**: Memory-efficient handling of large files through streaming uploads and downloads:

```python
# Streaming upload with generator
def generate_large_file():
    for i in range(100000):
        yield f"Line {i}\n".encode()

client.upload_binary(data=generate_large_file(), stream=True)

# Streaming download to disk
client.download_file(
    output="/tmp/large_file.bin",
    chunk_size=65536,  # 64KB chunks
    progress_callback=progress_callback
)

# Download to memory or file object
file_bytes = client.download_file(output=None)  # Returns bytes
with open("/tmp/file.bin", "wb") as f:
    client.download_file(output=f)  # Writes to file object
```

**Resource Management and Safety**: The SDK follows Python best practices for resource management:

- **Only closes files it opens**: User-provided file objects are never closed by the SDK
- **Automatic cleanup**: Context managers and proper resource cleanup for all operations
- **Memory efficiency**: Streaming support prevents loading large files entirely into memory
- **Error handling**: Comprehensive exception handling with detailed context

```python
# SDK opens and closes automatically
client.upload_file("/path/to/file.pdf")  # File opened/closed by SDK

# User files remain under user control
with open("/path/to/file.pdf", "rb") as f:
    client.upload_file(f)  # File stays open, user controls lifecycle
```

**Enhanced Download Capabilities**: Flexible download options with automatic directory creation and overwrite protection:

```python
# Download to file path (creates directories if needed)
client.download_file(output="/tmp/downloads/document.pdf")

# Download to file object (no auto-close)
with open("/tmp/file.pdf", "wb") as f:
    client.download_file(output=f)

# Download to memory
file_data = client.download_file(output=None)

# Overwrite protection
client.download_file(output="/tmp/existing.pdf", overwrite=False)  # Raises FileExistsError
client.download_file(output="/tmp/existing.pdf", overwrite=True)   # Overwrites safely
```

**Full Async Support**: All file operations have async equivalents with identical APIs:

```python
async def upload_example():
    client = AsyncKittyCAD()
    
    # Async upload with progress
    await client.upload_file_async(
        "/path/to/file.pdf",
        progress_callback=progress_callback
    )
    
    # Async streaming download
    await client.download_file_async(
        output="/tmp/large_download.bin",
        chunk_size=8192,
        progress_callback=progress_callback
    )
    
    await client.aclose()
```

**Low-Level API Access**: Advanced users can access the underlying file handling modules directly for custom implementations:

```python
from kittycad._multipart import upload_file_multipart, MultipartUploadContext
from kittycad._binary import upload_file_binary, BinaryUploadContext  
from kittycad._downloads import stream_download, DownloadContext

# Direct multipart upload with custom fields
response = upload_file_multipart(
    client=httpx_client,
    url="https://api.zoo.dev/upload",
    file_param="document",
    file_input="/path/to/file.pdf",
    additional_fields={"metadata": "custom_value"}
)

# Context managers for resource safety
with MultipartUploadContext("/path/to/file.pdf", progress_callback=callback) as upload:
    response = httpx.post(url, files=upload.files)
```

**Comprehensive Error Handling Integration**: File operations use the SDK's enhanced exception system with specific handling for file-related errors:

```python
from kittycad import KittyCADAPIError, KittyCADConnectionError

try:
    client.upload_file("/path/to/large_file.bin")
except KittyCADAPIError as e:
    if e.status_code == 413:
        print(f"File too large: {e.message}")
    elif e.status_code == 422:
        print(f"Invalid file format: {e.message}")
except KittyCADConnectionError as e:
    print(f"Network error during upload: {e.message}")
except FileNotFoundError:
    print("File not found on local system")
```

### Developer Benefits

1. **Better Debugging**: Readable model representations show key fields automatically
1. **Easier Serialization**: Built-in methods for JSON/dict conversion with sensible defaults
1. **Cleaner Module Structure**: More intuitive import paths for OAuth2 and other acronym-heavy models
1. **Enhanced Validation**: Stricter Pydantic settings catch more errors at development time
1. **Future-Proof**: Test coverage ensures acronym handling improvements don't regress
1. **Uniform Error Handling**: All errors use the same exception types with consistent attributes
1. **Rich Error Context**: Comprehensive debugging information in all exception types
1. **Predictable Error Behavior**: No more raw HTTPX exceptions surfacing to user code
1. **Intuitive File Operations**: File handling feels as natural as OpenAI, Stripe, or Boto3 SDKs
1. **Memory Efficient**: Streaming support handles files of any size without memory issues
1. **Progress Visibility**: Built-in progress tracking for better user experience
1. **Resource Safety**: Automatic resource management following Python best practices

## v1.0.0

### Quick Start - New Simple API 🎉

The KittyCAD Python SDK now features a streamlined, class-based API that's much easier to use:

```python
from kittycad import KittyCAD

# Create client (uses KITTYCAD_API_TOKEN/ZOO_API_TOKEN and ZOO_HOST environment variables)
client = KittyCAD()

# Make API calls directly
user = client.users.get_user_self()
print(f"Hello {user.name}!")

# WebSocket connections are seamless
with client.modeling.modeling_commands_ws(fps=30, webrtc=False, ...) as ws:
    # Send modeling commands
    ws.send(command)
    response = ws.recv()
```

**Async support:**

```python
from kittycad import AsyncKittyCAD

client = AsyncKittyCAD()
user = await client.users.get_user_self()
```

### Added - HTTP Client Pooling & Improved Performance ⚡

**Connection Pooling**: The client now uses persistent HTTP connections, significantly improving performance for multiple API calls by reusing TCP connections instead of establishing new ones for each request.

**Improved Error Handling**: Enhanced exception handling with better context and debugging information.

**Memory Efficiency**: Optimized memory usage through better connection management and resource cleanup.

### Added - OpenAI-Style Automatic Pagination 🎯

**Smart Pagination**: List endpoints now return iterators that automatically handle pagination, eliminating the need for manual page token management.

**Memory Efficient**: Uses generators for O(1) memory usage regardless of result count - items are fetched and yielded as needed.

**Type Safe**: Full type annotations and IDE support for all paginated endpoints.

#### Usage Examples

**Sync Pagination:**

```python
from kittycad import KittyCAD

client = KittyCAD()

# Automatically iterate through ALL results across pages
for api_call in client.api_calls.list_api_calls():
    print(f"API Call: {api_call.id}")
    # No manual pagination needed!

# Control page size
for item in client.api_calls.list_api_calls(limit=50):
    print(item)
```

**Async Pagination:**

```python
import asyncio
from kittycad import AsyncKittyCAD

async def main():
    client = AsyncKittyCAD()
    
    # Async iteration over all results
    async for api_call in client.api_calls.list_api_calls():
        print(f"API Call: {api_call.id}")
        
    await client.aclose()

asyncio.run(main())
```

#### Paginated Endpoints

The following endpoints now support automatic pagination:

- **API Calls**: `list_api_calls()`, `org_list_api_calls()`, `user_list_api_calls()`
- **ML**: `list_ml_prompts()`, `list_conversations_for_user()`, `list_text_to_cad_models_for_user()`
- **Organizations**: `list_org_members()`, `get_org_shortlinks()`, `list_orgs()`
- **Users**: `get_user_shortlinks()`, `list_users()`, `list_users_extended()`
- **Service Accounts**: `list_service_accounts_for_org()`
- **API Tokens**: `list_api_tokens_for_user()`

### Added - Enhanced Documentation 📚

**Comprehensive Pagination Guide**: New detailed documentation for the automatic pagination system with examples and advanced usage patterns.

**Updated API Reference**: Documentation now reflects the new client classes and pagination capabilities.

**Better Organization**: Restructured docs to highlight the new client approach and pagination features.

### Added - New Client Classes 🚨 BREAKING CHANGE

The SDK now provides unified client classes that eliminate the need for direct API imports and global configuration.

#### New Client Classes

- **`KittyCAD`**: Main synchronous client with all API endpoints as methods
- **`AsyncKittyCAD`**: Asynchronous client with async/await support and dedicated `AsyncClient` class
- Direct method access: `client.ping()`, `client.get_user()`, `client.modeling_commands_ws()`, etc.
- WebSocket support with convenient wrapper classes
- All API endpoints organized as client methods (no more direct API imports needed)
- Client configuration through constructor parameters (token, base_url, timeout, etc.)

#### Available API Categories

- **Meta**: `ping()`, `get_pricing_subscriptions()`, etc.
- **Users**: `get_user()`, `get_user_self()`, etc.
- **Organizations**: `get_org()`, `create_org_member()`, etc.
- **Modeling**: `modeling_commands_ws()`, `create_file_conversion()`, etc.
- **ML**: `ml_copilot_ws()`, `get_text_to_cad_model_for_user()`, etc.
- **Payments**: `create_payment()`, `get_payment()`, etc.
- And many more...

#### Usage Examples

**Synchronous Client:**

```python
from kittycad import KittyCAD

# With explicit token
client = KittyCAD(token="your-token-here")

# Or using environment variables (KITTYCAD_API_TOKEN/ZOO_API_TOKEN + ZOO_HOST)
client = KittyCAD()  # Automatically reads from environment

# REST endpoints
user = client.users.get_user(id="123")
pong = client.meta.ping()

# WebSocket endpoints
with client.modeling.modeling_commands_ws(fps=30, ...) as ws:
    ws.send(command)
    response = ws.recv()
```

**Asynchronous Client:**

```python
from kittycad import AsyncKittyCAD

# With explicit token
client = AsyncKittyCAD(token="your-token-here")

# Or using environment variables (KITTYCAD_API_TOKEN/ZOO_API_TOKEN + ZOO_HOST)
client = AsyncKittyCAD()  # Automatically reads from environment

# REST endpoints  
user = await client.users.get_user(id="123")
pong = await client.meta.ping()

# WebSocket endpoints (always sync)
with client.modeling.modeling_commands_ws(fps=30, ...) as ws:
    ws.send(command)
    response = ws.recv()
```

**Client Configuration Options:**

```python
from kittycad import KittyCAD

# All available configuration options
client = KittyCAD(
    token="your-token-here",           # Or omit to use env vars
    base_url="https://api.zoo.dev",    # Custom API base URL
    timeout=120.0,                     # Request timeout in seconds  
    cookies={"session": "abc123"},     # Additional cookies
    headers={"X-Custom": "header"},    # Additional headers
    verify_ssl=True                    # SSL verification setting
)
```

#### Migration from Direct API Imports

**Before:**

```python
from kittycad.api.users.get_user import sync
from kittycad.client import Client

client = Client(token="token")
user = sync(id="123", client=client)
```

**After:**

```python
from kittycad import KittyCAD

client = KittyCAD(token="token") 
user = client.users.get_user(id="123")
```

#### WebSocket Client Changes

WebSocket wrapper classes now require explicit client passing instead of using global state.

**Before:**

```python
# WebSocket classes used global client
ws = WebSocket(fps=30, ...)  # Used global client internally
```

**After:**

```python
# WebSocket classes require client parameter
client = KittyCAD(token="token")
ws = client.modeling.modeling_commands_ws(fps=30, ...)  # Client passed explicitly
```

#### Benefits of New Architecture

- **Better IDE support**: Full autocomplete and type hints for all endpoints
- **Simplified imports**: Only need `from kittycad import KittyCAD` or `AsyncKittyCAD`
- **Consistent patterns**: All endpoints follow the same calling convention
- **No global state**: Thread-safe, testable, and predictable client behavior
- **Clear separation**: Sync and async clients are distinct classes
- **WebSocket integration**: WebSocket endpoints work seamlessly with REST endpoints

### Changed - Exception-Based Error Handling 🚨 BREAKING CHANGE

The SDK has been transformed from returning error types to using idiomatic Python exceptions. This is a breaking change that makes the SDK more Pythonic and developer-friendly.

#### New Exception Hierarchy

- **`KittyCADError`**: Base exception for all KittyCAD errors
- **`KittyCADAPIError`**: Base for HTTP API errors (includes status code, error code, request ID)
- **`KittyCADClientError`**: 4xx client errors (inherits from KittyCADAPIError)
- **`KittyCADServerError`**: 5xx server errors (inherits from KittyCADAPIError)
- **`KittyCADConnectionError`**: Network/connection errors
- **`KittyCADTimeoutError`**: Request timeout errors

#### Migration Required

**Before:**

```python
result = get_user.sync(id="123", client=client)
if isinstance(result, Error):
    print(f"Error: {result.message}")
    return
user = result  # Could still be None or Error
```

**After:**

```python
try:
    user = client.users.get_user(id="123", client=client)  # Always User type
    # Use user directly - guaranteed to be correct type
except KittyCADAPIError as e:
    print(f"API call failed: {e}")
```

#### Rich Exception Messages

Exceptions now include comprehensive context:

- HTTP status code and status text
- API error message from server
- Error code from API
- Request ID for debugging
- Request method and URL
- Response headers

Example exception message:

```
403 Forbidden: User has outstanding invoices (request to DELETE /users/self) (error_code: OUTSTANDING_INVOICES) (request_id: req-abc123)
```

#### Clean Return Types

- All API functions now return only their expected types
- No more `Union[T, Error]` return types
- Type safety and IDE support greatly improved
- Error checking boilerplate eliminated

#### Breaking Changes

1. **Remove error checking code**: API functions now raise exceptions instead of returning Error objects
1. **Update imports**: Remove Error model imports, add exception imports from `kittycad`
1. **Exception handling**: Wrap API calls in try/catch blocks instead of checking return values

#### Migration Guide

1. **Update imports**:

   ```python
   # Remove
   from kittycad.models.error import Error

   # Add
   from kittycad import KittyCADAPIError, KittyCADClientError, KittyCADServerError
   ```

1. **Replace error checking**:

   ```python
   # OLD
   result = api_call.sync(client=client)
   if isinstance(result, Error):
       handle_error(result)
       return

   # NEW
   try:
       result = api_call.sync(client=client)
   except KittyCADAPIError as e:
       handle_error(e)
       return
   ```

1. **Exception information access**:

   ```python
   try:
       result = api_call.sync(client=client)
   except KittyCADAPIError as e:
       print(f"Status: {e.status_code}")
       print(f"Error code: {e.error_code}")
       print(f"Request ID: {e.request_id}")
       print(f"Headers: {e.headers}")
   ```

#### Benefits

- **Type Safety**: Return types are always the expected type, never Error
- **Python Conventions**: Uses standard exception patterns
- **Rich Context**: Exception messages include all relevant debugging information
- **Easier Debugging**: No need to dig into Error objects
- **Cleaner Code**: No error checking boilerplate needed
- **Better IDE Support**: Improved autocomplete and type checking

## v1.1.3

### Fixed – Typed responses instead of raw dicts

- All non-collection responses are now deserialized with Pydantic and returned as typed models, not raw `dict`s. This removes several cases where function signatures claimed to return models but actually returned JSON.

### Changed – Text-to-CAD model lookup return type

- `ml.get_text_to_cad_model_for_user()` now returns `TextToCadResponse` (a discriminated union RootModel) rather than a raw `dict` or an untyped `Union` dump.

### Migration

- Old behavior (returned `dict` or treated as `Union[TextToCad, TextToCadIteration, TextToCadMultiFileIteration]`):

  ```python
  result = client.ml.get_text_to_cad_model_for_user(id=some_id)
  # used result like a dict or tried to guess the shape
  ```

- New behavior (typed RootModel):

  ```python
  from kittycad.models.text_to_cad_response import TextToCadResponse

  resp: TextToCadResponse = client.ml.get_text_to_cad_model_for_user(id=some_id)
  model = resp.root  # one of: TextToCad | TextToCadIteration | TextToCadMultiFileIteration
  ```

- Why: The OpenAPI spec defines the response as `TextToCadResponse` (a discriminated `oneOf`). Returning the wrapper ensures reliable, validated parsing and a stable API.
