# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.insurance_type_code import InsuranceTypeCode
from .....commons.types.source_of_payment_code import SourceOfPaymentCode


class InsuranceCardBase(pydantic.BaseModel):
    group_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Box 11 on the CMS-1500 claim form.
    """

    plan_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Box 11c on the CMS-1500 claim form.
    """

    plan_type: typing.Optional[SourceOfPaymentCode] = None
    insurance_type: typing.Optional[InsuranceTypeCode] = None

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
