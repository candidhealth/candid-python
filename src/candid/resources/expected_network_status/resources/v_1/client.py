# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from ....commons.types.date import Date
from ....commons.types.insurance_type_code import InsuranceTypeCode
from ....commons.types.state import State
from .types.expected_network_status_response import ExpectedNetworkStatusResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def compute(
        self,
        *,
        external_patient_id: typing.Optional[str] = OMIT,
        subscriber_payer_id: str,
        subscriber_payer_name: str,
        subscriber_insurance_type: typing.Optional[InsuranceTypeCode] = OMIT,
        subscriber_plan_name: typing.Optional[str] = OMIT,
        billing_provider_npi: str,
        billing_provider_tin: str,
        rendering_provider_npi: str,
        contracted_state: State,
        date_of_service: Date,
    ) -> ExpectedNetworkStatusResponse:
        """
        **This endpoint is incubating.**
        Computes the expected network status given the provided information.

        Parameters:
            - external_patient_id: typing.Optional[str].

            - subscriber_payer_id: str.

            - subscriber_payer_name: str.

            - subscriber_insurance_type: typing.Optional[InsuranceTypeCode].

            - subscriber_plan_name: typing.Optional[str]. The descriptive name of the insurance plan selected by the subscriber, often indicating coverage specifics or tier.

            - billing_provider_npi: str. The National Provider Identifier (NPI) of the healthcare provider responsible for billing. A unique 10-digit identification number.

            - billing_provider_tin: str. Follow the 9-digit format of the Taxpayer Identification Number (TIN).

            - rendering_provider_npi: str. The National Provider Identifier (NPI) of the healthcare provider who delivered the services. A unique 10-digit identification number.

            - contracted_state: State. The state in which the healthcare provider has a contractual agreement with the insurance payer.

            - date_of_service: Date. Date formatted as YYYY-MM-DD; eg: 2019-08-25.

        """
        _request: typing.Dict[str, typing.Any] = {
            "subscriber_payer_id": subscriber_payer_id,
            "subscriber_payer_name": subscriber_payer_name,
            "billing_provider_npi": billing_provider_npi,
            "billing_provider_tin": billing_provider_tin,
            "rendering_provider_npi": rendering_provider_npi,
            "contracted_state": contracted_state,
            "date_of_service": date_of_service,
        }
        if external_patient_id is not OMIT:
            _request["external_patient_id"] = external_patient_id
        if subscriber_insurance_type is not OMIT:
            _request["subscriber_insurance_type"] = subscriber_insurance_type
        if subscriber_plan_name is not OMIT:
            _request["subscriber_plan_name"] = subscriber_plan_name
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/expected-network-status/v1"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ExpectedNetworkStatusResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def compute(
        self,
        *,
        external_patient_id: typing.Optional[str] = OMIT,
        subscriber_payer_id: str,
        subscriber_payer_name: str,
        subscriber_insurance_type: typing.Optional[InsuranceTypeCode] = OMIT,
        subscriber_plan_name: typing.Optional[str] = OMIT,
        billing_provider_npi: str,
        billing_provider_tin: str,
        rendering_provider_npi: str,
        contracted_state: State,
        date_of_service: Date,
    ) -> ExpectedNetworkStatusResponse:
        """
        **This endpoint is incubating.**
        Computes the expected network status given the provided information.

        Parameters:
            - external_patient_id: typing.Optional[str].

            - subscriber_payer_id: str.

            - subscriber_payer_name: str.

            - subscriber_insurance_type: typing.Optional[InsuranceTypeCode].

            - subscriber_plan_name: typing.Optional[str]. The descriptive name of the insurance plan selected by the subscriber, often indicating coverage specifics or tier.

            - billing_provider_npi: str. The National Provider Identifier (NPI) of the healthcare provider responsible for billing. A unique 10-digit identification number.

            - billing_provider_tin: str. Follow the 9-digit format of the Taxpayer Identification Number (TIN).

            - rendering_provider_npi: str. The National Provider Identifier (NPI) of the healthcare provider who delivered the services. A unique 10-digit identification number.

            - contracted_state: State. The state in which the healthcare provider has a contractual agreement with the insurance payer.

            - date_of_service: Date. Date formatted as YYYY-MM-DD; eg: 2019-08-25.

        """
        _request: typing.Dict[str, typing.Any] = {
            "subscriber_payer_id": subscriber_payer_id,
            "subscriber_payer_name": subscriber_payer_name,
            "billing_provider_npi": billing_provider_npi,
            "billing_provider_tin": billing_provider_tin,
            "rendering_provider_npi": rendering_provider_npi,
            "contracted_state": contracted_state,
            "date_of_service": date_of_service,
        }
        if external_patient_id is not OMIT:
            _request["external_patient_id"] = external_patient_id
        if subscriber_insurance_type is not OMIT:
            _request["subscriber_insurance_type"] = subscriber_insurance_type
        if subscriber_plan_name is not OMIT:
            _request["subscriber_plan_name"] = subscriber_plan_name
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/expected-network-status/v1"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ExpectedNetworkStatusResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
