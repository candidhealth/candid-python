# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ....commons.errors.entity_not_found_error import EntityNotFoundError
from ....commons.errors.http_request_validation_error import HttpRequestValidationError
from ....commons.types.entity_not_found_error_message import EntityNotFoundErrorMessage
from ....commons.types.page_token import PageToken
from ....commons.types.request_validation_error import RequestValidationError
from ..v_2.types.organization_provider_id import OrganizationProviderId
from ..v_2.types.organization_provider_sort_options import OrganizationProviderSortOptions
from .types.organization_provider_create_v_2 import OrganizationProviderCreateV2
from .types.organization_provider_page_v_2 import OrganizationProviderPageV2
from .types.organization_provider_update_v_2 import OrganizationProviderUpdateV2
from .types.organization_provider_v_2 import OrganizationProviderV2

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, organization_provider_id: OrganizationProviderId) -> OrganizationProviderV2:
        """
        Parameters:
            - organization_provider_id: OrganizationProviderId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/organization-providers/v3/{organization_provider_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationProviderV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        npi: typing.Optional[str] = None,
        is_rendering: typing.Optional[bool] = None,
        is_billing: typing.Optional[bool] = None,
        page_token: typing.Optional[PageToken] = None,
        sort: typing.Optional[OrganizationProviderSortOptions] = None,
    ) -> OrganizationProviderPageV2:
        """
        Parameters:
            - limit: typing.Optional[int]. Limit the number of results returned. Defaults to 100.

            - search_term: typing.Optional[str]. Filter to a name or a part of a name.

            - npi: typing.Optional[str]. Filter to a specific NPI.

            - is_rendering: typing.Optional[bool]. Filter to only rendering providers.

            - is_billing: typing.Optional[bool]. Filter to only billing providers.

            - page_token: typing.Optional[PageToken]. The page token to continue paging through a previous request.

            - sort: typing.Optional[OrganizationProviderSortOptions]. Defaults to PROVIDER_NAME_ASC.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/organization-providers/v3"),
            params=remove_none_from_dict(
                {
                    "limit": limit,
                    "search_term": search_term,
                    "npi": npi,
                    "is_rendering": is_rendering,
                    "is_billing": is_billing,
                    "page_token": page_token,
                    "sort": sort,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationProviderPageV2, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: OrganizationProviderCreateV2) -> OrganizationProviderV2:
        """
        Parameters:
            - request: OrganizationProviderCreateV2.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/organization-providers/v3"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationProviderV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self, organization_provider_id: OrganizationProviderId, *, request: OrganizationProviderUpdateV2
    ) -> OrganizationProviderV2:
        """
        Parameters:
            - organization_provider_id: OrganizationProviderId.

            - request: OrganizationProviderUpdateV2.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/organization-providers/v3/{organization_provider_id}"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationProviderV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, organization_provider_id: OrganizationProviderId) -> OrganizationProviderV2:
        """
        Parameters:
            - organization_provider_id: OrganizationProviderId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/organization-providers/v3/{organization_provider_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationProviderV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        npi: typing.Optional[str] = None,
        is_rendering: typing.Optional[bool] = None,
        is_billing: typing.Optional[bool] = None,
        page_token: typing.Optional[PageToken] = None,
        sort: typing.Optional[OrganizationProviderSortOptions] = None,
    ) -> OrganizationProviderPageV2:
        """
        Parameters:
            - limit: typing.Optional[int]. Limit the number of results returned. Defaults to 100.

            - search_term: typing.Optional[str]. Filter to a name or a part of a name.

            - npi: typing.Optional[str]. Filter to a specific NPI.

            - is_rendering: typing.Optional[bool]. Filter to only rendering providers.

            - is_billing: typing.Optional[bool]. Filter to only billing providers.

            - page_token: typing.Optional[PageToken]. The page token to continue paging through a previous request.

            - sort: typing.Optional[OrganizationProviderSortOptions]. Defaults to PROVIDER_NAME_ASC.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/organization-providers/v3"),
            params=remove_none_from_dict(
                {
                    "limit": limit,
                    "search_term": search_term,
                    "npi": npi,
                    "is_rendering": is_rendering,
                    "is_billing": is_billing,
                    "page_token": page_token,
                    "sort": sort,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationProviderPageV2, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: OrganizationProviderCreateV2) -> OrganizationProviderV2:
        """
        Parameters:
            - request: OrganizationProviderCreateV2.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/organization-providers/v3"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationProviderV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, organization_provider_id: OrganizationProviderId, *, request: OrganizationProviderUpdateV2
    ) -> OrganizationProviderV2:
        """
        Parameters:
            - organization_provider_id: OrganizationProviderId.

            - request: OrganizationProviderUpdateV2.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/organization-providers/v3/{organization_provider_id}"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationProviderV2, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
