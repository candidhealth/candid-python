# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.regions import Regions

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def set_(self, value: Regions) -> RegionsUpdate:
        return RegionsUpdate(__root__=_RegionsUpdate.Set(type="set", value=value))

    def remove(self) -> RegionsUpdate:
        return RegionsUpdate(__root__=_RegionsUpdate.Remove(type="remove"))


class RegionsUpdate(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_RegionsUpdate.Set, _RegionsUpdate.Remove]:
        return self.__root__

    def visit(self, set_: typing.Callable[[Regions], T_Result], remove: typing.Callable[[], T_Result]) -> T_Result:
        if self.__root__.type == "set":
            return set_(self.__root__.value)
        if self.__root__.type == "remove":
            return remove()

    __root__: typing_extensions.Annotated[
        typing.Union[_RegionsUpdate.Set, _RegionsUpdate.Remove], pydantic.Field(discriminator="type")
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


class _RegionsUpdate:
    class Set(pydantic.BaseModel):
        type: typing.Literal["set"] = "set"
        value: Regions

        class Config:
            frozen = True
            smart_union = True

    class Remove(pydantic.BaseModel):
        type: typing.Literal["remove"] = "remove"

        class Config:
            frozen = True
            smart_union = True


RegionsUpdate.update_forward_refs()
