from typing import List, Optional, Union

import pytest

from kittycad.api.ai import create_image_to_3d, create_text_to_3d
from kittycad.api.api_calls import (
    get_api_call,
    get_api_call_for_user,
    get_api_call_metrics,
    get_async_operation,
    list_api_calls,
    list_api_calls_for_user,
    list_async_operations,
    user_list_api_calls,
)
from kittycad.api.api_tokens import (
    create_api_token_for_user,
    delete_api_token_for_user,
    get_api_token_for_user,
    list_api_tokens_for_user,
)
from kittycad.api.apps import (
    apps_github_callback,
    apps_github_consent,
    apps_github_webhook,
)
from kittycad.api.constant import get_physics_constant
from kittycad.api.executor import create_executor_term, create_file_execution
from kittycad.api.file import (
    create_file_center_of_mass,
    create_file_conversion,
    create_file_conversion_with_base64_helper,
    create_file_density,
    create_file_mass,
    create_file_surface_area,
    create_file_volume,
)
from kittycad.api.hidden import auth_email, auth_email_callback, logout
from kittycad.api.meta import (
    get_ai_plugin_manifest,
    get_metadata,
    get_openai_schema,
    get_schema,
    ping,
)
from kittycad.api.modeling import cmd, cmd_batch, modeling_commands_ws
from kittycad.api.payments import (
    create_payment_information_for_user,
    create_payment_intent_for_user,
    delete_payment_information_for_user,
    delete_payment_method_for_user,
    get_payment_balance_for_user,
    get_payment_information_for_user,
    list_invoices_for_user,
    list_payment_methods_for_user,
    update_payment_information_for_user,
    validate_customer_tax_information_for_user,
)
from kittycad.api.unit import (
    get_acceleration_unit_conversion,
    get_angle_unit_conversion,
    get_angular_velocity_unit_conversion,
    get_area_unit_conversion,
    get_charge_unit_conversion,
    get_concentration_unit_conversion,
    get_data_transfer_rate_unit_conversion,
    get_data_unit_conversion,
    get_density_unit_conversion,
    get_energy_unit_conversion,
    get_force_unit_conversion,
    get_illuminance_unit_conversion,
    get_length_unit_conversion,
    get_magnetic_field_strength_unit_conversion,
    get_magnetic_flux_unit_conversion,
    get_mass_unit_conversion,
    get_metric_power_cubed_unit_conversion,
    get_metric_power_squared_unit_conversion,
    get_metric_power_unit_conversion,
    get_power_unit_conversion,
    get_pressure_unit_conversion,
    get_radiation_unit_conversion,
    get_radioactivity_unit_conversion,
    get_solid_angle_unit_conversion,
    get_temperature_unit_conversion,
    get_time_unit_conversion,
    get_velocity_unit_conversion,
    get_voltage_unit_conversion,
    get_volume_unit_conversion,
)
from kittycad.api.users import (
    delete_user_self,
    get_session_for_user,
    get_user,
    get_user_extended,
    get_user_front_hash_self,
    get_user_onboarding_self,
    get_user_self,
    get_user_self_extended,
    list_users,
    list_users_extended,
    update_user_self,
)
from kittycad.client import ClientFromEnv
from kittycad.models import (
    AiPluginManifest,
    ApiCallQueryGroup,
    ApiCallWithPrice,
    ApiCallWithPriceResultsPage,
    ApiToken,
    ApiTokenResultsPage,
    AppClientInfo,
    AsyncApiCallResultsPage,
    CodeOutput,
    Customer,
    CustomerBalance,
    Error,
    ExtendedUser,
    ExtendedUserResultsPage,
    FileCenterOfMass,
    FileConversion,
    FileDensity,
    FileMass,
    FileSurfaceArea,
    FileVolume,
    Invoice,
    Mesh,
    Metadata,
    ModelingOutcomes,
    Onboarding,
    PaymentIntent,
    PaymentMethod,
    PhysicsConstant,
    Pong,
    Session,
    UnitAccelerationConversion,
    UnitAngleConversion,
    UnitAngularVelocityConversion,
    UnitAreaConversion,
    UnitChargeConversion,
    UnitConcentrationConversion,
    UnitDataConversion,
    UnitDataTransferRateConversion,
    UnitDensityConversion,
    UnitEnergyConversion,
    UnitForceConversion,
    UnitIlluminanceConversion,
    UnitLengthConversion,
    UnitMagneticFieldStrengthConversion,
    UnitMagneticFluxConversion,
    UnitMassConversion,
    UnitMetricPowerConversion,
    UnitMetricPowerCubedConversion,
    UnitMetricPowerSquaredConversion,
    UnitPowerConversion,
    UnitPressureConversion,
    UnitRadiationConversion,
    UnitRadioactivityConversion,
    UnitSolidAngleConversion,
    UnitTemperatureConversion,
    UnitTimeConversion,
    UnitVelocityConversion,
    UnitVoltageConversion,
    UnitVolumeConversion,
    User,
    UserResultsPage,
    VerificationToken,
)
from kittycad.models.api_call_query_group_by import ApiCallQueryGroupBy
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.billing_info import BillingInfo
from kittycad.models.code_language import CodeLanguage
from kittycad.models.created_at_sort_mode import CreatedAtSortMode
from kittycad.models.email_authentication_form import EmailAuthenticationForm
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.file_import_format import FileImportFormat
from kittycad.models.image_type import ImageType
from kittycad.models.line3d import Line3d
from kittycad.models.modeling_cmd_id import ModelingCmdId
from kittycad.models.modeling_cmd_req import ModelingCmdReq
from kittycad.models.modeling_cmd_req_batch import ModelingCmdReqBatch
from kittycad.models.physics_constant_name import PhysicsConstantName
from kittycad.models.point3d import Point3d
from kittycad.models.unit_acceleration_format import UnitAccelerationFormat
from kittycad.models.unit_angle_format import UnitAngleFormat
from kittycad.models.unit_angular_velocity_format import UnitAngularVelocityFormat
from kittycad.models.unit_area_format import UnitAreaFormat
from kittycad.models.unit_charge_format import UnitChargeFormat
from kittycad.models.unit_concentration_format import UnitConcentrationFormat
from kittycad.models.unit_data_format import UnitDataFormat
from kittycad.models.unit_data_transfer_rate_format import UnitDataTransferRateFormat
from kittycad.models.unit_density_format import UnitDensityFormat
from kittycad.models.unit_energy_format import UnitEnergyFormat
from kittycad.models.unit_force_format import UnitForceFormat
from kittycad.models.unit_illuminance_format import UnitIlluminanceFormat
from kittycad.models.unit_length_format import UnitLengthFormat
from kittycad.models.unit_magnetic_field_strength_format import (
    UnitMagneticFieldStrengthFormat,
)
from kittycad.models.unit_magnetic_flux_format import UnitMagneticFluxFormat
from kittycad.models.unit_mass_format import UnitMassFormat
from kittycad.models.unit_metric_power import UnitMetricPower
from kittycad.models.unit_power_format import UnitPowerFormat
from kittycad.models.unit_pressure_format import UnitPressureFormat
from kittycad.models.unit_radiation_format import UnitRadiationFormat
from kittycad.models.unit_radioactivity_format import UnitRadioactivityFormat
from kittycad.models.unit_solid_angle_format import UnitSolidAngleFormat
from kittycad.models.unit_temperature_format import UnitTemperatureFormat
from kittycad.models.unit_time_format import UnitTimeFormat
from kittycad.models.unit_velocity_format import UnitVelocityFormat
from kittycad.models.unit_voltage_format import UnitVoltageFormat
from kittycad.models.unit_volume_format import UnitVolumeFormat
from kittycad.models.update_user import UpdateUser
from kittycad.types import Response


@pytest.mark.skip
def test_get_schema():
    # Create our client.
    client = ClientFromEnv()

    get_schema.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    get_schema.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_schema_async():
    # Create our client.
    client = ClientFromEnv()

    await get_schema.asyncio(
        client=client,
    )

    # OR run async with more info
    await get_schema.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_ai_plugin_manifest():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AiPluginManifest, Error]] = get_ai_plugin_manifest.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: AiPluginManifest = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[AiPluginManifest, Error]]
    ] = get_ai_plugin_manifest.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ai_plugin_manifest_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[AiPluginManifest, Error]
    ] = await get_ai_plugin_manifest.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[AiPluginManifest, Error]]
    ] = await get_ai_plugin_manifest.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_metadata():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Metadata, Error]] = get_metadata.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Metadata = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Metadata, Error]]] = get_metadata.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_metadata_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Metadata, Error]] = await get_metadata.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Metadata, Error]]
    ] = await get_metadata.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_image_to_3d():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Mesh, Error]] = create_image_to_3d.sync(
        client=client,
        input_format=ImageType.PNG,
        output_format=FileExportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Mesh = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Mesh, Error]]] = create_image_to_3d.sync_detailed(
        client=client,
        input_format=ImageType.PNG,
        output_format=FileExportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_image_to_3d_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Mesh, Error]] = await create_image_to_3d.asyncio(
        client=client,
        input_format=ImageType.PNG,
        output_format=FileExportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Mesh, Error]]
    ] = await create_image_to_3d.asyncio_detailed(
        client=client,
        input_format=ImageType.PNG,
        output_format=FileExportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_text_to_3d():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Mesh, Error]] = create_text_to_3d.sync(
        client=client,
        output_format=FileExportFormat.DAE,
        prompt="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Mesh = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Mesh, Error]]] = create_text_to_3d.sync_detailed(
        client=client,
        output_format=FileExportFormat.DAE,
        prompt="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_3d_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Mesh, Error]] = await create_text_to_3d.asyncio(
        client=client,
        output_format=FileExportFormat.DAE,
        prompt="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Mesh, Error]]
    ] = await create_text_to_3d.asyncio_detailed(
        client=client,
        output_format=FileExportFormat.DAE,
        prompt="<string>",
    )


@pytest.mark.skip
def test_get_api_call_metrics():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[ApiCallQueryGroup], Error]] = get_api_call_metrics.sync(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[ApiCallQueryGroup] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[List[ApiCallQueryGroup], Error]]
    ] = get_api_call_metrics.sync_detailed(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_metrics_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[List[ApiCallQueryGroup], Error]
    ] = await get_api_call_metrics.asyncio(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[ApiCallQueryGroup], Error]]
    ] = await get_api_call_metrics.asyncio_detailed(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )


@pytest.mark.skip
def test_list_api_calls():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = list_api_calls.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
    ] = list_api_calls.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = await list_api_calls.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
    ] = await list_api_calls.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_api_call():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = get_api_call.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPrice = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ApiCallWithPrice, Error]]
    ] = get_api_call.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = await get_api_call.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPrice, Error]]
    ] = await get_api_call.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_apps_github_callback():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = apps_github_callback.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = apps_github_callback.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_callback_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await apps_github_callback.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await apps_github_callback.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_apps_github_consent():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AppClientInfo, Error]] = apps_github_consent.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: AppClientInfo = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[AppClientInfo, Error]]
    ] = apps_github_consent.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_consent_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AppClientInfo, Error]] = await apps_github_consent.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[AppClientInfo, Error]]
    ] = await apps_github_consent.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_apps_github_webhook():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = apps_github_webhook.sync(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = apps_github_webhook.sync_detailed(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_webhook_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await apps_github_webhook.asyncio(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await apps_github_webhook.asyncio_detailed(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_list_async_operations():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[AsyncApiCallResultsPage, Error]
    ] = list_async_operations.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: AsyncApiCallResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[AsyncApiCallResultsPage, Error]]
    ] = list_async_operations.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_async_operations_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[AsyncApiCallResultsPage, Error]
    ] = await list_async_operations.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[AsyncApiCallResultsPage, Error]]
    ] = await list_async_operations.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_async_operation():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            Error,
        ]
    ] = get_async_operation.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Union[
        FileConversion,
        FileCenterOfMass,
        FileMass,
        FileVolume,
        FileDensity,
        FileSurfaceArea,
    ] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[
            Union[
                FileConversion,
                FileCenterOfMass,
                FileMass,
                FileVolume,
                FileDensity,
                FileSurfaceArea,
                Error,
            ]
        ]
    ] = get_async_operation.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_async_operation_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            Error,
        ]
    ] = await get_async_operation.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[
            Union[
                FileConversion,
                FileCenterOfMass,
                FileMass,
                FileVolume,
                FileDensity,
                FileSurfaceArea,
                Error,
            ]
        ]
    ] = await get_async_operation.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_auth_email():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[VerificationToken, Error]] = auth_email.sync(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: VerificationToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[VerificationToken, Error]]
    ] = auth_email.sync_detailed(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[VerificationToken, Error]] = await auth_email.asyncio(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[VerificationToken, Error]]
    ] = await auth_email.asyncio_detailed(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )


@pytest.mark.skip
def test_auth_email_callback():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = auth_email_callback.sync(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = auth_email_callback.sync_detailed(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_callback_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await auth_email_callback.asyncio(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await auth_email_callback.asyncio_detailed(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_physics_constant():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[PhysicsConstant, Error]] = get_physics_constant.sync(
        client=client,
        constant=PhysicsConstantName.PI,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: PhysicsConstant = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[PhysicsConstant, Error]]
    ] = get_physics_constant.sync_detailed(
        client=client,
        constant=PhysicsConstantName.PI,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_physics_constant_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[PhysicsConstant, Error]
    ] = await get_physics_constant.asyncio(
        client=client,
        constant=PhysicsConstantName.PI,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[PhysicsConstant, Error]]
    ] = await get_physics_constant.asyncio_detailed(
        client=client,
        constant=PhysicsConstantName.PI,
    )


@pytest.mark.skip
def test_create_file_center_of_mass():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileCenterOfMass, Error]] = create_file_center_of_mass.sync(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileCenterOfMass = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[FileCenterOfMass, Error]]
    ] = create_file_center_of_mass.sync_detailed(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_center_of_mass_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[FileCenterOfMass, Error]
    ] = await create_file_center_of_mass.asyncio(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileCenterOfMass, Error]]
    ] = await create_file_center_of_mass.asyncio_detailed(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_conversion_with_base64_helper():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[FileConversion, Error]
    ] = create_file_conversion_with_base64_helper.sync(
        client=client,
        output_format=FileExportFormat.DAE,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[FileConversion, Error]]
    ] = create_file_conversion.sync_detailed(
        client=client,
        output_format=FileExportFormat.DAE,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_with_base64_helper_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[FileConversion, Error]
    ] = await create_file_conversion_with_base64_helper.asyncio(
        client=client,
        output_format=FileExportFormat.DAE,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileConversion, Error]]
    ] = await create_file_conversion.asyncio_detailed(
        client=client,
        output_format=FileExportFormat.DAE,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_density():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileDensity, Error]] = create_file_density.sync(
        client=client,
        material_mass=3.14,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileDensity = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[FileDensity, Error]]
    ] = create_file_density.sync_detailed(
        client=client,
        material_mass=3.14,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_density_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileDensity, Error]] = await create_file_density.asyncio(
        client=client,
        material_mass=3.14,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileDensity, Error]]
    ] = await create_file_density.asyncio_detailed(
        client=client,
        material_mass=3.14,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_execution():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CodeOutput, Error]] = create_file_execution.sync(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CodeOutput = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[CodeOutput, Error]]
    ] = create_file_execution.sync_detailed(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_execution_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CodeOutput, Error]] = await create_file_execution.asyncio(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CodeOutput, Error]]
    ] = await create_file_execution.asyncio_detailed(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_mass():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileMass, Error]] = create_file_mass.sync(
        client=client,
        material_density=3.14,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileMass = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[FileMass, Error]]
    ] = create_file_mass.sync_detailed(
        client=client,
        material_density=3.14,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_mass_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileMass, Error]] = await create_file_mass.asyncio(
        client=client,
        material_density=3.14,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileMass, Error]]
    ] = await create_file_mass.asyncio_detailed(
        client=client,
        material_density=3.14,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_surface_area():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileSurfaceArea, Error]] = create_file_surface_area.sync(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileSurfaceArea = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[FileSurfaceArea, Error]]
    ] = create_file_surface_area.sync_detailed(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_surface_area_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[FileSurfaceArea, Error]
    ] = await create_file_surface_area.asyncio(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileSurfaceArea, Error]]
    ] = await create_file_surface_area.asyncio_detailed(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_volume():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileVolume, Error]] = create_file_volume.sync(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileVolume = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[FileVolume, Error]]
    ] = create_file_volume.sync_detailed(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_volume_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileVolume, Error]] = await create_file_volume.asyncio(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileVolume, Error]]
    ] = await create_file_volume.asyncio_detailed(
        client=client,
        src_format=FileImportFormat.DAE,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_logout():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = logout.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = logout.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_logout_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await logout.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await logout.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_cmd():
    # Create our client.
    client = ClientFromEnv()

    cmd.sync(
        client=client,
        body=ModelingCmdReq(
            cmd=Line3d(
                from_=Point3d(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                to=Point3d(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
            cmd_id=ModelingCmdId("<uuid>"),
            file_id="<string>",
        ),
    )

    # OR if you need more info (e.g. status_code)
    cmd.sync_detailed(
        client=client,
        body=ModelingCmdReq(
            cmd=Line3d(
                from_=Point3d(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                to=Point3d(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
            cmd_id=ModelingCmdId("<uuid>"),
            file_id="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_cmd_async():
    # Create our client.
    client = ClientFromEnv()

    await cmd.asyncio(
        client=client,
        body=ModelingCmdReq(
            cmd=Line3d(
                from_=Point3d(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                to=Point3d(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
            cmd_id=ModelingCmdId("<uuid>"),
            file_id="<string>",
        ),
    )

    # OR run async with more info
    await cmd.asyncio_detailed(
        client=client,
        body=ModelingCmdReq(
            cmd=Line3d(
                from_=Point3d(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                to=Point3d(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
            cmd_id=ModelingCmdId("<uuid>"),
            file_id="<string>",
        ),
    )


@pytest.mark.skip
def test_cmd_batch():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ModelingOutcomes, Error]] = cmd_batch.sync(
        client=client,
        body=ModelingCmdReqBatch(
            cmds={
                "<string>": ModelingCmdReq(
                    cmd=Line3d(
                        from_=Point3d(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        to=Point3d(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                    cmd_id=ModelingCmdId("<uuid>"),
                    file_id="<string>",
                )
            },
            file_id="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ModelingOutcomes = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ModelingOutcomes, Error]]
    ] = cmd_batch.sync_detailed(
        client=client,
        body=ModelingCmdReqBatch(
            cmds={
                "<string>": ModelingCmdReq(
                    cmd=Line3d(
                        from_=Point3d(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        to=Point3d(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                    cmd_id=ModelingCmdId("<uuid>"),
                    file_id="<string>",
                )
            },
            file_id="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_cmd_batch_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ModelingOutcomes, Error]] = await cmd_batch.asyncio(
        client=client,
        body=ModelingCmdReqBatch(
            cmds={
                "<string>": ModelingCmdReq(
                    cmd=Line3d(
                        from_=Point3d(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        to=Point3d(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                    cmd_id=ModelingCmdId("<uuid>"),
                    file_id="<string>",
                )
            },
            file_id="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ModelingOutcomes, Error]]
    ] = await cmd_batch.asyncio_detailed(
        client=client,
        body=ModelingCmdReqBatch(
            cmds={
                "<string>": ModelingCmdReq(
                    cmd=Line3d(
                        from_=Point3d(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        to=Point3d(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                    cmd_id=ModelingCmdId("<uuid>"),
                    file_id="<string>",
                )
            },
            file_id="<string>",
        ),
    )


@pytest.mark.skip
def test_get_openai_schema():
    # Create our client.
    client = ClientFromEnv()

    get_openai_schema.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    get_openai_schema.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_openai_schema_async():
    # Create our client.
    client = ClientFromEnv()

    await get_openai_schema.asyncio(
        client=client,
    )

    # OR run async with more info
    await get_openai_schema.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_ping():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Pong, Error]] = ping.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Pong = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Pong, Error]]] = ping.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ping_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Pong, Error]] = await ping.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Union[Pong, Error]]] = await ping.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_acceleration_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAccelerationConversion, Error]
    ] = get_acceleration_unit_conversion.sync(
        client=client,
        output_format=UnitAccelerationFormat.METERS_PER_SECOND_SQUARED,
        src_format=UnitAccelerationFormat.METERS_PER_SECOND_SQUARED,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitAccelerationConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitAccelerationConversion, Error]]
    ] = get_acceleration_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitAccelerationFormat.METERS_PER_SECOND_SQUARED,
        src_format=UnitAccelerationFormat.METERS_PER_SECOND_SQUARED,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_acceleration_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAccelerationConversion, Error]
    ] = await get_acceleration_unit_conversion.asyncio(
        client=client,
        output_format=UnitAccelerationFormat.METERS_PER_SECOND_SQUARED,
        src_format=UnitAccelerationFormat.METERS_PER_SECOND_SQUARED,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitAccelerationConversion, Error]]
    ] = await get_acceleration_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitAccelerationFormat.METERS_PER_SECOND_SQUARED,
        src_format=UnitAccelerationFormat.METERS_PER_SECOND_SQUARED,
        value=3.14,
    )


@pytest.mark.skip
def test_get_angle_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAngleConversion, Error]
    ] = get_angle_unit_conversion.sync(
        client=client,
        output_format=UnitAngleFormat.RADIAN,
        src_format=UnitAngleFormat.RADIAN,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitAngleConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitAngleConversion, Error]]
    ] = get_angle_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitAngleFormat.RADIAN,
        src_format=UnitAngleFormat.RADIAN,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_angle_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAngleConversion, Error]
    ] = await get_angle_unit_conversion.asyncio(
        client=client,
        output_format=UnitAngleFormat.RADIAN,
        src_format=UnitAngleFormat.RADIAN,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitAngleConversion, Error]]
    ] = await get_angle_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitAngleFormat.RADIAN,
        src_format=UnitAngleFormat.RADIAN,
        value=3.14,
    )


@pytest.mark.skip
def test_get_angular_velocity_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAngularVelocityConversion, Error]
    ] = get_angular_velocity_unit_conversion.sync(
        client=client,
        output_format=UnitAngularVelocityFormat.RADIANS_PER_SECOND,
        src_format=UnitAngularVelocityFormat.RADIANS_PER_SECOND,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitAngularVelocityConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitAngularVelocityConversion, Error]]
    ] = get_angular_velocity_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitAngularVelocityFormat.RADIANS_PER_SECOND,
        src_format=UnitAngularVelocityFormat.RADIANS_PER_SECOND,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_angular_velocity_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAngularVelocityConversion, Error]
    ] = await get_angular_velocity_unit_conversion.asyncio(
        client=client,
        output_format=UnitAngularVelocityFormat.RADIANS_PER_SECOND,
        src_format=UnitAngularVelocityFormat.RADIANS_PER_SECOND,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitAngularVelocityConversion, Error]]
    ] = await get_angular_velocity_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitAngularVelocityFormat.RADIANS_PER_SECOND,
        src_format=UnitAngularVelocityFormat.RADIANS_PER_SECOND,
        value=3.14,
    )


@pytest.mark.skip
def test_get_area_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UnitAreaConversion, Error]] = get_area_unit_conversion.sync(
        client=client,
        output_format=UnitAreaFormat.SQUARE_METER,
        src_format=UnitAreaFormat.SQUARE_METER,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitAreaConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitAreaConversion, Error]]
    ] = get_area_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitAreaFormat.SQUARE_METER,
        src_format=UnitAreaFormat.SQUARE_METER,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_area_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAreaConversion, Error]
    ] = await get_area_unit_conversion.asyncio(
        client=client,
        output_format=UnitAreaFormat.SQUARE_METER,
        src_format=UnitAreaFormat.SQUARE_METER,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitAreaConversion, Error]]
    ] = await get_area_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitAreaFormat.SQUARE_METER,
        src_format=UnitAreaFormat.SQUARE_METER,
        value=3.14,
    )


@pytest.mark.skip
def test_get_charge_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitChargeConversion, Error]
    ] = get_charge_unit_conversion.sync(
        client=client,
        output_format=UnitChargeFormat.COULOMB,
        src_format=UnitChargeFormat.COULOMB,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitChargeConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitChargeConversion, Error]]
    ] = get_charge_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitChargeFormat.COULOMB,
        src_format=UnitChargeFormat.COULOMB,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_charge_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitChargeConversion, Error]
    ] = await get_charge_unit_conversion.asyncio(
        client=client,
        output_format=UnitChargeFormat.COULOMB,
        src_format=UnitChargeFormat.COULOMB,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitChargeConversion, Error]]
    ] = await get_charge_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitChargeFormat.COULOMB,
        src_format=UnitChargeFormat.COULOMB,
        value=3.14,
    )


@pytest.mark.skip
def test_get_concentration_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitConcentrationConversion, Error]
    ] = get_concentration_unit_conversion.sync(
        client=client,
        output_format=UnitConcentrationFormat.PARTS_PER_MILLION,
        src_format=UnitConcentrationFormat.PARTS_PER_MILLION,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitConcentrationConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitConcentrationConversion, Error]]
    ] = get_concentration_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitConcentrationFormat.PARTS_PER_MILLION,
        src_format=UnitConcentrationFormat.PARTS_PER_MILLION,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_concentration_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitConcentrationConversion, Error]
    ] = await get_concentration_unit_conversion.asyncio(
        client=client,
        output_format=UnitConcentrationFormat.PARTS_PER_MILLION,
        src_format=UnitConcentrationFormat.PARTS_PER_MILLION,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitConcentrationConversion, Error]]
    ] = await get_concentration_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitConcentrationFormat.PARTS_PER_MILLION,
        src_format=UnitConcentrationFormat.PARTS_PER_MILLION,
        value=3.14,
    )


@pytest.mark.skip
def test_get_data_transfer_rate_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitDataTransferRateConversion, Error]
    ] = get_data_transfer_rate_unit_conversion.sync(
        client=client,
        output_format=UnitDataTransferRateFormat.BYTES_PER_SECOND,
        src_format=UnitDataTransferRateFormat.BYTES_PER_SECOND,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitDataTransferRateConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitDataTransferRateConversion, Error]]
    ] = get_data_transfer_rate_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitDataTransferRateFormat.BYTES_PER_SECOND,
        src_format=UnitDataTransferRateFormat.BYTES_PER_SECOND,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_data_transfer_rate_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitDataTransferRateConversion, Error]
    ] = await get_data_transfer_rate_unit_conversion.asyncio(
        client=client,
        output_format=UnitDataTransferRateFormat.BYTES_PER_SECOND,
        src_format=UnitDataTransferRateFormat.BYTES_PER_SECOND,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitDataTransferRateConversion, Error]]
    ] = await get_data_transfer_rate_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitDataTransferRateFormat.BYTES_PER_SECOND,
        src_format=UnitDataTransferRateFormat.BYTES_PER_SECOND,
        value=3.14,
    )


@pytest.mark.skip
def test_get_data_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UnitDataConversion, Error]] = get_data_unit_conversion.sync(
        client=client,
        output_format=UnitDataFormat.BYTE,
        src_format=UnitDataFormat.BYTE,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitDataConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitDataConversion, Error]]
    ] = get_data_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitDataFormat.BYTE,
        src_format=UnitDataFormat.BYTE,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_data_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitDataConversion, Error]
    ] = await get_data_unit_conversion.asyncio(
        client=client,
        output_format=UnitDataFormat.BYTE,
        src_format=UnitDataFormat.BYTE,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitDataConversion, Error]]
    ] = await get_data_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitDataFormat.BYTE,
        src_format=UnitDataFormat.BYTE,
        value=3.14,
    )


@pytest.mark.skip
def test_get_density_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitDensityConversion, Error]
    ] = get_density_unit_conversion.sync(
        client=client,
        output_format=UnitDensityFormat.KILOGRAMS_PER_CUBIC_METER,
        src_format=UnitDensityFormat.KILOGRAMS_PER_CUBIC_METER,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitDensityConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitDensityConversion, Error]]
    ] = get_density_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitDensityFormat.KILOGRAMS_PER_CUBIC_METER,
        src_format=UnitDensityFormat.KILOGRAMS_PER_CUBIC_METER,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_density_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitDensityConversion, Error]
    ] = await get_density_unit_conversion.asyncio(
        client=client,
        output_format=UnitDensityFormat.KILOGRAMS_PER_CUBIC_METER,
        src_format=UnitDensityFormat.KILOGRAMS_PER_CUBIC_METER,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitDensityConversion, Error]]
    ] = await get_density_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitDensityFormat.KILOGRAMS_PER_CUBIC_METER,
        src_format=UnitDensityFormat.KILOGRAMS_PER_CUBIC_METER,
        value=3.14,
    )


@pytest.mark.skip
def test_get_energy_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitEnergyConversion, Error]
    ] = get_energy_unit_conversion.sync(
        client=client,
        output_format=UnitEnergyFormat.JOULE,
        src_format=UnitEnergyFormat.JOULE,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitEnergyConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitEnergyConversion, Error]]
    ] = get_energy_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitEnergyFormat.JOULE,
        src_format=UnitEnergyFormat.JOULE,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_energy_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitEnergyConversion, Error]
    ] = await get_energy_unit_conversion.asyncio(
        client=client,
        output_format=UnitEnergyFormat.JOULE,
        src_format=UnitEnergyFormat.JOULE,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitEnergyConversion, Error]]
    ] = await get_energy_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitEnergyFormat.JOULE,
        src_format=UnitEnergyFormat.JOULE,
        value=3.14,
    )


@pytest.mark.skip
def test_get_force_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitForceConversion, Error]
    ] = get_force_unit_conversion.sync(
        client=client,
        output_format=UnitForceFormat.NEWTON,
        src_format=UnitForceFormat.NEWTON,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitForceConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitForceConversion, Error]]
    ] = get_force_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitForceFormat.NEWTON,
        src_format=UnitForceFormat.NEWTON,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_force_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitForceConversion, Error]
    ] = await get_force_unit_conversion.asyncio(
        client=client,
        output_format=UnitForceFormat.NEWTON,
        src_format=UnitForceFormat.NEWTON,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitForceConversion, Error]]
    ] = await get_force_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitForceFormat.NEWTON,
        src_format=UnitForceFormat.NEWTON,
        value=3.14,
    )


@pytest.mark.skip
def test_get_illuminance_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitIlluminanceConversion, Error]
    ] = get_illuminance_unit_conversion.sync(
        client=client,
        output_format=UnitIlluminanceFormat.LUX,
        src_format=UnitIlluminanceFormat.LUX,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitIlluminanceConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitIlluminanceConversion, Error]]
    ] = get_illuminance_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitIlluminanceFormat.LUX,
        src_format=UnitIlluminanceFormat.LUX,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_illuminance_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitIlluminanceConversion, Error]
    ] = await get_illuminance_unit_conversion.asyncio(
        client=client,
        output_format=UnitIlluminanceFormat.LUX,
        src_format=UnitIlluminanceFormat.LUX,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitIlluminanceConversion, Error]]
    ] = await get_illuminance_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitIlluminanceFormat.LUX,
        src_format=UnitIlluminanceFormat.LUX,
        value=3.14,
    )


@pytest.mark.skip
def test_get_length_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitLengthConversion, Error]
    ] = get_length_unit_conversion.sync(
        client=client,
        output_format=UnitLengthFormat.METER,
        src_format=UnitLengthFormat.METER,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitLengthConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitLengthConversion, Error]]
    ] = get_length_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitLengthFormat.METER,
        src_format=UnitLengthFormat.METER,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_length_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitLengthConversion, Error]
    ] = await get_length_unit_conversion.asyncio(
        client=client,
        output_format=UnitLengthFormat.METER,
        src_format=UnitLengthFormat.METER,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitLengthConversion, Error]]
    ] = await get_length_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitLengthFormat.METER,
        src_format=UnitLengthFormat.METER,
        value=3.14,
    )


@pytest.mark.skip
def test_get_magnetic_field_strength_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMagneticFieldStrengthConversion, Error]
    ] = get_magnetic_field_strength_unit_conversion.sync(
        client=client,
        output_format=UnitMagneticFieldStrengthFormat.TESLA,
        src_format=UnitMagneticFieldStrengthFormat.TESLA,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitMagneticFieldStrengthConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitMagneticFieldStrengthConversion, Error]]
    ] = get_magnetic_field_strength_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitMagneticFieldStrengthFormat.TESLA,
        src_format=UnitMagneticFieldStrengthFormat.TESLA,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_magnetic_field_strength_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMagneticFieldStrengthConversion, Error]
    ] = await get_magnetic_field_strength_unit_conversion.asyncio(
        client=client,
        output_format=UnitMagneticFieldStrengthFormat.TESLA,
        src_format=UnitMagneticFieldStrengthFormat.TESLA,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitMagneticFieldStrengthConversion, Error]]
    ] = await get_magnetic_field_strength_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitMagneticFieldStrengthFormat.TESLA,
        src_format=UnitMagneticFieldStrengthFormat.TESLA,
        value=3.14,
    )


@pytest.mark.skip
def test_get_magnetic_flux_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMagneticFluxConversion, Error]
    ] = get_magnetic_flux_unit_conversion.sync(
        client=client,
        output_format=UnitMagneticFluxFormat.WEBER,
        src_format=UnitMagneticFluxFormat.WEBER,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitMagneticFluxConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitMagneticFluxConversion, Error]]
    ] = get_magnetic_flux_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitMagneticFluxFormat.WEBER,
        src_format=UnitMagneticFluxFormat.WEBER,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_magnetic_flux_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMagneticFluxConversion, Error]
    ] = await get_magnetic_flux_unit_conversion.asyncio(
        client=client,
        output_format=UnitMagneticFluxFormat.WEBER,
        src_format=UnitMagneticFluxFormat.WEBER,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitMagneticFluxConversion, Error]]
    ] = await get_magnetic_flux_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitMagneticFluxFormat.WEBER,
        src_format=UnitMagneticFluxFormat.WEBER,
        value=3.14,
    )


@pytest.mark.skip
def test_get_mass_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UnitMassConversion, Error]] = get_mass_unit_conversion.sync(
        client=client,
        output_format=UnitMassFormat.GRAM,
        src_format=UnitMassFormat.GRAM,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitMassConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitMassConversion, Error]]
    ] = get_mass_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitMassFormat.GRAM,
        src_format=UnitMassFormat.GRAM,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_mass_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMassConversion, Error]
    ] = await get_mass_unit_conversion.asyncio(
        client=client,
        output_format=UnitMassFormat.GRAM,
        src_format=UnitMassFormat.GRAM,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitMassConversion, Error]]
    ] = await get_mass_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitMassFormat.GRAM,
        src_format=UnitMassFormat.GRAM,
        value=3.14,
    )


@pytest.mark.skip
def test_get_metric_power_cubed_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMetricPowerCubedConversion, Error]
    ] = get_metric_power_cubed_unit_conversion.sync(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitMetricPowerCubedConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitMetricPowerCubedConversion, Error]]
    ] = get_metric_power_cubed_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_metric_power_cubed_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMetricPowerCubedConversion, Error]
    ] = await get_metric_power_cubed_unit_conversion.asyncio(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitMetricPowerCubedConversion, Error]]
    ] = await get_metric_power_cubed_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )


@pytest.mark.skip
def test_get_metric_power_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMetricPowerConversion, Error]
    ] = get_metric_power_unit_conversion.sync(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitMetricPowerConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitMetricPowerConversion, Error]]
    ] = get_metric_power_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_metric_power_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMetricPowerConversion, Error]
    ] = await get_metric_power_unit_conversion.asyncio(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitMetricPowerConversion, Error]]
    ] = await get_metric_power_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )


@pytest.mark.skip
def test_get_metric_power_squared_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMetricPowerSquaredConversion, Error]
    ] = get_metric_power_squared_unit_conversion.sync(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitMetricPowerSquaredConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitMetricPowerSquaredConversion, Error]]
    ] = get_metric_power_squared_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_metric_power_squared_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMetricPowerSquaredConversion, Error]
    ] = await get_metric_power_squared_unit_conversion.asyncio(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitMetricPowerSquaredConversion, Error]]
    ] = await get_metric_power_squared_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitMetricPower.ATTO,
        src_format=UnitMetricPower.ATTO,
        value=3.14,
    )


@pytest.mark.skip
def test_get_power_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitPowerConversion, Error]
    ] = get_power_unit_conversion.sync(
        client=client,
        output_format=UnitPowerFormat.WATT,
        src_format=UnitPowerFormat.WATT,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitPowerConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitPowerConversion, Error]]
    ] = get_power_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitPowerFormat.WATT,
        src_format=UnitPowerFormat.WATT,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_power_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitPowerConversion, Error]
    ] = await get_power_unit_conversion.asyncio(
        client=client,
        output_format=UnitPowerFormat.WATT,
        src_format=UnitPowerFormat.WATT,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitPowerConversion, Error]]
    ] = await get_power_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitPowerFormat.WATT,
        src_format=UnitPowerFormat.WATT,
        value=3.14,
    )


@pytest.mark.skip
def test_get_pressure_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitPressureConversion, Error]
    ] = get_pressure_unit_conversion.sync(
        client=client,
        output_format=UnitPressureFormat.PASCAL,
        src_format=UnitPressureFormat.PASCAL,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitPressureConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitPressureConversion, Error]]
    ] = get_pressure_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitPressureFormat.PASCAL,
        src_format=UnitPressureFormat.PASCAL,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_pressure_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitPressureConversion, Error]
    ] = await get_pressure_unit_conversion.asyncio(
        client=client,
        output_format=UnitPressureFormat.PASCAL,
        src_format=UnitPressureFormat.PASCAL,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitPressureConversion, Error]]
    ] = await get_pressure_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitPressureFormat.PASCAL,
        src_format=UnitPressureFormat.PASCAL,
        value=3.14,
    )


@pytest.mark.skip
def test_get_radiation_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitRadiationConversion, Error]
    ] = get_radiation_unit_conversion.sync(
        client=client,
        output_format=UnitRadiationFormat.GRAY,
        src_format=UnitRadiationFormat.GRAY,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitRadiationConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitRadiationConversion, Error]]
    ] = get_radiation_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitRadiationFormat.GRAY,
        src_format=UnitRadiationFormat.GRAY,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_radiation_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitRadiationConversion, Error]
    ] = await get_radiation_unit_conversion.asyncio(
        client=client,
        output_format=UnitRadiationFormat.GRAY,
        src_format=UnitRadiationFormat.GRAY,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitRadiationConversion, Error]]
    ] = await get_radiation_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitRadiationFormat.GRAY,
        src_format=UnitRadiationFormat.GRAY,
        value=3.14,
    )


@pytest.mark.skip
def test_get_radioactivity_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitRadioactivityConversion, Error]
    ] = get_radioactivity_unit_conversion.sync(
        client=client,
        output_format=UnitRadioactivityFormat.BECQUEREL,
        src_format=UnitRadioactivityFormat.BECQUEREL,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitRadioactivityConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitRadioactivityConversion, Error]]
    ] = get_radioactivity_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitRadioactivityFormat.BECQUEREL,
        src_format=UnitRadioactivityFormat.BECQUEREL,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_radioactivity_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitRadioactivityConversion, Error]
    ] = await get_radioactivity_unit_conversion.asyncio(
        client=client,
        output_format=UnitRadioactivityFormat.BECQUEREL,
        src_format=UnitRadioactivityFormat.BECQUEREL,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitRadioactivityConversion, Error]]
    ] = await get_radioactivity_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitRadioactivityFormat.BECQUEREL,
        src_format=UnitRadioactivityFormat.BECQUEREL,
        value=3.14,
    )


@pytest.mark.skip
def test_get_solid_angle_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitSolidAngleConversion, Error]
    ] = get_solid_angle_unit_conversion.sync(
        client=client,
        output_format=UnitSolidAngleFormat.STERADIAN,
        src_format=UnitSolidAngleFormat.STERADIAN,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitSolidAngleConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitSolidAngleConversion, Error]]
    ] = get_solid_angle_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitSolidAngleFormat.STERADIAN,
        src_format=UnitSolidAngleFormat.STERADIAN,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_solid_angle_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitSolidAngleConversion, Error]
    ] = await get_solid_angle_unit_conversion.asyncio(
        client=client,
        output_format=UnitSolidAngleFormat.STERADIAN,
        src_format=UnitSolidAngleFormat.STERADIAN,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitSolidAngleConversion, Error]]
    ] = await get_solid_angle_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitSolidAngleFormat.STERADIAN,
        src_format=UnitSolidAngleFormat.STERADIAN,
        value=3.14,
    )


@pytest.mark.skip
def test_get_temperature_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitTemperatureConversion, Error]
    ] = get_temperature_unit_conversion.sync(
        client=client,
        output_format=UnitTemperatureFormat.KELVIN,
        src_format=UnitTemperatureFormat.KELVIN,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitTemperatureConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitTemperatureConversion, Error]]
    ] = get_temperature_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitTemperatureFormat.KELVIN,
        src_format=UnitTemperatureFormat.KELVIN,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_temperature_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitTemperatureConversion, Error]
    ] = await get_temperature_unit_conversion.asyncio(
        client=client,
        output_format=UnitTemperatureFormat.KELVIN,
        src_format=UnitTemperatureFormat.KELVIN,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitTemperatureConversion, Error]]
    ] = await get_temperature_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitTemperatureFormat.KELVIN,
        src_format=UnitTemperatureFormat.KELVIN,
        value=3.14,
    )


@pytest.mark.skip
def test_get_time_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UnitTimeConversion, Error]] = get_time_unit_conversion.sync(
        client=client,
        output_format=UnitTimeFormat.SECOND,
        src_format=UnitTimeFormat.SECOND,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitTimeConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitTimeConversion, Error]]
    ] = get_time_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitTimeFormat.SECOND,
        src_format=UnitTimeFormat.SECOND,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_time_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitTimeConversion, Error]
    ] = await get_time_unit_conversion.asyncio(
        client=client,
        output_format=UnitTimeFormat.SECOND,
        src_format=UnitTimeFormat.SECOND,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitTimeConversion, Error]]
    ] = await get_time_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitTimeFormat.SECOND,
        src_format=UnitTimeFormat.SECOND,
        value=3.14,
    )


@pytest.mark.skip
def test_get_velocity_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitVelocityConversion, Error]
    ] = get_velocity_unit_conversion.sync(
        client=client,
        output_format=UnitVelocityFormat.METERS_PER_SECOND,
        src_format=UnitVelocityFormat.METERS_PER_SECOND,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitVelocityConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitVelocityConversion, Error]]
    ] = get_velocity_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitVelocityFormat.METERS_PER_SECOND,
        src_format=UnitVelocityFormat.METERS_PER_SECOND,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_velocity_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitVelocityConversion, Error]
    ] = await get_velocity_unit_conversion.asyncio(
        client=client,
        output_format=UnitVelocityFormat.METERS_PER_SECOND,
        src_format=UnitVelocityFormat.METERS_PER_SECOND,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitVelocityConversion, Error]]
    ] = await get_velocity_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitVelocityFormat.METERS_PER_SECOND,
        src_format=UnitVelocityFormat.METERS_PER_SECOND,
        value=3.14,
    )


@pytest.mark.skip
def test_get_voltage_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitVoltageConversion, Error]
    ] = get_voltage_unit_conversion.sync(
        client=client,
        output_format=UnitVoltageFormat.VOLT,
        src_format=UnitVoltageFormat.VOLT,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitVoltageConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitVoltageConversion, Error]]
    ] = get_voltage_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitVoltageFormat.VOLT,
        src_format=UnitVoltageFormat.VOLT,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_voltage_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitVoltageConversion, Error]
    ] = await get_voltage_unit_conversion.asyncio(
        client=client,
        output_format=UnitVoltageFormat.VOLT,
        src_format=UnitVoltageFormat.VOLT,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitVoltageConversion, Error]]
    ] = await get_voltage_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitVoltageFormat.VOLT,
        src_format=UnitVoltageFormat.VOLT,
        value=3.14,
    )


@pytest.mark.skip
def test_get_volume_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitVolumeConversion, Error]
    ] = get_volume_unit_conversion.sync(
        client=client,
        output_format=UnitVolumeFormat.CUBIC_METER,
        src_format=UnitVolumeFormat.CUBIC_METER,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitVolumeConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UnitVolumeConversion, Error]]
    ] = get_volume_unit_conversion.sync_detailed(
        client=client,
        output_format=UnitVolumeFormat.CUBIC_METER,
        src_format=UnitVolumeFormat.CUBIC_METER,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_volume_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitVolumeConversion, Error]
    ] = await get_volume_unit_conversion.asyncio(
        client=client,
        output_format=UnitVolumeFormat.CUBIC_METER,
        src_format=UnitVolumeFormat.CUBIC_METER,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitVolumeConversion, Error]]
    ] = await get_volume_unit_conversion.asyncio_detailed(
        client=client,
        output_format=UnitVolumeFormat.CUBIC_METER,
        src_format=UnitVolumeFormat.CUBIC_METER,
        value=3.14,
    )


@pytest.mark.skip
def test_delete_user_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_user_self.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_user_self.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_user_self.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await delete_user_self.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_user_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = get_user_self.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[User, Error]]] = get_user_self.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = await get_user_self.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[User, Error]]
    ] = await get_user_self.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_user_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = update_user_self.sync(
        client=client,
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            last_name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[User, Error]]] = update_user_self.sync_detailed(
        client=client,
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            last_name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = await update_user_self.asyncio(
        client=client,
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            last_name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[User, Error]]
    ] = await update_user_self.asyncio_detailed(
        client=client,
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            last_name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_user_list_api_calls():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = user_list_api_calls.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
    ] = user_list_api_calls.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_user_list_api_calls_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = await user_list_api_calls.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
    ] = await user_list_api_calls.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_api_call_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = get_api_call_for_user.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPrice = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ApiCallWithPrice, Error]]
    ] = get_api_call_for_user.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPrice, Error]
    ] = await get_api_call_for_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPrice, Error]]
    ] = await get_api_call_for_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_list_api_tokens_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiTokenResultsPage, Error]] = list_api_tokens_for_user.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiTokenResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ApiTokenResultsPage, Error]]
    ] = list_api_tokens_for_user.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_tokens_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiTokenResultsPage, Error]
    ] = await list_api_tokens_for_user.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiTokenResultsPage, Error]]
    ] = await list_api_tokens_for_user.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_create_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = create_api_token_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ApiToken, Error]]
    ] = create_api_token_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = await create_api_token_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiToken, Error]]
    ] = await create_api_token_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_delete_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_api_token_for_user.sync(
        client=client,
        token="<uuid>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_api_token_for_user.sync_detailed(
        client=client,
        token="<uuid>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_api_token_for_user.asyncio(
        client=client,
        token="<uuid>",
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_api_token_for_user.asyncio_detailed(
        client=client,
        token="<uuid>",
    )


@pytest.mark.skip
def test_get_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = get_api_token_for_user.sync(
        client=client,
        token="<uuid>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ApiToken, Error]]
    ] = get_api_token_for_user.sync_detailed(
        client=client,
        token="<uuid>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = await get_api_token_for_user.asyncio(
        client=client,
        token="<uuid>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiToken, Error]]
    ] = await get_api_token_for_user.asyncio_detailed(
        client=client,
        token="<uuid>",
    )


@pytest.mark.skip
def test_get_user_self_extended():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUser, Error]] = get_user_self_extended.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ExtendedUser = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ExtendedUser, Error]]
    ] = get_user_self_extended.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUser, Error]] = await get_user_self_extended.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ExtendedUser, Error]]
    ] = await get_user_self_extended.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_user_front_hash_self():
    # Create our client.
    client = ClientFromEnv()

    get_user_front_hash_self.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    get_user_front_hash_self.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_front_hash_self_async():
    # Create our client.
    client = ClientFromEnv()

    await get_user_front_hash_self.asyncio(
        client=client,
    )

    # OR run async with more info
    await get_user_front_hash_self.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_user_onboarding_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Onboarding, Error]] = get_user_onboarding_self.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Onboarding = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[Onboarding, Error]]
    ] = get_user_onboarding_self.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_onboarding_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Onboarding, Error]] = await get_user_onboarding_self.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Onboarding, Error]]
    ] = await get_user_onboarding_self.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_delete_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_payment_information_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Error]
    ] = delete_payment_information_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_payment_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_payment_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = get_payment_information_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[Customer, Error]]
    ] = get_payment_information_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await get_payment_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await get_payment_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = create_payment_information_for_user.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[Customer, Error]]
    ] = create_payment_information_for_user.sync_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await create_payment_information_for_user.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await create_payment_information_for_user.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_update_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = update_payment_information_for_user.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[Customer, Error]]
    ] = update_payment_information_for_user.sync_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await update_payment_information_for_user.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await update_payment_information_for_user.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_get_payment_balance_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = get_payment_balance_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[CustomerBalance, Error]]
    ] = get_payment_balance_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[CustomerBalance, Error]
    ] = await get_payment_balance_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CustomerBalance, Error]]
    ] = await get_payment_balance_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_payment_intent_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[PaymentIntent, Error]] = create_payment_intent_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: PaymentIntent = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[PaymentIntent, Error]]
    ] = create_payment_intent_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[PaymentIntent, Error]
    ] = await create_payment_intent_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[PaymentIntent, Error]]
    ] = await create_payment_intent_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_invoices_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[Invoice], Error]] = list_invoices_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[Invoice] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[List[Invoice], Error]]
    ] = list_invoices_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[List[Invoice], Error]
    ] = await list_invoices_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[Invoice], Error]]
    ] = await list_invoices_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_payment_methods_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[List[PaymentMethod], Error]
    ] = list_payment_methods_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[PaymentMethod] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[List[PaymentMethod], Error]]
    ] = list_payment_methods_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_payment_methods_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[List[PaymentMethod], Error]
    ] = await list_payment_methods_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[PaymentMethod], Error]]
    ] = await list_payment_methods_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_delete_payment_method_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_payment_method_for_user.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_payment_method_for_user.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_payment_method_for_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_payment_method_for_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = validate_customer_tax_information_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Error]
    ] = validate_customer_tax_information_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await validate_customer_tax_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await validate_customer_tax_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_session_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Session, Error]] = get_session_for_user.sync(
        client=client,
        token="<uuid>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Session = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[Session, Error]]
    ] = get_session_for_user.sync_detailed(
        client=client,
        token="<uuid>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_session_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Session, Error]] = await get_session_for_user.asyncio(
        client=client,
        token="<uuid>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Session, Error]]
    ] = await get_session_for_user.asyncio_detailed(
        client=client,
        token="<uuid>",
    )


@pytest.mark.skip
def test_list_users():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UserResultsPage, Error]] = list_users.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UserResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[UserResultsPage, Error]]
    ] = list_users.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UserResultsPage, Error]] = await list_users.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UserResultsPage, Error]]
    ] = await list_users.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_list_users_extended():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUserResultsPage, Error]] = list_users_extended.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ExtendedUserResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ExtendedUserResultsPage, Error]]
    ] = list_users_extended.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ExtendedUserResultsPage, Error]
    ] = await list_users_extended.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ExtendedUserResultsPage, Error]]
    ] = await list_users_extended.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_user_extended():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUser, Error]] = get_user_extended.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ExtendedUser = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ExtendedUser, Error]]
    ] = get_user_extended.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUser, Error]] = await get_user_extended.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ExtendedUser, Error]]
    ] = await get_user_extended.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_get_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = get_user.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[User, Error]]] = get_user.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = await get_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[Optional[Union[User, Error]]] = await get_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_list_api_calls_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = list_api_calls_for_user.sync(
        client=client,
        id="<string>",
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
    ] = list_api_calls_for_user.sync_detailed(
        client=client,
        id="<string>",
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = await list_api_calls_for_user.asyncio(
        client=client,
        id="<string>",
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
    ] = await list_api_calls_for_user.asyncio_detailed(
        client=client,
        id="<string>",
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_create_executor_term():
    # Create our client.
    client = ClientFromEnv()

    create_executor_term.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    create_executor_term.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_executor_term_async():
    # Create our client.
    client = ClientFromEnv()

    await create_executor_term.asyncio(
        client=client,
    )

    # OR run async with more info
    await create_executor_term.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_modeling_commands_ws():
    # Create our client.
    client = ClientFromEnv()

    modeling_commands_ws.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    modeling_commands_ws.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_modeling_commands_ws_async():
    # Create our client.
    client = ClientFromEnv()

    await modeling_commands_ws.asyncio(
        client=client,
    )

    # OR run async with more info
    await modeling_commands_ws.asyncio_detailed(
        client=client,
    )
