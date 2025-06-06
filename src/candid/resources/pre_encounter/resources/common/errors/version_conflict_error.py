# This file was auto-generated by Fern from our API Definition.

import typing

from ......core.api_error import ApiError
from ..types.version_conflict_error_body import VersionConflictErrorBody


class VersionConflictError(ApiError):
    def __init__(self, body: VersionConflictErrorBody, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=409, headers=headers, body=body)
