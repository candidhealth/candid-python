# This file was auto-generated by Fern from our API Definition.

from .......core.client_wrapper import SyncClientWrapper
import typing
from ....common.types.page_token import PageToken
from .types.sort_field_string import SortFieldString
from ....common.types.sort_direction import SortDirection
from .types.filter_query_string import FilterQueryString
from .......core.request_options import RequestOptions
from .types.patient_list_page import PatientListPage
from json.decoder import JSONDecodeError
from .......core.api_error import ApiError
from .......core.pydantic_utilities import parse_obj_as
from ....common.errors.bad_request_error import BadRequestError
from ....common.types.error_base_4_xx import ErrorBase4Xx
from .types.appointment_list_page import AppointmentListPage
from .......core.client_wrapper import AsyncClientWrapper


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_patient_list(
        self,
        *,
        page_token: typing.Optional[PageToken] = None,
        limit: typing.Optional[int] = None,
        sort_field: typing.Optional[SortFieldString] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        filters: typing.Optional[FilterQueryString] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatientListPage:
        """
        Gets patients with dependent objects for patients that match the query parameters.

        Parameters
        ----------
        page_token : typing.Optional[PageToken]

        limit : typing.Optional[int]

        sort_field : typing.Optional[SortFieldString]
            Defaults to patient.updatedAt.

        sort_direction : typing.Optional[SortDirection]
            Defaults to ascending.

        filters : typing.Optional[FilterQueryString]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientListPage

        Examples
        --------
        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.pre_encounter.lists.v_1.get_patient_list(
            page_token="string",
            limit=1,
            sort_field="string",
            sort_direction="asc",
            filters="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "lists/v1/patient",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            params={
                "page_token": page_token,
                "limit": limit,
                "sort_field": sort_field,
                "sort_direction": sort_direction,
                "filters": filters,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                PatientListPage,
                parse_obj_as(
                    type_=PatientListPage,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "BadRequestError":
                raise BadRequestError(
                    typing.cast(
                        ErrorBase4Xx,
                        parse_obj_as(
                            type_=ErrorBase4Xx,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_appointment_list(
        self,
        *,
        sort_field: typing.Optional[SortFieldString] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        filters: typing.Optional[FilterQueryString] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppointmentListPage:
        """
        Searches for appointments that match the query parameters.

        Parameters
        ----------
        sort_field : typing.Optional[SortFieldString]
            Defaults to appointment.startTimestamp.

        sort_direction : typing.Optional[SortDirection]
            Defaults to asc.

        limit : typing.Optional[int]
            Defaults to 100.

        page_token : typing.Optional[PageToken]

        filters : typing.Optional[FilterQueryString]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppointmentListPage

        Examples
        --------
        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.pre_encounter.lists.v_1.get_appointment_list(
            sort_field="string",
            sort_direction="asc",
            limit=1,
            page_token="string",
            filters="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "lists/v1/appointment",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            params={
                "sort_field": sort_field,
                "sort_direction": sort_direction,
                "limit": limit,
                "page_token": page_token,
                "filters": filters,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                AppointmentListPage,
                parse_obj_as(
                    type_=AppointmentListPage,  # type: ignore
                    object_=_response_json,
                ),
            )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_patient_list(
        self,
        *,
        page_token: typing.Optional[PageToken] = None,
        limit: typing.Optional[int] = None,
        sort_field: typing.Optional[SortFieldString] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        filters: typing.Optional[FilterQueryString] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatientListPage:
        """
        Gets patients with dependent objects for patients that match the query parameters.

        Parameters
        ----------
        page_token : typing.Optional[PageToken]

        limit : typing.Optional[int]

        sort_field : typing.Optional[SortFieldString]
            Defaults to patient.updatedAt.

        sort_direction : typing.Optional[SortDirection]
            Defaults to ascending.

        filters : typing.Optional[FilterQueryString]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientListPage

        Examples
        --------
        import asyncio

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.pre_encounter.lists.v_1.get_patient_list(
                page_token="string",
                limit=1,
                sort_field="string",
                sort_direction="asc",
                filters="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lists/v1/patient",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            params={
                "page_token": page_token,
                "limit": limit,
                "sort_field": sort_field,
                "sort_direction": sort_direction,
                "filters": filters,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                PatientListPage,
                parse_obj_as(
                    type_=PatientListPage,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "BadRequestError":
                raise BadRequestError(
                    typing.cast(
                        ErrorBase4Xx,
                        parse_obj_as(
                            type_=ErrorBase4Xx,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_appointment_list(
        self,
        *,
        sort_field: typing.Optional[SortFieldString] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        filters: typing.Optional[FilterQueryString] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppointmentListPage:
        """
        Searches for appointments that match the query parameters.

        Parameters
        ----------
        sort_field : typing.Optional[SortFieldString]
            Defaults to appointment.startTimestamp.

        sort_direction : typing.Optional[SortDirection]
            Defaults to asc.

        limit : typing.Optional[int]
            Defaults to 100.

        page_token : typing.Optional[PageToken]

        filters : typing.Optional[FilterQueryString]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppointmentListPage

        Examples
        --------
        import asyncio

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.pre_encounter.lists.v_1.get_appointment_list(
                sort_field="string",
                sort_direction="asc",
                limit=1,
                page_token="string",
                filters="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lists/v1/appointment",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            params={
                "sort_field": sort_field,
                "sort_direction": sort_direction,
                "limit": limit,
                "page_token": page_token,
                "filters": filters,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                AppointmentListPage,
                parse_obj_as(
                    type_=AppointmentListPage,  # type: ignore
                    object_=_response_json,
                ),
            )
        raise ApiError(status_code=_response.status_code, body=_response_json)
