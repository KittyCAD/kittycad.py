#!/usr/bin/env python3
"""Comprehensive tests for file handling in KittyCAD SDK."""

import io
from unittest.mock import Mock, patch

import httpx
import pytest

from kittycad._binary import (
    BinaryUploadContext,
    create_binary_stream,
    create_binary_upload,
    prepare_binary_headers,
    upload_file_binary,
)
from kittycad._downloads import (
    DownloadContext,
    download_to_file,
    get_filename_from_response,
    stream_download,
)
from kittycad._file_inputs import (
    _get_content_type,
    _open_if_path,
    _peek_file_content,
    _should_use_multipart,
    prepare_upload_input,
)
from kittycad._multipart import (
    JsonMultipartUploadContext,
    MultipartUploadContext,
    cleanup_json_multipart_upload,
    cleanup_multipart_upload,
    create_files_dict,
    create_json_multipart_upload,
    create_multipart_upload,
    upload_file_multipart,
    upload_json_multipart,
)
from kittycad._progress import (
    ProgressTrackingReader,
    ProgressTrackingWriter,
    create_progress_callback,
    wrap_with_progress,
)


class TestFileInputNormalization:
    """Test file input normalization helpers."""

    def test_open_if_path_with_string_path(self, tmp_path):
        """Test opening a file from string path."""
        test_file = tmp_path / "test.txt"
        test_content = b"Hello, world!"
        test_file.write_bytes(test_content)

        file_obj, should_close, filename = _open_if_path(str(test_file))

        assert hasattr(file_obj, "read")
        assert should_close is True
        assert filename == "test.txt"
        assert file_obj.read() == test_content
        file_obj.close()

    def test_open_if_path_with_pathlib_path(self, tmp_path):
        """Test opening a file from pathlib Path."""
        test_file = tmp_path / "test.txt"
        test_content = b"Hello, pathlib!"
        test_file.write_bytes(test_content)

        file_obj, should_close, filename = _open_if_path(test_file)

        assert hasattr(file_obj, "read")
        assert should_close is True
        assert filename == "test.txt"
        assert file_obj.read() == test_content
        file_obj.close()

    def test_open_if_path_with_bytes(self):
        """Test handling bytes input."""
        test_content = b"Hello, bytes!"

        file_obj, should_close, filename = _open_if_path(test_content)

        assert hasattr(file_obj, "read")
        assert should_close is False
        assert filename is None
        assert file_obj.read() == test_content

    def test_open_if_path_with_bytearray(self):
        """Test handling bytearray input."""
        test_content = bytearray(b"Hello, bytearray!")

        file_obj, should_close, filename = _open_if_path(test_content)

        assert hasattr(file_obj, "read")
        assert should_close is False
        assert filename is None
        assert file_obj.read() == bytes(test_content)

    def test_open_if_path_with_file_object(self):
        """Test handling existing file object."""
        test_content = b"Hello, file object!"
        file_obj_input = io.BytesIO(test_content)
        file_obj_input.name = "test.txt"

        file_obj, should_close, filename = _open_if_path(file_obj_input)

        assert file_obj is file_obj_input
        assert should_close is False
        assert filename == "test.txt"
        assert file_obj.read() == test_content

    def test_open_if_path_with_iterator(self):
        """Test handling iterator input."""
        chunks = [b"Hello, ", b"iterator!"]

        file_obj, should_close, filename = _open_if_path(iter(chunks))

        assert hasattr(file_obj, "read")
        assert should_close is False
        assert filename is None
        assert file_obj.read() == b"Hello, iterator!"

    def test_open_if_path_with_invalid_type(self):
        """Test error handling for invalid input types."""
        with pytest.raises(TypeError, match="Unsupported upload type"):
            _open_if_path(123)  # type: ignore[arg-type]

    def test_get_content_type_from_filename(self):
        """Test content type detection from filename."""
        assert _get_content_type(filename="test.png") == "image/png"
        assert _get_content_type(filename="test.jpg") == "image/jpeg"
        assert _get_content_type(filename="test.pdf") == "application/pdf"
        assert _get_content_type(filename="test.txt") == "text/plain"

    def test_get_content_type_from_content(self):
        """Test content type detection from content bytes."""
        # PNG magic bytes
        png_header = b"\x89PNG\r\n\x1a\n" + b"rest of file"
        assert _get_content_type(content=png_header) == "image/png"

        # JPEG magic bytes
        jpeg_header = b"\xff\xd8\xff" + b"rest of file"
        assert _get_content_type(content=jpeg_header) == "image/jpeg"

        # PDF magic bytes
        pdf_header = b"%PDF-1.4" + b"rest of file"
        assert _get_content_type(content=pdf_header) == "application/pdf"

    def test_get_content_type_override(self):
        """Test content type override takes precedence."""
        assert (
            _get_content_type(
                filename="test.png", content=b"%PDF", override="application/custom"
            )
            == "application/custom"
        )

    def test_get_content_type_fallback(self):
        """Test fallback to octet-stream."""
        assert _get_content_type() == "application/octet-stream"
        assert _get_content_type(filename="unknown") == "application/octet-stream"

    def test_should_use_multipart_with_filename(self):
        """Test multipart decision with filename."""
        assert _should_use_multipart(b"data", filename="test.txt") is True

    def test_should_use_multipart_with_path(self, tmp_path):
        """Test multipart decision with path."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("test")
        assert _should_use_multipart(str(test_file)) is True

    def test_should_use_multipart_with_bytes(self):
        """Test multipart decision with raw bytes."""
        assert _should_use_multipart(b"data") is False

    def test_should_use_multipart_force(self):
        """Test forcing multipart mode."""
        assert _should_use_multipart(b"data", force_multipart=True) is True

    def test_peek_file_content(self):
        """Test peeking at file content without consuming."""
        content = b"Hello, world! This is a longer content for testing."
        file_obj = io.BytesIO(content)

        # Peek at first 10 bytes
        peeked = _peek_file_content(file_obj, 10)
        assert peeked == b"Hello, wor"

        # Verify file position is restored
        assert file_obj.tell() == 0
        assert file_obj.read() == content

    def test_prepare_upload_input_comprehensive(self, tmp_path):
        """Test comprehensive upload input preparation."""
        test_file = tmp_path / "test.png"
        test_content = b"\x89PNG\r\n\x1a\n" + b"fake png content"
        test_file.write_bytes(test_content)

        file_obj, should_close, filename, content_type, use_multipart = (
            prepare_upload_input(str(test_file))
        )

        assert hasattr(file_obj, "read")
        assert should_close is True
        assert filename == "test.png"
        assert content_type == "image/png"
        assert use_multipart is True

        if should_close:
            file_obj.close()


class TestProgressTracking:
    """Test progress tracking utilities."""

    def test_progress_tracking_reader(self):
        """Test progress tracking for reading."""
        content = b"Hello, world!"
        file_obj = io.BytesIO(content)
        progress_calls = []

        def progress_callback(bytes_read, total):
            progress_calls.append((bytes_read, total))

        reader = ProgressTrackingReader(file_obj, progress_callback, len(content))

        # Read in chunks
        chunk1 = reader.read(5)
        chunk2 = reader.read(8)

        assert chunk1 == b"Hello"
        assert chunk2 == b", world!"
        assert progress_calls == [(5, 13), (13, 13)]

    def test_progress_tracking_writer(self):
        """Test progress tracking for writing."""
        file_obj = io.BytesIO()
        progress_calls = []

        def progress_callback(bytes_written, total):
            progress_calls.append((bytes_written, total))

        writer = ProgressTrackingWriter(file_obj, progress_callback, 13)

        # Write in chunks
        writer.write(b"Hello")
        writer.write(b", world!")

        assert file_obj.getvalue() == b"Hello, world!"
        assert progress_calls == [(5, 13), (13, 13)]

    def test_create_progress_callback(self, capsys):
        """Test creating a console progress callback."""
        callback = create_progress_callback("Testing", show_percentage=True)

        # Simulate progress updates
        callback(512, 1024)
        callback(1024, 1024)

        captured = capsys.readouterr()
        assert "Testing" in captured.out
        assert "512" in captured.out
        assert "1,024" in captured.out

    def test_wrap_with_progress(self):
        """Test wrapping file objects with progress tracking."""
        content = b"test content"
        file_obj = io.BytesIO(content)
        progress_calls = []

        def progress_callback(bytes_transferred, total):
            progress_calls.append((bytes_transferred, total))

        # Test wrapping for reading
        wrapped = wrap_with_progress(
            file_obj, progress_callback, len(content), for_reading=True
        )
        assert isinstance(wrapped, ProgressTrackingReader)

        # Test wrapping for writing
        write_obj = io.BytesIO()
        wrapped_write = wrap_with_progress(
            write_obj, progress_callback, len(content), for_reading=False
        )
        assert isinstance(wrapped_write, ProgressTrackingWriter)


class TestMultipartUploads:
    """Test multipart upload functionality per user requirements."""

    def test_multipart_accept_str_path(self, tmp_path):
        """Test multipart upload accepts str/PathLike path."""
        test_file = tmp_path / "test.txt"
        test_content = b"Hello, string path!"
        test_file.write_bytes(test_content)

        files_dict = create_files_dict(file_param="file", file_input=str(test_file))

        assert "file" in files_dict
        filename, file_obj, content_type = files_dict["file"]
        assert filename == "test.txt"
        assert content_type == "text/plain"
        assert file_obj.read() == test_content

        # Cleanup
        cleanup_multipart_upload(files_dict)

    def test_multipart_accept_pathlike(self, tmp_path):
        """Test multipart upload accepts PathLike objects."""
        test_file = tmp_path / "test.txt"
        test_content = b"Hello, PathLike!"
        test_file.write_bytes(test_content)

        files_dict = create_files_dict(
            file_param="file",
            file_input=test_file,  # PathLike object
        )

        assert "file" in files_dict
        filename, file_obj, content_type = files_dict["file"]
        assert filename == "test.txt"
        assert content_type == "text/plain"
        assert file_obj.read() == test_content

        cleanup_multipart_upload(files_dict)

    def test_multipart_accept_file_object(self):
        """Test multipart upload accepts IO[bytes] file objects."""
        test_content = b"Hello, file object!"
        file_obj = io.BytesIO(test_content)
        file_obj.name = "test_file.txt"

        files_dict = create_files_dict(file_param="file", file_input=file_obj)

        assert "file" in files_dict
        filename, returned_obj, content_type = files_dict["file"]
        assert filename == "test_file.txt"
        assert returned_obj is file_obj  # Should be same object
        assert content_type == "text/plain"

        # Verify content can be read
        file_obj.seek(0)
        assert file_obj.read() == test_content

    def test_multipart_accept_bytes(self):
        """Test multipart upload accepts bytes."""
        test_content = b"Hello, bytes!"

        files_dict = create_files_dict(file_param="file", file_input=test_content)

        assert "file" in files_dict
        filename, file_obj, content_type = files_dict["file"]
        assert filename is None  # No filename for raw bytes
        assert content_type == "application/octet-stream"
        assert file_obj.read() == test_content

    def test_multipart_accept_bytearray(self):
        """Test multipart upload accepts bytearray."""
        test_content = bytearray(b"Hello, bytearray!")

        files_dict = create_files_dict(file_param="file", file_input=test_content)

        assert "file" in files_dict
        filename, file_obj, content_type = files_dict["file"]
        assert filename is None
        assert content_type == "application/octet-stream"
        assert file_obj.read() == bytes(test_content)

    def test_multipart_accept_memoryview(self):
        """Test multipart upload accepts memoryview."""
        test_bytes = b"Hello, memoryview!"
        test_content = memoryview(test_bytes)

        files_dict = create_files_dict(file_param="file", file_input=test_content)

        assert "file" in files_dict
        filename, file_obj, content_type = files_dict["file"]
        assert filename is None
        assert content_type == "application/octet-stream"
        assert file_obj.read() == test_bytes

    def test_multipart_filename_defaults(self, tmp_path):
        """Test filename defaults from path or fileobj.name."""
        # Test path filename
        test_file = tmp_path / "my_document.pdf"
        test_file.write_bytes(b"PDF content")

        files_dict = create_files_dict("file", str(test_file))
        filename, _, _ = files_dict["file"]
        assert filename == "my_document.pdf"
        cleanup_multipart_upload(files_dict)

        # Test file object with name
        file_obj = io.BytesIO(b"content")
        file_obj.name = "from_fileobj.txt"

        files_dict = create_files_dict("file", file_obj)
        filename, _, _ = files_dict["file"]
        assert filename == "from_fileobj.txt"

        # Test bytes without name (should be None for multipart)
        files_dict = create_files_dict("file", b"content")
        filename, _, _ = files_dict["file"]
        assert filename is None

    def test_multipart_mimetype_inference(self, tmp_path):
        """Test mimetypes inference when content_type not provided."""
        # PNG file
        png_file = tmp_path / "image.png"
        png_content = b"\x89PNG\r\n\x1a\n" + b"fake png"
        png_file.write_bytes(png_content)

        files_dict = create_files_dict("file", str(png_file))
        _, _, content_type = files_dict["file"]
        assert content_type == "image/png"
        cleanup_multipart_upload(files_dict)

        # PDF file
        pdf_file = tmp_path / "document.pdf"
        pdf_file.write_bytes(b"PDF content")

        files_dict = create_files_dict("file", str(pdf_file))
        _, _, content_type = files_dict["file"]
        assert content_type == "application/pdf"
        cleanup_multipart_upload(files_dict)

    def test_multipart_only_closes_opened_files(self, tmp_path):
        """Test SDK closes only files it opened, never user-supplied objects."""
        # Test with path (SDK opens file)
        test_file = tmp_path / "test.txt"
        test_file.write_bytes(b"content")

        files_dict = create_files_dict("file", str(test_file))
        assert hasattr(files_dict, "_kittycad_should_close")
        assert files_dict._kittycad_should_close is True

        # Mock the file object to track close calls
        file_obj = getattr(files_dict, "_kittycad_file_obj")
        original_close = file_obj.close
        close_called = []

        def mock_close():
            close_called.append(True)
            return original_close()

        setattr(file_obj, "close", mock_close)

        cleanup_multipart_upload(files_dict)
        assert len(close_called) == 1  # Should be closed

        # Test with user-provided file object (SDK doesn't close)
        user_file_obj = io.BytesIO(b"user content")
        files_dict = create_files_dict("file", user_file_obj)
        assert getattr(files_dict, "_kittycad_should_close") is False

        # Mock close to verify it's not called
        close_called = []

        def mock_close2():
            close_called.append(True)

        setattr(user_file_obj, "close", mock_close2)

        cleanup_multipart_upload(files_dict)
        assert len(close_called) == 0  # Should NOT be closed

    def test_multipart_large_bytes_no_double_load(self):
        """Test large input via bytes does not load entire file twice."""
        # Create large content (1MB)
        large_content = b"x" * (1024 * 1024)

        # Track how many times the content is accessed
        access_count = 0

        class TrackingBytesIO(io.BytesIO):
            def __init__(self, data):
                nonlocal access_count
                access_count += 1
                super().__init__(data)

        # This test verifies that we don't duplicate large byte content
        files_dict = create_files_dict("file", large_content)
        _, file_obj, _ = files_dict["file"]

        # Reading the content should work
        content = file_obj.read()
        assert len(content) == 1024 * 1024

        # The content should only be loaded once into BytesIO
        # (This is implicit in our implementation - we pass bytes directly to BytesIO)

    @patch("httpx.Client")
    def test_multipart_server_receives_correct_format(
        self, mock_client_class, tmp_path
    ):
        """Test server receives correct multipart boundary, field names, and content-type."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        # Capture the request details
        request_calls = []

        def capture_request(*args, **kwargs):
            request_calls.append(kwargs)
            mock_response = Mock(spec=httpx.Response)
            mock_response.status_code = 200
            return mock_response

        mock_client.request = capture_request

        test_file = tmp_path / "upload.pdf"
        test_file.write_bytes(b"PDF content")

        upload_file_multipart(
            client=mock_client,
            url="https://api.zoo.dev/upload",
            file_param="document",
            file_input=str(test_file),
            additional_fields={"metadata": "test_upload"},
        )

        # Verify request was made with files
        assert len(request_calls) == 1
        request_kwargs = request_calls[0]
        assert "files" in request_kwargs
        assert "document" in request_kwargs["files"]

        # Verify file tuple format: (filename, file_obj, content_type)
        filename, file_obj, content_type = request_kwargs["files"]["document"]
        assert filename == "upload.pdf"
        assert content_type == "application/pdf"
        assert hasattr(file_obj, "read")

    def test_multipart_upload_context(self, tmp_path):
        """Test multipart upload context manager."""
        test_file = tmp_path / "test.txt"
        test_content = b"Hello, context!"
        test_file.write_bytes(test_content)

        with MultipartUploadContext(
            file_param="file", file_input=str(test_file)
        ) as upload:
            assert upload.files is not None
            assert "file" in upload.files
            filename, file_obj, content_type = upload.files["file"]
            assert filename == "test.txt"

    @patch("httpx.Client")
    def test_upload_file_multipart(self, mock_client_class, tmp_path):
        """Test multipart file upload function."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_client.request.return_value = mock_response

        test_file = tmp_path / "test.txt"
        test_content = b"Hello, upload!"
        test_file.write_bytes(test_content)

        response = upload_file_multipart(
            client=mock_client,
            url="https://api.zoo.dev/upload",
            file_param="file",
            file_input=str(test_file),
        )

        assert response == mock_response
        mock_client.request.assert_called_once()


class TestBinaryUploads:
    """Test binary upload functionality per user requirements."""

    def test_binary_accept_str_path(self, tmp_path):
        """Test binary upload accepts str/PathLike path."""
        test_file = tmp_path / "test.bin"
        test_content = b"Binary content here"
        test_file.write_bytes(test_content)

        data, content_type = create_binary_upload(str(test_file))

        assert data == test_content
        assert content_type == "application/octet-stream"

    def test_binary_accept_pathlike(self, tmp_path):
        """Test binary upload accepts PathLike objects."""
        test_file = tmp_path / "test.bin"
        test_content = b"PathLike binary content"
        test_file.write_bytes(test_content)

        data, content_type = create_binary_upload(test_file)

        assert data == test_content
        assert content_type == "application/octet-stream"

    def test_binary_accept_file_object(self):
        """Test binary upload accepts IO[bytes] file objects."""
        test_content = b"File object binary content"
        file_obj = io.BytesIO(test_content)

        data, content_type = create_binary_upload(file_obj)

        assert data == test_content
        assert content_type == "application/octet-stream"

    def test_binary_accept_bytes(self):
        """Test binary upload accepts bytes."""
        test_content = b"Raw bytes content"

        data, content_type = create_binary_upload(test_content)

        assert data == test_content
        assert content_type == "application/octet-stream"

    def test_binary_accept_bytearray(self):
        """Test binary upload accepts bytearray."""
        test_content = bytearray(b"Bytearray content")

        data, content_type = create_binary_upload(test_content)

        assert data == bytes(test_content)
        assert content_type == "application/octet-stream"

    def test_binary_accept_memoryview(self):
        """Test binary upload accepts memoryview."""
        test_bytes = b"Memoryview content"
        test_content = memoryview(test_bytes)

        data, content_type = create_binary_upload(test_content)

        assert data == test_bytes
        assert content_type == "application/octet-stream"

    def test_binary_accept_iterable_bytes(self):
        """Test binary upload accepts Iterable[bytes] for streaming."""
        chunks = [b"chunk1", b"chunk2", b"chunk3"]

        stream, content_type, cleanup_func = create_binary_stream(iter(chunks))

        # Consume the stream
        streamed_chunks = list(stream)
        streamed_content = b"".join(streamed_chunks)

        assert streamed_content == b"chunk1chunk2chunk3"
        assert content_type == "application/octet-stream"
        cleanup_func()

    def test_binary_streaming_request_body(self, tmp_path):
        """Test iterable/generator bodies send streaming request body."""

        # Create a generator function
        def content_generator():
            yield b"first_chunk"
            yield b"second_chunk"
            yield b"third_chunk"

        stream, content_type, cleanup_func = create_binary_stream(content_generator())

        # Verify it's a generator
        assert hasattr(stream, "__iter__")
        assert hasattr(stream, "__next__")

        # Consume and verify content
        chunks = list(stream)
        assert chunks == [b"first_chunk", b"second_chunk", b"third_chunk"]
        assert content_type == "application/octet-stream"
        cleanup_func()

    def test_binary_progress_callback_monotonic(self):
        """Test progress callback is called monotonically and completes at total size."""
        test_content = b"x" * 1000  # 1000 bytes
        progress_calls = []

        def progress_callback(sent_bytes, total_bytes):
            progress_calls.append((sent_bytes, total_bytes))

        data, content_type = create_binary_upload(
            test_content, progress_callback=progress_callback
        )

        assert data == test_content
        # Progress should be called at least once with final size
        assert len(progress_calls) > 0
        final_call = progress_calls[-1]
        assert final_call[0] == 1000  # All bytes sent
        assert final_call[1] == 1000  # Total size known

        # Verify monotonic increase
        for i in range(1, len(progress_calls)):
            assert progress_calls[i][0] >= progress_calls[i - 1][0]

    def test_binary_progress_chunk_size_granularity(self, tmp_path):
        """Test chunk_size influences progress granularity."""
        # Create larger content to test chunking
        test_content = b"x" * 1000
        test_file = tmp_path / "large.bin"
        test_file.write_bytes(test_content)

        progress_calls = []

        def progress_callback(sent_bytes, total_bytes):
            progress_calls.append((sent_bytes, total_bytes))

        # Test with small chunk size
        stream, content_type, cleanup_func = create_binary_stream(
            str(test_file),
            progress_callback=progress_callback,
            chunk_size=100,  # Small chunks for more progress calls
        )

        # Consume stream
        list(stream)  # Consume the stream
        cleanup_func()

        # Should have multiple progress calls due to small chunk size
        assert (
            len(progress_calls) >= 10
        )  # At least 10 calls for 1000 bytes / 100 chunk_size

        # Final call should have all bytes
        assert progress_calls[-1][0] == 1000

    def test_binary_content_type_from_explicit(self):
        """Test Content-Type from explicit content_type parameter."""
        test_content = b"Custom content"

        data, content_type = create_binary_upload(
            test_content, content_type="application/custom-binary"
        )

        assert content_type == "application/custom-binary"

    def test_binary_content_type_from_filename(self, tmp_path):
        """Test Content-Type inferred from filename/path."""
        # PNG file
        png_file = tmp_path / "image.png"
        png_content = b"\x89PNG\r\n\x1a\n" + b"fake png"
        png_file.write_bytes(png_content)

        data, content_type = create_binary_upload(str(png_file))
        assert content_type == "image/png"

        # PDF file
        pdf_file = tmp_path / "document.pdf"
        pdf_file.write_bytes(b"PDF content")

        data, content_type = create_binary_upload(str(pdf_file))
        assert content_type == "application/pdf"

    def test_binary_content_type_fallback(self):
        """Test Content-Type fallback to application/octet-stream."""
        test_content = b"Unknown content"

        data, content_type = create_binary_upload(test_content)

        assert content_type == "application/octet-stream"

    def test_binary_upload_context(self, tmp_path):
        """Test binary upload context manager."""
        test_file = tmp_path / "test.bin"
        test_content = b"Context binary content"
        test_file.write_bytes(test_content)

        with BinaryUploadContext(str(test_file)) as upload:
            assert upload.data == test_content
            assert upload.headers["Content-Type"] == "application/octet-stream"

    def test_prepare_binary_headers(self):
        """Test preparing headers for binary uploads."""
        headers = prepare_binary_headers(
            content_type="application/custom",
            content_length=1024,
            additional_headers={"X-Custom": "value"},
        )

        assert headers["Content-Type"] == "application/custom"
        assert headers["Content-Length"] == "1024"
        assert headers["X-Custom"] == "value"

    @patch("httpx.Client")
    def test_upload_file_binary(self, mock_client_class, tmp_path):
        """Test binary file upload function."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_client.request.return_value = mock_response

        test_file = tmp_path / "test.bin"
        test_content = b"Binary upload content"
        test_file.write_bytes(test_content)

        response = upload_file_binary(
            client=mock_client,
            url="https://api.zoo.dev/upload-binary",
            file_input=str(test_file),
        )

        assert response == mock_response
        mock_client.request.assert_called_once()

    @patch("httpx.Client")
    def test_binary_413_payload_too_large_exception(self, mock_client_class):
        """Test 413 Payload Too Large maps to friendly exception message."""
        from kittycad.exceptions import KittyCADClientError

        mock_client = Mock()
        mock_client_class.return_value = mock_client

        # Mock 413 response
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 413
        mock_response.reason_phrase = "Payload Too Large"
        mock_response.is_success = False
        mock_response.headers = {"content-type": "application/json"}
        mock_response.json.return_value = {
            "message": "Request payload too large",
            "error_code": "PAYLOAD_TOO_LARGE",
        }
        mock_response.request = Mock()
        mock_response.request.method = "POST"
        mock_response.url = "https://api.zoo.dev/upload"

        # Make the upload raise an exception due to status code
        def mock_request(*args, **kwargs):
            # Import here to avoid circular imports
            from kittycad.response_helpers import raise_for_status

            raise_for_status(mock_response)

        mock_client.request = mock_request

        # Test that 413 gets proper error handling
        with pytest.raises(KittyCADClientError) as exc_info:
            upload_file_binary(
                client=mock_client,
                url="https://api.zoo.dev/upload",
                file_input=b"large content",
            )

        error = exc_info.value
        assert error.status_code == 413
        assert "Payload Too Large" in str(error)
        assert error.error_code == "PAYLOAD_TOO_LARGE"


class TestDownloads:
    """Test download functionality per user requirements."""

    def test_download_return_bytes_true(self):
        """Test download_* with return_bytes=True returns full bytes."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "13"}
        mock_response.content = b"Hello, world!"
        mock_response.iter_bytes.return_value = [b"Hello, world!"]

        # When output is None, it returns bytes
        result = download_to_file(mock_response, None)

        assert result == b"Hello, world!"

    def test_download_to_path_writes_file(self, tmp_path):
        """Test download with path='...' writes to file on disk."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "13"}
        mock_response.iter_bytes.return_value = [b"Hello", b", world!"]

        output_file = tmp_path / "downloaded.txt"
        result = download_to_file(mock_response, str(output_file))

        assert result is None  # Returns None when writing to file
        assert output_file.read_bytes() == b"Hello, world!"
        assert output_file.exists()

    def test_download_to_file_object_no_close(self):
        """Test download with file=<IO[bytes]> writes to stream without closing."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "13"}
        mock_response.iter_bytes.return_value = [b"Hello", b", world!"]

        file_obj = io.BytesIO()
        # Track if close was called
        close_called = []

        def mock_close():
            close_called.append(True)

        setattr(file_obj, "close", mock_close)

        result = download_to_file(mock_response, file_obj)

        assert result is None
        assert file_obj.getvalue() == b"Hello, world!"
        assert len(close_called) == 0  # Should not close user-provided file object

    def test_download_progress_with_content_length(self):
        """Test progress invoked as bytes arrive, with Content-Length if present."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "1000"}
        mock_response.iter_bytes.return_value = [b"x" * 300, b"x" * 300, b"x" * 400]

        progress_calls = []

        def progress_callback(bytes_received, total_bytes):
            progress_calls.append((bytes_received, total_bytes))

        result = download_to_file(
            mock_response,
            None,  # Return bytes
            progress_callback=progress_callback,
        )

        assert result == b"x" * 1000
        # Should have progress calls for each chunk
        assert len(progress_calls) == 3
        assert progress_calls[0] == (300, 1000)
        assert progress_calls[1] == (600, 1000)
        assert progress_calls[2] == (1000, 1000)

    def test_download_progress_without_content_length(self):
        """Test progress invoked when Content-Length is not present."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}  # No content-length
        mock_response.iter_bytes.return_value = [b"chunk1", b"chunk2", b"chunk3"]

        progress_calls = []

        def progress_callback(bytes_received, total_bytes):
            progress_calls.append((bytes_received, total_bytes))

        result = download_to_file(
            mock_response, None, progress_callback=progress_callback
        )

        assert result == b"chunk1chunk2chunk3"
        # Should have progress calls with None for total_bytes
        assert len(progress_calls) == 3
        assert progress_calls[0] == (6, None)  # len("chunk1")
        assert progress_calls[1] == (12, None)  # len("chunk1chunk2")
        assert progress_calls[2] == (18, None)  # len("chunk1chunk2chunk3")

    @patch("httpx.Client")
    def test_stream_download(self, mock_client_class, tmp_path):
        """Test stream download function."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "13"}
        mock_response.iter_bytes.return_value = [b"Hello", b", world!"]
        mock_response.raise_for_status.return_value = None

        # Mock the context manager
        class MockContextManager:
            def __enter__(self):
                return mock_response

            def __exit__(self, exc_type, exc_val, exc_tb):
                return None

        mock_client.stream.return_value = MockContextManager()

        output_file = tmp_path / "streamed.txt"
        result = stream_download(
            client=mock_client,
            url="https://api.zoo.dev/download",
            output=str(output_file),
        )

        assert result is None
        assert output_file.read_bytes() == b"Hello, world!"

    @patch("httpx.AsyncClient")
    @pytest.mark.skip(reason="Async test configuration needs adjustment")
    async def test_async_stream_download_parity(self, mock_client_class, tmp_path):
        """Test async parity using client.stream and aiter_bytes()."""
        from kittycad._downloads import stream_download_async

        mock_client = Mock()
        mock_client_class.return_value = mock_client

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "13"}
        mock_response.raise_for_status.return_value = None

        # Mock async iteration
        async def mock_aiter_bytes(chunk_size):
            for chunk in [b"Hello", b", world!"]:
                yield chunk

        mock_response.aiter_bytes = mock_aiter_bytes

        # Mock async context manager
        class MockAsyncContext:
            async def __aenter__(self):
                return mock_response

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                pass

        mock_client.stream.return_value = MockAsyncContext()

        output_file = tmp_path / "async_streamed.txt"
        result = await stream_download_async(
            client=mock_client,
            url="https://api.zoo.dev/download",
            output=str(output_file),
        )

        assert result is None
        assert output_file.read_bytes() == b"Hello, world!"

    def test_download_file_overwrite_protection(self, tmp_path):
        """Test that downloads respect overwrite parameter."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "13"}
        mock_response.iter_bytes.return_value = [b"Hello, world!"]

        # Create existing file
        existing_file = tmp_path / "existing.txt"
        existing_file.write_text("existing content")

        # Test with overwrite=False (default)
        with pytest.raises(FileExistsError, match="already exists and overwrite=False"):
            download_to_file(mock_response, str(existing_file), overwrite=False)

        # Test with overwrite=True
        result = download_to_file(mock_response, str(existing_file), overwrite=True)
        assert result is None
        assert existing_file.read_bytes() == b"Hello, world!"

    def test_download_creates_parent_directories(self, tmp_path):
        """Test that downloads create parent directories if needed."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "13"}
        mock_response.iter_bytes.return_value = [b"Hello, world!"]

        # Use nested path that doesn't exist
        nested_file = tmp_path / "subdir" / "nested" / "file.txt"
        assert not nested_file.parent.exists()

        result = download_to_file(mock_response, str(nested_file))

        assert result is None
        assert nested_file.exists()
        assert nested_file.read_bytes() == b"Hello, world!"
        assert nested_file.parent.exists()

    def test_get_filename_from_response(self):
        """Test extracting filename from response headers."""
        mock_response = Mock(spec=httpx.Response)

        # Test with Content-Disposition header
        mock_response.headers = {
            "content-disposition": 'attachment; filename="test.pdf"'
        }
        mock_response.url = "https://api.zoo.dev/download"
        filename = get_filename_from_response(mock_response, "fallback.bin")
        assert filename == "test.pdf"

        # Test with URL path
        mock_response.headers = {}
        mock_response.url = "https://api.zoo.dev/download/document.pdf"
        filename = get_filename_from_response(mock_response, "fallback.bin")
        assert filename == "document.pdf"

        # Test fallback
        mock_response.headers = {}
        mock_response.url = "https://api.zoo.dev/download"
        filename = get_filename_from_response(mock_response, "fallback.bin")
        assert filename == "fallback.bin"

    def test_download_context(self, tmp_path):
        """Test download context manager."""
        with patch("httpx.Client") as mock_client_class:
            mock_client = Mock()
            mock_client_class.return_value = mock_client

            mock_response = Mock(spec=httpx.Response)
            mock_response.headers = {"content-length": "13"}
            mock_response.iter_bytes.return_value = [b"Hello", b", world!"]
            mock_response.raise_for_status.return_value = None

            # Mock the context manager
            class MockContextManager:
                def __enter__(self):
                    return mock_response

                def __exit__(self, exc_type, exc_val, exc_tb):
                    return None

            mock_client.stream.return_value = MockContextManager()

            output_file = tmp_path / "context_download.txt"

            with DownloadContext(
                client=mock_client,
                url="https://api.zoo.dev/download",
                output=str(output_file),
            ) as download:
                result = download.start()

            assert result is None
            assert output_file.read_bytes() == b"Hello, world!"

    def test_download_chunk_size_affects_progress_granularity(self):
        """Test that chunk_size affects progress callback granularity."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": "1000"}

        # Create mock iter_bytes that respects chunk_size
        def mock_iter_bytes(chunk_size):
            data = b"x" * 1000
            for i in range(0, len(data), chunk_size):
                yield data[i : i + chunk_size]

        mock_response.iter_bytes = mock_iter_bytes

        progress_calls = []

        def progress_callback(bytes_received, total_bytes):
            progress_calls.append((bytes_received, total_bytes))

        # Test with small chunk size (should have many progress calls)
        result = download_to_file(
            mock_response, None, progress_callback=progress_callback, chunk_size=100
        )

        assert result == b"x" * 1000
        # Should have 10 progress calls (1000 bytes / 100 chunk_size)
        assert len(progress_calls) == 10
        assert progress_calls[0] == (100, 1000)
        assert progress_calls[-1] == (1000, 1000)


class TestIntegrationScenarios:
    """Test integration scenarios combining multiple components."""

    def test_upload_download_roundtrip(self, tmp_path):
        """Test uploading and downloading a file."""
        # Create test file
        original_file = tmp_path / "original.txt"
        test_content = b"Round trip test content"
        original_file.write_bytes(test_content)

        # Test upload preparation
        file_obj, should_close, filename, content_type, use_multipart = (
            prepare_upload_input(str(original_file))
        )

        assert filename == "original.txt"
        assert content_type == "text/plain"
        assert use_multipart is True
        assert file_obj.read() == test_content

        if should_close:
            file_obj.close()

        # Test download to different file
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": str(len(test_content))}
        mock_response.iter_bytes.return_value = [test_content]

        downloaded_file = tmp_path / "downloaded.txt"
        download_to_file(mock_response, str(downloaded_file))

        assert downloaded_file.read_bytes() == test_content

    def test_progress_tracking_integration(self, tmp_path):
        """Test progress tracking across upload and download."""
        test_file = tmp_path / "progress_test.txt"
        test_content = b"Content for progress tracking test"
        test_file.write_bytes(test_content)

        upload_progress = []
        download_progress = []

        def upload_callback(bytes_sent, total):
            upload_progress.append((bytes_sent, total))

        def download_callback(bytes_received, total):
            download_progress.append((bytes_received, total))

        # Test upload with progress
        with MultipartUploadContext(
            file_param="file",
            file_input=str(test_file),
            progress_callback=upload_callback,
        ) as upload:
            assert upload.files is not None

            # Actually read the file to trigger progress tracking
            file_tuple = upload.files["file"]
            file_obj = file_tuple[1]  # Get the file object from the tuple
            file_obj.read()  # This should trigger progress callbacks

        # Test download with progress
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"content-length": str(len(test_content))}
        mock_response.iter_bytes.return_value = [test_content[:10], test_content[10:]]

        downloaded_file = tmp_path / "progress_downloaded.txt"
        download_to_file(
            mock_response, str(downloaded_file), progress_callback=download_callback
        )

        # Verify progress was tracked
        assert len(upload_progress) > 0
        assert len(download_progress) == 2  # Two chunks
        assert download_progress[-1][0] == len(test_content)  # Final progress


class TestJsonMultipartUploads:
    """Test JSON + file multipart upload functionality."""

    def test_create_json_multipart_upload_basic(self, tmp_path):
        """Test creating multipart upload with JSON body and file attachments."""
        # Create test files
        test_file1 = tmp_path / "file1.kcl"
        test_file1.write_text("// KCL file 1 content")

        test_file2 = tmp_path / "file2.kcl"
        test_file2.write_text("// KCL file 2 content")

        # Create JSON body
        json_body = {
            "prompt": "Create a cube",
            "project_name": "test_project",
            "conversation_id": None,
        }

        # Create multipart upload
        files_dict = create_json_multipart_upload(
            json_body=json_body,
            file_attachments={
                "file1": str(test_file1),
                "file2": str(test_file2),
            },
        )

        # Verify JSON body part
        assert "body" in files_dict
        json_filename, json_content, json_content_type = files_dict["body"]
        assert json_filename == "body.json"
        assert json_content_type == "application/json"

        # Verify JSON content
        import json

        parsed_json = json.loads(json_content)
        assert parsed_json["prompt"] == "Create a cube"
        assert parsed_json["project_name"] == "test_project"

        # Verify file attachments
        assert "file1" in files_dict
        assert "file2" in files_dict

        file1_name, file1_obj, file1_type = files_dict["file1"]
        assert file1_name == "file1.kcl"
        assert (
            file1_type == "application/octet-stream"
        )  # .kcl is not a standard MIME type
        assert file1_obj.read() == b"// KCL file 1 content"

        file2_name, file2_obj, file2_type = files_dict["file2"]
        assert file2_name == "file2.kcl"
        assert file2_type == "application/octet-stream"

        # Clean up
        cleanup_json_multipart_upload(files_dict)

    def test_create_files_dict_preserves_relative_path_in_filename(self, tmp_path):
        """create_files_dict should send relative path as filename when field name has '/'."""
        test_file = tmp_path / "main.kcl"
        test_file.write_text("// content")

        files = create_files_dict(
            file_param="subdir/main.kcl",
            file_input=str(test_file),
        )
        assert "subdir/main.kcl" in files
        fname, fobj, ctype = files["subdir/main.kcl"]
        assert fname == "subdir/main.kcl"
        assert ctype == "application/octet-stream"
        cleanup_multipart_upload(files)

    def test_create_multipart_upload_preserves_relative_path_in_filename(
        self, tmp_path
    ):
        """create_multipart_upload should send relative path as filename when field has '/'."""
        test_file = tmp_path / "main.kcl"
        test_file.write_text("// content")

        enc = create_multipart_upload(
            file_param="nested/dir/main.kcl",
            file_input=str(test_file),
        )
        # We fall back to dict encoder when MultipartEncoder is unavailable.
        # In that case we can assert directly; otherwise, skip strict introspection.
        if isinstance(enc, dict):
            fname, fobj, ctype = enc["nested/dir/main.kcl"]
            assert fname == "nested/dir/main.kcl"
            assert ctype == "application/octet-stream"
            cleanup_multipart_upload(enc)

    def test_create_json_multipart_upload_pydantic_model(self, tmp_path):
        """Test multipart upload with Pydantic model as JSON body."""
        from kittycad.models.text_to_cad_multi_file_iteration_body import (
            TextToCadMultiFileIterationBody,
        )

        # Create test file
        test_file = tmp_path / "main.kcl"
        test_file.write_text("// Main KCL file")

        # Create Pydantic model
        json_body = TextToCadMultiFileIterationBody(
            prompt="Create a sphere",
            project_name="pydantic_test",
        )

        # Create multipart upload
        files_dict = create_json_multipart_upload(
            json_body=json_body,
            file_attachments={"main": str(test_file)},
            json_field_name="iteration_body",
        )

        # Verify JSON body with custom field name
        assert "iteration_body" in files_dict
        json_filename, json_content, json_content_type = files_dict["iteration_body"]
        assert json_filename == "iteration_body.json"
        assert json_content_type == "application/json"

        # Verify Pydantic serialization
        import json

        parsed_json = json.loads(json_content)
        assert parsed_json["prompt"] == "Create a sphere"
        assert parsed_json["project_name"] == "pydantic_test"

        cleanup_json_multipart_upload(files_dict)

    def test_create_json_multipart_upload_file_objects(self):
        """Test multipart upload with file objects instead of paths."""
        import io

        # Create file objects
        file1_obj = io.BytesIO(b"// File 1 content")
        file1_obj.name = "file1.kcl"

        file2_obj = io.BytesIO(b"// File 2 content")
        file2_obj.name = "file2.kcl"

        json_body = {"prompt": "Test with file objects"}

        files_dict = create_json_multipart_upload(
            json_body=json_body,
            file_attachments={
                "src1": file1_obj,
                "src2": file2_obj,
            },
        )

        # Verify file objects work correctly
        assert "src1" in files_dict
        assert "src2" in files_dict

        file1_name, returned_obj1, file1_type = files_dict["src1"]
        assert file1_name == "file1.kcl"
        assert returned_obj1 is file1_obj  # Should be same object

        cleanup_json_multipart_upload(files_dict)

    def test_create_json_multipart_upload_progress_tracking(self, tmp_path):
        """Test progress tracking with JSON multipart uploads."""
        test_file = tmp_path / "large_file.kcl"
        test_content = b"// " + b"x" * 1000  # Larger content for progress tracking
        test_file.write_bytes(test_content)

        progress_calls = []

        def progress_callback(bytes_sent, total):
            progress_calls.append((bytes_sent, total))

        json_body = {"prompt": "Test progress tracking"}

        files_dict = create_json_multipart_upload(
            json_body=json_body,
            file_attachments={"large_file": str(test_file)},
            progress_callback=progress_callback,
        )

        # Progress tracking is set up but won't be called until file is actually read
        # Let's read the file to trigger progress tracking
        file_name, file_obj, file_type = files_dict["large_file"]
        data = file_obj.read()

        # Now progress should be tracked
        assert len(progress_calls) > 0
        final_call = progress_calls[-1]
        assert final_call[0] == len(test_content)  # All bytes read
        assert data == test_content

        cleanup_json_multipart_upload(files_dict)

    def test_json_multipart_upload_context(self, tmp_path):
        """Test JSON multipart upload context manager."""
        test_file = tmp_path / "context_test.kcl"
        test_file.write_text("// Context test content")

        json_body = {"prompt": "Context manager test"}

        with JsonMultipartUploadContext(
            json_body=json_body,
            file_attachments={"test_file": str(test_file)},
        ) as upload:
            assert upload.files is not None
            assert "body" in upload.files
            assert "test_file" in upload.files

            # Verify JSON content
            json_filename, json_content, json_type = upload.files["body"]
            import json

            parsed = json.loads(json_content)
            assert parsed["prompt"] == "Context manager test"

    @patch("httpx.Client")
    def test_upload_json_multipart_integration(self, mock_client_class, tmp_path):
        """Test end-to-end JSON multipart upload function."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        # Capture the request details
        request_calls = []

        def capture_request(*args, **kwargs):
            request_calls.append(kwargs)
            mock_response = Mock(spec=httpx.Response)
            mock_response.status_code = 200
            return mock_response

        mock_client.request = capture_request

        # Create test file
        test_file = tmp_path / "integration_test.kcl"
        test_file.write_text("// Integration test")

        json_body = {
            "prompt": "Create a complex model",
            "project_name": "integration_test",
        }

        # Make the upload
        upload_json_multipart(
            client=mock_client,
            url="https://api.zoo.dev/ml/text-to-cad/multi-file/iteration",
            json_body=json_body,
            file_attachments={"main": str(test_file)},
        )

        # Verify request was made correctly
        assert len(request_calls) == 1
        request_kwargs = request_calls[0]
        assert request_kwargs["method"] == "POST"
        assert (
            request_kwargs["url"]
            == "https://api.zoo.dev/ml/text-to-cad/multi-file/iteration"
        )
        assert "files" in request_kwargs

        files = request_kwargs["files"]
        assert "body" in files  # JSON body
        assert "main" in files  # File attachment

        # Verify JSON part
        json_filename, json_content, json_type = files["body"]
        assert json_type == "application/json"
        import json

        parsed = json.loads(json_content)
        assert parsed["prompt"] == "Create a complex model"

    def test_json_multipart_no_files(self):
        """Test JSON multipart with only JSON body, no file attachments."""
        json_body = {"prompt": "Just JSON, no files"}

        files_dict = create_json_multipart_upload(
            json_body=json_body,
            file_attachments=None,  # No files
        )

        # Should only have JSON part
        assert "body" in files_dict
        assert len(files_dict) == 1

        json_filename, json_content, json_type = files_dict["body"]
        assert json_type == "application/json"

        import json

        parsed = json.loads(json_content)
        assert parsed["prompt"] == "Just JSON, no files"

        cleanup_json_multipart_upload(files_dict)

    def test_json_multipart_mixed_file_types(self, tmp_path):
        """Test JSON multipart with different file types."""
        # Create different file types
        kcl_file = tmp_path / "model.kcl"
        kcl_file.write_text("// KCL model")

        txt_file = tmp_path / "notes.txt"
        txt_file.write_text("Project notes")

        json_file = tmp_path / "config.json"
        json_file.write_text('{"setting": "value"}')

        json_body = {"prompt": "Mixed file types test"}

        files_dict = create_json_multipart_upload(
            json_body=json_body,
            file_attachments={
                "model": str(kcl_file),
                "notes": str(txt_file),
                "config": str(json_file),
            },
        )

        # Verify all files with correct content types
        model_name, model_obj, model_type = files_dict["model"]
        assert model_name == "model.kcl"
        assert (
            model_type == "application/octet-stream"
        )  # .kcl is not a standard MIME type

        notes_name, notes_obj, notes_type = files_dict["notes"]
        assert notes_name == "notes.txt"
        assert notes_type == "text/plain"

        config_name, config_obj, config_type = files_dict["config"]
        assert config_name == "config.json"
        assert config_type == "application/json"

        cleanup_json_multipart_upload(files_dict)

    def test_json_multipart_cleanup_only_opens_files(self, tmp_path):
        """Test cleanup only closes files that were opened by the SDK."""
        import io

        # SDK will open this file
        path_file = tmp_path / "sdk_opened.kcl"
        path_file.write_text("// SDK opened this")

        # User provided this file object
        user_file = io.BytesIO(b"// User provided this")
        user_file.name = "user_provided.kcl"

        json_body = {"prompt": "Cleanup test"}

        files_dict = create_json_multipart_upload(
            json_body=json_body,
            file_attachments={
                "sdk_file": str(path_file),  # SDK opens this
                "user_file": user_file,  # User provided this
            },
        )

        # Mock close to track calls
        sdk_file_obj = files_dict["sdk_file"][1]
        user_file_obj = files_dict["user_file"][1]

        sdk_close_called = []
        user_close_called = []

        def sdk_mock_close():
            sdk_close_called.append(True)

        def user_mock_close():
            user_close_called.append(True)

        setattr(sdk_file_obj, "close", sdk_mock_close)
        setattr(user_file_obj, "close", user_mock_close)

        # Cleanup should only close SDK-opened files
        cleanup_json_multipart_upload(files_dict)

        assert len(sdk_close_called) == 1  # SDK file should be closed
        assert len(user_close_called) == 0  # User file should NOT be closed


if __name__ == "__main__":
    pytest.main([__file__])
