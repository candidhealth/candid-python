# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.encounter_id import EncounterId
from .....commons.types.task_id import TaskId
from ...commons.types.task_category import TaskCategory
from ...commons.types.task_status import TaskStatus
from ...commons.types.task_type import TaskType
from .task_assignment import TaskAssignment
from .task_note import TaskNote


class Task(pydantic.BaseModel):
    task_id: TaskId
    encounter_id: EncounterId
    task_type: TaskType
    description: str
    blocks_claim_submission: bool
    external_id: str
    patient_name: str
    patient_external_id: str
    payer_name: typing.Optional[str] = None
    payer_id: typing.Optional[str] = None
    status: TaskStatus
    notes: typing.List[TaskNote]
    created_at: dt.datetime
    updated_at: dt.datetime = pydantic.Field()
    """
    The time of most recent update to the task only
    """

    agg_updated_at: dt.datetime = pydantic.Field()
    """
    The time of most recent update to the task or any of its notes
    """

    date_of_service: dt.date
    assignments: typing.List[TaskAssignment]
    category: typing.Optional[TaskCategory] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
