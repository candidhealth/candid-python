# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.http_response import AsyncHttpResponse, HttpResponse
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import parse_obj_as
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


class RawV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def compute_for_rendering_provider(
        self,
        rendering_provider_id: OrganizationProviderId,
        *,
        request: ExpectedNetworkStatusRequestV2,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExpectedNetworkStatusResponseV2]:
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
        HttpResponse[ExpectedNetworkStatusResponseV2]
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
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ExpectedNetworkStatusResponseV2,
                parse_obj_as(
                    type_=ExpectedNetworkStatusResponseV2,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ExpectedNetworkStatusCheckErrorMessage,
                        parse_obj_as(
                            type_=ExpectedNetworkStatusCheckErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrganizationNotAuthorizedErrorMessage,
                        parse_obj_as(
                            type_=OrganizationNotAuthorizedErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def compute_all_in_network_providers(
        self, *, request: ComputeAllInNetworkProvidersRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComputeAllInNetworkProvidersResponse]:
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
        HttpResponse[ComputeAllInNetworkProvidersResponse]
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
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ComputeAllInNetworkProvidersResponse,
                parse_obj_as(
                    type_=ComputeAllInNetworkProvidersResponse,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ExpectedNetworkStatusCheckErrorMessage,
                        parse_obj_as(
                            type_=ExpectedNetworkStatusCheckErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrganizationNotAuthorizedErrorMessage,
                        parse_obj_as(
                            type_=OrganizationNotAuthorizedErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def compute_for_rendering_provider(
        self,
        rendering_provider_id: OrganizationProviderId,
        *,
        request: ExpectedNetworkStatusRequestV2,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExpectedNetworkStatusResponseV2]:
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
        AsyncHttpResponse[ExpectedNetworkStatusResponseV2]
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
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ExpectedNetworkStatusResponseV2,
                parse_obj_as(
                    type_=ExpectedNetworkStatusResponseV2,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ExpectedNetworkStatusCheckErrorMessage,
                        parse_obj_as(
                            type_=ExpectedNetworkStatusCheckErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrganizationNotAuthorizedErrorMessage,
                        parse_obj_as(
                            type_=OrganizationNotAuthorizedErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def compute_all_in_network_providers(
        self, *, request: ComputeAllInNetworkProvidersRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComputeAllInNetworkProvidersResponse]:
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
        AsyncHttpResponse[ComputeAllInNetworkProvidersResponse]
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
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ComputeAllInNetworkProvidersResponse,
                parse_obj_as(
                    type_=ComputeAllInNetworkProvidersResponse,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ExpectedNetworkStatusCheckError":
                raise ExpectedNetworkStatusCheckError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ExpectedNetworkStatusCheckErrorMessage,
                        parse_obj_as(
                            type_=ExpectedNetworkStatusCheckErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
            if _response_json["errorName"] == "OrganizationNotAuthorizedError":
                raise OrganizationNotAuthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrganizationNotAuthorizedErrorMessage,
                        parse_obj_as(
                            type_=OrganizationNotAuthorizedErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
