# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ....commons.errors.entity_not_found_error import EntityNotFoundError
from ....commons.errors.unauthorized_error import UnauthorizedError
from ....commons.errors.unprocessable_entity_error import UnprocessableEntityError
from ....commons.types.claim_id import ClaimId
from ....commons.types.entity_not_found_error_message import EntityNotFoundErrorMessage
from ....commons.types.page_token import PageToken
from ....commons.types.provider_id import ProviderId
from ....commons.types.service_line_id import ServiceLineId
from ....commons.types.sort_direction import SortDirection
from ....commons.types.unauthorized_error_message import UnauthorizedErrorMessage
from ....commons.types.unprocessable_entity_error_message import UnprocessableEntityErrorMessage
from ....financials.types.note_update import NoteUpdate
from ....payers.resources.v_3.types.payer_uuid import PayerUuid
from .types.insurance_payment import InsurancePayment
from .types.insurance_payment_create import InsurancePaymentCreate
from .types.insurance_payment_id import InsurancePaymentId
from .types.insurance_payment_sort_field import InsurancePaymentSortField
from .types.insurance_payments_page import InsurancePaymentsPage

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        payer_uuid: typing.Optional[PayerUuid] = None,
        claim_id: typing.Optional[ClaimId] = None,
        service_line_id: typing.Optional[ServiceLineId] = None,
        billing_provider_id: typing.Optional[ProviderId] = None,
        sort: typing.Optional[InsurancePaymentSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsurancePaymentsPage:
        """
        Returns all non-ERA originated insurance payments satisfying the search criteria

        Parameters
        ----------
        limit : typing.Optional[int]
            Defaults to 100. The value must be greater than 0 and less than 1000.

        payer_uuid : typing.Optional[PayerUuid]

        claim_id : typing.Optional[ClaimId]

        service_line_id : typing.Optional[ServiceLineId]

        billing_provider_id : typing.Optional[ProviderId]

        sort : typing.Optional[InsurancePaymentSortField]
            Defaults to payment_timestamp

        sort_direction : typing.Optional[SortDirection]
            Sort direction. Defaults to descending order if not provided.

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsurancePaymentsPage

        Examples
        --------
        import uuid

        from candid import SortDirection
        from candid.client import CandidApiClient
        from candid.resources.insurance_payments.v_1 import InsurancePaymentSortField

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.insurance_payments.v_1.get_multi(
            limit=1,
            payer_uuid=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            claim_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            service_line_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            billing_provider_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            sort=InsurancePaymentSortField.AMOUNT_CENTS,
            sort_direction=SortDirection.ASC,
            page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/insurance-payments/v1",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            params={
                "limit": limit,
                "payer_uuid": jsonable_encoder(payer_uuid),
                "claim_id": jsonable_encoder(claim_id),
                "service_line_id": jsonable_encoder(service_line_id),
                "billing_provider_id": jsonable_encoder(billing_provider_id),
                "sort": sort,
                "sort_direction": sort_direction,
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(InsurancePaymentsPage, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, insurance_payment_id: InsurancePaymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InsurancePayment:
        """
        Retrieves a previously created insurance payment by its `insurance_payment_id`.
        If the payment does not exist, a `403` will be thrown.

        Parameters
        ----------
        insurance_payment_id : InsurancePaymentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsurancePayment

        Examples
        --------
        import uuid

        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.insurance_payments.v_1.get(
            insurance_payment_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/insurance-payments/v1/{jsonable_encoder(insurance_payment_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(InsurancePayment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, request: InsurancePaymentCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> InsurancePayment:
        """
        Creates a new insurance payment record and returns the newly created `InsurancePayment` object. This endpoint
        should only be used for insurance payments that do not have a corresponding ERA (for example: a settlement check
        from a payer). If the payment is an ERA, then you should used the insurance-adjudications API.

        Parameters
        ----------
        request : InsurancePaymentCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsurancePayment

        Examples
        --------
        import datetime
        import uuid

        from candid import AllocationCreate, AllocationTargetCreate_ServiceLineById
        from candid.client import CandidApiClient
        from candid.resources.insurance_payments.v_1 import InsurancePaymentCreate
        from candid.resources.payers.v_3 import PayerIdentifier_PayerInfo

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.insurance_payments.v_1.create(
            request=InsurancePaymentCreate(
                payer_identifier=PayerIdentifier_PayerInfo(),
                amount_cents=1,
                payment_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                payment_note="string",
                allocations=[
                    AllocationCreate(
                        amount_cents=1,
                        target=AllocationTargetCreate_ServiceLineById(
                            value=uuid.UUID(
                                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                            )
                        ),
                    )
                ],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/insurance-payments/v1",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(InsurancePayment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        insurance_payment_id: InsurancePaymentId,
        *,
        payment_timestamp: typing.Optional[dt.datetime] = OMIT,
        payment_note: typing.Optional[NoteUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsurancePayment:
        """
        Updates the patient payment record matching the provided insurance_payment_id. If updating the payment amount,
        then the allocations must be appropriately updated as well.

        Parameters
        ----------
        insurance_payment_id : InsurancePaymentId

        payment_timestamp : typing.Optional[dt.datetime]

        payment_note : typing.Optional[NoteUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsurancePayment

        Examples
        --------
        import datetime
        import uuid

        from candid import NoteUpdate_Set
        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.insurance_payments.v_1.update(
            insurance_payment_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            payment_timestamp=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            payment_note=NoteUpdate_Set(value="string"),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/insurance-payments/v1/{jsonable_encoder(insurance_payment_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="PATCH",
            json={"payment_timestamp": payment_timestamp, "payment_note": payment_note},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(InsurancePayment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, insurance_payment_id: InsurancePaymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the insurance payment record matching the provided `insurance_payment_id`.
        If the matching record's organization_id does not match the authenticated user's
        current organization_id, then a response code of `403` will be returned.

        Parameters
        ----------
        insurance_payment_id : InsurancePaymentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import uuid

        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.insurance_payments.v_1.delete(
            insurance_payment_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/insurance-payments/v1/{jsonable_encoder(insurance_payment_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        payer_uuid: typing.Optional[PayerUuid] = None,
        claim_id: typing.Optional[ClaimId] = None,
        service_line_id: typing.Optional[ServiceLineId] = None,
        billing_provider_id: typing.Optional[ProviderId] = None,
        sort: typing.Optional[InsurancePaymentSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsurancePaymentsPage:
        """
        Returns all non-ERA originated insurance payments satisfying the search criteria

        Parameters
        ----------
        limit : typing.Optional[int]
            Defaults to 100. The value must be greater than 0 and less than 1000.

        payer_uuid : typing.Optional[PayerUuid]

        claim_id : typing.Optional[ClaimId]

        service_line_id : typing.Optional[ServiceLineId]

        billing_provider_id : typing.Optional[ProviderId]

        sort : typing.Optional[InsurancePaymentSortField]
            Defaults to payment_timestamp

        sort_direction : typing.Optional[SortDirection]
            Sort direction. Defaults to descending order if not provided.

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsurancePaymentsPage

        Examples
        --------
        import asyncio
        import uuid

        from candid import SortDirection
        from candid.client import AsyncCandidApiClient
        from candid.resources.insurance_payments.v_1 import InsurancePaymentSortField

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.insurance_payments.v_1.get_multi(
                limit=1,
                payer_uuid=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                claim_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                service_line_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                billing_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                sort=InsurancePaymentSortField.AMOUNT_CENTS,
                sort_direction=SortDirection.ASC,
                page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/insurance-payments/v1",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            params={
                "limit": limit,
                "payer_uuid": jsonable_encoder(payer_uuid),
                "claim_id": jsonable_encoder(claim_id),
                "service_line_id": jsonable_encoder(service_line_id),
                "billing_provider_id": jsonable_encoder(billing_provider_id),
                "sort": sort,
                "sort_direction": sort_direction,
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(InsurancePaymentsPage, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, insurance_payment_id: InsurancePaymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InsurancePayment:
        """
        Retrieves a previously created insurance payment by its `insurance_payment_id`.
        If the payment does not exist, a `403` will be thrown.

        Parameters
        ----------
        insurance_payment_id : InsurancePaymentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsurancePayment

        Examples
        --------
        import asyncio
        import uuid

        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.insurance_payments.v_1.get(
                insurance_payment_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/insurance-payments/v1/{jsonable_encoder(insurance_payment_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(InsurancePayment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, request: InsurancePaymentCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> InsurancePayment:
        """
        Creates a new insurance payment record and returns the newly created `InsurancePayment` object. This endpoint
        should only be used for insurance payments that do not have a corresponding ERA (for example: a settlement check
        from a payer). If the payment is an ERA, then you should used the insurance-adjudications API.

        Parameters
        ----------
        request : InsurancePaymentCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsurancePayment

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid import AllocationCreate, AllocationTargetCreate_ServiceLineById
        from candid.client import AsyncCandidApiClient
        from candid.resources.insurance_payments.v_1 import InsurancePaymentCreate
        from candid.resources.payers.v_3 import PayerIdentifier_PayerInfo

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.insurance_payments.v_1.create(
                request=InsurancePaymentCreate(
                    payer_identifier=PayerIdentifier_PayerInfo(),
                    amount_cents=1,
                    payment_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    payment_note="string",
                    allocations=[
                        AllocationCreate(
                            amount_cents=1,
                            target=AllocationTargetCreate_ServiceLineById(
                                value=uuid.UUID(
                                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                                )
                            ),
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/insurance-payments/v1",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(InsurancePayment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        insurance_payment_id: InsurancePaymentId,
        *,
        payment_timestamp: typing.Optional[dt.datetime] = OMIT,
        payment_note: typing.Optional[NoteUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsurancePayment:
        """
        Updates the patient payment record matching the provided insurance_payment_id. If updating the payment amount,
        then the allocations must be appropriately updated as well.

        Parameters
        ----------
        insurance_payment_id : InsurancePaymentId

        payment_timestamp : typing.Optional[dt.datetime]

        payment_note : typing.Optional[NoteUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsurancePayment

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid import NoteUpdate_Set
        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.insurance_payments.v_1.update(
                insurance_payment_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                payment_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                payment_note=NoteUpdate_Set(value="string"),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/insurance-payments/v1/{jsonable_encoder(insurance_payment_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="PATCH",
            json={"payment_timestamp": payment_timestamp, "payment_note": payment_note},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(InsurancePayment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, insurance_payment_id: InsurancePaymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the insurance payment record matching the provided `insurance_payment_id`.
        If the matching record's organization_id does not match the authenticated user's
        current organization_id, then a response code of `403` will be returned.

        Parameters
        ----------
        insurance_payment_id : InsurancePaymentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import uuid

        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.insurance_payments.v_1.delete(
                insurance_payment_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/insurance-payments/v1/{jsonable_encoder(insurance_payment_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
