# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts
from .refund_reason import RefundReason

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def set_(self, value: RefundReason) -> RefundReasonUpdate:
        return RefundReasonUpdate(__root__=_RefundReasonUpdate.Set(type="set", value=value))

    def remove(self) -> RefundReasonUpdate:
        return RefundReasonUpdate(__root__=_RefundReasonUpdate.Remove(type="remove"))


class RefundReasonUpdate(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_RefundReasonUpdate.Set, _RefundReasonUpdate.Remove]:
        return self.__root__

    def visit(self, set_: typing.Callable[[RefundReason], T_Result], remove: typing.Callable[[], T_Result]) -> T_Result:
        if self.__root__.type == "set":
            return set_(self.__root__.value)
        if self.__root__.type == "remove":
            return remove()

    __root__: typing_extensions.Annotated[
        typing.Union[_RefundReasonUpdate.Set, _RefundReasonUpdate.Remove], pydantic.Field(discriminator="type")
    ]

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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _RefundReasonUpdate:
    class Set(pydantic.BaseModel):
        type: typing.Literal["set"] = "set"
        value: RefundReason

        class Config:
            frozen = True
            smart_union = True

    class Remove(pydantic.BaseModel):
        type: typing.Literal["remove"] = "remove"

        class Config:
            frozen = True
            smart_union = True


RefundReasonUpdate.update_forward_refs()
