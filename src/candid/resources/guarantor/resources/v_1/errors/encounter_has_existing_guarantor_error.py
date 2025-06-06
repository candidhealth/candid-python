# This file was auto-generated by Fern from our API Definition.

import typing

from ......core.api_error import ApiError
from ..types.encounter_has_existing_guarantor_error_type import EncounterHasExistingGuarantorErrorType


class EncounterHasExistingGuarantorError(ApiError):
    def __init__(
        self, body: EncounterHasExistingGuarantorErrorType, headers: typing.Optional[typing.Dict[str, str]] = None
    ):
        super().__init__(status_code=409, headers=headers, body=body)
