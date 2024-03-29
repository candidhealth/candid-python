# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....financials.types.allocation_create import AllocationCreate
from .....payers.resources.v_3.types.payer_identifier import PayerIdentifier

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InsurancePaymentCreate(pydantic.BaseModel):
    payer_identifier: PayerIdentifier
    amount_cents: int
    payment_timestamp: typing.Optional[dt.datetime] = None
    payment_note: typing.Optional[str] = None
    allocations: typing.List[AllocationCreate]

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
