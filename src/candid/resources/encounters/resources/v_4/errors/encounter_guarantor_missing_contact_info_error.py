# This file was auto-generated by Fern from our API Definition.

from ......core.api_error import ApiError
from ..types.encounter_guarantor_missing_contact_info_error_type import EncounterGuarantorMissingContactInfoErrorType


class EncounterGuarantorMissingContactInfoError(ApiError):
    def __init__(self, body: EncounterGuarantorMissingContactInfoErrorType):
        super().__init__(status_code=422, body=body)
