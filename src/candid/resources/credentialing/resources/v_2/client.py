# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import uuid

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ....commons.types.page_token import PageToken
from ....commons.types.provider_credentialing_span_id import ProviderCredentialingSpanId
from ....commons.types.regions import Regions
from .raw_client import AsyncRawV2Client, RawV2Client
from .types.provider_credentialing_span import ProviderCredentialingSpan
from .types.provider_credentialing_span_page import ProviderCredentialingSpanPage

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV2Client
        """
        return self._raw_client

    def create(
        self,
        *,
        rendering_provider_id: uuid.UUID,
        contracting_provider_id: uuid.UUID,
        payer_uuid: uuid.UUID,
        regions: Regions,
        start_date: typing.Optional[dt.date] = OMIT,
        end_date: typing.Optional[dt.date] = OMIT,
        submitted_date: typing.Optional[dt.date] = OMIT,
        payer_loaded_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderCredentialingSpan:
        """
        Parameters
        ----------
        rendering_provider_id : uuid.UUID
            The ID of the rendering provider covered by the credentialing span.

        contracting_provider_id : uuid.UUID
            The ID of the practice location at which the rendering provider is covered by the credentialing span.

        payer_uuid : uuid.UUID
            The ID of the payer covered by the credentialing span.

        regions : Regions
            The states covered by the credentialing span. A span may be national and cover all states.

        start_date : typing.Optional[dt.date]
            Start date of the credentialing span.

        end_date : typing.Optional[dt.date]
            End date of the credentialing span.

        submitted_date : typing.Optional[dt.date]
            Date that the credential paperwork was submitted.

        payer_loaded_date : typing.Optional[dt.date]
            Date that the payer loaded the credentialing span into their system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderCredentialingSpan

        Examples
        --------
        import uuid

        from candid import CandidApiClient
        from candid.resources.commons import Regions_States, State

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.credentialing.v_2.create(
            rendering_provider_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            contracting_provider_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            payer_uuid=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            regions=Regions_States(
                states=[State.AA, State.AA],
            ),
        )
        """
        _response = self._raw_client.create(
            rendering_provider_id=rendering_provider_id,
            contracting_provider_id=contracting_provider_id,
            payer_uuid=payer_uuid,
            regions=regions,
            start_date=start_date,
            end_date=end_date,
            submitted_date=submitted_date,
            payer_loaded_date=payer_loaded_date,
            request_options=request_options,
        )
        return _response.data

    def get(
        self,
        provider_credentialing_id: ProviderCredentialingSpanId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderCredentialingSpan:
        """
        Parameters
        ----------
        provider_credentialing_id : ProviderCredentialingSpanId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderCredentialingSpan

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.credentialing.v_2.get(
            provider_credentialing_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.get(provider_credentialing_id, request_options=request_options)
        return _response.data

    def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        payer_uuid: typing.Optional[uuid.UUID] = None,
        provider_id: typing.Optional[uuid.UUID] = None,
        as_rendering_provider: typing.Optional[bool] = None,
        as_contracting_provider: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderCredentialingSpanPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities per page, defaults to 100.

        page_token : typing.Optional[PageToken]

        payer_uuid : typing.Optional[uuid.UUID]
            Filter by payer.

        provider_id : typing.Optional[uuid.UUID]
            Filter to a particular provider. Use in conjunction as_rendering_provider and as_contracting_provider.

        as_rendering_provider : typing.Optional[bool]
            Filter to credentialing spans where the provider is a rendering provider. To use this filter provider_id is required.

        as_contracting_provider : typing.Optional[bool]
            Filter to credentialing spans where the provider is a contracting provider. To use this filter provider_id is required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderCredentialingSpanPage

        Examples
        --------
        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.credentialing.v_2.get_all()
        """
        _response = self._raw_client.get_all(
            limit=limit,
            page_token=page_token,
            payer_uuid=payer_uuid,
            provider_id=provider_id,
            as_rendering_provider=as_rendering_provider,
            as_contracting_provider=as_contracting_provider,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self,
        provider_credentialing_id: ProviderCredentialingSpanId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Soft deletes a credentialing span rate from the system.

        Parameters
        ----------
        provider_credentialing_id : ProviderCredentialingSpanId

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
        client.credentialing.v_2.delete(
            provider_credentialing_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.delete(provider_credentialing_id, request_options=request_options)
        return _response.data

    def update(
        self,
        provider_credentialing_id: ProviderCredentialingSpanId,
        *,
        contracting_provider_id: typing.Optional[uuid.UUID] = OMIT,
        payer_uuid: typing.Optional[uuid.UUID] = OMIT,
        start_date: typing.Optional[dt.date] = OMIT,
        end_date: typing.Optional[dt.date] = OMIT,
        regions: typing.Optional[Regions] = OMIT,
        submitted_date: typing.Optional[dt.date] = OMIT,
        payer_loaded_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderCredentialingSpan:
        """
        Parameters
        ----------
        provider_credentialing_id : ProviderCredentialingSpanId

        contracting_provider_id : typing.Optional[uuid.UUID]
            The ID of the practice location at which the rendering provider is covered by the credentialing span.

        payer_uuid : typing.Optional[uuid.UUID]
            The ID of the payer doing the credentialing.

        start_date : typing.Optional[dt.date]
            Start date of the credentialing span.

        end_date : typing.Optional[dt.date]
            End date of the credentialing span.

        regions : typing.Optional[Regions]
            The states covered by the credentialing span. A span may be national and cover all states.

        submitted_date : typing.Optional[dt.date]
            Date that the credential paperwork was submitted.

        payer_loaded_date : typing.Optional[dt.date]
            Date that the payer loaded the credentialing span into their system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderCredentialingSpan

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.credentialing.v_2.update(
            provider_credentialing_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.update(
            provider_credentialing_id,
            contracting_provider_id=contracting_provider_id,
            payer_uuid=payer_uuid,
            start_date=start_date,
            end_date=end_date,
            regions=regions,
            submitted_date=submitted_date,
            payer_loaded_date=payer_loaded_date,
            request_options=request_options,
        )
        return _response.data


class AsyncV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV2Client
        """
        return self._raw_client

    async def create(
        self,
        *,
        rendering_provider_id: uuid.UUID,
        contracting_provider_id: uuid.UUID,
        payer_uuid: uuid.UUID,
        regions: Regions,
        start_date: typing.Optional[dt.date] = OMIT,
        end_date: typing.Optional[dt.date] = OMIT,
        submitted_date: typing.Optional[dt.date] = OMIT,
        payer_loaded_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderCredentialingSpan:
        """
        Parameters
        ----------
        rendering_provider_id : uuid.UUID
            The ID of the rendering provider covered by the credentialing span.

        contracting_provider_id : uuid.UUID
            The ID of the practice location at which the rendering provider is covered by the credentialing span.

        payer_uuid : uuid.UUID
            The ID of the payer covered by the credentialing span.

        regions : Regions
            The states covered by the credentialing span. A span may be national and cover all states.

        start_date : typing.Optional[dt.date]
            Start date of the credentialing span.

        end_date : typing.Optional[dt.date]
            End date of the credentialing span.

        submitted_date : typing.Optional[dt.date]
            Date that the credential paperwork was submitted.

        payer_loaded_date : typing.Optional[dt.date]
            Date that the payer loaded the credentialing span into their system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderCredentialingSpan

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.commons import Regions_States, State

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.credentialing.v_2.create(
                rendering_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                contracting_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                payer_uuid=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                regions=Regions_States(
                    states=[State.AA, State.AA],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            rendering_provider_id=rendering_provider_id,
            contracting_provider_id=contracting_provider_id,
            payer_uuid=payer_uuid,
            regions=regions,
            start_date=start_date,
            end_date=end_date,
            submitted_date=submitted_date,
            payer_loaded_date=payer_loaded_date,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self,
        provider_credentialing_id: ProviderCredentialingSpanId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderCredentialingSpan:
        """
        Parameters
        ----------
        provider_credentialing_id : ProviderCredentialingSpanId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderCredentialingSpan

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
            await client.credentialing.v_2.get(
                provider_credentialing_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(provider_credentialing_id, request_options=request_options)
        return _response.data

    async def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        payer_uuid: typing.Optional[uuid.UUID] = None,
        provider_id: typing.Optional[uuid.UUID] = None,
        as_rendering_provider: typing.Optional[bool] = None,
        as_contracting_provider: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderCredentialingSpanPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities per page, defaults to 100.

        page_token : typing.Optional[PageToken]

        payer_uuid : typing.Optional[uuid.UUID]
            Filter by payer.

        provider_id : typing.Optional[uuid.UUID]
            Filter to a particular provider. Use in conjunction as_rendering_provider and as_contracting_provider.

        as_rendering_provider : typing.Optional[bool]
            Filter to credentialing spans where the provider is a rendering provider. To use this filter provider_id is required.

        as_contracting_provider : typing.Optional[bool]
            Filter to credentialing spans where the provider is a contracting provider. To use this filter provider_id is required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderCredentialingSpanPage

        Examples
        --------
        import asyncio

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.credentialing.v_2.get_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all(
            limit=limit,
            page_token=page_token,
            payer_uuid=payer_uuid,
            provider_id=provider_id,
            as_rendering_provider=as_rendering_provider,
            as_contracting_provider=as_contracting_provider,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self,
        provider_credentialing_id: ProviderCredentialingSpanId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Soft deletes a credentialing span rate from the system.

        Parameters
        ----------
        provider_credentialing_id : ProviderCredentialingSpanId

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
            await client.credentialing.v_2.delete(
                provider_credentialing_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(provider_credentialing_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        provider_credentialing_id: ProviderCredentialingSpanId,
        *,
        contracting_provider_id: typing.Optional[uuid.UUID] = OMIT,
        payer_uuid: typing.Optional[uuid.UUID] = OMIT,
        start_date: typing.Optional[dt.date] = OMIT,
        end_date: typing.Optional[dt.date] = OMIT,
        regions: typing.Optional[Regions] = OMIT,
        submitted_date: typing.Optional[dt.date] = OMIT,
        payer_loaded_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderCredentialingSpan:
        """
        Parameters
        ----------
        provider_credentialing_id : ProviderCredentialingSpanId

        contracting_provider_id : typing.Optional[uuid.UUID]
            The ID of the practice location at which the rendering provider is covered by the credentialing span.

        payer_uuid : typing.Optional[uuid.UUID]
            The ID of the payer doing the credentialing.

        start_date : typing.Optional[dt.date]
            Start date of the credentialing span.

        end_date : typing.Optional[dt.date]
            End date of the credentialing span.

        regions : typing.Optional[Regions]
            The states covered by the credentialing span. A span may be national and cover all states.

        submitted_date : typing.Optional[dt.date]
            Date that the credential paperwork was submitted.

        payer_loaded_date : typing.Optional[dt.date]
            Date that the payer loaded the credentialing span into their system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderCredentialingSpan

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
            await client.credentialing.v_2.update(
                provider_credentialing_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            provider_credentialing_id,
            contracting_provider_id=contracting_provider_id,
            payer_uuid=payer_uuid,
            start_date=start_date,
            end_date=end_date,
            regions=regions,
            submitted_date=submitted_date,
            payer_loaded_date=payer_loaded_date,
            request_options=request_options,
        )
        return _response.data
