# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .new_rate import NewRate as resources_fee_schedules_resources_v_3_types_new_rate_NewRate
from .new_rate_version import NewRateVersion

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def new_rate(self, value: resources_fee_schedules_resources_v_3_types_new_rate_NewRate) -> RateUpload:
        return RateUpload(__root__=_RateUpload.NewRate(**value.dict(exclude_unset=True), type="new_rate"))

    def new_version(self, value: NewRateVersion) -> RateUpload:
        return RateUpload(__root__=_RateUpload.NewVersion(**value.dict(exclude_unset=True), type="new_version"))


class RateUpload(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_RateUpload.NewRate, _RateUpload.NewVersion]:
        return self.__root__

    def visit(
        self,
        new_rate: typing.Callable[[resources_fee_schedules_resources_v_3_types_new_rate_NewRate], T_Result],
        new_version: typing.Callable[[NewRateVersion], T_Result],
    ) -> T_Result:
        if self.__root__.type == "new_rate":
            return new_rate(
                resources_fee_schedules_resources_v_3_types_new_rate_NewRate(
                    **self.__root__.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if self.__root__.type == "new_version":
            return new_version(NewRateVersion(**self.__root__.dict(exclude_unset=True, exclude={"type"})))

    __root__: typing_extensions.Annotated[
        typing.Union[_RateUpload.NewRate, _RateUpload.NewVersion], pydantic.Field(discriminator="type")
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


class _RateUpload:
    class NewRate(resources_fee_schedules_resources_v_3_types_new_rate_NewRate):
        type: typing.Literal["new_rate"] = "new_rate"

        class Config:
            frozen = True
            smart_union = True
            allow_population_by_field_name = True
            populate_by_name = True

    class NewVersion(NewRateVersion):
        type: typing.Literal["new_version"] = "new_version"

        class Config:
            frozen = True
            smart_union = True
            allow_population_by_field_name = True
            populate_by_name = True


RateUpload.update_forward_refs()
