# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.rate_id import RateId
from .....commons.types.user_id import UserId
from .dimensions import Dimensions
from .rate_entry import RateEntry


class Rate(pydantic.BaseModel):
    """
    A comprehensive rate including the current rate value and all values for historic time ranges. The time ranges specified by each RateEntry are disjoint. A rate must always have at least one entry.
    """

    rate_id: RateId
    dimensions: Dimensions = pydantic.Field()
    """
    The dimension values that distinguish this rate from others.
    """

    version: int = pydantic.Field()
    """
    The version of this rate in the system.
    """

    updated_at: dt.date
    updated_by: UserId
    entries: typing.List[RateEntry]

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
