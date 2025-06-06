# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.claim_id import ClaimId
from .....payers.resources.v_3.types.payer_uuid import PayerUuid
from .claim_adjudication import ClaimAdjudication
from .insurance_adjudication_id import InsuranceAdjudicationId


class InsuranceAdjudication(UniversalBaseModel):
    insurance_adjudication_id: InsuranceAdjudicationId
    payer_uuid: PayerUuid
    post_date: typing.Optional[dt.date] = None
    check_number: typing.Optional[str] = None
    check_date: dt.date
    note: typing.Optional[str] = None
    claims: typing.Dict[ClaimId, typing.List[ClaimAdjudication]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
