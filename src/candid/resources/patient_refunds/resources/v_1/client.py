# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ....commons.types.claim_id import ClaimId
from ....commons.types.invoice_id import InvoiceId
from ....commons.types.page_token import PageToken
from ....commons.types.patient_external_id import PatientExternalId
from ....commons.types.provider_id import ProviderId
from ....commons.types.service_line_id import ServiceLineId
from ....commons.types.sort_direction import SortDirection
from ....financials.types.allocation_create import AllocationCreate
from ....financials.types.invoice_update import InvoiceUpdate
from ....financials.types.note_update import NoteUpdate
from ....financials.types.patient_transaction_source import PatientTransactionSource
from ....financials.types.refund_reason import RefundReason
from ....financials.types.refund_reason_update import RefundReasonUpdate
from .raw_client import AsyncRawV1Client, RawV1Client
from .types.patient_refund import PatientRefund
from .types.patient_refund_id import PatientRefundId
from .types.patient_refund_sort_field import PatientRefundSortField
from .types.patient_refunds_page import PatientRefundsPage

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
        limit: typing.Optional[int] = None,
        patient_external_id: typing.Optional[PatientExternalId] = None,
        claim_id: typing.Optional[ClaimId] = None,
        service_line_id: typing.Optional[ServiceLineId] = None,
        billing_provider_id: typing.Optional[ProviderId] = None,
        unattributed: typing.Optional[bool] = None,
        invoice_id: typing.Optional[InvoiceId] = None,
        sources: typing.Optional[
            typing.Union[PatientTransactionSource, typing.Sequence[PatientTransactionSource]]
        ] = None,
        sort: typing.Optional[PatientRefundSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatientRefundsPage:
        """
        Returns all patient refunds satisfying the search criteria AND whose organization_id matches
        the current organization_id of the authenticated user.

        Parameters
        ----------
        limit : typing.Optional[int]
            Defaults to 100. The value must be greater than 0 and less than 1000.

        patient_external_id : typing.Optional[PatientExternalId]

        claim_id : typing.Optional[ClaimId]

        service_line_id : typing.Optional[ServiceLineId]

        billing_provider_id : typing.Optional[ProviderId]

        unattributed : typing.Optional[bool]
            returns payments with unattributed allocations if set to true

        invoice_id : typing.Optional[InvoiceId]

        sources : typing.Optional[typing.Union[PatientTransactionSource, typing.Sequence[PatientTransactionSource]]]

        sort : typing.Optional[PatientRefundSortField]
            Defaults to refund_timestamp

        sort_direction : typing.Optional[SortDirection]
            Sort direction. Defaults to descending order if not provided.

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientRefundsPage

        Examples
        --------
        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.patient_refunds.v_1.get_multi()
        """
        _response = self._raw_client.get_multi(
            limit=limit,
            patient_external_id=patient_external_id,
            claim_id=claim_id,
            service_line_id=service_line_id,
            billing_provider_id=billing_provider_id,
            unattributed=unattributed,
            invoice_id=invoice_id,
            sources=sources,
            sort=sort,
            sort_direction=sort_direction,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def get(
        self, patient_refund_id: PatientRefundId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PatientRefund:
        """
        Retrieves a previously created patient refund by its `patient_refund_id`.

        Parameters
        ----------
        patient_refund_id : PatientRefundId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientRefund

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.patient_refunds.v_1.get(
            patient_refund_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.get(patient_refund_id, request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        amount_cents: int,
        patient_external_id: PatientExternalId,
        allocations: typing.Sequence[AllocationCreate],
        refund_timestamp: typing.Optional[dt.datetime] = OMIT,
        refund_note: typing.Optional[str] = OMIT,
        invoice: typing.Optional[InvoiceId] = OMIT,
        refund_reason: typing.Optional[RefundReason] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatientRefund:
        """
        Creates a new patient refund record and returns the newly created PatientRefund object.
        The allocations can describe whether the refund is being applied toward a specific service line,
        claim, or billing provider.

        Parameters
        ----------
        amount_cents : int

        patient_external_id : PatientExternalId

        allocations : typing.Sequence[AllocationCreate]

        refund_timestamp : typing.Optional[dt.datetime]

        refund_note : typing.Optional[str]

        invoice : typing.Optional[InvoiceId]

        refund_reason : typing.Optional[RefundReason]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientRefund

        Examples
        --------
        import uuid

        from candid import CandidApiClient
        from candid.resources.financials import (
            AllocationCreate,
            AllocationTargetCreate_ServiceLineById,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.patient_refunds.v_1.create(
            amount_cents=1,
            patient_external_id="patient_external_id",
            allocations=[
                AllocationCreate(
                    amount_cents=1,
                    target=AllocationTargetCreate_ServiceLineById(
                        value=uuid.UUID(
                            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                        )
                    ),
                ),
                AllocationCreate(
                    amount_cents=1,
                    target=AllocationTargetCreate_ServiceLineById(
                        value=uuid.UUID(
                            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                        )
                    ),
                ),
            ],
        )
        """
        _response = self._raw_client.create(
            amount_cents=amount_cents,
            patient_external_id=patient_external_id,
            allocations=allocations,
            refund_timestamp=refund_timestamp,
            refund_note=refund_note,
            invoice=invoice,
            refund_reason=refund_reason,
            request_options=request_options,
        )
        return _response.data

    def update(
        self,
        patient_refund_id: PatientRefundId,
        *,
        refund_timestamp: typing.Optional[dt.datetime] = OMIT,
        refund_note: typing.Optional[NoteUpdate] = OMIT,
        invoice: typing.Optional[InvoiceUpdate] = OMIT,
        refund_reason: typing.Optional[RefundReasonUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatientRefund:
        """
        Updates the patient refund record matching the provided patient_refund_id.

        Parameters
        ----------
        patient_refund_id : PatientRefundId

        refund_timestamp : typing.Optional[dt.datetime]

        refund_note : typing.Optional[NoteUpdate]

        invoice : typing.Optional[InvoiceUpdate]

        refund_reason : typing.Optional[RefundReasonUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientRefund

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.patient_refunds.v_1.update(
            patient_refund_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.update(
            patient_refund_id,
            refund_timestamp=refund_timestamp,
            refund_note=refund_note,
            invoice=invoice,
            refund_reason=refund_reason,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, patient_refund_id: PatientRefundId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the patient refund record matching the provided patient_refund_id.

        Parameters
        ----------
        patient_refund_id : PatientRefundId

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
        client.patient_refunds.v_1.delete(
            patient_refund_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.delete(patient_refund_id, request_options=request_options)
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
        limit: typing.Optional[int] = None,
        patient_external_id: typing.Optional[PatientExternalId] = None,
        claim_id: typing.Optional[ClaimId] = None,
        service_line_id: typing.Optional[ServiceLineId] = None,
        billing_provider_id: typing.Optional[ProviderId] = None,
        unattributed: typing.Optional[bool] = None,
        invoice_id: typing.Optional[InvoiceId] = None,
        sources: typing.Optional[
            typing.Union[PatientTransactionSource, typing.Sequence[PatientTransactionSource]]
        ] = None,
        sort: typing.Optional[PatientRefundSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatientRefundsPage:
        """
        Returns all patient refunds satisfying the search criteria AND whose organization_id matches
        the current organization_id of the authenticated user.

        Parameters
        ----------
        limit : typing.Optional[int]
            Defaults to 100. The value must be greater than 0 and less than 1000.

        patient_external_id : typing.Optional[PatientExternalId]

        claim_id : typing.Optional[ClaimId]

        service_line_id : typing.Optional[ServiceLineId]

        billing_provider_id : typing.Optional[ProviderId]

        unattributed : typing.Optional[bool]
            returns payments with unattributed allocations if set to true

        invoice_id : typing.Optional[InvoiceId]

        sources : typing.Optional[typing.Union[PatientTransactionSource, typing.Sequence[PatientTransactionSource]]]

        sort : typing.Optional[PatientRefundSortField]
            Defaults to refund_timestamp

        sort_direction : typing.Optional[SortDirection]
            Sort direction. Defaults to descending order if not provided.

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientRefundsPage

        Examples
        --------
        import asyncio

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.patient_refunds.v_1.get_multi()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_multi(
            limit=limit,
            patient_external_id=patient_external_id,
            claim_id=claim_id,
            service_line_id=service_line_id,
            billing_provider_id=billing_provider_id,
            unattributed=unattributed,
            invoice_id=invoice_id,
            sources=sources,
            sort=sort,
            sort_direction=sort_direction,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, patient_refund_id: PatientRefundId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PatientRefund:
        """
        Retrieves a previously created patient refund by its `patient_refund_id`.

        Parameters
        ----------
        patient_refund_id : PatientRefundId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientRefund

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
            await client.patient_refunds.v_1.get(
                patient_refund_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(patient_refund_id, request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        amount_cents: int,
        patient_external_id: PatientExternalId,
        allocations: typing.Sequence[AllocationCreate],
        refund_timestamp: typing.Optional[dt.datetime] = OMIT,
        refund_note: typing.Optional[str] = OMIT,
        invoice: typing.Optional[InvoiceId] = OMIT,
        refund_reason: typing.Optional[RefundReason] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatientRefund:
        """
        Creates a new patient refund record and returns the newly created PatientRefund object.
        The allocations can describe whether the refund is being applied toward a specific service line,
        claim, or billing provider.

        Parameters
        ----------
        amount_cents : int

        patient_external_id : PatientExternalId

        allocations : typing.Sequence[AllocationCreate]

        refund_timestamp : typing.Optional[dt.datetime]

        refund_note : typing.Optional[str]

        invoice : typing.Optional[InvoiceId]

        refund_reason : typing.Optional[RefundReason]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientRefund

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.financials import (
            AllocationCreate,
            AllocationTargetCreate_ServiceLineById,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.patient_refunds.v_1.create(
                amount_cents=1,
                patient_external_id="patient_external_id",
                allocations=[
                    AllocationCreate(
                        amount_cents=1,
                        target=AllocationTargetCreate_ServiceLineById(
                            value=uuid.UUID(
                                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                            )
                        ),
                    ),
                    AllocationCreate(
                        amount_cents=1,
                        target=AllocationTargetCreate_ServiceLineById(
                            value=uuid.UUID(
                                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                            )
                        ),
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            amount_cents=amount_cents,
            patient_external_id=patient_external_id,
            allocations=allocations,
            refund_timestamp=refund_timestamp,
            refund_note=refund_note,
            invoice=invoice,
            refund_reason=refund_reason,
            request_options=request_options,
        )
        return _response.data

    async def update(
        self,
        patient_refund_id: PatientRefundId,
        *,
        refund_timestamp: typing.Optional[dt.datetime] = OMIT,
        refund_note: typing.Optional[NoteUpdate] = OMIT,
        invoice: typing.Optional[InvoiceUpdate] = OMIT,
        refund_reason: typing.Optional[RefundReasonUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatientRefund:
        """
        Updates the patient refund record matching the provided patient_refund_id.

        Parameters
        ----------
        patient_refund_id : PatientRefundId

        refund_timestamp : typing.Optional[dt.datetime]

        refund_note : typing.Optional[NoteUpdate]

        invoice : typing.Optional[InvoiceUpdate]

        refund_reason : typing.Optional[RefundReasonUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatientRefund

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
            await client.patient_refunds.v_1.update(
                patient_refund_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            patient_refund_id,
            refund_timestamp=refund_timestamp,
            refund_note=refund_note,
            invoice=invoice,
            refund_reason=refund_reason,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, patient_refund_id: PatientRefundId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the patient refund record matching the provided patient_refund_id.

        Parameters
        ----------
        patient_refund_id : PatientRefundId

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
            await client.patient_refunds.v_1.delete(
                patient_refund_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(patient_refund_id, request_options=request_options)
        return _response.data
