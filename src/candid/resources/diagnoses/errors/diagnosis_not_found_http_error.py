# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.diagnosis_not_found_error import DiagnosisNotFoundError


class DiagnosisNotFoundHttpError(ApiError):
    def __init__(self, body: DiagnosisNotFoundError):
        super().__init__(status_code=404, body=body)