# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts


class PayerThreshold(pydantic.BaseModel):
    """
    Rate thresholds that determine fee schedule rate matching behavior. When a service line is adjudicated by a payer Candid determines if the payer's allowed amount "matches" the rate value. If the allowed amount doesn't equal the rate value, Candid moves the claim to a PAID_INCORRECTLY state. These optional thresholds allow a user to set wiggle room to avoid claims moving to PAID_INCORRECTLY and instead have them move directly to FINALIZED_PAID when the payer's allowed amount is greater than [rate_cents - lower_threshold_cents] and less than [rate_cents + upper_threshold_cents].\n Additionally, a client can set disable_paid_incorrectly to avoid the PAID_INCORRECTLY claim status entirely.
    """

    upper_threshold_cents: typing.Optional[int] = None
    lower_threshold_cents: typing.Optional[int] = None
    disable_paid_incorrectly: bool

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
