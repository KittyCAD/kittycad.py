import datetime
from typing import Dict, List, Optional, Union

import pytest

from kittycad import KittyCAD
from kittycad.models import (
    AccountProvider,
    ApiCallQueryGroup,
    ApiCallWithPrice,
    ApiCallWithPriceResultsPage,
    ApiToken,
    ApiTokenResultsPage,
    AppClientInfo,
    AsyncApiCallResultsPage,
    AuthApiKeyResponse,
    CodeOutput,
    ConversationResultsPage,
    CreateShortlinkResponse,
    Customer,
    CustomerBalance,
    DiscountCode,
    ExtendedUser,
    ExtendedUserResultsPage,
    FileCenterOfMass,
    FileConversion,
    FileDensity,
    FileMass,
    FileSurfaceArea,
    FileVolume,
    Invoice,
    IpAddrInfo,
    KclCodeCompletionResponse,
    KclModel,
    MlCopilotClientMessage,
    MlPrompt,
    MlPromptResultsPage,
    Org,
    OrgMember,
    OrgMemberResultsPage,
    OrgResultsPage,
    PaymentIntent,
    PaymentMethod,
    Pong,
    SamlIdentityProvider,
    ServiceAccount,
    ServiceAccountResultsPage,
    Session,
    ShortlinkResultsPage,
    TextToCad,
    TextToCadIteration,
    TextToCadMultiFileIteration,
    TextToCadResponse,
    TextToCadResponseResultsPage,
    UnitAngleConversion,
    UnitAreaConversion,
    UnitCurrentConversion,
    UnitEnergyConversion,
    UnitForceConversion,
    UnitFrequencyConversion,
    UnitLengthConversion,
    UnitMassConversion,
    UnitPowerConversion,
    UnitPressureConversion,
    UnitTemperatureConversion,
    UnitTorqueConversion,
    UnitVolumeConversion,
    User,
    UserOrgInfo,
    UserResultsPage,
    VerificationTokenResponse,
    WebSocketRequest,
    ZooProductSubscriptions,
)
from kittycad.models.add_org_member import AddOrgMember
from kittycad.models.api_call_query_group_by import ApiCallQueryGroupBy
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.api_token_uuid import ApiTokenUuid
from kittycad.models.axis import Axis
from kittycad.models.axis_direction_pair import AxisDirectionPair
from kittycad.models.base64data import Base64Data
from kittycad.models.billing_info import BillingInfo
from kittycad.models.code_language import CodeLanguage
from kittycad.models.code_option import CodeOption
from kittycad.models.conversion_params import ConversionParams
from kittycad.models.create_shortlink_request import CreateShortlinkRequest
from kittycad.models.created_at_sort_mode import CreatedAtSortMode
from kittycad.models.crm_data import CrmData
from kittycad.models.direction import Direction
from kittycad.models.email_authentication_form import EmailAuthenticationForm
from kittycad.models.enterprise_subscription_tier_price import (
    EnterpriseSubscriptionTierPrice,
    OptionFlat,
)
from kittycad.models.event import Event, OptionModelingAppEvent
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.file_import_format import FileImportFormat
from kittycad.models.idp_metadata_source import (
    IdpMetadataSource,
    OptionBase64EncodedXml,
)
from kittycad.models.input_format3d import InputFormat3d, OptionStep
from kittycad.models.inquiry_form import InquiryForm
from kittycad.models.inquiry_type import InquiryType
from kittycad.models.kcl_code_completion_params import KclCodeCompletionParams
from kittycad.models.kcl_code_completion_request import KclCodeCompletionRequest
from kittycad.models.ml_copilot_client_message import OptionHeaders, OptionUser
from kittycad.models.ml_feedback import MlFeedback
from kittycad.models.modeling_app_event_type import ModelingAppEventType
from kittycad.models.modeling_app_individual_subscription_tier import (
    ModelingAppIndividualSubscriptionTier,
)
from kittycad.models.modeling_app_organization_subscription_tier import (
    ModelingAppOrganizationSubscriptionTier,
)
from kittycad.models.org_details import OrgDetails
from kittycad.models.output_format3d import OptionPly, OutputFormat3d
from kittycad.models.plan_interval import PlanInterval
from kittycad.models.ply_storage import PlyStorage
from kittycad.models.post_effect_type import PostEffectType
from kittycad.models.privacy_settings import PrivacySettings
from kittycad.models.saml_identity_provider_create import SamlIdentityProviderCreate
from kittycad.models.selection import OptionSceneByName, Selection
from kittycad.models.service_account_uuid import ServiceAccountUuid
from kittycad.models.session_uuid import SessionUuid
from kittycad.models.source_position import SourcePosition
from kittycad.models.source_range import SourceRange
from kittycad.models.source_range_prompt import SourceRangePrompt
from kittycad.models.store_coupon_params import StoreCouponParams
from kittycad.models.subscribe import Subscribe
from kittycad.models.system import System
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody
from kittycad.models.text_to_cad_iteration_body import TextToCadIterationBody
from kittycad.models.text_to_cad_multi_file_iteration_body import (
    TextToCadMultiFileIterationBody,
)
from kittycad.models.unit_angle import UnitAngle
from kittycad.models.unit_area import UnitArea
from kittycad.models.unit_current import UnitCurrent
from kittycad.models.unit_density import UnitDensity
from kittycad.models.unit_energy import UnitEnergy
from kittycad.models.unit_force import UnitForce
from kittycad.models.unit_frequency import UnitFrequency
from kittycad.models.unit_length import UnitLength
from kittycad.models.unit_mass import UnitMass
from kittycad.models.unit_power import UnitPower
from kittycad.models.unit_pressure import UnitPressure
from kittycad.models.unit_temperature import UnitTemperature
from kittycad.models.unit_torque import UnitTorque
from kittycad.models.unit_volume import UnitVolume
from kittycad.models.update_member_to_org_body import UpdateMemberToOrgBody
from kittycad.models.update_payment_balance import UpdatePaymentBalance
from kittycad.models.update_shortlink_request import UpdateShortlinkRequest
from kittycad.models.update_user import UpdateUser
from kittycad.models.user_identifier import UserIdentifier
from kittycad.models.user_org_role import UserOrgRole
from kittycad.models.uuid import Uuid
from kittycad.models.web_socket_request import OptionDebug
from kittycad.models.zoo_product_subscriptions_org_request import (
    ZooProductSubscriptionsOrgRequest,
)
from kittycad.models.zoo_product_subscriptions_user_request import (
    ZooProductSubscriptionsUserRequest,
)


@pytest.mark.skip
def test_get_schema():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result = client.api.meta.get_schema()

    print(result)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_schema_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result = await client.api.meta.get_schema.asyncio()


@pytest.mark.skip
def test_get_ipinfo():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: IpAddrInfo = client.api.meta.get_ipinfo()

    body: IpAddrInfo = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ipinfo_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: IpAddrInfo = await client.api.meta.get_ipinfo.asyncio()


@pytest.mark.skip
def test_create_text_to_cad():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCad = client.api.ml.create_text_to_cad(
        output_format=FileExportFormat.FBX,
        kcl=None,
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )

    body: TextToCad = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCad = await client.api.ml.create_text_to_cad.asyncio(
        output_format=FileExportFormat.FBX,
        kcl=None,
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )


@pytest.mark.skip
def test_get_api_call_metrics():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[ApiCallQueryGroup] = client.api.api_calls.get_api_call_metrics(
        group_by=ApiCallQueryGroupBy.EMAIL
    )

    body: List[ApiCallQueryGroup] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_metrics_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[
        ApiCallQueryGroup
    ] = await client.api.api_calls.get_api_call_metrics.asyncio(
        group_by=ApiCallQueryGroupBy.EMAIL
    )


@pytest.mark.skip
def test_list_api_calls():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPriceResultsPage = client.api.api_calls.list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: ApiCallWithPriceResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPriceResultsPage = (
        await client.api.api_calls.list_api_calls.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
        )
    )


@pytest.mark.skip
def test_get_api_call():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = client.api.api_calls.get_api_call(id="<string>")

    body: ApiCallWithPrice = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = await client.api.api_calls.get_api_call.asyncio(
        id="<string>"
    )


@pytest.mark.skip
def test_apps_github_callback():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.apps.apps_github_callback()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_callback_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.apps.apps_github_callback.asyncio()


@pytest.mark.skip
def test_apps_github_consent():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AppClientInfo = client.api.apps.apps_github_consent()

    body: AppClientInfo = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_consent_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AppClientInfo = await client.api.apps.apps_github_consent.asyncio()


@pytest.mark.skip
def test_apps_github_webhook():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.apps.apps_github_webhook(body=bytes("some bytes", "utf-8"))


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_webhook_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.apps.apps_github_webhook.asyncio(body=bytes("some bytes", "utf-8"))


@pytest.mark.skip
def test_list_async_operations():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AsyncApiCallResultsPage = client.api.api_calls.list_async_operations(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,
        page_token=None,
    )

    body: AsyncApiCallResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_async_operations_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AsyncApiCallResultsPage = (
        await client.api.api_calls.list_async_operations.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            status=ApiCallStatus.QUEUED,
            limit=None,
            page_token=None,
        )
    )


@pytest.mark.skip
def test_get_async_operation():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            TextToCad,
            TextToCadIteration,
            TextToCadMultiFileIteration,
        ]
    ] = client.api.api_calls.get_async_operation(id="<string>")

    body: Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            TextToCad,
            TextToCadIteration,
            TextToCadMultiFileIteration,
        ]
    ] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_async_operation_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            TextToCad,
            TextToCadIteration,
            TextToCadMultiFileIteration,
        ]
    ] = await client.api.api_calls.get_async_operation.asyncio(id="<string>")


@pytest.mark.skip
def test_auth_api_key():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AuthApiKeyResponse = client.api.hidden.auth_api_key()

    body: AuthApiKeyResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_api_key_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AuthApiKeyResponse = await client.api.hidden.auth_api_key.asyncio()


@pytest.mark.skip
def test_auth_email():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: VerificationTokenResponse = client.api.hidden.auth_email(
        body=EmailAuthenticationForm(
            email="<string>",
        )
    )

    body: VerificationTokenResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: VerificationTokenResponse = await client.api.hidden.auth_email.asyncio(
        body=EmailAuthenticationForm(
            email="<string>",
        )
    )


@pytest.mark.skip
def test_auth_email_callback():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.hidden.auth_email_callback(
        email="<string>", token="<string>", callback_url=None
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_callback_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.hidden.auth_email_callback.asyncio(
        email="<string>", token="<string>", callback_url=None
    )


@pytest.mark.skip
def test_get_auth_saml_by_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.hidden.get_auth_saml_by_org(org_id=Uuid("<string>"), callback_url=None)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_auth_saml_by_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.hidden.get_auth_saml_by_org.asyncio(
        org_id=Uuid("<string>"), callback_url=None
    )


@pytest.mark.skip
def test_get_auth_saml():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.hidden.get_auth_saml(provider_id=Uuid("<string>"), callback_url=None)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_auth_saml_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.hidden.get_auth_saml.asyncio(
        provider_id=Uuid("<string>"), callback_url=None
    )


@pytest.mark.skip
def test_post_auth_saml():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.hidden.post_auth_saml(
        provider_id=Uuid("<string>"), body=bytes("some bytes", "utf-8")
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_post_auth_saml_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.hidden.post_auth_saml.asyncio(
        provider_id=Uuid("<string>"), body=bytes("some bytes", "utf-8")
    )


@pytest.mark.skip
def test_community_sso():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.meta.community_sso(sig="<string>", sso="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_community_sso_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.meta.community_sso.asyncio(sig="<string>", sso="<string>")


@pytest.mark.skip
def test_create_debug_uploads():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[str] = client.api.meta.create_debug_uploads()

    body: List[str] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_debug_uploads_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[str] = await client.api.meta.create_debug_uploads.asyncio()


@pytest.mark.skip
def test_create_event():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.meta.create_event(
        body=Event(
            OptionModelingAppEvent(
                created_at=datetime.datetime.now(),
                event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
                project_name="<string>",
                source_id="<string>",
                user_id="<string>",
            )
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_event_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.meta.create_event.asyncio(
        body=Event(
            OptionModelingAppEvent(
                created_at=datetime.datetime.now(),
                event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
                project_name="<string>",
                source_id="<string>",
                user_id="<string>",
            )
        )
    )


@pytest.mark.skip
def test_create_file_center_of_mass():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileCenterOfMass = client.api.file.create_file_center_of_mass(
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileCenterOfMass = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_center_of_mass_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileCenterOfMass = await client.api.file.create_file_center_of_mass.asyncio(
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_conversion_options():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileConversion = client.api.file.create_file_conversion_options(
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionPly(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    selection=Selection(
                        OptionSceneByName(
                            name="<string>",
                        )
                    ),
                    storage=PlyStorage.ASCII,
                    units=UnitLength.CM,
                )
            ),
            src_format=InputFormat3d(
                OptionStep(
                    split_closed_faces=False,
                )
            ),
        )
    )

    body: FileConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_options_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileConversion = (
        await client.api.file.create_file_conversion_options.asyncio(
            body=ConversionParams(
                output_format=OutputFormat3d(
                    OptionPly(
                        coords=System(
                            forward=AxisDirectionPair(
                                axis=Axis.Y,
                                direction=Direction.POSITIVE,
                            ),
                            up=AxisDirectionPair(
                                axis=Axis.Y,
                                direction=Direction.POSITIVE,
                            ),
                        ),
                        selection=Selection(
                            OptionSceneByName(
                                name="<string>",
                            )
                        ),
                        storage=PlyStorage.ASCII,
                        units=UnitLength.CM,
                    )
                ),
                src_format=InputFormat3d(
                    OptionStep(
                        split_closed_faces=False,
                    )
                ),
            )
        )
    )


@pytest.mark.skip
def test_create_file_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileConversion = client.api.file.create_file_conversion(
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileConversion = await client.api.file.create_file_conversion.asyncio(
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_density():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileDensity = client.api.file.create_file_density(
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileDensity = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_density_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileDensity = await client.api.file.create_file_density.asyncio(
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_execution():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CodeOutput = client.api.executor.create_file_execution(
        lang=CodeLanguage.GO, output=None, body=bytes("some bytes", "utf-8")
    )

    body: CodeOutput = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_execution_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CodeOutput = await client.api.executor.create_file_execution.asyncio(
        lang=CodeLanguage.GO, output=None, body=bytes("some bytes", "utf-8")
    )


@pytest.mark.skip
def test_create_file_mass():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileMass = client.api.file.create_file_mass(
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileMass = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_mass_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileMass = await client.api.file.create_file_mass.asyncio(
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_surface_area():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileSurfaceArea = client.api.file.create_file_surface_area(
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileSurfaceArea = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_surface_area_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileSurfaceArea = await client.api.file.create_file_surface_area.asyncio(
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_volume():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileVolume = client.api.file.create_file_volume(
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileVolume = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_volume_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileVolume = await client.api.file.create_file_volume.asyncio(
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_internal_get_api_token_for_discord_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = client.api.meta.internal_get_api_token_for_discord_user(
        discord_id="<string>"
    )

    body: ApiToken = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_internal_get_api_token_for_discord_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = (
        await client.api.meta.internal_get_api_token_for_discord_user.asyncio(
            discord_id="<string>"
        )
    )


@pytest.mark.skip
def test_logout():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.hidden.logout()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_logout_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.hidden.logout.asyncio()


@pytest.mark.skip
def test_list_ml_prompts():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: MlPromptResultsPage = client.api.ml.list_ml_prompts(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: MlPromptResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_ml_prompts_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: MlPromptResultsPage = await client.api.ml.list_ml_prompts.asyncio(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )


@pytest.mark.skip
def test_get_ml_prompt():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: MlPrompt = client.api.ml.get_ml_prompt(id="<string>")

    body: MlPrompt = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ml_prompt_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: MlPrompt = await client.api.ml.get_ml_prompt.asyncio(id="<string>")


@pytest.mark.skip
def test_list_conversations_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ConversationResultsPage = client.api.ml.list_conversations_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: ConversationResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_conversations_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ConversationResultsPage = (
        await client.api.ml.list_conversations_for_user.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
        )
    )


@pytest.mark.skip
def test_create_proprietary_to_kcl():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: KclModel = client.api.ml.create_proprietary_to_kcl(
        code_option=CodeOption.PARSE
    )

    body: KclModel = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_proprietary_to_kcl_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: KclModel = await client.api.ml.create_proprietary_to_kcl.asyncio(
        code_option=CodeOption.PARSE
    )


@pytest.mark.skip
def test_create_kcl_code_completions():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: KclCodeCompletionResponse = client.api.ml.create_kcl_code_completions(
        body=KclCodeCompletionRequest(
            extra=KclCodeCompletionParams(
                language="<string>",
                trim_by_indentation=False,
            ),
            prompt="<string>",
            stop=["<string>"],
            stream=False,
            suffix="<string>",
        )
    )

    body: KclCodeCompletionResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_kcl_code_completions_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: KclCodeCompletionResponse = (
        await client.api.ml.create_kcl_code_completions.asyncio(
            body=KclCodeCompletionRequest(
                extra=KclCodeCompletionParams(
                    language="<string>",
                    trim_by_indentation=False,
                ),
                prompt="<string>",
                stop=["<string>"],
                stream=False,
                suffix="<string>",
            )
        )
    )


@pytest.mark.skip
def test_create_text_to_cad_iteration():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadIteration = client.api.ml.create_text_to_cad_iteration(
        body=TextToCadIterationBody(
            original_source_code="<string>",
            source_ranges=[
                SourceRangePrompt(
                    prompt="<string>",
                    range=SourceRange(
                        end=SourcePosition(
                            column=10,
                            line=10,
                        ),
                        start=SourcePosition(
                            column=10,
                            line=10,
                        ),
                    ),
                )
            ],
        )
    )

    body: TextToCadIteration = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_iteration_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadIteration = (
        await client.api.ml.create_text_to_cad_iteration.asyncio(
            body=TextToCadIterationBody(
                original_source_code="<string>",
                source_ranges=[
                    SourceRangePrompt(
                        prompt="<string>",
                        range=SourceRange(
                            end=SourcePosition(
                                column=10,
                                line=10,
                            ),
                            start=SourcePosition(
                                column=10,
                                line=10,
                            ),
                        ),
                    )
                ],
            )
        )
    )


@pytest.mark.skip
def test_create_text_to_cad_multi_file_iteration():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadMultiFileIteration = (
        client.api.ml.create_text_to_cad_multi_file_iteration(
            body=TextToCadMultiFileIterationBody(
                source_ranges=[
                    SourceRangePrompt(
                        prompt="<string>",
                        range=SourceRange(
                            end=SourcePosition(
                                column=10,
                                line=10,
                            ),
                            start=SourcePosition(
                                column=10,
                                line=10,
                            ),
                        ),
                    )
                ],
            )
        )
    )

    body: TextToCadMultiFileIteration = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_multi_file_iteration_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadMultiFileIteration = (
        await client.api.ml.create_text_to_cad_multi_file_iteration.asyncio(
            body=TextToCadMultiFileIterationBody(
                source_ranges=[
                    SourceRangePrompt(
                        prompt="<string>",
                        range=SourceRange(
                            end=SourcePosition(
                                column=10,
                                line=10,
                            ),
                            start=SourcePosition(
                                column=10,
                                line=10,
                            ),
                        ),
                    )
                ],
            )
        )
    )


@pytest.mark.skip
def test_delete_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.orgs.delete_org()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.orgs.delete_org.asyncio()


@pytest.mark.skip
def test_get_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = client.api.orgs.get_org()

    body: Org = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = await client.api.orgs.get_org.asyncio()


@pytest.mark.skip
def test_create_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = client.api.orgs.create_org(
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        )
    )

    body: Org = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = await client.api.orgs.create_org.asyncio(
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_update_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = client.api.orgs.update_org(
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        )
    )

    body: Org = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = await client.api.orgs.update_org.asyncio(
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_org_list_api_calls():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPriceResultsPage = client.api.api_calls.org_list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: ApiCallWithPriceResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_org_list_api_calls_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPriceResultsPage = (
        await client.api.api_calls.org_list_api_calls.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
        )
    )


@pytest.mark.skip
def test_get_api_call_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = client.api.api_calls.get_api_call_for_org(id="<string>")

    body: ApiCallWithPrice = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = await client.api.api_calls.get_api_call_for_org.asyncio(
        id="<string>"
    )


@pytest.mark.skip
def test_list_org_members():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMemberResultsPage = client.api.orgs.list_org_members(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,
        page_token=None,
    )

    body: OrgMemberResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_org_members_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMemberResultsPage = await client.api.orgs.list_org_members.asyncio(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,
        page_token=None,
    )


@pytest.mark.skip
def test_create_org_member():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = client.api.orgs.create_org_member(
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        )
    )

    body: OrgMember = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_member_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = await client.api.orgs.create_org_member.asyncio(
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        )
    )


@pytest.mark.skip
def test_delete_org_member():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.orgs.delete_org_member(user_id=Uuid("<string>"))


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_member_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.orgs.delete_org_member.asyncio(user_id=Uuid("<string>"))


@pytest.mark.skip
def test_get_org_member():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = client.api.orgs.get_org_member(user_id=Uuid("<string>"))

    body: OrgMember = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_member_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = await client.api.orgs.get_org_member.asyncio(
        user_id=Uuid("<string>")
    )


@pytest.mark.skip
def test_update_org_member():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = client.api.orgs.update_org_member(
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )

    body: OrgMember = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_member_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = await client.api.orgs.update_org_member.asyncio(
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )


@pytest.mark.skip
def test_delete_payment_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.payments.delete_payment_information_for_org()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.payments.delete_payment_information_for_org.asyncio()


@pytest.mark.skip
def test_get_payment_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.api.payments.get_payment_information_for_org()

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = (
        await client.api.payments.get_payment_information_for_org.asyncio()
    )


@pytest.mark.skip
def test_create_payment_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.api.payments.create_payment_information_for_org(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = (
        await client.api.payments.create_payment_information_for_org.asyncio(
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            )
        )
    )


@pytest.mark.skip
def test_update_payment_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.api.payments.update_payment_information_for_org(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = (
        await client.api.payments.update_payment_information_for_org.asyncio(
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            )
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.api.payments.get_payment_balance_for_org(
        include_total_due=False
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = (
        await client.api.payments.get_payment_balance_for_org.asyncio(
            include_total_due=False
        )
    )


@pytest.mark.skip
def test_create_payment_intent_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PaymentIntent = client.api.payments.create_payment_intent_for_org()

    body: PaymentIntent = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PaymentIntent = (
        await client.api.payments.create_payment_intent_for_org.asyncio()
    )


@pytest.mark.skip
def test_list_invoices_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[Invoice] = client.api.payments.list_invoices_for_org()

    body: List[Invoice] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[Invoice] = await client.api.payments.list_invoices_for_org.asyncio()


@pytest.mark.skip
def test_list_payment_methods_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[PaymentMethod] = client.api.payments.list_payment_methods_for_org()

    body: List[PaymentMethod] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_payment_methods_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[
        PaymentMethod
    ] = await client.api.payments.list_payment_methods_for_org.asyncio()


@pytest.mark.skip
def test_delete_payment_method_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.payments.delete_payment_method_for_org(id="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.payments.delete_payment_method_for_org.asyncio(id="<string>")


@pytest.mark.skip
def test_get_org_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.api.payments.get_org_subscription()

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_subscription_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.api.payments.get_org_subscription.asyncio()
    )


@pytest.mark.skip
def test_create_org_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.api.payments.create_org_subscription(
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_subscription_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.api.payments.create_org_subscription.asyncio(
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            )
        )
    )


@pytest.mark.skip
def test_update_org_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.api.payments.update_org_subscription(
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_subscription_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.api.payments.update_org_subscription.asyncio(
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            )
        )
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.payments.validate_customer_tax_information_for_org()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.payments.validate_customer_tax_information_for_org.asyncio()


@pytest.mark.skip
def test_get_org_privacy_settings():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = client.api.orgs.get_org_privacy_settings()

    body: PrivacySettings = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_privacy_settings_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = await client.api.orgs.get_org_privacy_settings.asyncio()


@pytest.mark.skip
def test_update_org_privacy_settings():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = client.api.orgs.update_org_privacy_settings(
        body=PrivacySettings(
            can_train_on_data=False,
        )
    )

    body: PrivacySettings = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_privacy_settings_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = await client.api.orgs.update_org_privacy_settings.asyncio(
        body=PrivacySettings(
            can_train_on_data=False,
        )
    )


@pytest.mark.skip
def test_delete_org_saml_idp():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.orgs.delete_org_saml_idp()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_saml_idp_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.orgs.delete_org_saml_idp.asyncio()


@pytest.mark.skip
def test_get_org_saml_idp():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = client.api.orgs.get_org_saml_idp()

    body: SamlIdentityProvider = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_saml_idp_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = await client.api.orgs.get_org_saml_idp.asyncio()


@pytest.mark.skip
def test_create_org_saml_idp():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = client.api.orgs.create_org_saml_idp(
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        )
    )

    body: SamlIdentityProvider = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_saml_idp_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = await client.api.orgs.create_org_saml_idp.asyncio(
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        )
    )


@pytest.mark.skip
def test_update_org_saml_idp():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = client.api.orgs.update_org_saml_idp(
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        )
    )

    body: SamlIdentityProvider = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_saml_idp_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = await client.api.orgs.update_org_saml_idp.asyncio(
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        )
    )


@pytest.mark.skip
def test_list_service_accounts_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccountResultsPage = (
        client.api.service_accounts.list_service_accounts_for_org(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
        )
    )

    body: ServiceAccountResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_service_accounts_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccountResultsPage = (
        await client.api.service_accounts.list_service_accounts_for_org.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
        )
    )


@pytest.mark.skip
def test_create_service_account_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccount = client.api.service_accounts.create_service_account_for_org(
        label=None
    )

    body: ServiceAccount = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_service_account_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccount = (
        await client.api.service_accounts.create_service_account_for_org.asyncio(
            label=None
        )
    )


@pytest.mark.skip
def test_delete_service_account_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.service_accounts.delete_service_account_for_org(
        token=ServiceAccountUuid("<string>")
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_service_account_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.service_accounts.delete_service_account_for_org.asyncio(
        token=ServiceAccountUuid("<string>")
    )


@pytest.mark.skip
def test_get_service_account_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccount = client.api.service_accounts.get_service_account_for_org(
        token=ServiceAccountUuid("<string>")
    )

    body: ServiceAccount = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_service_account_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccount = (
        await client.api.service_accounts.get_service_account_for_org.asyncio(
            token=ServiceAccountUuid("<string>")
        )
    )


@pytest.mark.skip
def test_get_org_shortlinks():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ShortlinkResultsPage = client.api.orgs.get_org_shortlinks(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: ShortlinkResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_shortlinks_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ShortlinkResultsPage = await client.api.orgs.get_org_shortlinks.asyncio(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )


@pytest.mark.skip
def test_list_orgs():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgResultsPage = client.api.orgs.list_orgs(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: OrgResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_orgs_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgResultsPage = await client.api.orgs.list_orgs.asyncio(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )


@pytest.mark.skip
def test_get_any_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = client.api.orgs.get_any_org(id=Uuid("<string>"))

    body: Org = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_any_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = await client.api.orgs.get_any_org.asyncio(id=Uuid("<string>"))


@pytest.mark.skip
def test_update_enterprise_pricing_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.api.orgs.update_enterprise_pricing_for_org(
        id=Uuid("<string>"),
        body=EnterpriseSubscriptionTierPrice(
            OptionFlat(
                interval=PlanInterval.DAY,
                price=3.14,
            )
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_enterprise_pricing_for_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.api.orgs.update_enterprise_pricing_for_org.asyncio(
            id=Uuid("<string>"),
            body=EnterpriseSubscriptionTierPrice(
                OptionFlat(
                    interval=PlanInterval.DAY,
                    price=3.14,
                )
            ),
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_any_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.api.payments.get_payment_balance_for_any_org(
        include_total_due=False, id=Uuid("<string>")
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = (
        await client.api.payments.get_payment_balance_for_any_org.asyncio(
            include_total_due=False, id=Uuid("<string>")
        )
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.api.payments.update_payment_balance_for_any_org(
        id=Uuid("<string>"), include_total_due=False, body=UpdatePaymentBalance()
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_balance_for_any_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = (
        await client.api.payments.update_payment_balance_for_any_org.asyncio(
            id=Uuid("<string>"), include_total_due=False, body=UpdatePaymentBalance()
        )
    )


@pytest.mark.skip
def test_ping():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Pong = client.api.meta.ping()

    body: Pong = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ping_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Pong = await client.api.meta.ping.asyncio()


@pytest.mark.skip
def test_get_pricing_subscriptions():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Dict = client.api.meta.get_pricing_subscriptions()

    body: Dict = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_pricing_subscriptions_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Dict = await client.api.meta.get_pricing_subscriptions.asyncio()


@pytest.mark.skip
def test_create_store_coupon():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: DiscountCode = client.api.store.create_store_coupon(
        body=StoreCouponParams(
            percent_off=10,
        )
    )

    body: DiscountCode = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_store_coupon_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: DiscountCode = await client.api.store.create_store_coupon.asyncio(
        body=StoreCouponParams(
            percent_off=10,
        )
    )


@pytest.mark.skip
def test_get_angle_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitAngleConversion = client.api.unit.get_angle_unit_conversion(
        input_unit=UnitAngle.DEGREES, output_unit=UnitAngle.DEGREES, value=3.14
    )

    body: UnitAngleConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_angle_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitAngleConversion = (
        await client.api.unit.get_angle_unit_conversion.asyncio(
            input_unit=UnitAngle.DEGREES, output_unit=UnitAngle.DEGREES, value=3.14
        )
    )


@pytest.mark.skip
def test_get_area_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitAreaConversion = client.api.unit.get_area_unit_conversion(
        input_unit=UnitArea.CM2, output_unit=UnitArea.CM2, value=3.14
    )

    body: UnitAreaConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_area_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitAreaConversion = await client.api.unit.get_area_unit_conversion.asyncio(
        input_unit=UnitArea.CM2, output_unit=UnitArea.CM2, value=3.14
    )


@pytest.mark.skip
def test_get_current_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitCurrentConversion = client.api.unit.get_current_unit_conversion(
        input_unit=UnitCurrent.AMPERES, output_unit=UnitCurrent.AMPERES, value=3.14
    )

    body: UnitCurrentConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_current_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitCurrentConversion = (
        await client.api.unit.get_current_unit_conversion.asyncio(
            input_unit=UnitCurrent.AMPERES, output_unit=UnitCurrent.AMPERES, value=3.14
        )
    )


@pytest.mark.skip
def test_get_energy_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitEnergyConversion = client.api.unit.get_energy_unit_conversion(
        input_unit=UnitEnergy.BTU, output_unit=UnitEnergy.BTU, value=3.14
    )

    body: UnitEnergyConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_energy_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitEnergyConversion = (
        await client.api.unit.get_energy_unit_conversion.asyncio(
            input_unit=UnitEnergy.BTU, output_unit=UnitEnergy.BTU, value=3.14
        )
    )


@pytest.mark.skip
def test_get_force_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitForceConversion = client.api.unit.get_force_unit_conversion(
        input_unit=UnitForce.DYNES, output_unit=UnitForce.DYNES, value=3.14
    )

    body: UnitForceConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_force_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitForceConversion = (
        await client.api.unit.get_force_unit_conversion.asyncio(
            input_unit=UnitForce.DYNES, output_unit=UnitForce.DYNES, value=3.14
        )
    )


@pytest.mark.skip
def test_get_frequency_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitFrequencyConversion = client.api.unit.get_frequency_unit_conversion(
        input_unit=UnitFrequency.GIGAHERTZ,
        output_unit=UnitFrequency.GIGAHERTZ,
        value=3.14,
    )

    body: UnitFrequencyConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_frequency_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitFrequencyConversion = (
        await client.api.unit.get_frequency_unit_conversion.asyncio(
            input_unit=UnitFrequency.GIGAHERTZ,
            output_unit=UnitFrequency.GIGAHERTZ,
            value=3.14,
        )
    )


@pytest.mark.skip
def test_get_length_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitLengthConversion = client.api.unit.get_length_unit_conversion(
        input_unit=UnitLength.CM, output_unit=UnitLength.CM, value=3.14
    )

    body: UnitLengthConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_length_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitLengthConversion = (
        await client.api.unit.get_length_unit_conversion.asyncio(
            input_unit=UnitLength.CM, output_unit=UnitLength.CM, value=3.14
        )
    )


@pytest.mark.skip
def test_get_mass_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitMassConversion = client.api.unit.get_mass_unit_conversion(
        input_unit=UnitMass.G, output_unit=UnitMass.G, value=3.14
    )

    body: UnitMassConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_mass_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitMassConversion = await client.api.unit.get_mass_unit_conversion.asyncio(
        input_unit=UnitMass.G, output_unit=UnitMass.G, value=3.14
    )


@pytest.mark.skip
def test_get_power_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitPowerConversion = client.api.unit.get_power_unit_conversion(
        input_unit=UnitPower.BTU_PER_MINUTE,
        output_unit=UnitPower.BTU_PER_MINUTE,
        value=3.14,
    )

    body: UnitPowerConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_power_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitPowerConversion = (
        await client.api.unit.get_power_unit_conversion.asyncio(
            input_unit=UnitPower.BTU_PER_MINUTE,
            output_unit=UnitPower.BTU_PER_MINUTE,
            value=3.14,
        )
    )


@pytest.mark.skip
def test_get_pressure_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitPressureConversion = client.api.unit.get_pressure_unit_conversion(
        input_unit=UnitPressure.ATMOSPHERES,
        output_unit=UnitPressure.ATMOSPHERES,
        value=3.14,
    )

    body: UnitPressureConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_pressure_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitPressureConversion = (
        await client.api.unit.get_pressure_unit_conversion.asyncio(
            input_unit=UnitPressure.ATMOSPHERES,
            output_unit=UnitPressure.ATMOSPHERES,
            value=3.14,
        )
    )


@pytest.mark.skip
def test_get_temperature_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitTemperatureConversion = client.api.unit.get_temperature_unit_conversion(
        input_unit=UnitTemperature.CELSIUS,
        output_unit=UnitTemperature.CELSIUS,
        value=3.14,
    )

    body: UnitTemperatureConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_temperature_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitTemperatureConversion = (
        await client.api.unit.get_temperature_unit_conversion.asyncio(
            input_unit=UnitTemperature.CELSIUS,
            output_unit=UnitTemperature.CELSIUS,
            value=3.14,
        )
    )


@pytest.mark.skip
def test_get_torque_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitTorqueConversion = client.api.unit.get_torque_unit_conversion(
        input_unit=UnitTorque.NEWTON_METRES,
        output_unit=UnitTorque.NEWTON_METRES,
        value=3.14,
    )

    body: UnitTorqueConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_torque_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitTorqueConversion = (
        await client.api.unit.get_torque_unit_conversion.asyncio(
            input_unit=UnitTorque.NEWTON_METRES,
            output_unit=UnitTorque.NEWTON_METRES,
            value=3.14,
        )
    )


@pytest.mark.skip
def test_get_volume_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitVolumeConversion = client.api.unit.get_volume_unit_conversion(
        input_unit=UnitVolume.CM3, output_unit=UnitVolume.CM3, value=3.14
    )

    body: UnitVolumeConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_volume_unit_conversion_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitVolumeConversion = (
        await client.api.unit.get_volume_unit_conversion.asyncio(
            input_unit=UnitVolume.CM3, output_unit=UnitVolume.CM3, value=3.14
        )
    )


@pytest.mark.skip
def test_delete_user_self():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.users.delete_user_self()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_self_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.users.delete_user_self.asyncio()


@pytest.mark.skip
def test_get_user_self():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = client.api.users.get_user_self()

    body: User = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = await client.api.users.get_user_self.asyncio()


@pytest.mark.skip
def test_update_user_self():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = client.api.users.update_user_self(
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            image="<string>",
            last_name="<string>",
            phone="<string>",
        )
    )

    body: User = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_self_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = await client.api.users.update_user_self.asyncio(
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            image="<string>",
            last_name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_user_list_api_calls():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPriceResultsPage = client.api.api_calls.user_list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: ApiCallWithPriceResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_user_list_api_calls_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPriceResultsPage = (
        await client.api.api_calls.user_list_api_calls.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
        )
    )


@pytest.mark.skip
def test_get_api_call_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = client.api.api_calls.get_api_call_for_user(id="<string>")

    body: ApiCallWithPrice = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = await client.api.api_calls.get_api_call_for_user.asyncio(
        id="<string>"
    )


@pytest.mark.skip
def test_list_api_tokens_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiTokenResultsPage = client.api.api_tokens.list_api_tokens_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: ApiTokenResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_tokens_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiTokenResultsPage = (
        await client.api.api_tokens.list_api_tokens_for_user.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
        )
    )


@pytest.mark.skip
def test_create_api_token_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = client.api.api_tokens.create_api_token_for_user(label=None)

    body: ApiToken = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_api_token_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = await client.api.api_tokens.create_api_token_for_user.asyncio(
        label=None
    )


@pytest.mark.skip
def test_delete_api_token_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.api_tokens.delete_api_token_for_user(token=ApiTokenUuid("<string>"))


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_api_token_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.api_tokens.delete_api_token_for_user.asyncio(
        token=ApiTokenUuid("<string>")
    )


@pytest.mark.skip
def test_get_api_token_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = client.api.api_tokens.get_api_token_for_user(
        token=ApiTokenUuid("<string>")
    )

    body: ApiToken = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_token_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = await client.api.api_tokens.get_api_token_for_user.asyncio(
        token=ApiTokenUuid("<string>")
    )


@pytest.mark.skip
def test_patch_user_crm():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.users.patch_user_crm(body=CrmData())


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_patch_user_crm_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.users.patch_user_crm.asyncio(body=CrmData())


@pytest.mark.skip
def test_get_user_self_extended():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUser = client.api.users.get_user_self_extended()

    body: ExtendedUser = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_extended_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUser = await client.api.users.get_user_self_extended.asyncio()


@pytest.mark.skip
def test_put_user_form_self():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.users.put_user_form_self(
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_user_form_self_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.users.put_user_form_self.asyncio(
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        )
    )


@pytest.mark.skip
def test_get_oauth2_providers_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[AccountProvider] = client.api.users.get_oauth2_providers_for_user()

    body: List[AccountProvider] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_oauth2_providers_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[
        AccountProvider
    ] = await client.api.users.get_oauth2_providers_for_user.asyncio()


@pytest.mark.skip
def test_get_user_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserOrgInfo = client.api.orgs.get_user_org()

    body: UserOrgInfo = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_org_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserOrgInfo = await client.api.orgs.get_user_org.asyncio()


@pytest.mark.skip
def test_delete_payment_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.payments.delete_payment_information_for_user()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.payments.delete_payment_information_for_user.asyncio()


@pytest.mark.skip
def test_get_payment_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.api.payments.get_payment_information_for_user()

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = (
        await client.api.payments.get_payment_information_for_user.asyncio()
    )


@pytest.mark.skip
def test_create_payment_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.api.payments.create_payment_information_for_user(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = (
        await client.api.payments.create_payment_information_for_user.asyncio(
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            )
        )
    )


@pytest.mark.skip
def test_update_payment_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.api.payments.update_payment_information_for_user(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = (
        await client.api.payments.update_payment_information_for_user.asyncio(
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            )
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.api.payments.get_payment_balance_for_user(
        include_total_due=False
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = (
        await client.api.payments.get_payment_balance_for_user.asyncio(
            include_total_due=False
        )
    )


@pytest.mark.skip
def test_create_payment_intent_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PaymentIntent = client.api.payments.create_payment_intent_for_user()

    body: PaymentIntent = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PaymentIntent = (
        await client.api.payments.create_payment_intent_for_user.asyncio()
    )


@pytest.mark.skip
def test_list_invoices_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[Invoice] = client.api.payments.list_invoices_for_user()

    body: List[Invoice] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[Invoice] = await client.api.payments.list_invoices_for_user.asyncio()


@pytest.mark.skip
def test_list_payment_methods_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[PaymentMethod] = client.api.payments.list_payment_methods_for_user()

    body: List[PaymentMethod] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_payment_methods_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[
        PaymentMethod
    ] = await client.api.payments.list_payment_methods_for_user.asyncio()


@pytest.mark.skip
def test_delete_payment_method_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.payments.delete_payment_method_for_user(id="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.payments.delete_payment_method_for_user.asyncio(id="<string>")


@pytest.mark.skip
def test_get_user_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.api.payments.get_user_subscription()

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_subscription_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.api.payments.get_user_subscription.asyncio()
    )


@pytest.mark.skip
def test_create_user_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.api.payments.create_user_subscription(
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_user_subscription_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.api.payments.create_user_subscription.asyncio(
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            )
        )
    )


@pytest.mark.skip
def test_update_user_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.api.payments.update_user_subscription(
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_subscription_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.api.payments.update_user_subscription.asyncio(
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            )
        )
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.payments.validate_customer_tax_information_for_user()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.payments.validate_customer_tax_information_for_user.asyncio()


@pytest.mark.skip
def test_get_user_privacy_settings():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = client.api.users.get_user_privacy_settings()

    body: PrivacySettings = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_privacy_settings_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = await client.api.users.get_user_privacy_settings.asyncio()


@pytest.mark.skip
def test_update_user_privacy_settings():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = client.api.users.update_user_privacy_settings(
        body=PrivacySettings(
            can_train_on_data=False,
        )
    )

    body: PrivacySettings = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_privacy_settings_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = (
        await client.api.users.update_user_privacy_settings.asyncio(
            body=PrivacySettings(
                can_train_on_data=False,
            )
        )
    )


@pytest.mark.skip
def test_get_session_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Session = client.api.users.get_session_for_user(
        token=SessionUuid("<string>")
    )

    body: Session = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_session_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Session = await client.api.users.get_session_for_user.asyncio(
        token=SessionUuid("<string>")
    )


@pytest.mark.skip
def test_get_user_shortlinks():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ShortlinkResultsPage = client.api.users.get_user_shortlinks(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: ShortlinkResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_shortlinks_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ShortlinkResultsPage = await client.api.users.get_user_shortlinks.asyncio(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )


@pytest.mark.skip
def test_create_user_shortlink():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CreateShortlinkResponse = client.api.users.create_user_shortlink(
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        )
    )

    body: CreateShortlinkResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_user_shortlink_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CreateShortlinkResponse = (
        await client.api.users.create_user_shortlink.asyncio(
            body=CreateShortlinkRequest(
                restrict_to_org=False,
                url="<string>",
            )
        )
    )


@pytest.mark.skip
def test_delete_user_shortlink():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.users.delete_user_shortlink(key="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_shortlink_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.users.delete_user_shortlink.asyncio(key="<string>")


@pytest.mark.skip
def test_redirect_user_shortlink():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.hidden.redirect_user_shortlink(key="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_redirect_user_shortlink_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.hidden.redirect_user_shortlink.asyncio(key="<string>")


@pytest.mark.skip
def test_update_user_shortlink():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.users.update_user_shortlink(
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_shortlink_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.users.update_user_shortlink.asyncio(
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )


@pytest.mark.skip
def test_list_text_to_cad_models_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadResponseResultsPage = (
        client.api.ml.list_text_to_cad_models_for_user(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            conversation_id=Uuid("<string>"),
            limit=None,
            page_token=None,
            no_models=None,
        )
    )

    body: TextToCadResponseResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_text_to_cad_models_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadResponseResultsPage = (
        await client.api.ml.list_text_to_cad_models_for_user.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            conversation_id=Uuid("<string>"),
            limit=None,
            page_token=None,
            no_models=None,
        )
    )


@pytest.mark.skip
def test_get_text_to_cad_model_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadResponse = client.api.ml.get_text_to_cad_model_for_user(
        id="<string>"
    )

    body: TextToCadResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_text_to_cad_model_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadResponse = (
        await client.api.ml.get_text_to_cad_model_for_user.asyncio(id="<string>")
    )


@pytest.mark.skip
def test_create_text_to_cad_model_feedback():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.ml.create_text_to_cad_model_feedback(
        id="<string>", feedback=MlFeedback.THUMBS_UP
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_model_feedback_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.ml.create_text_to_cad_model_feedback.asyncio(
        id="<string>", feedback=MlFeedback.THUMBS_UP
    )


@pytest.mark.skip
def test_list_users():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserResultsPage = client.api.users.list_users(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: UserResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserResultsPage = await client.api.users.list_users.asyncio(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )


@pytest.mark.skip
def test_list_users_extended():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUserResultsPage = client.api.users.list_users_extended(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )

    body: ExtendedUserResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_extended_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUserResultsPage = (
        await client.api.users.list_users_extended.asyncio(
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
        )
    )


@pytest.mark.skip
def test_get_user_extended():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUser = client.api.users.get_user_extended(
        id=UserIdentifier("<string>")
    )

    body: ExtendedUser = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_extended_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUser = await client.api.users.get_user_extended.asyncio(
        id=UserIdentifier("<string>")
    )


@pytest.mark.skip
def test_get_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = client.api.users.get_user(id=UserIdentifier("<string>"))

    body: User = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = await client.api.users.get_user.asyncio(
        id=UserIdentifier("<string>")
    )


@pytest.mark.skip
def test_list_api_calls_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPriceResultsPage = client.api.api_calls.list_api_calls_for_user(
        id=UserIdentifier("<string>"),
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,
        page_token=None,
    )

    body: ApiCallWithPriceResultsPage = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPriceResultsPage = (
        await client.api.api_calls.list_api_calls_for_user.asyncio(
            id=UserIdentifier("<string>"),
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,
            page_token=None,
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_any_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.api.payments.get_payment_balance_for_any_user(
        id=UserIdentifier("<string>"), include_total_due=False
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = (
        await client.api.payments.get_payment_balance_for_any_user.asyncio(
            id=UserIdentifier("<string>"), include_total_due=False
        )
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.api.payments.update_payment_balance_for_any_user(
        id=UserIdentifier("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_balance_for_any_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = (
        await client.api.payments.update_payment_balance_for_any_user.asyncio(
            id=UserIdentifier("<string>"),
            include_total_due=False,
            body=UpdatePaymentBalance(),
        )
    )


@pytest.mark.skip
def test_update_subscription_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.api.users.update_subscription_for_user(
        id=UserIdentifier("<string>"),
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_subscription_for_user_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.api.users.update_subscription_for_user.asyncio(
            id=UserIdentifier("<string>"),
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )


@pytest.mark.skip
def test_put_public_form():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.users.put_public_form(
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_public_form_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.users.put_public_form.asyncio(
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        )
    )


@pytest.mark.skip
def test_put_public_subscribe():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api.users.put_public_subscribe(
        body=Subscribe(
            email="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_public_subscribe_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api.users.put_public_subscribe.asyncio(
        body=Subscribe(
            email="<string>",
        )
    )


@pytest.mark.skip
def test_create_executor_term():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    with client.api.executor.create_executor_term.WebSocket() as websocket:
        # Send a message.
        websocket.send("{}")

        # Get the messages.
        for message in websocket:
            print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_executor_term_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client.api.executor.create_executor_term.asyncio()

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_ml_copilot_ws():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    with client.api.ml.ml_copilot_ws.WebSocket() as websocket:
        # Send a message.
        websocket.send(
            MlCopilotClientMessage(
                OptionUser(
                    content="<string>",
                    current_files={"<string>": b"<bytes>"},
                    source_ranges=[
                        SourceRangePrompt(
                            prompt="<string>",
                            range=SourceRange(
                                end=SourcePosition(
                                    column=10,
                                    line=10,
                                ),
                                start=SourcePosition(
                                    column=10,
                                    line=10,
                                ),
                            ),
                        )
                    ],
                )
            )
        )

        # Get a message.
        message = websocket.recv()
        print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ml_copilot_ws_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client.api.ml.ml_copilot_ws.asyncio()

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_ml_reasoning_ws():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    with client.api.ml.ml_reasoning_ws.WebSocket(id="<string>") as websocket:
        # Send a message.
        websocket.send(
            MlCopilotClientMessage(
                OptionHeaders(
                    headers={"<string>": "<string>"},
                )
            )
        )

        # Get a message.
        message = websocket.recv()
        print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ml_reasoning_ws_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client.api.ml.ml_reasoning_ws.asyncio(id="<string>")

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_modeling_commands_ws():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    with client.api.modeling.modeling_commands_ws.WebSocket(
        fps=10,
        post_effect=PostEffectType.PHOSPHOR,
        show_grid=False,
        unlocked_framerate=False,
        video_res_height=10,
        video_res_width=10,
        webrtc=False,
        api_call_id=None,
        pool=None,
        replay=None,
    ) as websocket:
        # Send a message.
        websocket.send(WebSocketRequest(OptionDebug()))

        # Get a message.
        message = websocket.recv()
        print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_modeling_commands_ws_async():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client.api.modeling.modeling_commands_ws.asyncio(
        fps=10,
        post_effect=PostEffectType.PHOSPHOR,
        show_grid=False,
        unlocked_framerate=False,
        video_res_height=10,
        video_res_width=10,
        webrtc=False,
        api_call_id=None,
        pool=None,
        replay=None,
    )

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)
