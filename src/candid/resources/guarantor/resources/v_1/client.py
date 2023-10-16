# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from ....commons.types.email import Email
from ....commons.types.encounter_id import EncounterId
from ....commons.types.phone_number import PhoneNumber
from ....commons.types.street_address_short_zip import StreetAddressShortZip
from .errors.encounter_has_existing_guarantor_error import EncounterHasExistingGuarantorError
from .types.encounter_has_existing_guarantor_error_type import EncounterHasExistingGuarantorErrorType
from .types.guarantor import Guarantor
from .types.guarantor_create import GuarantorCreate
from .types.guarantor_id import GuarantorId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, encounter_id: EncounterId, *, request: GuarantorCreate) -> Guarantor:
        """
        Parameters:
            - encounter_id: EncounterId.

            - request: GuarantorCreate.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/guarantors/v1/{encounter_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Guarantor, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EncounterHasExistingGuarantorError":
                raise EncounterHasExistingGuarantorError(
                    pydantic.parse_obj_as(EncounterHasExistingGuarantorErrorType, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, guarantor_id: GuarantorId) -> Guarantor:
        """
        Parameters:
            - guarantor_id: GuarantorId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/guarantors/v1/{guarantor_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Guarantor, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        guarantor_id: GuarantorId,
        *,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        date_of_birth: typing.Optional[dt.date] = OMIT,
        address: typing.Optional[StreetAddressShortZip] = OMIT,
        phone_numbers: typing.Optional[typing.List[PhoneNumber]] = OMIT,
        phone_consent: typing.Optional[bool] = OMIT,
        email: typing.Optional[Email] = OMIT,
        email_consent: typing.Optional[bool] = OMIT,
    ) -> Guarantor:
        """
        Parameters:
            - guarantor_id: GuarantorId.

            - first_name: typing.Optional[str].

            - last_name: typing.Optional[str].

            - external_id: typing.Optional[str]. A unique identifier for the guarantor assigned by an external system.

            - date_of_birth: typing.Optional[dt.date]. Date formatted as YYYY-MM-DD; eg: 2019-08-25.

            - address: typing.Optional[StreetAddressShortZip].

            - phone_numbers: typing.Optional[typing.List[PhoneNumber]].

            - phone_consent: typing.Optional[bool].

            - email: typing.Optional[Email].

            - email_consent: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if first_name is not OMIT:
            _request["first_name"] = first_name
        if last_name is not OMIT:
            _request["last_name"] = last_name
        if external_id is not OMIT:
            _request["external_id"] = external_id
        if date_of_birth is not OMIT:
            _request["date_of_birth"] = date_of_birth
        if address is not OMIT:
            _request["address"] = address
        if phone_numbers is not OMIT:
            _request["phone_numbers"] = phone_numbers
        if phone_consent is not OMIT:
            _request["phone_consent"] = phone_consent
        if email is not OMIT:
            _request["email"] = email
        if email_consent is not OMIT:
            _request["email_consent"] = email_consent
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/guarantors/v1/{guarantor_id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Guarantor, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, encounter_id: EncounterId, *, request: GuarantorCreate) -> Guarantor:
        """
        Parameters:
            - encounter_id: EncounterId.

            - request: GuarantorCreate.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/guarantors/v1/{encounter_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Guarantor, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EncounterHasExistingGuarantorError":
                raise EncounterHasExistingGuarantorError(
                    pydantic.parse_obj_as(EncounterHasExistingGuarantorErrorType, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, guarantor_id: GuarantorId) -> Guarantor:
        """
        Parameters:
            - guarantor_id: GuarantorId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/guarantors/v1/{guarantor_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Guarantor, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        guarantor_id: GuarantorId,
        *,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        external_id: typing.Optional[str] = OMIT,
        date_of_birth: typing.Optional[dt.date] = OMIT,
        address: typing.Optional[StreetAddressShortZip] = OMIT,
        phone_numbers: typing.Optional[typing.List[PhoneNumber]] = OMIT,
        phone_consent: typing.Optional[bool] = OMIT,
        email: typing.Optional[Email] = OMIT,
        email_consent: typing.Optional[bool] = OMIT,
    ) -> Guarantor:
        """
        Parameters:
            - guarantor_id: GuarantorId.

            - first_name: typing.Optional[str].

            - last_name: typing.Optional[str].

            - external_id: typing.Optional[str]. A unique identifier for the guarantor assigned by an external system.

            - date_of_birth: typing.Optional[dt.date]. Date formatted as YYYY-MM-DD; eg: 2019-08-25.

            - address: typing.Optional[StreetAddressShortZip].

            - phone_numbers: typing.Optional[typing.List[PhoneNumber]].

            - phone_consent: typing.Optional[bool].

            - email: typing.Optional[Email].

            - email_consent: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if first_name is not OMIT:
            _request["first_name"] = first_name
        if last_name is not OMIT:
            _request["last_name"] = last_name
        if external_id is not OMIT:
            _request["external_id"] = external_id
        if date_of_birth is not OMIT:
            _request["date_of_birth"] = date_of_birth
        if address is not OMIT:
            _request["address"] = address
        if phone_numbers is not OMIT:
            _request["phone_numbers"] = phone_numbers
        if phone_consent is not OMIT:
            _request["phone_consent"] = phone_consent
        if email is not OMIT:
            _request["email"] = email
        if email_consent is not OMIT:
            _request["email_consent"] = email_consent
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/guarantors/v1/{guarantor_id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Guarantor, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
