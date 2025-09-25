"""Windows CA smoke test to ensure the SDK respects platform certificate trust."""

from __future__ import annotations

import json
import os
import ssl
import urllib.error
import urllib.request

import pytest

WIN_CA_HOST = os.environ.get("WIN_CA_HOST", "https://127.0.0.1:4443")
_EXPECT_SUCCESS = os.environ.get("WIN_CA_EXPECT_SUCCESS") == "1"

if os.environ.get("WIN_CA_SMOKE") != "1" or os.name != "nt":
    pytest.skip(
        "win-ca smoke skipped unless WIN_CA_SMOKE=1 on Windows", allow_module_level=True
    )


def _attempt_request() -> tuple[bool, str | None]:
    ctx = ssl.create_default_context()
    request = urllib.request.Request(WIN_CA_HOST)
    try:
        with urllib.request.urlopen(request, context=ctx, timeout=5) as resp:
            body = resp.read().decode("utf-8")
        return True, body
    except ssl.SSLCertVerificationError:
        return False, None
    except urllib.error.URLError as exc:
        # When the certificate is untrusted, URLError will wrap the same SSL error.
        if isinstance(exc.reason, ssl.SSLCertVerificationError):
            return False, None
        raise


def test_win_ca_smoke() -> None:
    succeeded, body = _attempt_request()
    if _EXPECT_SUCCESS:
        assert succeeded, "HTTPS request should succeed once the test root is trusted"
        assert body is not None, "HTTPS request should include a response body"
        try:
            payload = json.loads(body)
        except json.JSONDecodeError as exc:
            pytest.fail(f"Expected JSON response, got {body!r}: {exc}")
        assert isinstance(payload, dict), (
            f"Expected JSON object response, got {type(payload).__name__}: {payload!r}"
        )
        assert payload.get("status") == "ok", (
            "HTTPS proxy should return {'status': 'ok'}"
        )
    else:
        assert not succeeded, (
            "HTTPS request should fail before the test root is trusted"
        )
