# This file was auto-generated by Fern from our API Definition.

from ......core.api_error import ApiError
from ..types.expected_network_status_check_error_message import ExpectedNetworkStatusCheckErrorMessage


class ExpectedNetworkStatusCheckError(ApiError):
    def __init__(self, body: ExpectedNetworkStatusCheckErrorMessage):
        super().__init__(status_code=422, body=body)
