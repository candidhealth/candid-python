# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from .....commons.types.encounter_external_id import EncounterExternalId
from .....commons.types.organization_id import OrganizationId
from .....commons.types.patient_external_id import PatientExternalId
from .....commons.types.service_line_id import ServiceLineId
from .patient_payment_id import PatientPaymentId
from .patient_payment_source import PatientPaymentSource
from .patient_payment_status import PatientPaymentStatus


class PatientPayment(pydantic.BaseModel):
    patient_payment_id: PatientPaymentId
    organization_id: OrganizationId
    source_internal_id: str
    source: PatientPaymentSource
    amount_cents: int
    payment_timestamp: typing.Optional[dt.datetime]
    status: typing.Optional[PatientPaymentStatus]
    payment_name: typing.Optional[str]
    payment_note: typing.Optional[str]
    patient_external_id: typing.Optional[PatientExternalId]
    encounter_external_id: typing.Optional[EncounterExternalId]
    service_line_id: typing.Optional[ServiceLineId]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
