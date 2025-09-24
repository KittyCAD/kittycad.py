"""Windows CA smoke test to ensure the SDK respects platform certificate trust."""

from __future__ import annotations

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


def _attempt_request() -> bool:
    ctx = ssl.create_default_context()
    request = urllib.request.Request(WIN_CA_HOST)
    try:
        with urllib.request.urlopen(request, context=ctx, timeout=5) as resp:
            resp.read()
        return True
    except ssl.SSLCertVerificationError:
        return False
    except urllib.error.URLError as exc:
        # When the certificate is untrusted, URLError will wrap the same SSL error.
        if isinstance(exc.reason, ssl.SSLCertVerificationError):
            return False
        raise


def test_win_ca_smoke() -> None:
    succeeded = _attempt_request()
    if _EXPECT_SUCCESS:
        assert succeeded, "HTTPS request should succeed once the test root is trusted"
    else:
        assert not succeeded, (
            "HTTPS request should fail before the test root is trusted"
        )
