# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from .....financials.types.allocation import Allocation
from .....financials.types.refund_reason import RefundReason
from .....payers.resources.v_3.types.payer import Payer
from .insurance_refund_id import InsuranceRefundId


class InsuranceRefund(pydantic.BaseModel):
    insurance_refund_id: InsuranceRefundId
    payer: Payer
    amount_cents: int
    refund_timestamp: typing.Optional[dt.datetime]
    refund_note: typing.Optional[str]
    allocations: typing.List[Allocation]
    refund_reason: typing.Optional[RefundReason]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
