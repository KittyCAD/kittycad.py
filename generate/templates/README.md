# KittyCAD Python SDK Template System

This directory contains the Jinja2 templates used to generate the Python SDK code. The template system has been designed with maintainability and extensibility in mind.

## Template Architecture

### Core Principles

1. **DRY (Don't Repeat Yourself)**: Common patterns are extracted into reusable macros
2. **Separation of Concerns**: Business logic is computed in Python, templates handle presentation
3. **Conditional Blocks**: Single templates handle multiple variants (sync/async, regular/paginated)
4. **Documentation**: All templates and macros are thoroughly documented

### Key Files

#### `shared_macros.jinja2`
Contains reusable macros for common code generation patterns:

- `function_signature()` - Generate function signatures with proper parameter handling
- `build_url()` - Build URLs with path parameters and query strings  
- `http_request_call()` - Execute HTTP requests (sync/async variants)
- `parse_response()` - Parse HTTP responses with error handling
- `pagination_setup()` - Setup pagination iterators
- `websocket_connect()` - WebSocket connection handling

#### `universal_function.py.jinja2`
The main template that consolidates all function types:

- Regular HTTP functions (sync/async)
- Paginated functions (sync/async)
- WebSocket functions (sync/async)

Uses the `function_type` context variable to dispatch to appropriate implementation.

#### Legacy Templates (maintained for compatibility)
- `sync_function.py.jinja2` / `async_function.py.jinja2` - Basic HTTP functions
- `sync_paginated_function.py.jinja2` / `async_paginated_function.py.jinja2` - Pagination
- `websocket_sync_function.py.jinja2` / `websocket_async_function.py.jinja2` - WebSockets

## Usage

### Using the Universal Template

```python
from generate.utils import render_universal_function

# Generate a regular sync function
render_universal_function(
    func_name="get_user",
    endpoint=endpoint_spec,
    args=processed_args,
    response_type="User",
    output_path="output.py",
    function_type="regular",
    is_async=False
)

# Generate a paginated async function  
render_universal_function(
    func_name="list_users",
    endpoint=endpoint_spec,
    args=processed_args,
    response_type="UserPage",
    output_path="output.py", 
    function_type="paginated",
    is_async=True
)
```

### Context Preparation

The `prepare_function_context()` function in `utils.py` handles all business logic:

```python
context = prepare_function_context(
    func_name="example_function",
    endpoint={"method": "GET", "url": "/api/users"},
    args=processed_parameters,
    response_type="UserResponse",
    is_async=True,
    is_paginated=False,
    is_websocket=False,
    # Additional context
    api_section="users",
    file_info=file_upload_info
)
```

## Extending the Templates

### Adding New Function Features

1. **Add Context Variables**: Update `prepare_function_context()` in `utils.py`
2. **Add Template Logic**: Use conditional blocks in `universal_function.py.jinja2`
3. **Create Macros**: Add reusable patterns to `shared_macros.jinja2`

Example - Adding streaming support:

```python
# In prepare_function_context()
context.update({
    "is_streaming": kwargs.get("is_streaming", False),
    "stream_type": kwargs.get("stream_type", "")
})

# In universal_function.py.jinja2
{% if is_streaming %}
    {{ stream_request_call(method, stream_type, is_async) }}
{% else %}
    {{ http_request_call(method, has_request_body, request_body_type, file_info, is_async) }}
{% endif %}
```

### Creating New Macros

Add macros to `shared_macros.jinja2` with full documentation:

```jinja2
{# 
   Generate streaming request handling
   
   Args:
     method: HTTP method
     stream_type: Type of streaming (event-stream, binary, etc.)
     is_async: Boolean flag for async handling
#}
{% macro stream_request_call(method, stream_type, is_async=false) -%}
    # Implementation here
{%- endmacro %}
```

## Best Practices

### Template Guidelines

1. **Keep templates simple**: Complex logic belongs in Python, not Jinja
2. **Use macros for repetition**: Don't duplicate code blocks
3. **Document everything**: Include clear comments and parameter documentation
4. **Parameterize variants**: Use boolean flags rather than separate templates

### Context Guidelines

1. **Pre-compute in Python**: All boolean flags, processed data should be ready-to-use
2. **Use descriptive names**: `has_request_body` not `req_body`
3. **Group related data**: Use dictionaries for related information (e.g., `file_info`)
4. **Validate context**: Ensure all required variables are present

### Maintenance Guidelines

1. **Test thoroughly**: Changes affect all generated code
2. **Update documentation**: Keep this README current
3. **Consider backward compatibility**: Legacy templates may still be in use
4. **Performance matters**: Template rendering happens for every function

## Migration Guide

### From Legacy Templates

To migrate from legacy templates to the universal template:

1. **Identify function type**: regular, paginated, or websocket
2. **Update context preparation**: Use `prepare_function_context()`
3. **Switch template**: Use `universal_function.py.jinja2`
4. **Test thoroughly**: Ensure output matches expected format

### Future Improvements

- **Template inheritance**: Consider Jinja extends for complex templates
- **More granular macros**: Split large macros into smaller, focused ones  
- **Type safety**: Add type hints to template context preparation
- **Performance optimization**: Cache compiled templates for better performance

## Troubleshooting

### Common Issues

1. **Missing context variables**: Check `prepare_function_context()` implementation
2. **Template not found**: Ensure template is in the templates directory
3. **Macro import errors**: Verify `{% from 'shared_macros.jinja2' import ... %}`
4. **Generated code formatting**: Run `ruff format` on generated files

### Debugging Templates

1. **Use template comments**: Add `{# DEBUG: variable_name = {{ variable_name }} #}`
2. **Check context**: Print context dictionary before rendering
3. **Validate macros**: Test macros independently with minimal context
4. **Compare outputs**: Diff generated code with expected results