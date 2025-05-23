# This file was auto-generated by Fern from our API Definition.

import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ....commons.types.page_token import PageToken
from ....commons.types.payer_plan_group_id import PayerPlanGroupId
from ....commons.types.sort_direction import SortDirection
from ....commons.types.source_of_payment_code import SourceOfPaymentCode
from ....payers.resources.v_3.types.payer_id import PayerId
from ....payers.resources.v_3.types.payer_uuid import PayerUuid
from .raw_client import AsyncRawV1Client, RawV1Client
from .types.mutable_payer_plan_group import MutablePayerPlanGroup
from .types.payer_plan_group import PayerPlanGroup
from .types.payer_plan_group_page import PayerPlanGroupPage
from .types.payer_plan_group_sort_field import PayerPlanGroupSortField

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

    def get_multi(
        self,
        *,
        plan_group_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        payer_uuid: typing.Optional[typing.Union[PayerUuid, typing.Sequence[PayerUuid]]] = None,
        payer_id: typing.Optional[typing.Union[PayerId, typing.Sequence[PayerId]]] = None,
        plan_type: typing.Optional[typing.Union[SourceOfPaymentCode, typing.Sequence[SourceOfPaymentCode]]] = None,
        is_active: typing.Optional[bool] = None,
        payer_plan_group_id: typing.Optional[typing.Union[PayerPlanGroupId, typing.Sequence[PayerPlanGroupId]]] = None,
        limit: typing.Optional[int] = None,
        sort_by_similarity: typing.Optional[str] = None,
        sort: typing.Optional[PayerPlanGroupSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayerPlanGroupPage:
        """
        Returns all payer plan groups matching filter criteria.

        Parameters
        ----------
        plan_group_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        payer_uuid : typing.Optional[typing.Union[PayerUuid, typing.Sequence[PayerUuid]]]

        payer_id : typing.Optional[typing.Union[PayerId, typing.Sequence[PayerId]]]

        plan_type : typing.Optional[typing.Union[SourceOfPaymentCode, typing.Sequence[SourceOfPaymentCode]]]

        is_active : typing.Optional[bool]

        payer_plan_group_id : typing.Optional[typing.Union[PayerPlanGroupId, typing.Sequence[PayerPlanGroupId]]]

        limit : typing.Optional[int]
            Defaults to 100. Cannot exc

        sort_by_similarity : typing.Optional[str]
            If this property is passed, the results will be ordered by those that contain a payer_id, payer_name, plan_group_name, or
            payer_address most similar to the value passed. This will take precedence over the sort and sort_direction properties. This
            will always sort in order of most similar to least similar.

        sort : typing.Optional[PayerPlanGroupSortField]
            Defaults to plan_group_name. If sort_by_similarity is passed, that sort will takes precedence over this property.

        sort_direction : typing.Optional[SortDirection]
            Sort direction. Defaults to ascending order if not provided.

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroupPage

        Examples
        --------
        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.payer_plan_groups.v_1.get_multi()
        """
        _response = self._raw_client.get_multi(
            plan_group_name=plan_group_name,
            payer_uuid=payer_uuid,
            payer_id=payer_id,
            plan_type=plan_type,
            is_active=is_active,
            payer_plan_group_id=payer_plan_group_id,
            limit=limit,
            sort_by_similarity=sort_by_similarity,
            sort=sort,
            sort_direction=sort_direction,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get(
        self, payer_plan_group_id: PayerPlanGroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PayerPlanGroup:
        """
        Return a plan group with a given ID.

        Parameters
        ----------
        payer_plan_group_id : PayerPlanGroupId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroup

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.payer_plan_groups.v_1.get(
            payer_plan_group_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.get(payer_plan_group_id, request_options=request_options)
        return _response.data

    def create(
        self, *, request: MutablePayerPlanGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> PayerPlanGroup:
        """
        Create a payer plan group

        Parameters
        ----------
        request : MutablePayerPlanGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroup

        Examples
        --------
        import uuid

        from candid import CandidApiClient
        from candid.resources.commons import SourceOfPaymentCode
        from candid.resources.payer_plan_groups.resources.v_1 import (
            MutablePayerPlanGroup,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.payer_plan_groups.v_1.create(
            request=MutablePayerPlanGroup(
                plan_group_name="plan_group_name",
                payer_uuid=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                plan_type=SourceOfPaymentCode.SELF_PAY,
            ),
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    def update(
        self,
        payer_plan_group_id: PayerPlanGroupId,
        *,
        request: MutablePayerPlanGroup,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayerPlanGroup:
        """
        Update any of the fields on a payer plan group

        Parameters
        ----------
        payer_plan_group_id : PayerPlanGroupId

        request : MutablePayerPlanGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroup

        Examples
        --------
        import uuid

        from candid import CandidApiClient
        from candid.resources.commons import SourceOfPaymentCode
        from candid.resources.payer_plan_groups.resources.v_1 import (
            MutablePayerPlanGroup,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.payer_plan_groups.v_1.update(
            payer_plan_group_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=MutablePayerPlanGroup(
                plan_group_name="plan_group_name",
                payer_uuid=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                plan_type=SourceOfPaymentCode.SELF_PAY,
            ),
        )
        """
        _response = self._raw_client.update(payer_plan_group_id, request=request, request_options=request_options)
        return _response.data

    def deactivate(
        self, payer_plan_group_id: PayerPlanGroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PayerPlanGroup:
        """
        Marks the payer plan group as deactivated

        Parameters
        ----------
        payer_plan_group_id : PayerPlanGroupId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroup

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.payer_plan_groups.v_1.deactivate(
            payer_plan_group_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.deactivate(payer_plan_group_id, request_options=request_options)
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

    async def get_multi(
        self,
        *,
        plan_group_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        payer_uuid: typing.Optional[typing.Union[PayerUuid, typing.Sequence[PayerUuid]]] = None,
        payer_id: typing.Optional[typing.Union[PayerId, typing.Sequence[PayerId]]] = None,
        plan_type: typing.Optional[typing.Union[SourceOfPaymentCode, typing.Sequence[SourceOfPaymentCode]]] = None,
        is_active: typing.Optional[bool] = None,
        payer_plan_group_id: typing.Optional[typing.Union[PayerPlanGroupId, typing.Sequence[PayerPlanGroupId]]] = None,
        limit: typing.Optional[int] = None,
        sort_by_similarity: typing.Optional[str] = None,
        sort: typing.Optional[PayerPlanGroupSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayerPlanGroupPage:
        """
        Returns all payer plan groups matching filter criteria.

        Parameters
        ----------
        plan_group_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        payer_uuid : typing.Optional[typing.Union[PayerUuid, typing.Sequence[PayerUuid]]]

        payer_id : typing.Optional[typing.Union[PayerId, typing.Sequence[PayerId]]]

        plan_type : typing.Optional[typing.Union[SourceOfPaymentCode, typing.Sequence[SourceOfPaymentCode]]]

        is_active : typing.Optional[bool]

        payer_plan_group_id : typing.Optional[typing.Union[PayerPlanGroupId, typing.Sequence[PayerPlanGroupId]]]

        limit : typing.Optional[int]
            Defaults to 100. Cannot exc

        sort_by_similarity : typing.Optional[str]
            If this property is passed, the results will be ordered by those that contain a payer_id, payer_name, plan_group_name, or
            payer_address most similar to the value passed. This will take precedence over the sort and sort_direction properties. This
            will always sort in order of most similar to least similar.

        sort : typing.Optional[PayerPlanGroupSortField]
            Defaults to plan_group_name. If sort_by_similarity is passed, that sort will takes precedence over this property.

        sort_direction : typing.Optional[SortDirection]
            Sort direction. Defaults to ascending order if not provided.

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroupPage

        Examples
        --------
        import asyncio

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.payer_plan_groups.v_1.get_multi()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_multi(
            plan_group_name=plan_group_name,
            payer_uuid=payer_uuid,
            payer_id=payer_id,
            plan_type=plan_type,
            is_active=is_active,
            payer_plan_group_id=payer_plan_group_id,
            limit=limit,
            sort_by_similarity=sort_by_similarity,
            sort=sort,
            sort_direction=sort_direction,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, payer_plan_group_id: PayerPlanGroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PayerPlanGroup:
        """
        Return a plan group with a given ID.

        Parameters
        ----------
        payer_plan_group_id : PayerPlanGroupId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroup

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
            await client.payer_plan_groups.v_1.get(
                payer_plan_group_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(payer_plan_group_id, request_options=request_options)
        return _response.data

    async def create(
        self, *, request: MutablePayerPlanGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> PayerPlanGroup:
        """
        Create a payer plan group

        Parameters
        ----------
        request : MutablePayerPlanGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroup

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.commons import SourceOfPaymentCode
        from candid.resources.payer_plan_groups.resources.v_1 import (
            MutablePayerPlanGroup,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.payer_plan_groups.v_1.create(
                request=MutablePayerPlanGroup(
                    plan_group_name="plan_group_name",
                    payer_uuid=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    plan_type=SourceOfPaymentCode.SELF_PAY,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    async def update(
        self,
        payer_plan_group_id: PayerPlanGroupId,
        *,
        request: MutablePayerPlanGroup,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayerPlanGroup:
        """
        Update any of the fields on a payer plan group

        Parameters
        ----------
        payer_plan_group_id : PayerPlanGroupId

        request : MutablePayerPlanGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroup

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.commons import SourceOfPaymentCode
        from candid.resources.payer_plan_groups.resources.v_1 import (
            MutablePayerPlanGroup,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.payer_plan_groups.v_1.update(
                payer_plan_group_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                request=MutablePayerPlanGroup(
                    plan_group_name="plan_group_name",
                    payer_uuid=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    plan_type=SourceOfPaymentCode.SELF_PAY,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(payer_plan_group_id, request=request, request_options=request_options)
        return _response.data

    async def deactivate(
        self, payer_plan_group_id: PayerPlanGroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PayerPlanGroup:
        """
        Marks the payer plan group as deactivated

        Parameters
        ----------
        payer_plan_group_id : PayerPlanGroupId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPlanGroup

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
            await client.payer_plan_groups.v_1.deactivate(
                payer_plan_group_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deactivate(payer_plan_group_id, request_options=request_options)
        return _response.data
