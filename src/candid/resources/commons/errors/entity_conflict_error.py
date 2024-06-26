# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.entity_conflict_error_message import EntityConflictErrorMessage


class EntityConflictError(ApiError):
    def __init__(self, body: EntityConflictErrorMessage):
        super().__init__(status_code=409, body=body)
