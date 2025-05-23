# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.service_line_id import ServiceLineId
from .....non_insurance_payers.resources.v_1.types.non_insurance_payer import NonInsurancePayer
from .insurance_write_off_reason import InsuranceWriteOffReason
from .write_off_id import WriteOffId


class NonInsurancePayerWriteOff(UniversalBaseModel):
    write_off_id: WriteOffId
    non_insurance_payer: NonInsurancePayer
    service_line_id: ServiceLineId
    write_off_timestamp: dt.datetime
    write_off_note: typing.Optional[str] = None
    write_off_reason: InsuranceWriteOffReason
    reverts_write_off_id: typing.Optional[WriteOffId] = None
    reverted_by_write_off_id: typing.Optional[WriteOffId] = None
    amount_cents: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
