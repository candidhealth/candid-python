# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .......core.api_error import ApiError
from .......core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .......core.http_response import AsyncHttpResponse, HttpResponse
from .......core.jsonable_encoder import jsonable_encoder
from .......core.pydantic_utilities import parse_obj_as
from .......core.request_options import RequestOptions
from ....common.types.note_id import NoteId
from .types.mutable_note import MutableNote
from .types.note import Note

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, id: NoteId, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Note]:
        """
        Gets a note by NoteId.

        Parameters
        ----------
        id : NoteId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Note]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"notes/v1/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                Note,
                parse_obj_as(
                    type_=Note,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self, *, request: MutableNote, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Note]:
        """
        Adds a new note.

        Parameters
        ----------
        request : MutableNote

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Note]
        """
        _response = self._client_wrapper.httpx_client.request(
            "notes/v1",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                Note,
                parse_obj_as(
                    type_=Note,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self, id: NoteId, version: str, *, request: MutableNote, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Note]:
        """
        Updates a note. The path must contain the most recent version to prevent races.

        Parameters
        ----------
        id : NoteId

        version : str

        request : MutableNote

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Note]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"notes/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                Note,
                parse_obj_as(
                    type_=Note,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deactivate(
        self, id: NoteId, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Sets a note as deactivated.  The path must contain the most recent version to prevent races.

        Parameters
        ----------
        id : NoteId

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"notes/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="DELETE",
            request_options=request_options,
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
        self, id: NoteId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Note]:
        """
        Gets a note by NoteId.

        Parameters
        ----------
        id : NoteId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Note]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"notes/v1/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                Note,
                parse_obj_as(
                    type_=Note,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self, *, request: MutableNote, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Note]:
        """
        Adds a new note.

        Parameters
        ----------
        request : MutableNote

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Note]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notes/v1",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                Note,
                parse_obj_as(
                    type_=Note,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self, id: NoteId, version: str, *, request: MutableNote, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Note]:
        """
        Updates a note. The path must contain the most recent version to prevent races.

        Parameters
        ----------
        id : NoteId

        version : str

        request : MutableNote

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Note]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"notes/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                Note,
                parse_obj_as(
                    type_=Note,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deactivate(
        self, id: NoteId, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Sets a note as deactivated.  The path must contain the most recent version to prevent races.

        Parameters
        ----------
        id : NoteId

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"notes/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return AsyncHttpResponse(response=_response, data=None)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
