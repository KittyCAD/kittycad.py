# Changelog

All notable changes to the KittyCAD Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Quick Start - New Simple API 🎉

The KittyCAD Python SDK now features a streamlined, class-based API that's much easier to use:

```python
from kittycad import KittyCAD

# Create client (uses KITTYCAD_API_TOKEN/ZOO_API_TOKEN and ZOO_HOST environment variables)
client = KittyCAD()

# Make API calls directly
user = client.get_user_self()
print(f"Hello {user.name}!")

# WebSocket connections are seamless
with client.modeling_commands_ws(fps=30, webrtc=False, ...) as ws:
    # Send modeling commands
    ws.send(command)
    response = ws.recv()
```

**Async support:**

```python
from kittycad import AsyncKittyCAD

client = AsyncKittyCAD()
user = await client.get_user_self()
```

### Added - New Client Classes 🚨 BREAKING CHANGE

The SDK now provides unified client classes that eliminate the need for direct API imports and global configuration.

#### New Client Classes

- **`KittyCAD`**: Main synchronous client with all API endpoints as methods
- **`AsyncKittyCAD`**: Asynchronous client with async/await support
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
user = client.get_user(id="123")
pong = client.ping()

# WebSocket endpoints
with client.modeling_commands_ws(fps=30, ...) as ws:
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
user = await client.get_user(id="123")
pong = await client.ping()

# WebSocket endpoints (always sync)
with client.modeling_commands_ws(fps=30, ...) as ws:
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
user = client.get_user(id="123")
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
ws = client.modeling_commands_ws(fps=30, ...)  # Client passed explicitly
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
    user = get_user.sync(id="123", client=client)  # Always User type
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

______________________________________________________________________

## Previous Versions

For changes prior to this version, see the git history or individual release notes.
