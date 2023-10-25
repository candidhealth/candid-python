# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from ....commons.types.invoice_id import InvoiceId
from ....commons.types.patient_external_id import PatientExternalId
from ....financials.types.refund_allocation import RefundAllocation
from .types.patient_refund import PatientRefund
from .types.patient_refund_id import PatientRefundId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, patient_refund_id: PatientRefundId) -> PatientRefund:
        """
        **This endpoint is incubating.**
        Retrieves a previously created patient refund by its `patient_refund_id`.

        Parameters:
            - patient_refund_id: PatientRefundId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/patient-refunds/v1/{patient_refund_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientRefund, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        amount_cents: int,
        refund_timestamp: typing.Optional[dt.datetime] = OMIT,
        refund_note: typing.Optional[str] = OMIT,
        patient_external_id: typing.Optional[PatientExternalId] = OMIT,
        allocations: typing.List[RefundAllocation],
        invoice: typing.Optional[InvoiceId] = OMIT,
    ) -> PatientRefund:
        """
        **This endpoint is incubating.**
        Creates a new patient refund record and returns the newly created PatientRefund object.
        The allocations can describe whether the refund is being applied toward a specific service line,
        claim, or billing provider.

        Parameters:
            - amount_cents: int.

            - refund_timestamp: typing.Optional[dt.datetime].

            - refund_note: typing.Optional[str].

            - patient_external_id: typing.Optional[PatientExternalId].

            - allocations: typing.List[RefundAllocation].

            - invoice: typing.Optional[InvoiceId].
        """
        _request: typing.Dict[str, typing.Any] = {"amount_cents": amount_cents, "allocations": allocations}
        if refund_timestamp is not OMIT:
            _request["refund_timestamp"] = refund_timestamp
        if refund_note is not OMIT:
            _request["refund_note"] = refund_note
        if patient_external_id is not OMIT:
            _request["patient_external_id"] = patient_external_id
        if invoice is not OMIT:
            _request["invoice"] = invoice
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/patient-refunds/v1"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientRefund, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, patient_refund_id: PatientRefundId) -> None:
        """
        **This endpoint is incubating.**
        Deletes the patient refund record matching the provided patient_refund_id.

        Parameters:
            - patient_refund_id: PatientRefundId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/patient-refunds/v1/{patient_refund_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, patient_refund_id: PatientRefundId) -> PatientRefund:
        """
        **This endpoint is incubating.**
        Retrieves a previously created patient refund by its `patient_refund_id`.

        Parameters:
            - patient_refund_id: PatientRefundId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/patient-refunds/v1/{patient_refund_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientRefund, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        amount_cents: int,
        refund_timestamp: typing.Optional[dt.datetime] = OMIT,
        refund_note: typing.Optional[str] = OMIT,
        patient_external_id: typing.Optional[PatientExternalId] = OMIT,
        allocations: typing.List[RefundAllocation],
        invoice: typing.Optional[InvoiceId] = OMIT,
    ) -> PatientRefund:
        """
        **This endpoint is incubating.**
        Creates a new patient refund record and returns the newly created PatientRefund object.
        The allocations can describe whether the refund is being applied toward a specific service line,
        claim, or billing provider.

        Parameters:
            - amount_cents: int.

            - refund_timestamp: typing.Optional[dt.datetime].

            - refund_note: typing.Optional[str].

            - patient_external_id: typing.Optional[PatientExternalId].

            - allocations: typing.List[RefundAllocation].

            - invoice: typing.Optional[InvoiceId].
        """
        _request: typing.Dict[str, typing.Any] = {"amount_cents": amount_cents, "allocations": allocations}
        if refund_timestamp is not OMIT:
            _request["refund_timestamp"] = refund_timestamp
        if refund_note is not OMIT:
            _request["refund_note"] = refund_note
        if patient_external_id is not OMIT:
            _request["patient_external_id"] = patient_external_id
        if invoice is not OMIT:
            _request["invoice"] = invoice
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/patient-refunds/v1"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientRefund, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, patient_refund_id: PatientRefundId) -> None:
        """
        **This endpoint is incubating.**
        Deletes the patient refund record matching the provided patient_refund_id.

        Parameters:
            - patient_refund_id: PatientRefundId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/patient-refunds/v1/{patient_refund_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
