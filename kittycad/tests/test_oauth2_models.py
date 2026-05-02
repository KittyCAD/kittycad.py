import datetime
import json
from typing import cast

from kittycad.models import (
    CreateOAuth2AppRequest,
    OAuth2AppClientType,
    OAuth2AppGrantType,
    OAuth2AppMode,
    OAuth2AppResponse,
    OAuth2AuthorizationDecisionResponse,
    OAuth2AuthorizationRequestResponse,
    OAuth2Scope,
    UpdateOAuth2AppRequest,
)


def test_oauth2_app_request_models_serialize_optional_fields():
    create_request = CreateOAuth2AppRequest(
        grant_types=[
            OAuth2AppGrantType.AUTHORIZATION_CODE,
            OAuth2AppGrantType.REFRESH_TOKEN,
        ],
        mode=OAuth2AppMode.DEVELOPMENT,
        name="Local Modeling App",
        redirect_uris=["http://localhost:3000/oauth/callback"],
    )

    assert create_request.to_dict() == {
        "grant_types": ["authorization_code", "refresh_token"],
        "mode": "development",
        "name": "Local Modeling App",
        "redirect_uris": ["http://localhost:3000/oauth/callback"],
    }

    update_request = UpdateOAuth2AppRequest(
        mode=OAuth2AppMode.PRODUCTION,
        redirect_uris=["https://example.com/oauth/callback"],
    )

    assert update_request.to_dict() == {
        "mode": "production",
        "redirect_uris": ["https://example.com/oauth/callback"],
    }


def test_oauth2_app_response_round_trips_server_json():
    payload = {
        "client_id": "0d0438f5-658c-4f73-94f6-82c2562f38d8",
        "client_type": "public",
        "created_at": "2026-05-02T18:52:36Z",
        "first_party": False,
        "grant_types": ["authorization_code", "device_code"],
        "is_active": True,
        "mode": "production",
        "name": "Production Modeling App",
        "redirect_uris": ["https://example.com/oauth/callback"],
        "updated_at": "2026-05-02T19:01:00Z",
    }

    app = cast(OAuth2AppResponse, OAuth2AppResponse.from_dict(payload))

    assert app.client_id == payload["client_id"]
    assert app.client_type == OAuth2AppClientType.PUBLIC.value
    assert app.grant_types == [
        OAuth2AppGrantType.AUTHORIZATION_CODE.value,
        OAuth2AppGrantType.DEVICE_CODE.value,
    ]
    assert app.mode == OAuth2AppMode.PRODUCTION.value
    assert app.created_at == datetime.datetime(
        2026, 5, 2, 18, 52, 36, tzinfo=datetime.timezone.utc
    )

    dumped = json.loads(app.to_json())
    assert dumped["client_id"] == payload["client_id"]
    assert dumped["client_type"] == "public"
    assert dumped["grant_types"] == ["authorization_code", "device_code"]
    assert dumped["mode"] == "production"


def test_oauth2_authorization_models_serialize_scopes_and_redirects():
    authorization = cast(
        OAuth2AuthorizationRequestResponse,
        OAuth2AuthorizationRequestResponse.from_json(
            json.dumps(
                {
                    "app_name": "Modeling App",
                    "expires_at": "2026-05-02T19:22:36Z",
                    "owner_name": "Zoo",
                    "redirect_uri": "https://example.com/oauth/callback",
                    "request_id": "1b6de6f4-7dfa-4c90-a4e1-bf29f0260772",
                    "scopes": ["modeling", "admin:write"],
                }
            )
        ),
    )

    assert authorization.scopes == [
        OAuth2Scope.MODELING.value,
        OAuth2Scope.ADMIN_WRITE.value,
    ]
    assert authorization.to_dict()["scopes"] == ["modeling", "admin:write"]

    decision = OAuth2AuthorizationDecisionResponse(
        redirect_url="https://example.com/oauth/callback?code=abc"
    )

    assert decision.to_dict() == {
        "redirect_url": "https://example.com/oauth/callback?code=abc"
    }


def test_oauth2_enums_stringify_to_wire_values():
    assert str(OAuth2AppMode.DEVELOPMENT) == "development"
    assert str(OAuth2AppMode.PRODUCTION) == "production"
    assert str(OAuth2Scope.MODELING) == "modeling"
    assert str(OAuth2Scope.ADMIN_WRITE) == "admin:write"
