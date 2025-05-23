# This file was auto-generated by Fern from our API Definition.

import typing

from .......core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .......core.request_options import RequestOptions
from ....common.types.page_token import PageToken
from ....common.types.sort_direction import SortDirection
from .raw_client import AsyncRawV1Client, RawV1Client
from .types.appointment_list_page import AppointmentListPage
from .types.filter_query_string import FilterQueryString
from .types.patient_list_page import PatientListPage
from .types.sort_field_string import SortFieldString


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV1Client
        """
        return self._raw_client

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
        client.pre_encounter.lists.v_1.get_patient_list()
        """
        _response = self._raw_client.get_patient_list(
            page_token=page_token,
            limit=limit,
            sort_field=sort_field,
            sort_direction=sort_direction,
            filters=filters,
            request_options=request_options,
        )
        return _response.data

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
        client.pre_encounter.lists.v_1.get_appointment_list()
        """
        _response = self._raw_client.get_appointment_list(
            sort_field=sort_field,
            sort_direction=sort_direction,
            limit=limit,
            page_token=page_token,
            filters=filters,
            request_options=request_options,
        )
        return _response.data


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV1Client
        """
        return self._raw_client

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
            await client.pre_encounter.lists.v_1.get_patient_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_patient_list(
            page_token=page_token,
            limit=limit,
            sort_field=sort_field,
            sort_direction=sort_direction,
            filters=filters,
            request_options=request_options,
        )
        return _response.data

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
            await client.pre_encounter.lists.v_1.get_appointment_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_appointment_list(
            sort_field=sort_field,
            sort_direction=sort_direction,
            limit=limit,
            page_token=page_token,
            filters=filters,
            request_options=request_options,
        )
        return _response.data
