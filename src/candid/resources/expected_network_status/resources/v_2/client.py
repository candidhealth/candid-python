# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.query_encoder import encode_query
from .....core.remove_none_from_dict import remove_none_from_dict
from .....core.request_options import RequestOptions
from ....commons.errors.organization_not_authorized_error import OrganizationNotAuthorizedError
from ....commons.types.organization_not_authorized_error_message import OrganizationNotAuthorizedErrorMessage
from ....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from .errors.expected_network_status_check_error import ExpectedNetworkStatusCheckError
from .types.compute_all_in_network_providers_request import ComputeAllInNetworkProvidersRequest
from .types.compute_all_in_network_providers_response import ComputeAllInNetworkProvidersResponse
from .types.expected_network_status_check_error_message import ExpectedNetworkStatusCheckErrorMessage
from .types.expected_network_status_request_v_2 import ExpectedNetworkStatusRequestV2
from .types.expected_network_status_response_v_2 import ExpectedNetworkStatusResponseV2

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

        from candid import FacilityTypeCode, State, StreetAddressShortZip
        from candid.client import CandidApi
        from candid.resources.expected_network_status.v_2 import (
            ExpectedNetworkStatusRequestV2,
            ExpectedNetworkStatusSubscriberInformation,
            ServiceType,
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
                service_type=ServiceType.NEW_PATIENT_VIDEO_APPT,
                place_of_service_code=FacilityTypeCode.PHARMACY,
                subscriber_information=ExpectedNetworkStatusSubscriberInformation(),
                patient_address=StreetAddressShortZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
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
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/expected-network-status/v2/compute/{jsonable_encoder(rendering_provider_id)}",
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExpectedNetworkStatusResponseV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    pydantic_v1.parse_obj_as(ExpectedNetworkStatusCheckErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    pydantic_v1.parse_obj_as(OrganizationNotAuthorizedErrorMessage, _response_json["content"])  # type: ignore
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

        from candid import FacilityTypeCode, State, StreetAddressShortZip
        from candid.client import CandidApi
        from candid.resources.expected_network_status.v_2 import (
            ComputeAllInNetworkProvidersRequest,
            ExpectedNetworkStatusSubscriberInformation,
            ServiceType,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.expected_network_status.v_2.compute_all_in_network_providers(
            request=ComputeAllInNetworkProvidersRequest(
                service_type=ServiceType.NEW_PATIENT_VIDEO_APPT,
                place_of_service_code=FacilityTypeCode.PHARMACY,
                subscriber_information=ExpectedNetworkStatusSubscriberInformation(),
                patient_address=StreetAddressShortZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
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
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/expected-network-status/v2/compute"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ComputeAllInNetworkProvidersResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    pydantic_v1.parse_obj_as(ExpectedNetworkStatusCheckErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    pydantic_v1.parse_obj_as(OrganizationNotAuthorizedErrorMessage, _response_json["content"])  # type: ignore
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
        import datetime
        import uuid

        from candid import FacilityTypeCode, State, StreetAddressShortZip
        from candid.client import AsyncCandidApi
        from candid.resources.expected_network_status.v_2 import (
            ExpectedNetworkStatusRequestV2,
            ExpectedNetworkStatusSubscriberInformation,
            ServiceType,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.expected_network_status.v_2.compute_for_rendering_provider(
            rendering_provider_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=ExpectedNetworkStatusRequestV2(
                service_type=ServiceType.NEW_PATIENT_VIDEO_APPT,
                place_of_service_code=FacilityTypeCode.PHARMACY,
                subscriber_information=ExpectedNetworkStatusSubscriberInformation(),
                patient_address=StreetAddressShortZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
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
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/expected-network-status/v2/compute/{jsonable_encoder(rendering_provider_id)}",
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExpectedNetworkStatusResponseV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    pydantic_v1.parse_obj_as(ExpectedNetworkStatusCheckErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    pydantic_v1.parse_obj_as(OrganizationNotAuthorizedErrorMessage, _response_json["content"])  # type: ignore
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
        import datetime
        import uuid

        from candid import FacilityTypeCode, State, StreetAddressShortZip
        from candid.client import AsyncCandidApi
        from candid.resources.expected_network_status.v_2 import (
            ComputeAllInNetworkProvidersRequest,
            ExpectedNetworkStatusSubscriberInformation,
            ServiceType,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.expected_network_status.v_2.compute_all_in_network_providers(
            request=ComputeAllInNetworkProvidersRequest(
                service_type=ServiceType.NEW_PATIENT_VIDEO_APPT,
                place_of_service_code=FacilityTypeCode.PHARMACY,
                subscriber_information=ExpectedNetworkStatusSubscriberInformation(),
                patient_address=StreetAddressShortZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
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
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/expected-network-status/v2/compute"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ComputeAllInNetworkProvidersResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    pydantic_v1.parse_obj_as(ExpectedNetworkStatusCheckErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    pydantic_v1.parse_obj_as(OrganizationNotAuthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
