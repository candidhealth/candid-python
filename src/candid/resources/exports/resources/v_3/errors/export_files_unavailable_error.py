# This file was auto-generated by Fern from our API Definition.

from ......core.api_error import ApiError
from .....commons.types.error_message import ErrorMessage


class ExportFilesUnavailableError(ApiError):
    def __init__(self, body: ErrorMessage):
        super().__init__(status_code=503, body=body)
