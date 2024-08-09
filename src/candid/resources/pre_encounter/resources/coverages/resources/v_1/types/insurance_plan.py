# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime
from ........core.pydantic_utilities import deep_union_pydantic_dicts
from .....common.types.payer_id import PayerId
from .....common.types.period import Period
from .insurance_type_code import InsuranceTypeCode
from .network_type import NetworkType


class InsurancePlan(pydantic.BaseModel):
    member_id: str
    payer_id: PayerId
    payer_name: str
    group_number: typing.Optional[str] = None
    name: typing.Optional[str] = None
    plan_type: typing.Optional[NetworkType] = None
    type: typing.Optional[InsuranceTypeCode] = None
    period: typing.Optional[Period] = None
    insurance_card_image_locator: typing.Optional[str] = None

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
