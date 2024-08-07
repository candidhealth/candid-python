# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .......core.api_error import ApiError
from .......core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .......core.datetime_utils import serialize_datetime
from .......core.jsonable_encoder import jsonable_encoder
from .......core.pydantic_utilities import pydantic_v1
from .......core.request_options import RequestOptions
from ....common.errors.not_found_error import NotFoundError
from ....common.errors.version_conflict_error import VersionConflictError
from ....common.types.not_found_error_body import NotFoundErrorBody
from ....common.types.version_conflict_error_body import VersionConflictErrorBody
from .types.mutable_patient import MutablePatient
from .types.patient import Patient
from .types.patient_id import PatientId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, request: MutablePatient, request_options: typing.Optional[RequestOptions] = None) -> Patient:
        """
        Adds a patient. VersionConflictError is returned when the patient's external ID is already in use.

        Parameters
        ----------
        request : MutablePatient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Patient

        Examples
        --------
        import datetime
        import uuid

        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment
        from candid.resources.pre_encounter import (Address, ContactPoint,
                                                    DisabilityStatus, Ethnicity,
                                                    Gender, HumanName, Period, Race,
                                                    Relationship, Sex,
                                                    SexualOrientation)
        from candid.resources.pre_encounter.patients.v_1 import (Contact,
                                                                 ExternalProvenance,
                                                                 ExternalProvider,
                                                                 FilingOrder,
                                                                 MaritalStatus,
                                                                 MutablePatient)

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.pre_encounter.patients.v_1.create(request=MutablePatient(name=HumanName(), other_names=[HumanName()], gender=Gender.MAN, birth_date=datetime.date.fromisoformat("2023-01-15", ), social_security_number='string', biological_sex=Sex.FEMALE, sexual_orientation=SexualOrientation.HETEROSEXUAL, race=Race.AMERICAN_INDIAN_OR_ALASKA_NATIVE, ethnicity=Ethnicity.HISPANIC_OR_LATINO, disability_status=DisabilityStatus.DISABLED, marital_status=MaritalStatus.ANNULLED, deceased=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00", ), multiple_birth=1, primary_address=Address(), other_addresses=[Address()], primary_telecom=ContactPoint(), other_telecoms=[ContactPoint()], email='string', electronic_communication_opt_in=True, photo='string', language='string', external_provenance=ExternalProvenance(external_id='string', system_name='string', ), contacts=[Contact(relationship=[Relationship.SELF], name=HumanName(), gender=Gender.MAN, telecoms=[ContactPoint()], addresses=[Address()], period=Period(), )], general_practitioners=[ExternalProvider(name=HumanName(), npi='string', telecoms=[ContactPoint()], addresses=[Address()], period=Period(), )], filing_order=FilingOrder(coverages=[uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", )], ), ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "patients/v1",
            base_url=self._client_wrapper.get_environment().pre_encounter,
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
            return pydantic_v1.parse_obj_as(Patient, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: PatientId, *, request_options: typing.Optional[RequestOptions] = None) -> Patient:
        """
        Gets a patient.

        Parameters
        ----------
        id : PatientId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Patient

        Examples
        --------
        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.pre_encounter.patients.v_1.get(id='string', )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"patients/v1/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Patient, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_history(
        self, id: PatientId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Patient]:
        """
        Gets a patient along with it's full history. The return list is ordered by version ascending.

        Parameters
        ----------
        id : PatientId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Patient]

        Examples
        --------
        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.pre_encounter.patients.v_1.get_history(id='string', )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"patients/v1/{jsonable_encoder(id)}/history",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Patient], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: PatientId,
        version: str,
        *,
        request: MutablePatient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Patient:
        """
        Updates a patient. The path must contain the most recent version to prevent races. Updating historic versions is not supported.

        Parameters
        ----------
        id : PatientId

        version : str

        request : MutablePatient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Patient

        Examples
        --------
        import datetime
        import uuid

        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment
        from candid.resources.pre_encounter import (Address, ContactPoint,
                                                    DisabilityStatus, Ethnicity,
                                                    Gender, HumanName, Period, Race,
                                                    Relationship, Sex,
                                                    SexualOrientation)
        from candid.resources.pre_encounter.patients.v_1 import (Contact,
                                                                 ExternalProvenance,
                                                                 ExternalProvider,
                                                                 FilingOrder,
                                                                 MaritalStatus,
                                                                 MutablePatient)

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.pre_encounter.patients.v_1.update(id='string', version='string', request=MutablePatient(name=HumanName(), other_names=[HumanName()], gender=Gender.MAN, birth_date=datetime.date.fromisoformat("2023-01-15", ), social_security_number='string', biological_sex=Sex.FEMALE, sexual_orientation=SexualOrientation.HETEROSEXUAL, race=Race.AMERICAN_INDIAN_OR_ALASKA_NATIVE, ethnicity=Ethnicity.HISPANIC_OR_LATINO, disability_status=DisabilityStatus.DISABLED, marital_status=MaritalStatus.ANNULLED, deceased=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00", ), multiple_birth=1, primary_address=Address(), other_addresses=[Address()], primary_telecom=ContactPoint(), other_telecoms=[ContactPoint()], email='string', electronic_communication_opt_in=True, photo='string', language='string', external_provenance=ExternalProvenance(external_id='string', system_name='string', ), contacts=[Contact(relationship=[Relationship.SELF], name=HumanName(), gender=Gender.MAN, telecoms=[ContactPoint()], addresses=[Address()], period=Period(), )], general_practitioners=[ExternalProvider(name=HumanName(), npi='string', telecoms=[ContactPoint()], addresses=[Address()], period=Period(), )], filing_order=FilingOrder(coverages=[uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", )], ), ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"patients/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Patient, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def deactivate(
        self, id: PatientId, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Sets a patient as deactivated. The path must contain the most recent version to prevent races. Dactivating historic versions is not supported. Subsequent updates via PUT to the patient will "reactivate" the patient and set the deactivated flag to false.

        Parameters
        ----------
        id : PatientId

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.pre_encounter.patients.v_1.deactivate(id='string', version='string', )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"patients/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
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
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def search(
        self, *, name_contains: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Patient]:
        """
        Searches for patients that match the query parameters.

        Parameters
        ----------
        name_contains : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Patient]

        Examples
        --------
        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.pre_encounter.patients.v_1.search(name_contains='string', )
        """
        _response = self._client_wrapper.httpx_client.request(
            "patients/v1",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            params={"name_contains": name_contains},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Patient], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def scan(
        self, *, since: dt.datetime, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Patient]:
        """
        Scans up to 100 patient updates. The since query parameter is inclusive, and the result list is ordered by updatedAt descending.

        Parameters
        ----------
        since : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Patient]

        Examples
        --------
        import datetime

        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.pre_encounter.patients.v_1.scan(since=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00", ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "patients/v1/updates/scan",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            params={"since": serialize_datetime(since)},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Patient], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self, *, request: MutablePatient, request_options: typing.Optional[RequestOptions] = None
    ) -> Patient:
        """
        Adds a patient. VersionConflictError is returned when the patient's external ID is already in use.

        Parameters
        ----------
        request : MutablePatient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Patient

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment
        from candid.resources.pre_encounter import (Address, ContactPoint,
                                                    DisabilityStatus, Ethnicity,
                                                    Gender, HumanName, Period, Race,
                                                    Relationship, Sex,
                                                    SexualOrientation)
        from candid.resources.pre_encounter.patients.v_1 import (Contact,
                                                                 ExternalProvenance,
                                                                 ExternalProvider,
                                                                 FilingOrder,
                                                                 MaritalStatus,
                                                                 MutablePatient)

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.pre_encounter.patients.v_1.create(request=MutablePatient(name=HumanName(), other_names=[HumanName()], gender=Gender.MAN, birth_date=datetime.date.fromisoformat("2023-01-15", ), social_security_number='string', biological_sex=Sex.FEMALE, sexual_orientation=SexualOrientation.HETEROSEXUAL, race=Race.AMERICAN_INDIAN_OR_ALASKA_NATIVE, ethnicity=Ethnicity.HISPANIC_OR_LATINO, disability_status=DisabilityStatus.DISABLED, marital_status=MaritalStatus.ANNULLED, deceased=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00", ), multiple_birth=1, primary_address=Address(), other_addresses=[Address()], primary_telecom=ContactPoint(), other_telecoms=[ContactPoint()], email='string', electronic_communication_opt_in=True, photo='string', language='string', external_provenance=ExternalProvenance(external_id='string', system_name='string', ), contacts=[Contact(relationship=[Relationship.SELF], name=HumanName(), gender=Gender.MAN, telecoms=[ContactPoint()], addresses=[Address()], period=Period(), )], general_practitioners=[ExternalProvider(name=HumanName(), npi='string', telecoms=[ContactPoint()], addresses=[Address()], period=Period(), )], filing_order=FilingOrder(coverages=[uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", )], ), ), )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "patients/v1",
            base_url=self._client_wrapper.get_environment().pre_encounter,
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
            return pydantic_v1.parse_obj_as(Patient, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: PatientId, *, request_options: typing.Optional[RequestOptions] = None) -> Patient:
        """
        Gets a patient.

        Parameters
        ----------
        id : PatientId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Patient

        Examples
        --------
        import asyncio

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.pre_encounter.patients.v_1.get(id='string', )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"patients/v1/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Patient, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_history(
        self, id: PatientId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Patient]:
        """
        Gets a patient along with it's full history. The return list is ordered by version ascending.

        Parameters
        ----------
        id : PatientId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Patient]

        Examples
        --------
        import asyncio

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.pre_encounter.patients.v_1.get_history(id='string', )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"patients/v1/{jsonable_encoder(id)}/history",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Patient], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: PatientId,
        version: str,
        *,
        request: MutablePatient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Patient:
        """
        Updates a patient. The path must contain the most recent version to prevent races. Updating historic versions is not supported.

        Parameters
        ----------
        id : PatientId

        version : str

        request : MutablePatient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Patient

        Examples
        --------
        import asyncio
        import datetime
        import uuid

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment
        from candid.resources.pre_encounter import (Address, ContactPoint,
                                                    DisabilityStatus, Ethnicity,
                                                    Gender, HumanName, Period, Race,
                                                    Relationship, Sex,
                                                    SexualOrientation)
        from candid.resources.pre_encounter.patients.v_1 import (Contact,
                                                                 ExternalProvenance,
                                                                 ExternalProvider,
                                                                 FilingOrder,
                                                                 MaritalStatus,
                                                                 MutablePatient)

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.pre_encounter.patients.v_1.update(id='string', version='string', request=MutablePatient(name=HumanName(), other_names=[HumanName()], gender=Gender.MAN, birth_date=datetime.date.fromisoformat("2023-01-15", ), social_security_number='string', biological_sex=Sex.FEMALE, sexual_orientation=SexualOrientation.HETEROSEXUAL, race=Race.AMERICAN_INDIAN_OR_ALASKA_NATIVE, ethnicity=Ethnicity.HISPANIC_OR_LATINO, disability_status=DisabilityStatus.DISABLED, marital_status=MaritalStatus.ANNULLED, deceased=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00", ), multiple_birth=1, primary_address=Address(), other_addresses=[Address()], primary_telecom=ContactPoint(), other_telecoms=[ContactPoint()], email='string', electronic_communication_opt_in=True, photo='string', language='string', external_provenance=ExternalProvenance(external_id='string', system_name='string', ), contacts=[Contact(relationship=[Relationship.SELF], name=HumanName(), gender=Gender.MAN, telecoms=[ContactPoint()], addresses=[Address()], period=Period(), )], general_practitioners=[ExternalProvider(name=HumanName(), npi='string', telecoms=[ContactPoint()], addresses=[Address()], period=Period(), )], filing_order=FilingOrder(coverages=[uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", )], ), ), )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"patients/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Patient, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def deactivate(
        self, id: PatientId, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Sets a patient as deactivated. The path must contain the most recent version to prevent races. Dactivating historic versions is not supported. Subsequent updates via PUT to the patient will "reactivate" the patient and set the deactivated flag to false.

        Parameters
        ----------
        id : PatientId

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.pre_encounter.patients.v_1.deactivate(id='string', version='string', )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"patients/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
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
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def search(
        self, *, name_contains: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Patient]:
        """
        Searches for patients that match the query parameters.

        Parameters
        ----------
        name_contains : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Patient]

        Examples
        --------
        import asyncio

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.pre_encounter.patients.v_1.search(name_contains='string', )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "patients/v1",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            params={"name_contains": name_contains},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Patient], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def scan(
        self, *, since: dt.datetime, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Patient]:
        """
        Scans up to 100 patient updates. The since query parameter is inclusive, and the result list is ordered by updatedAt descending.

        Parameters
        ----------
        since : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Patient]

        Examples
        --------
        import asyncio
        import datetime

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.pre_encounter.patients.v_1.scan(since=datetime.datetime.fromisoformat("2024-01-15 09:30:00+00:00", ), )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "patients/v1/updates/scan",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            params={"since": serialize_datetime(since)},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Patient], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
