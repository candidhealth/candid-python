# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.query_encoder import encode_query
from .....core.remove_none_from_dict import remove_none_from_dict
from .....core.request_options import RequestOptions
from ....commons.types.page_token import PageToken
from .types.payer import Payer
from .types.payer_page import PayerPage
from .types.payer_uuid import PayerUuid


class V3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, payer_uuid: PayerUuid, *, request_options: typing.Optional[RequestOptions] = None) -> Payer:
        """
        Parameters
        ----------
        payer_uuid : PayerUuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payer

        Examples
        --------
        import uuid

        from candid.client import CandidApi

        client = CandidApi(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.payers.v_3.get(
            payer_uuid=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/payers/v3/{jsonable_encoder(payer_uuid)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Payer, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayerPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities per page, defaults to 100.

        search_term : typing.Optional[str]

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPage

        Examples
        --------
        from candid.client import CandidApi

        client = CandidApi(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.payers.v_3.get_all(
            limit=100,
            search_term="john",
            page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/payers/v3"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "limit": limit,
                            "search_term": search_term,
                            "page_token": page_token,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PayerPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, payer_uuid: PayerUuid, *, request_options: typing.Optional[RequestOptions] = None) -> Payer:
        """
        Parameters
        ----------
        payer_uuid : PayerUuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payer

        Examples
        --------
        import uuid

        from candid.client import AsyncCandidApi

        client = AsyncCandidApi(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.payers.v_3.get(
            payer_uuid=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/payers/v3/{jsonable_encoder(payer_uuid)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Payer, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayerPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities per page, defaults to 100.

        search_term : typing.Optional[str]

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPage

        Examples
        --------
        from candid.client import AsyncCandidApi

        client = AsyncCandidApi(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.payers.v_3.get_all(
            limit=100,
            search_term="john",
            page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/payers/v3"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "limit": limit,
                            "search_term": search_term,
                            "page_token": page_token,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PayerPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
