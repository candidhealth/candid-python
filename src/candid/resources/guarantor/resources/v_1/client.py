# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ....commons.errors.http_request_validations_error import HttpRequestValidationsError
from ....commons.types.encounter_id import EncounterId
from ....commons.types.request_validation_error import RequestValidationError
from .errors.encounter_has_existing_guarantor_error import EncounterHasExistingGuarantorError
from .types.encounter_has_existing_guarantor_error_type import EncounterHasExistingGuarantorErrorType
from .types.guarantor import Guarantor
from .types.guarantor_create import GuarantorCreate
from .types.guarantor_id import GuarantorId
from .types.guarantor_update import GuarantorUpdate

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        encounter_id: EncounterId,
        *,
        request: GuarantorCreate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Guarantor:
        """
        Creates a new guarantor and returns the newly created Guarantor object.

        Parameters
        ----------
        encounter_id : EncounterId

        request : GuarantorCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guarantor

        Examples
        --------
        import datetime
        import uuid

        from candid import PhoneNumber, PhoneNumberType, State, StreetAddressShortZip
        from candid.client import CandidApiClient
        from candid.resources.guarantor.v_1 import GuarantorCreate

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.guarantor.v_1.create(
            encounter_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=GuarantorCreate(
                phone_numbers=[
                    PhoneNumber(
                        number="1234567890",
                        type=PhoneNumberType.HOME,
                    )
                ],
                phone_consent=True,
                email="johndoe@joincandidhealth.com",
                email_consent=True,
                first_name="string",
                last_name="string",
                external_id="string",
                date_of_birth=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                address=StreetAddressShortZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/guarantors/v1/{jsonable_encoder(encounter_id)}",
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
            return pydantic_v1.parse_obj_as(Guarantor, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EncounterHasExistingGuarantorError":
                raise EncounterHasExistingGuarantorError(
                    pydantic_v1.parse_obj_as(EncounterHasExistingGuarantorErrorType, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "HttpRequestValidationsError":
                raise HttpRequestValidationsError(
                    pydantic_v1.parse_obj_as(typing.List[RequestValidationError], _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, guarantor_id: GuarantorId, *, request_options: typing.Optional[RequestOptions] = None) -> Guarantor:
        """
        Retrieves a guarantor by its `guarantor_id`.

        Parameters
        ----------
        guarantor_id : GuarantorId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guarantor

        Examples
        --------
        import uuid

        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.guarantor.v_1.get(
            guarantor_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/guarantors/v1/{jsonable_encoder(guarantor_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Guarantor, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        guarantor_id: GuarantorId,
        *,
        request: GuarantorUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Guarantor:
        """
        Updates a guarantor by its `guarantor_id`.

        Parameters
        ----------
        guarantor_id : GuarantorId

        request : GuarantorUpdate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guarantor

        Examples
        --------
        import datetime
        import uuid

        from candid import State, StreetAddressShortZip
        from candid.client import CandidApiClient
        from candid.resources.guarantor.v_1 import GuarantorUpdate

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.guarantor.v_1.update(
            guarantor_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=GuarantorUpdate(
                first_name="string",
                last_name="string",
                external_id="string",
                date_of_birth=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                address=StreetAddressShortZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
                phone_numbers=[],
                phone_consent=True,
                email="johndoe@joincandidhealth.com",
                email_consent=True,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/guarantors/v1/{jsonable_encoder(guarantor_id)}",
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
            return pydantic_v1.parse_obj_as(Guarantor, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        encounter_id: EncounterId,
        *,
        request: GuarantorCreate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Guarantor:
        """
        Creates a new guarantor and returns the newly created Guarantor object.

        Parameters
        ----------
        encounter_id : EncounterId

        request : GuarantorCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guarantor

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid import PhoneNumber, PhoneNumberType, State, StreetAddressShortZip
        from candid.client import AsyncCandidApiClient
        from candid.resources.guarantor.v_1 import GuarantorCreate

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.guarantor.v_1.create(
                encounter_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                request=GuarantorCreate(
                    phone_numbers=[
                        PhoneNumber(
                            number="1234567890",
                            type=PhoneNumberType.HOME,
                        )
                    ],
                    phone_consent=True,
                    email="johndoe@joincandidhealth.com",
                    email_consent=True,
                    first_name="string",
                    last_name="string",
                    external_id="string",
                    date_of_birth=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    address=StreetAddressShortZip(
                        address_1="123 Main St",
                        address_2="Apt 1",
                        city="New York",
                        state=State.NY,
                        zip_code="10001",
                        zip_plus_four_code="1234",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/guarantors/v1/{jsonable_encoder(encounter_id)}",
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
            return pydantic_v1.parse_obj_as(Guarantor, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EncounterHasExistingGuarantorError":
                raise EncounterHasExistingGuarantorError(
                    pydantic_v1.parse_obj_as(EncounterHasExistingGuarantorErrorType, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "HttpRequestValidationsError":
                raise HttpRequestValidationsError(
                    pydantic_v1.parse_obj_as(typing.List[RequestValidationError], _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, guarantor_id: GuarantorId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Guarantor:
        """
        Retrieves a guarantor by its `guarantor_id`.

        Parameters
        ----------
        guarantor_id : GuarantorId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guarantor

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
            await client.guarantor.v_1.get(
                guarantor_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/guarantors/v1/{jsonable_encoder(guarantor_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Guarantor, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        guarantor_id: GuarantorId,
        *,
        request: GuarantorUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Guarantor:
        """
        Updates a guarantor by its `guarantor_id`.

        Parameters
        ----------
        guarantor_id : GuarantorId

        request : GuarantorUpdate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Guarantor

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid import State, StreetAddressShortZip
        from candid.client import AsyncCandidApiClient
        from candid.resources.guarantor.v_1 import GuarantorUpdate

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.guarantor.v_1.update(
                guarantor_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                request=GuarantorUpdate(
                    first_name="string",
                    last_name="string",
                    external_id="string",
                    date_of_birth=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    address=StreetAddressShortZip(
                        address_1="123 Main St",
                        address_2="Apt 1",
                        city="New York",
                        state=State.NY,
                        zip_code="10001",
                        zip_plus_four_code="1234",
                    ),
                    phone_numbers=[],
                    phone_consent=True,
                    email="johndoe@joincandidhealth.com",
                    email_consent=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/guarantors/v1/{jsonable_encoder(guarantor_id)}",
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
            return pydantic_v1.parse_obj_as(Guarantor, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
