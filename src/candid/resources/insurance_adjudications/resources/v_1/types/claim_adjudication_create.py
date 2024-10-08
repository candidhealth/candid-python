# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.service_line_id import ServiceLineId
from .....era_commons.types.claim_status_code_create import ClaimStatusCodeCreate
from .....x_12.resources.v_1.types.claim_adjustment_reason_code import ClaimAdjustmentReasonCode
from .service_line_adjudication_create import ServiceLineAdjudicationCreate


class ClaimAdjudicationCreate(pydantic.BaseModel):
    claim_status_code: ClaimStatusCodeCreate
    insurance_paid_amount_cents: typing.Optional[int] = None
    charge_amount_cents: typing.Optional[int] = None
    service_lines: typing.Dict[ServiceLineId, typing.List[ServiceLineAdjudicationCreate]]
    payer_claim_number: typing.Optional[str] = None
    carcs: typing.List[ClaimAdjustmentReasonCode]

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
