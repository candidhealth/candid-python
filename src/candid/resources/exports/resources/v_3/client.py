# This file was auto-generated by Fern from our API Definition.

from .....core.client_wrapper import SyncClientWrapper
import datetime as dt
import typing
from .....core.request_options import RequestOptions
from .types.get_exports_response import GetExportsResponse
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from .....core.pydantic_utilities import parse_obj_as
from ....commons.errors.http_request_validations_error import HttpRequestValidationsError
from ....commons.types.request_validation_error import RequestValidationError
from .errors.export_files_unavailable_error import ExportFilesUnavailableError
from ....commons.types.error_message import ErrorMessage
from .errors.missing_daily_incremental_export_file_error import MissingDailyIncrementalExportFileError
from .errors.export_not_yet_available_error import ExportNotYetAvailableError
from .errors.export_date_too_early_error import ExportDateTooEarlyError
from .....core.client_wrapper import AsyncClientWrapper


class V3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_exports(
        self, *, start_date: dt.date, end_date: dt.date, request_options: typing.Optional[RequestOptions] = None
    ) -> GetExportsResponse:
        """
        Retrieve CSV-formatted reports on claim submissions and outcomes. This endpoint returns Export objects that contain an
        authenticated URL to a customer's reports with a 2min TTL. The schema for the CSV export can be found [here](https://app.joincandidhealth.com/files/exports_schema.csv).

        **Schema changes:** Changing column order, removing columns, or changing the name of a column is considered a
        [Breaking Change](../../../api-principles/breaking-changes). Adding new columns to the end of the Exports file is not considered a
        Breaking Change and happens periodically. For this reason, it is important that any downstream automation or processes built on top
        of Candid Health's export files be resilient to the addition of new columns at the end of the file.

        **SLA guarantees:** Files for a given date are guaranteed to be available after 3 business days. For example, Friday's file will be
        available by Wednesday at the latest. If file generation is still in progress upon request before 3 business days have passed, the
        caller will receive a 422 response. If the file has already been generated, it will be served. Historic files should be available
        up to 90 days in the past by default. Please email our [Support team](mailto:support@joincandidhealth.com) with any data requests
        outside of these stated guarantees.

        Parameters
        ----------
        start_date : dt.date
            Beginning date of claim versions returned in the export, ISO 8601 date e.g. 2019-08-24.
            Must be at least 1 calendar day in the past. Cannot be earlier than 2022-10-07.

        end_date : dt.date
            Ending date of claim versions returned in the export, ISO 8601 date; e.g. 2019-08-24.
            Must be within 30 days of start_date.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExportsResponse

        Examples
        --------
        import datetime

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.exports.v_3.get_exports(
            start_date=datetime.date.fromisoformat(
                "2023-10-01",
            ),
            end_date=datetime.date.fromisoformat(
                "2023-10-02",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/exports/v3",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            params={
                "start_date": str(start_date),
                "end_date": str(end_date),
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                GetExportsResponse,
                parse_obj_as(
                    type_=GetExportsResponse,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationsError":
                raise HttpRequestValidationsError(
                    typing.cast(
                        typing.List[RequestValidationError],
                        parse_obj_as(
                            type_=typing.List[RequestValidationError],  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "ExportFilesUnavailableError":
                raise ExportFilesUnavailableError(
                    typing.cast(
                        ErrorMessage,
                        parse_obj_as(
                            type_=ErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "MissingDailyIncrementalExportFileError":
                raise MissingDailyIncrementalExportFileError(
                    typing.cast(
                        ErrorMessage,
                        parse_obj_as(
                            type_=ErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "ExportNotYetAvailableError":
                raise ExportNotYetAvailableError(
                    typing.cast(
                        ErrorMessage,
                        parse_obj_as(
                            type_=ErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "ExportDateTooEarlyError":
                raise ExportDateTooEarlyError(
                    typing.cast(
                        ErrorMessage,
                        parse_obj_as(
                            type_=ErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_exports(
        self, *, start_date: dt.date, end_date: dt.date, request_options: typing.Optional[RequestOptions] = None
    ) -> GetExportsResponse:
        """
        Retrieve CSV-formatted reports on claim submissions and outcomes. This endpoint returns Export objects that contain an
        authenticated URL to a customer's reports with a 2min TTL. The schema for the CSV export can be found [here](https://app.joincandidhealth.com/files/exports_schema.csv).

        **Schema changes:** Changing column order, removing columns, or changing the name of a column is considered a
        [Breaking Change](../../../api-principles/breaking-changes). Adding new columns to the end of the Exports file is not considered a
        Breaking Change and happens periodically. For this reason, it is important that any downstream automation or processes built on top
        of Candid Health's export files be resilient to the addition of new columns at the end of the file.

        **SLA guarantees:** Files for a given date are guaranteed to be available after 3 business days. For example, Friday's file will be
        available by Wednesday at the latest. If file generation is still in progress upon request before 3 business days have passed, the
        caller will receive a 422 response. If the file has already been generated, it will be served. Historic files should be available
        up to 90 days in the past by default. Please email our [Support team](mailto:support@joincandidhealth.com) with any data requests
        outside of these stated guarantees.

        Parameters
        ----------
        start_date : dt.date
            Beginning date of claim versions returned in the export, ISO 8601 date e.g. 2019-08-24.
            Must be at least 1 calendar day in the past. Cannot be earlier than 2022-10-07.

        end_date : dt.date
            Ending date of claim versions returned in the export, ISO 8601 date; e.g. 2019-08-24.
            Must be within 30 days of start_date.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExportsResponse

        Examples
        --------
        import asyncio
        import datetime

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.exports.v_3.get_exports(
                start_date=datetime.date.fromisoformat(
                    "2023-10-01",
                ),
                end_date=datetime.date.fromisoformat(
                    "2023-10-02",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/exports/v3",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            params={
                "start_date": str(start_date),
                "end_date": str(end_date),
            },
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return typing.cast(
                GetExportsResponse,
                parse_obj_as(
                    type_=GetExportsResponse,  # type: ignore
                    object_=_response_json,
                ),
            )
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationsError":
                raise HttpRequestValidationsError(
                    typing.cast(
                        typing.List[RequestValidationError],
                        parse_obj_as(
                            type_=typing.List[RequestValidationError],  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "ExportFilesUnavailableError":
                raise ExportFilesUnavailableError(
                    typing.cast(
                        ErrorMessage,
                        parse_obj_as(
                            type_=ErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "MissingDailyIncrementalExportFileError":
                raise MissingDailyIncrementalExportFileError(
                    typing.cast(
                        ErrorMessage,
                        parse_obj_as(
                            type_=ErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "ExportNotYetAvailableError":
                raise ExportNotYetAvailableError(
                    typing.cast(
                        ErrorMessage,
                        parse_obj_as(
                            type_=ErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
            if _response_json["errorName"] == "ExportDateTooEarlyError":
                raise ExportDateTooEarlyError(
                    typing.cast(
                        ErrorMessage,
                        parse_obj_as(
                            type_=ErrorMessage,  # type: ignore
                            object_=_response_json["content"],
                        ),
                    )
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
