# This file was auto-generated by Fern from our API Definition.

import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ....commons.types.page_token import PageToken
from ....commons.types.sort_direction import SortDirection
from .raw_client import AsyncRawV1Client, RawV1Client
from .types.create_non_insurance_payer_request import CreateNonInsurancePayerRequest
from .types.non_insurance_payer import NonInsurancePayer
from .types.non_insurance_payer_id import NonInsurancePayerId
from .types.non_insurance_payer_page import NonInsurancePayerPage
from .types.non_insurance_payer_sort_field import NonInsurancePayerSortField
from .types.non_insurance_payer_update_request import NonInsurancePayerUpdateRequest
from .types.toggle_non_insurance_payer_enablement_request import ToggleNonInsurancePayerEnablementRequest

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


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

    def create(
        self, *, request: CreateNonInsurancePayerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> NonInsurancePayer:
        """
        Parameters
        ----------
        request : CreateNonInsurancePayerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayer

        Examples
        --------
        from candid import CandidApiClient
        from candid.resources.non_insurance_payers.resources.v_1 import (
            CreateNonInsurancePayerRequest,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.non_insurance_payers.v_1.create(
            request=CreateNonInsurancePayerRequest(
                name="name",
            ),
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    def toggle_enablement(
        self,
        non_insurance_payer_id: NonInsurancePayerId,
        *,
        request: ToggleNonInsurancePayerEnablementRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NonInsurancePayer:
        """
        Parameters
        ----------
        non_insurance_payer_id : NonInsurancePayerId

        request : ToggleNonInsurancePayerEnablementRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayer

        Examples
        --------
        import uuid

        from candid import CandidApiClient
        from candid.resources.non_insurance_payers.resources.v_1 import (
            ToggleNonInsurancePayerEnablementRequest,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.non_insurance_payers.v_1.toggle_enablement(
            non_insurance_payer_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=ToggleNonInsurancePayerEnablementRequest(
                enabled=True,
            ),
        )
        """
        _response = self._raw_client.toggle_enablement(
            non_insurance_payer_id, request=request, request_options=request_options
        )
        return _response.data

    def get_multi(
        self,
        *,
        name: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        sort: typing.Optional[NonInsurancePayerSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NonInsurancePayerPage:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        category : typing.Optional[str]

        enabled : typing.Optional[bool]

        sort : typing.Optional[NonInsurancePayerSortField]

        sort_direction : typing.Optional[SortDirection]

        limit : typing.Optional[int]
            Defaults to 100

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayerPage

        Examples
        --------
        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.non_insurance_payers.v_1.get_multi()
        """
        _response = self._raw_client.get_multi(
            name=name,
            category=category,
            enabled=enabled,
            sort=sort,
            sort_direction=sort_direction,
            limit=limit,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get(
        self, non_insurance_payer_id: NonInsurancePayerId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NonInsurancePayer:
        """
        Parameters
        ----------
        non_insurance_payer_id : NonInsurancePayerId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayer

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.non_insurance_payers.v_1.get(
            non_insurance_payer_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.get(non_insurance_payer_id, request_options=request_options)
        return _response.data

    def update(
        self,
        non_insurance_payer_id: NonInsurancePayerId,
        *,
        request: NonInsurancePayerUpdateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NonInsurancePayer:
        """
        Parameters
        ----------
        non_insurance_payer_id : NonInsurancePayerId

        request : NonInsurancePayerUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayer

        Examples
        --------
        import uuid

        from candid import CandidApiClient
        from candid.resources.non_insurance_payers.resources.v_1 import (
            NonInsurancePayerUpdateRequest,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.non_insurance_payers.v_1.update(
            non_insurance_payer_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=NonInsurancePayerUpdateRequest(),
        )
        """
        _response = self._raw_client.update(non_insurance_payer_id, request=request, request_options=request_options)
        return _response.data

    def delete(
        self, non_insurance_payer_id: NonInsurancePayerId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        non_insurance_payer_id : NonInsurancePayerId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.non_insurance_payers.v_1.delete(
            non_insurance_payer_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.delete(non_insurance_payer_id, request_options=request_options)
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

    async def create(
        self, *, request: CreateNonInsurancePayerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> NonInsurancePayer:
        """
        Parameters
        ----------
        request : CreateNonInsurancePayerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayer

        Examples
        --------
        import asyncio

        from candid import AsyncCandidApiClient
        from candid.resources.non_insurance_payers.resources.v_1 import (
            CreateNonInsurancePayerRequest,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.non_insurance_payers.v_1.create(
                request=CreateNonInsurancePayerRequest(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    async def toggle_enablement(
        self,
        non_insurance_payer_id: NonInsurancePayerId,
        *,
        request: ToggleNonInsurancePayerEnablementRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NonInsurancePayer:
        """
        Parameters
        ----------
        non_insurance_payer_id : NonInsurancePayerId

        request : ToggleNonInsurancePayerEnablementRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayer

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.non_insurance_payers.resources.v_1 import (
            ToggleNonInsurancePayerEnablementRequest,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.non_insurance_payers.v_1.toggle_enablement(
                non_insurance_payer_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                request=ToggleNonInsurancePayerEnablementRequest(
                    enabled=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.toggle_enablement(
            non_insurance_payer_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_multi(
        self,
        *,
        name: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        sort: typing.Optional[NonInsurancePayerSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NonInsurancePayerPage:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        category : typing.Optional[str]

        enabled : typing.Optional[bool]

        sort : typing.Optional[NonInsurancePayerSortField]

        sort_direction : typing.Optional[SortDirection]

        limit : typing.Optional[int]
            Defaults to 100

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayerPage

        Examples
        --------
        import asyncio

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.non_insurance_payers.v_1.get_multi()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_multi(
            name=name,
            category=category,
            enabled=enabled,
            sort=sort,
            sort_direction=sort_direction,
            limit=limit,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, non_insurance_payer_id: NonInsurancePayerId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NonInsurancePayer:
        """
        Parameters
        ----------
        non_insurance_payer_id : NonInsurancePayerId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayer

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.non_insurance_payers.v_1.get(
                non_insurance_payer_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(non_insurance_payer_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        non_insurance_payer_id: NonInsurancePayerId,
        *,
        request: NonInsurancePayerUpdateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NonInsurancePayer:
        """
        Parameters
        ----------
        non_insurance_payer_id : NonInsurancePayerId

        request : NonInsurancePayerUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonInsurancePayer

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.non_insurance_payers.resources.v_1 import (
            NonInsurancePayerUpdateRequest,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.non_insurance_payers.v_1.update(
                non_insurance_payer_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                request=NonInsurancePayerUpdateRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            non_insurance_payer_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete(
        self, non_insurance_payer_id: NonInsurancePayerId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        non_insurance_payer_id : NonInsurancePayerId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.non_insurance_payers.v_1.delete(
                non_insurance_payer_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(non_insurance_payer_id, request_options=request_options)
        return _response.data
