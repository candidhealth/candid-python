# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ......core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .patient_write_off_reason import PatientWriteOffReason
from .....commons.types.service_line_id import ServiceLineId
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .....payers.resources.v_3.types.payer_identifier import PayerIdentifier
from .insurance_write_off_target import InsuranceWriteOffTarget
from .insurance_write_off_reason import InsuranceWriteOffReason


class WriteOffCreate_Patient(UniversalBaseModel):
    type: typing.Literal["patient"] = "patient"
    write_off_timestamp: dt.datetime
    write_off_note: typing.Optional[str] = None
    write_off_reason: PatientWriteOffReason
    service_line_id: ServiceLineId
    amount_cents: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WriteOffCreate_Insurance(UniversalBaseModel):
    type: typing.Literal["insurance"] = "insurance"
    payer_identifier: PayerIdentifier
    write_off_target: InsuranceWriteOffTarget
    write_off_timestamp: dt.datetime
    write_off_note: typing.Optional[str] = None
    write_off_reason: InsuranceWriteOffReason
    amount_cents: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


WriteOffCreate = typing.Union[WriteOffCreate_Patient, WriteOffCreate_Insurance]
