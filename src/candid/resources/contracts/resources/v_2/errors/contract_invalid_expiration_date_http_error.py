# This file was auto-generated by Fern from our API Definition.

from ......core.api_error import ApiError
from ..types.contract_invalid_expiration_date_error import ContractInvalidExpirationDateError


class ContractInvalidExpirationDateHttpError(ApiError):
    def __init__(self, body: ContractInvalidExpirationDateError):
        super().__init__(status_code=422, body=body)
