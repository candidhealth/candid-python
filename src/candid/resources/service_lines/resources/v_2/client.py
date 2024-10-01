# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ....commons.errors.entity_not_found_error import EntityNotFoundError
from ....commons.errors.http_request_validation_error import HttpRequestValidationError
from ....commons.errors.unauthorized_error import UnauthorizedError
from ....commons.types.entity_not_found_error_message import EntityNotFoundErrorMessage
from ....commons.types.request_validation_error import RequestValidationError
from ....commons.types.service_line_id import ServiceLineId
from ....commons.types.unauthorized_error_message import UnauthorizedErrorMessage
from .types.service_line import ServiceLine
from .types.service_line_create_standalone import ServiceLineCreateStandalone
from .types.service_line_update import ServiceLineUpdate

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self, *, request: ServiceLineCreateStandalone, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceLine:
        """
        Parameters
        ----------
        request : ServiceLineCreateStandalone

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceLine

        Examples
        --------
        import datetime
        import uuid

        from candid import FacilityTypeCode, ProcedureModifier, ServiceLineUnits
        from candid.client import CandidApiClient
        from candid.resources.service_lines.v_2 import (
            DenialReasonContent,
            ServiceLineCreateStandalone,
            ServiceLineDenialReason,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.service_lines.v_2.create(
            request=ServiceLineCreateStandalone(
                modifiers=[ProcedureModifier.TWENTY_TWO],
                charge_amount_cents=1,
                diagnosis_id_zero=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                diagnosis_id_one=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                diagnosis_id_two=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                diagnosis_id_three=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                denial_reason=ServiceLineDenialReason(
                    reason=DenialReasonContent.AUTHORIZATION_REQUIRED,
                ),
                place_of_service_code=FacilityTypeCode.PHARMACY,
                procedure_code="string",
                quantity="string",
                units=ServiceLineUnits.MJ,
                claim_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                description="string",
                date_of_service=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                end_date_of_service=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/service-lines/v2",
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
            return pydantic_v1.parse_obj_as(ServiceLine, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic_v1.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        service_line_id: ServiceLineId,
        *,
        request: ServiceLineUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceLine:
        """
        Parameters
        ----------
        service_line_id : ServiceLineId

        request : ServiceLineUpdate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceLine

        Examples
        --------
        import datetime
        import uuid

        from candid import FacilityTypeCode, ProcedureModifier, ServiceLineUnits
        from candid.client import CandidApiClient
        from candid.resources.service_lines.v_2 import (
            DenialReasonContent,
            DrugIdentification,
            MeasurementUnitCode,
            ServiceIdQualifier,
            ServiceLineDenialReason,
            ServiceLineUpdate,
            TestResult_Hematocrit,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.service_lines.v_2.update(
            service_line_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=ServiceLineUpdate(
                edit_reason="string",
                modifiers=[ProcedureModifier.TWENTY_TWO],
                charge_amount_cents=1,
                diagnosis_id_zero=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                diagnosis_id_one=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                diagnosis_id_two=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                diagnosis_id_three=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                drug_identification=DrugIdentification(
                    service_id_qualifier=ServiceIdQualifier.EAN_UCC_13,
                    national_drug_code="string",
                    national_drug_unit_count="string",
                    measurement_unit_code=MeasurementUnitCode.MILLILITERS,
                    link_sequence_number="string",
                    pharmacy_prescription_number="string",
                    conversion_formula="string",
                ),
                denial_reason=ServiceLineDenialReason(
                    reason=DenialReasonContent.AUTHORIZATION_REQUIRED,
                ),
                place_of_service_code=FacilityTypeCode.PHARMACY,
                units=ServiceLineUnits.MJ,
                procedure_code="string",
                quantity="string",
                description="string",
                date_of_service=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                end_date_of_service=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                test_result=TestResult_Hematocrit(value=1.1),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/service-lines/v2/{jsonable_encoder(service_line_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="PATCH",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ServiceLine, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic_v1.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, service_line_id: ServiceLineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        service_line_id : ServiceLineId

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
        client.service_lines.v_2.delete(
            service_line_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/service-lines/v2/{jsonable_encoder(service_line_id)}",
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
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self, *, request: ServiceLineCreateStandalone, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceLine:
        """
        Parameters
        ----------
        request : ServiceLineCreateStandalone

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceLine

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid import FacilityTypeCode, ProcedureModifier, ServiceLineUnits
        from candid.client import AsyncCandidApiClient
        from candid.resources.service_lines.v_2 import (
            DenialReasonContent,
            ServiceLineCreateStandalone,
            ServiceLineDenialReason,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.service_lines.v_2.create(
                request=ServiceLineCreateStandalone(
                    modifiers=[ProcedureModifier.TWENTY_TWO],
                    charge_amount_cents=1,
                    diagnosis_id_zero=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    diagnosis_id_one=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    diagnosis_id_two=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    diagnosis_id_three=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    denial_reason=ServiceLineDenialReason(
                        reason=DenialReasonContent.AUTHORIZATION_REQUIRED,
                    ),
                    place_of_service_code=FacilityTypeCode.PHARMACY,
                    procedure_code="string",
                    quantity="string",
                    units=ServiceLineUnits.MJ,
                    claim_id=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    description="string",
                    date_of_service=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    end_date_of_service=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/service-lines/v2",
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
            return pydantic_v1.parse_obj_as(ServiceLine, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic_v1.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        service_line_id: ServiceLineId,
        *,
        request: ServiceLineUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceLine:
        """
        Parameters
        ----------
        service_line_id : ServiceLineId

        request : ServiceLineUpdate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceLine

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid import FacilityTypeCode, ProcedureModifier, ServiceLineUnits
        from candid.client import AsyncCandidApiClient
        from candid.resources.service_lines.v_2 import (
            DenialReasonContent,
            DrugIdentification,
            MeasurementUnitCode,
            ServiceIdQualifier,
            ServiceLineDenialReason,
            ServiceLineUpdate,
            TestResult_Hematocrit,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.service_lines.v_2.update(
                service_line_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                request=ServiceLineUpdate(
                    edit_reason="string",
                    modifiers=[ProcedureModifier.TWENTY_TWO],
                    charge_amount_cents=1,
                    diagnosis_id_zero=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    diagnosis_id_one=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    diagnosis_id_two=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    diagnosis_id_three=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    drug_identification=DrugIdentification(
                        service_id_qualifier=ServiceIdQualifier.EAN_UCC_13,
                        national_drug_code="string",
                        national_drug_unit_count="string",
                        measurement_unit_code=MeasurementUnitCode.MILLILITERS,
                        link_sequence_number="string",
                        pharmacy_prescription_number="string",
                        conversion_formula="string",
                    ),
                    denial_reason=ServiceLineDenialReason(
                        reason=DenialReasonContent.AUTHORIZATION_REQUIRED,
                    ),
                    place_of_service_code=FacilityTypeCode.PHARMACY,
                    units=ServiceLineUnits.MJ,
                    procedure_code="string",
                    quantity="string",
                    description="string",
                    date_of_service=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    end_date_of_service=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    test_result=TestResult_Hematocrit(value=1.1),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/service-lines/v2/{jsonable_encoder(service_line_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="PATCH",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ServiceLine, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic_v1.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, service_line_id: ServiceLineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        service_line_id : ServiceLineId

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
            await client.service_lines.v_2.delete(
                service_line_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/service-lines/v2/{jsonable_encoder(service_line_id)}",
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
        raise ApiError(status_code=_response.status_code, body=_response_json)
