# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
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
        self, rendering_provider_id: OrganizationProviderId, *, request: ExpectedNetworkStatusRequestV2
    ) -> ExpectedNetworkStatusResponseV2:
        """
        Computes the expected network status for a given rendering provider.
        This endpoint is not available to all customers. Reach out to the Candid sales team
        to discuss enabling this endpoint if it is not available for your organization.

        Parameters:
            - rendering_provider_id: OrganizationProviderId.

            - request: ExpectedNetworkStatusRequestV2.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/expected-network-status/v2/compute/{rendering_provider_id}",
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ExpectedNetworkStatusResponseV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    pydantic.parse_obj_as(ExpectedNetworkStatusCheckErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    pydantic.parse_obj_as(OrganizationNotAuthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def compute_all_in_network_providers(
        self, *, request: ComputeAllInNetworkProvidersRequest
    ) -> ComputeAllInNetworkProvidersResponse:
        """
        Computes all the in network providers for a given set of inputs.
        This endpoint is not available to all customers. Reach out to the Candid sales team
        to discuss enabling this endpoint if it is not available for your organization.

        Parameters:
            - request: ComputeAllInNetworkProvidersRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/expected-network-status/v2/compute"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ComputeAllInNetworkProvidersResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    pydantic.parse_obj_as(ExpectedNetworkStatusCheckErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    pydantic.parse_obj_as(OrganizationNotAuthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def compute_for_rendering_provider(
        self, rendering_provider_id: OrganizationProviderId, *, request: ExpectedNetworkStatusRequestV2
    ) -> ExpectedNetworkStatusResponseV2:
        """
        Computes the expected network status for a given rendering provider.
        This endpoint is not available to all customers. Reach out to the Candid sales team
        to discuss enabling this endpoint if it is not available for your organization.

        Parameters:
            - rendering_provider_id: OrganizationProviderId.

            - request: ExpectedNetworkStatusRequestV2.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/expected-network-status/v2/compute/{rendering_provider_id}",
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ExpectedNetworkStatusResponseV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    pydantic.parse_obj_as(ExpectedNetworkStatusCheckErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    pydantic.parse_obj_as(OrganizationNotAuthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def compute_all_in_network_providers(
        self, *, request: ComputeAllInNetworkProvidersRequest
    ) -> ComputeAllInNetworkProvidersResponse:
        """
        Computes all the in network providers for a given set of inputs.
        This endpoint is not available to all customers. Reach out to the Candid sales team
        to discuss enabling this endpoint if it is not available for your organization.

        Parameters:
            - request: ComputeAllInNetworkProvidersRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/expected-network-status/v2/compute"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ComputeAllInNetworkProvidersResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    pydantic.parse_obj_as(ExpectedNetworkStatusCheckErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    pydantic.parse_obj_as(OrganizationNotAuthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
