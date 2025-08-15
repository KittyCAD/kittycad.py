# Changelog

All notable changes to the KittyCAD Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
2. **Update imports**: Remove Error model imports, add exception imports from `kittycad`
3. **Exception handling**: Wrap API calls in try/catch blocks instead of checking return values

#### Migration Guide

1. **Update imports**:
   ```python
   # Remove
   from kittycad.models.error import Error
   
   # Add
   from kittycad import KittyCADAPIError, KittyCADClientError, KittyCADServerError
   ```

2. **Replace error checking**:
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

3. **Exception information access**:
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

---

## Previous Versions

For changes prior to this version, see the git history or individual release notes.