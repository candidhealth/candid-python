# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from .....core.api_error import ApiError
from .....core.remove_none_from_headers import remove_none_from_headers
from .....environment import CandidApiEnvironment
from ...types.task_id import TaskId
from .types.task_actions import TaskActions


class V3Client:
    def __init__(
        self, *, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token

    def get_actions(self, task_id: TaskId) -> TaskActions:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/tasks/v3/{task_id}/actions"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TaskActions, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV3Client:
    def __init__(
        self, *, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token

    async def get_actions(self, task_id: TaskId) -> TaskActions:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"api/tasks/v3/{task_id}/actions"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TaskActions, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
