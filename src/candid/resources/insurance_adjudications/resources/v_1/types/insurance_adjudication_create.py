# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.claim_id import ClaimId
from .....payers.resources.v_3.types.payer_identifier import PayerIdentifier
from .....remits.resources.v_1.types.payee import Payee
from .claim_adjudication_create import ClaimAdjudicationCreate

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InsuranceAdjudicationCreate(pydantic.BaseModel):
    payer_identifier: PayerIdentifier
    payee: Payee
    post_date: typing.Optional[dt.date] = None
    check_number: typing.Optional[str] = None
    check_date: dt.date
    note: typing.Optional[str] = None
    claims: typing.Dict[ClaimId, typing.List[ClaimAdjudicationCreate]]

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
