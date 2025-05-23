# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..... import core
from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.http_response import AsyncHttpResponse, HttpResponse
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import parse_obj_as
from .....core.request_options import RequestOptions
from ....commons.types.encounter_id import EncounterId
from .types.attachment_id import AttachmentId
from .types.encounter_attachment import EncounterAttachment
from .types.encounter_attachment_type import EncounterAttachmentType

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, encounter_id: EncounterId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[EncounterAttachment]]:
        """
        Parameters
        ----------
        encounter_id : EncounterId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[EncounterAttachment]]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/encounter-attachments/v1/{jsonable_encoder(encounter_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                typing.List[EncounterAttachment],
                parse_obj_as(
                    type_=typing.List[EncounterAttachment],  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        encounter_id: EncounterId,
        *,
        attachment_file: core.File,
        attachment_type: EncounterAttachmentType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AttachmentId]:
        """
        Uploads a file to the encounter. The file will be stored in the
        encounter's attachments.

        Parameters
        ----------
        encounter_id : EncounterId

        attachment_file : core.File
            See core.File for more documentation

        attachment_type : EncounterAttachmentType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AttachmentId]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/encounter-attachments/v1/{jsonable_encoder(encounter_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="PUT",
            data={
                "attachment_type": attachment_type,
            },
            files={
                "attachment_file": attachment_file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                AttachmentId,
                parse_obj_as(
                    type_=AttachmentId,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self,
        encounter_id: EncounterId,
        *,
        attachment_id: AttachmentId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        encounter_id : EncounterId

        attachment_id : AttachmentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/encounter-attachments/v1/{jsonable_encoder(encounter_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="DELETE",
            json={
                "attachment_id": attachment_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return HttpResponse(response=_response, data=None)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, encounter_id: EncounterId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[EncounterAttachment]]:
        """
        Parameters
        ----------
        encounter_id : EncounterId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[EncounterAttachment]]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/encounter-attachments/v1/{jsonable_encoder(encounter_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                typing.List[EncounterAttachment],
                parse_obj_as(
                    type_=typing.List[EncounterAttachment],  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        encounter_id: EncounterId,
        *,
        attachment_file: core.File,
        attachment_type: EncounterAttachmentType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AttachmentId]:
        """
        Uploads a file to the encounter. The file will be stored in the
        encounter's attachments.

        Parameters
        ----------
        encounter_id : EncounterId

        attachment_file : core.File
            See core.File for more documentation

        attachment_type : EncounterAttachmentType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AttachmentId]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/encounter-attachments/v1/{jsonable_encoder(encounter_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="PUT",
            data={
                "attachment_type": attachment_type,
            },
            files={
                "attachment_file": attachment_file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                AttachmentId,
                parse_obj_as(
                    type_=AttachmentId,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self,
        encounter_id: EncounterId,
        *,
        attachment_id: AttachmentId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        encounter_id : EncounterId

        attachment_id : AttachmentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/encounter-attachments/v1/{jsonable_encoder(encounter_id)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="DELETE",
            json={
                "attachment_id": attachment_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return AsyncHttpResponse(response=_response, data=None)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
