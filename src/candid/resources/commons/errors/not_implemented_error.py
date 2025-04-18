# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.not_implemented_error_message import NotImplementedErrorMessage


class NotImplementedError(ApiError):
    def __init__(self, body: NotImplementedErrorMessage):
        super().__init__(status_code=501, body=body)
