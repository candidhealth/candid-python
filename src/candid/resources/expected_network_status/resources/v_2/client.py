# This file was auto-generated by Fern from our API Definition.

import typing
from .....core.client_wrapper import SyncClientWrapper
from ....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from .types.expected_network_status_request_v_2 import ExpectedNetworkStatusRequestV2
from .....core.request_options import RequestOptions
from .types.expected_network_status_response_v_2 import ExpectedNetworkStatusResponseV2
from .....core.jsonable_encoder import jsonable_encoder
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from .....core.pydantic_utilities import parse_obj_as
from .errors.expected_network_status_check_error import ExpectedNetworkStatusCheckError
from .types.expected_network_status_check_error_message import ExpectedNetworkStatusCheckErrorMessage
from ....commons.errors.organization_not_authorized_error import OrganizationNotAuthorizedError
from ....commons.types.organization_not_authorized_error_message import OrganizationNotAuthorizedErrorMessage
from .types.compute_all_in_network_providers_request import ComputeAllInNetworkProvidersRequest
from .types.compute_all_in_network_providers_response import ComputeAllInNetworkProvidersResponse
from .....core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def compute_for_rendering_provider(
        self,
        rendering_provider_id: OrganizationProviderId,
        *,
        request: ExpectedNetworkStatusRequestV2,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpectedNetworkStatusResponseV2:
        """
        Computes the expected network status for a given rendering provider.
        This endpoint is not available to all customers. Reach out to the Candid sales team
        to discuss enabling this endpoint if it is not available for your organization.

        Parameters
        ----------
        rendering_provider_id : OrganizationProviderId

        request : ExpectedNetworkStatusRequestV2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpectedNetworkStatusResponseV2

        Examples
        --------
        import datetime
        import uuid

        from candid import CandidApiClient
        from candid.resources.commons import StreetAddressShortZip
        from candid.resources.expected_network_status.resources.v_2 import (
            ExpectedNetworkStatusRequestV2,
            ExpectedNetworkStatusSubscriberInformation,
            InsuranceType,
            InsuranceTypeCodes_InsuranceTypeCode,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.expected_network_status.v_2.compute_for_rendering_provider(
            rendering_provider_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=ExpectedNetworkStatusRequestV2(
                service_type="new_patient_video_appt",
                place_of_service_code="01",
                subscriber_information=ExpectedNetworkStatusSubscriberInformation(
                    payer_uuid=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    member_id="string",
                    insurance_type=InsuranceType(
                        line_of_business="medicare",
                        insurance_type_codes=InsuranceTypeCodes_InsuranceTypeCode(
                            value="01"
                        ),
                    ),
                ),
                patient_address=StreetAddressShortZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state="NY",
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
                billing_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                organization_service_facility_id=uuid.UUID(
                    "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
                ),
                date_of_service=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/expected-network-status/v2/compute/{jsonable_encoder(rendering_provider_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                ExpectedNetworkStatusResponseV2,
                parse_obj_as(
                    type_=ExpectedNetworkStatusResponseV2,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    typing.cast(
                        ExpectedNetworkStatusCheckErrorMessage,
                        parse_obj_as(
                            type_=ExpectedNetworkStatusCheckErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    typing.cast(
                        OrganizationNotAuthorizedErrorMessage,
                        parse_obj_as(
                            type_=OrganizationNotAuthorizedErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def compute_all_in_network_providers(
        self, *, request: ComputeAllInNetworkProvidersRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ComputeAllInNetworkProvidersResponse:
        """
        Computes all the in network providers for a given set of inputs.
        This endpoint is not available to all customers. Reach out to the Candid sales team
        to discuss enabling this endpoint if it is not available for your organization.

        Parameters
        ----------
        request : ComputeAllInNetworkProvidersRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComputeAllInNetworkProvidersResponse

        Examples
        --------
        import datetime
        import uuid

        from candid import CandidApiClient
        from candid.resources.commons import StreetAddressShortZip
        from candid.resources.expected_network_status.resources.v_2 import (
            ComputeAllInNetworkProvidersRequest,
            ExpectedNetworkStatusSubscriberInformation,
            InsuranceType,
            InsuranceTypeCodes_InsuranceTypeCode,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.expected_network_status.v_2.compute_all_in_network_providers(
            request=ComputeAllInNetworkProvidersRequest(
                service_type="new_patient_video_appt",
                place_of_service_code="01",
                subscriber_information=ExpectedNetworkStatusSubscriberInformation(
                    payer_uuid=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    member_id="string",
                    insurance_type=InsuranceType(
                        line_of_business="medicare",
                        insurance_type_codes=InsuranceTypeCodes_InsuranceTypeCode(
                            value="01"
                        ),
                    ),
                ),
                patient_address=StreetAddressShortZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state="NY",
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
                billing_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                organization_service_facility_id=uuid.UUID(
                    "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
                ),
                date_of_service=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/expected-network-status/v2/compute",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                ComputeAllInNetworkProvidersResponse,
                parse_obj_as(
                    type_=ComputeAllInNetworkProvidersResponse,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    typing.cast(
                        ExpectedNetworkStatusCheckErrorMessage,
                        parse_obj_as(
                            type_=ExpectedNetworkStatusCheckErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    typing.cast(
                        OrganizationNotAuthorizedErrorMessage,
                        parse_obj_as(
                            type_=OrganizationNotAuthorizedErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def compute_for_rendering_provider(
        self,
        rendering_provider_id: OrganizationProviderId,
        *,
        request: ExpectedNetworkStatusRequestV2,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpectedNetworkStatusResponseV2:
        """
        Computes the expected network status for a given rendering provider.
        This endpoint is not available to all customers. Reach out to the Candid sales team
        to discuss enabling this endpoint if it is not available for your organization.

        Parameters
        ----------
        rendering_provider_id : OrganizationProviderId

        request : ExpectedNetworkStatusRequestV2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpectedNetworkStatusResponseV2

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.commons import StreetAddressShortZip
        from candid.resources.expected_network_status.resources.v_2 import (
            ExpectedNetworkStatusRequestV2,
            ExpectedNetworkStatusSubscriberInformation,
            InsuranceType,
            InsuranceTypeCodes_InsuranceTypeCode,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.expected_network_status.v_2.compute_for_rendering_provider(
                rendering_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                request=ExpectedNetworkStatusRequestV2(
                    service_type="new_patient_video_appt",
                    place_of_service_code="01",
                    subscriber_information=ExpectedNetworkStatusSubscriberInformation(
                        payer_uuid=uuid.UUID(
                            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                        ),
                        member_id="string",
                        insurance_type=InsuranceType(
                            line_of_business="medicare",
                            insurance_type_codes=InsuranceTypeCodes_InsuranceTypeCode(
                                value="01"
                            ),
                        ),
                    ),
                    patient_address=StreetAddressShortZip(
                        address_1="123 Main St",
                        address_2="Apt 1",
                        city="New York",
                        state="NY",
                        zip_code="10001",
                        zip_plus_four_code="1234",
                    ),
                    billing_provider_id=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    organization_service_facility_id=uuid.UUID(
                        "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
                    ),
                    date_of_service=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/expected-network-status/v2/compute/{jsonable_encoder(rendering_provider_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                ExpectedNetworkStatusResponseV2,
                parse_obj_as(
                    type_=ExpectedNetworkStatusResponseV2,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    typing.cast(
                        ExpectedNetworkStatusCheckErrorMessage,
                        parse_obj_as(
                            type_=ExpectedNetworkStatusCheckErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    typing.cast(
                        OrganizationNotAuthorizedErrorMessage,
                        parse_obj_as(
                            type_=OrganizationNotAuthorizedErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def compute_all_in_network_providers(
        self, *, request: ComputeAllInNetworkProvidersRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ComputeAllInNetworkProvidersResponse:
        """
        Computes all the in network providers for a given set of inputs.
        This endpoint is not available to all customers. Reach out to the Candid sales team
        to discuss enabling this endpoint if it is not available for your organization.

        Parameters
        ----------
        request : ComputeAllInNetworkProvidersRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComputeAllInNetworkProvidersResponse

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.commons import StreetAddressShortZip
        from candid.resources.expected_network_status.resources.v_2 import (
            ComputeAllInNetworkProvidersRequest,
            ExpectedNetworkStatusSubscriberInformation,
            InsuranceType,
            InsuranceTypeCodes_InsuranceTypeCode,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.expected_network_status.v_2.compute_all_in_network_providers(
                request=ComputeAllInNetworkProvidersRequest(
                    service_type="new_patient_video_appt",
                    place_of_service_code="01",
                    subscriber_information=ExpectedNetworkStatusSubscriberInformation(
                        payer_uuid=uuid.UUID(
                            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                        ),
                        member_id="string",
                        insurance_type=InsuranceType(
                            line_of_business="medicare",
                            insurance_type_codes=InsuranceTypeCodes_InsuranceTypeCode(
                                value="01"
                            ),
                        ),
                    ),
                    patient_address=StreetAddressShortZip(
                        address_1="123 Main St",
                        address_2="Apt 1",
                        city="New York",
                        state="NY",
                        zip_code="10001",
                        zip_plus_four_code="1234",
                    ),
                    billing_provider_id=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    organization_service_facility_id=uuid.UUID(
                        "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
                    ),
                    date_of_service=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/expected-network-status/v2/compute",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                ComputeAllInNetworkProvidersResponse,
                parse_obj_as(
                    type_=ComputeAllInNetworkProvidersResponse,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    typing.cast(
                        ExpectedNetworkStatusCheckErrorMessage,
                        parse_obj_as(
                            type_=ExpectedNetworkStatusCheckErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    typing.cast(
                        OrganizationNotAuthorizedErrorMessage,
                        parse_obj_as(
                            type_=OrganizationNotAuthorizedErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
