# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .....commons.types.date import Date

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DateUpdate_Set(pydantic.BaseModel):
    type: typing_extensions.Literal["set"]
    value: Date

    class Config:
        frozen = True
        smart_union = True


class DateUpdate_Remove(pydantic.BaseModel):
    type: typing_extensions.Literal["remove"]

    class Config:
        frozen = True
        smart_union = True


DateUpdate = typing.Union[DateUpdate_Set, DateUpdate_Remove]
