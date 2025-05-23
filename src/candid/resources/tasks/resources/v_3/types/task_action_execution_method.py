# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskActionExecutionMethod_CloseTask(UniversalBaseModel):
    type: typing.Literal["close_task"] = "close_task"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TaskActionExecutionMethod = TaskActionExecutionMethod_CloseTask
