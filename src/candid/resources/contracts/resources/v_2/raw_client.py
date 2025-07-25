# This file was auto-generated by Fern from our API Definition.

import typing
import uuid
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.http_response import AsyncHttpResponse, HttpResponse
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import parse_obj_as
from .....core.request_options import RequestOptions
from ....commons.errors.entity_not_found_error import EntityNotFoundError
from ....commons.errors.unprocessable_entity_error import UnprocessableEntityError
from ....commons.types.date import Date
from ....commons.types.entity_not_found_error_message import EntityNotFoundErrorMessage
from ....commons.types.page_token import PageToken
from ....commons.types.regions import Regions
from ....commons.types.sort_direction import SortDirection
from ....commons.types.state import State
from ....commons.types.unprocessable_entity_error_message import UnprocessableEntityErrorMessage
from .errors.contract_invalid_expiration_date_http_error import ContractInvalidExpirationDateHttpError
from .errors.contract_is_linked_to_fee_schedule_http_error import ContractIsLinkedToFeeScheduleHttpError
from .types.authorized_signatory import AuthorizedSignatory
from .types.authorized_signatory_update import AuthorizedSignatoryUpdate
from .types.contract_id import ContractId
from .types.contract_invalid_expiration_date_error import ContractInvalidExpirationDateError
from .types.contract_is_linked_to_fee_schedule_error import ContractIsLinkedToFeeScheduleError
from .types.contract_sort_field import ContractSortField
from .types.contract_status import ContractStatus
from .types.contract_with_providers import ContractWithProviders
from .types.contracting_provider_id import ContractingProviderId
from .types.contracts_page import ContractsPage
from .types.date_update import DateUpdate
from .types.insurance_types import InsuranceTypes
from .types.regions_update import RegionsUpdate
from .types.rendering_providerid import RenderingProviderid

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, contract_id: ContractId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContractWithProviders]:
        """
        Parameters
        ----------
        contract_id : ContractId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContractWithProviders]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/contracts/v2/{jsonable_encoder(contract_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ContractWithProviders,
                parse_obj_as(
                    type_=ContractWithProviders,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EntityNotFoundErrorMessage,
                        parse_obj_as(
                            type_=EntityNotFoundErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_multi(
        self,
        *,
        page_token: typing.Optional[PageToken] = None,
        limit: typing.Optional[int] = None,
        contracting_provider_id: typing.Optional[ContractingProviderId] = None,
        rendering_provider_ids: typing.Optional[
            typing.Union[RenderingProviderid, typing.Sequence[RenderingProviderid]]
        ] = None,
        payer_names: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        states: typing.Optional[typing.Union[State, typing.Sequence[State]]] = None,
        contract_status: typing.Optional[ContractStatus] = None,
        sort: typing.Optional[ContractSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContractsPage]:
        """
        Parameters
        ----------
        page_token : typing.Optional[PageToken]

        limit : typing.Optional[int]
            Max number of contracts returned. Defaults to 1000. Max is 1000.

        contracting_provider_id : typing.Optional[ContractingProviderId]

        rendering_provider_ids : typing.Optional[typing.Union[RenderingProviderid, typing.Sequence[RenderingProviderid]]]

        payer_names : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter to contracts that include any of the included payer names.

        states : typing.Optional[typing.Union[State, typing.Sequence[State]]]

        contract_status : typing.Optional[ContractStatus]
            The status of the contract. Defaults to `pending`

        sort : typing.Optional[ContractSortField]
            Potentially sort by a contract related attribute.  Defaults to created_at

        sort_direction : typing.Optional[SortDirection]
            Direction of sort, defaulting to desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContractsPage]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/contracts/v2",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            params={
                "page_token": page_token,
                "limit": limit,
                "contracting_provider_id": contracting_provider_id,
                "rendering_provider_ids": rendering_provider_ids,
                "payer_names": payer_names,
                "states": states,
                "contract_status": contract_status,
                "sort": sort,
                "sort_direction": sort_direction,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ContractsPage,
                parse_obj_as(
                    type_=ContractsPage,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        contracting_provider_id: ContractingProviderId,
        rendering_provider_ids: typing.Set[RenderingProviderid],
        payer_uuid: uuid.UUID,
        effective_date: Date,
        regions: Regions,
        commercial_insurance_types: InsuranceTypes,
        medicare_insurance_types: InsuranceTypes,
        medicaid_insurance_types: InsuranceTypes,
        expiration_date: typing.Optional[Date] = OMIT,
        contract_status: typing.Optional[ContractStatus] = OMIT,
        authorized_signatory: typing.Optional[AuthorizedSignatory] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContractWithProviders]:
        """
        Creates a new contract within the user's current organization

        Parameters
        ----------
        contracting_provider_id : ContractingProviderId
            The UUID of the provider under agreement to the contract

        rendering_provider_ids : typing.Set[RenderingProviderid]
            A rendering provider isn't contracted directly with the payer but can render
            services under the contract held by the contracting provider.
            Max items is 1000.

        payer_uuid : uuid.UUID
            The UUID of the insurance company under agreement to the contract

        effective_date : Date
            The starting day upon which the contract is effective

        regions : Regions
            The state(s) to which the contract's coverage extends.
            It may also be set to "national" for the entirety of the US.

        commercial_insurance_types : InsuranceTypes
            The commercial plan insurance types this contract applies.

        medicare_insurance_types : InsuranceTypes
            The Medicare plan insurance types this contract applies.

        medicaid_insurance_types : InsuranceTypes
            The Medicaid plan insurance types this contract applies.

        expiration_date : typing.Optional[Date]
            An optional end day upon which the contract expires

        contract_status : typing.Optional[ContractStatus]

        authorized_signatory : typing.Optional[AuthorizedSignatory]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContractWithProviders]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/contracts/v2",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="POST",
            json={
                "contracting_provider_id": contracting_provider_id,
                "rendering_provider_ids": rendering_provider_ids,
                "payer_uuid": payer_uuid,
                "effective_date": effective_date,
                "expiration_date": expiration_date,
                "regions": regions,
                "contract_status": contract_status,
                "authorized_signatory": authorized_signatory,
                "commercial_insurance_types": commercial_insurance_types,
                "medicare_insurance_types": medicare_insurance_types,
                "medicaid_insurance_types": medicaid_insurance_types,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ContractWithProviders,
                parse_obj_as(
                    type_=ContractWithProviders,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, contract_id: ContractId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        contract_id : ContractId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/contracts/v2/{jsonable_encoder(contract_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return HttpResponse(response=_response, data=None)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ContractIsLinkedToFeeScheduleHttpError":
                raise ContractIsLinkedToFeeScheduleHttpError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContractIsLinkedToFeeScheduleError,
                        parse_obj_as(
                            type_=ContractIsLinkedToFeeScheduleError,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        contract_id: ContractId,
        *,
        rendering_provider_ids: typing.Optional[typing.Set[RenderingProviderid]] = OMIT,
        effective_date: typing.Optional[Date] = OMIT,
        expiration_date: typing.Optional[DateUpdate] = OMIT,
        regions: typing.Optional[RegionsUpdate] = OMIT,
        contract_status: typing.Optional[ContractStatus] = OMIT,
        authorized_signatory: typing.Optional[AuthorizedSignatoryUpdate] = OMIT,
        commercial_insurance_types: typing.Optional[InsuranceTypes] = OMIT,
        medicare_insurance_types: typing.Optional[InsuranceTypes] = OMIT,
        medicaid_insurance_types: typing.Optional[InsuranceTypes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContractWithProviders]:
        """
        Parameters
        ----------
        contract_id : ContractId

        rendering_provider_ids : typing.Optional[typing.Set[RenderingProviderid]]
            A rendering provider isn't contracted directly with the payer but can render
            services under the contract held by the contracting provider.
            Max items is 1000.

        effective_date : typing.Optional[Date]
            The starting day upon which the contract is effective

        expiration_date : typing.Optional[DateUpdate]
            An optional end day upon which the contract expires

        regions : typing.Optional[RegionsUpdate]
            If present, the contract's rendering providers will be patched to this exact
            value, overriding what was set before.

        contract_status : typing.Optional[ContractStatus]

        authorized_signatory : typing.Optional[AuthorizedSignatoryUpdate]

        commercial_insurance_types : typing.Optional[InsuranceTypes]

        medicare_insurance_types : typing.Optional[InsuranceTypes]

        medicaid_insurance_types : typing.Optional[InsuranceTypes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContractWithProviders]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/contracts/v2/{jsonable_encoder(contract_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="PATCH",
            json={
                "rendering_provider_ids": rendering_provider_ids,
                "effective_date": effective_date,
                "expiration_date": expiration_date,
                "regions": regions,
                "contract_status": contract_status,
                "authorized_signatory": authorized_signatory,
                "commercial_insurance_types": commercial_insurance_types,
                "medicare_insurance_types": medicare_insurance_types,
                "medicaid_insurance_types": medicaid_insurance_types,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ContractWithProviders,
                parse_obj_as(
                    type_=ContractWithProviders,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityErrorMessage,
                        parse_obj_as(
                            type_=UnprocessableEntityErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
            if _response_json["errorName"] == "ContractInvalidExpirationDateHttpError":
                raise ContractInvalidExpirationDateHttpError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContractInvalidExpirationDateError,
                        parse_obj_as(
                            type_=ContractInvalidExpirationDateError,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, contract_id: ContractId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContractWithProviders]:
        """
        Parameters
        ----------
        contract_id : ContractId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContractWithProviders]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/contracts/v2/{jsonable_encoder(contract_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ContractWithProviders,
                parse_obj_as(
                    type_=ContractWithProviders,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EntityNotFoundErrorMessage,
                        parse_obj_as(
                            type_=EntityNotFoundErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_multi(
        self,
        *,
        page_token: typing.Optional[PageToken] = None,
        limit: typing.Optional[int] = None,
        contracting_provider_id: typing.Optional[ContractingProviderId] = None,
        rendering_provider_ids: typing.Optional[
            typing.Union[RenderingProviderid, typing.Sequence[RenderingProviderid]]
        ] = None,
        payer_names: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        states: typing.Optional[typing.Union[State, typing.Sequence[State]]] = None,
        contract_status: typing.Optional[ContractStatus] = None,
        sort: typing.Optional[ContractSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContractsPage]:
        """
        Parameters
        ----------
        page_token : typing.Optional[PageToken]

        limit : typing.Optional[int]
            Max number of contracts returned. Defaults to 1000. Max is 1000.

        contracting_provider_id : typing.Optional[ContractingProviderId]

        rendering_provider_ids : typing.Optional[typing.Union[RenderingProviderid, typing.Sequence[RenderingProviderid]]]

        payer_names : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter to contracts that include any of the included payer names.

        states : typing.Optional[typing.Union[State, typing.Sequence[State]]]

        contract_status : typing.Optional[ContractStatus]
            The status of the contract. Defaults to `pending`

        sort : typing.Optional[ContractSortField]
            Potentially sort by a contract related attribute.  Defaults to created_at

        sort_direction : typing.Optional[SortDirection]
            Direction of sort, defaulting to desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContractsPage]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/contracts/v2",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            params={
                "page_token": page_token,
                "limit": limit,
                "contracting_provider_id": contracting_provider_id,
                "rendering_provider_ids": rendering_provider_ids,
                "payer_names": payer_names,
                "states": states,
                "contract_status": contract_status,
                "sort": sort,
                "sort_direction": sort_direction,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ContractsPage,
                parse_obj_as(
                    type_=ContractsPage,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        contracting_provider_id: ContractingProviderId,
        rendering_provider_ids: typing.Set[RenderingProviderid],
        payer_uuid: uuid.UUID,
        effective_date: Date,
        regions: Regions,
        commercial_insurance_types: InsuranceTypes,
        medicare_insurance_types: InsuranceTypes,
        medicaid_insurance_types: InsuranceTypes,
        expiration_date: typing.Optional[Date] = OMIT,
        contract_status: typing.Optional[ContractStatus] = OMIT,
        authorized_signatory: typing.Optional[AuthorizedSignatory] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContractWithProviders]:
        """
        Creates a new contract within the user's current organization

        Parameters
        ----------
        contracting_provider_id : ContractingProviderId
            The UUID of the provider under agreement to the contract

        rendering_provider_ids : typing.Set[RenderingProviderid]
            A rendering provider isn't contracted directly with the payer but can render
            services under the contract held by the contracting provider.
            Max items is 1000.

        payer_uuid : uuid.UUID
            The UUID of the insurance company under agreement to the contract

        effective_date : Date
            The starting day upon which the contract is effective

        regions : Regions
            The state(s) to which the contract's coverage extends.
            It may also be set to "national" for the entirety of the US.

        commercial_insurance_types : InsuranceTypes
            The commercial plan insurance types this contract applies.

        medicare_insurance_types : InsuranceTypes
            The Medicare plan insurance types this contract applies.

        medicaid_insurance_types : InsuranceTypes
            The Medicaid plan insurance types this contract applies.

        expiration_date : typing.Optional[Date]
            An optional end day upon which the contract expires

        contract_status : typing.Optional[ContractStatus]

        authorized_signatory : typing.Optional[AuthorizedSignatory]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContractWithProviders]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/contracts/v2",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="POST",
            json={
                "contracting_provider_id": contracting_provider_id,
                "rendering_provider_ids": rendering_provider_ids,
                "payer_uuid": payer_uuid,
                "effective_date": effective_date,
                "expiration_date": expiration_date,
                "regions": regions,
                "contract_status": contract_status,
                "authorized_signatory": authorized_signatory,
                "commercial_insurance_types": commercial_insurance_types,
                "medicare_insurance_types": medicare_insurance_types,
                "medicaid_insurance_types": medicaid_insurance_types,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ContractWithProviders,
                parse_obj_as(
                    type_=ContractWithProviders,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, contract_id: ContractId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        contract_id : ContractId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/contracts/v2/{jsonable_encoder(contract_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return AsyncHttpResponse(response=_response, data=None)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "ContractIsLinkedToFeeScheduleHttpError":
                raise ContractIsLinkedToFeeScheduleHttpError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContractIsLinkedToFeeScheduleError,
                        parse_obj_as(
                            type_=ContractIsLinkedToFeeScheduleError,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        contract_id: ContractId,
        *,
        rendering_provider_ids: typing.Optional[typing.Set[RenderingProviderid]] = OMIT,
        effective_date: typing.Optional[Date] = OMIT,
        expiration_date: typing.Optional[DateUpdate] = OMIT,
        regions: typing.Optional[RegionsUpdate] = OMIT,
        contract_status: typing.Optional[ContractStatus] = OMIT,
        authorized_signatory: typing.Optional[AuthorizedSignatoryUpdate] = OMIT,
        commercial_insurance_types: typing.Optional[InsuranceTypes] = OMIT,
        medicare_insurance_types: typing.Optional[InsuranceTypes] = OMIT,
        medicaid_insurance_types: typing.Optional[InsuranceTypes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContractWithProviders]:
        """
        Parameters
        ----------
        contract_id : ContractId

        rendering_provider_ids : typing.Optional[typing.Set[RenderingProviderid]]
            A rendering provider isn't contracted directly with the payer but can render
            services under the contract held by the contracting provider.
            Max items is 1000.

        effective_date : typing.Optional[Date]
            The starting day upon which the contract is effective

        expiration_date : typing.Optional[DateUpdate]
            An optional end day upon which the contract expires

        regions : typing.Optional[RegionsUpdate]
            If present, the contract's rendering providers will be patched to this exact
            value, overriding what was set before.

        contract_status : typing.Optional[ContractStatus]

        authorized_signatory : typing.Optional[AuthorizedSignatoryUpdate]

        commercial_insurance_types : typing.Optional[InsuranceTypes]

        medicare_insurance_types : typing.Optional[InsuranceTypes]

        medicaid_insurance_types : typing.Optional[InsuranceTypes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContractWithProviders]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/contracts/v2/{jsonable_encoder(contract_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="PATCH",
            json={
                "rendering_provider_ids": rendering_provider_ids,
                "effective_date": effective_date,
                "expiration_date": expiration_date,
                "regions": regions,
                "contract_status": contract_status,
                "authorized_signatory": authorized_signatory,
                "commercial_insurance_types": commercial_insurance_types,
                "medicare_insurance_types": medicare_insurance_types,
                "medicaid_insurance_types": medicaid_insurance_types,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ContractWithProviders,
                parse_obj_as(
                    type_=ContractWithProviders,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityErrorMessage,
                        parse_obj_as(
                            type_=UnprocessableEntityErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
            if _response_json["errorName"] == "ContractInvalidExpirationDateHttpError":
                raise ContractInvalidExpirationDateHttpError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContractInvalidExpirationDateError,
                        parse_obj_as(
                            type_=ContractInvalidExpirationDateError,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    ),
                )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
