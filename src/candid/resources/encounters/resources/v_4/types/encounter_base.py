# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from .....commons.types.date import Date
from .....commons.types.encounter_external_id import EncounterExternalId
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from .intervention import Intervention
from .medication import Medication
from .prior_authorization_number import PriorAuthorizationNumber
from .synchronicity_type import SynchronicityType
from .vitals import Vitals


class EncounterBase(pydantic.BaseModel):
    external_id: typing.Optional[EncounterExternalId] = pydantic.Field(
        description=(
            "A client-specified unique ID to associate with this encounter;\n"
            "for example, your internal encounter ID or a Dr. Chrono encounter ID.\n"
            "This field should not contain PHI.\n"
        )
    )
    date_of_service: Date = pydantic.Field(
        description=(
            "Date formatted as YYYY-MM-DD; eg: 2019-08-24.\n"
            "This date must be the local date in the timezone where the service occurred.\n"
            "Box 24a on the CMS-1500 claim form.\n"
            "If service occurred over a range of dates, this should be the start date.\n"
        )
    )
    end_date_of_service: typing.Optional[Date] = pydantic.Field(
        description=(
            "Date formatted as YYYY-MM-DD; eg: 2019-08-25.\n"
            "This date must be the local date in the timezone where the service occurred.\n"
            "If omitted, the Encounter is assumed to be for a single day.\n"
            "Must not be temporally before the date_of_service field.\n"
        )
    )
    prior_authorization_number: typing.Optional[PriorAuthorizationNumber] = pydantic.Field(
        description=("Box 23 on the CMS-1500 claim form.\n")
    )
    patient_authorized_release: bool = pydantic.Field(
        description=(
            "Whether this patient has authorized the release of medical information\n"
            "for billing purpose.\n"
            "Box 12 on the CMS-1500 claim form.\n"
        )
    )
    benefits_assigned_to_provider: bool = pydantic.Field(
        description=(
            "Whether this patient has authorized insurance payments to be made to you,\n"
            "not them. If false, patient may receive reimbursement.\n"
            "Box 13 on the CMS-1500 claim form.\n"
        )
    )
    provider_accepts_assignment: bool = pydantic.Field(
        description=(
            "Whether you have accepted the patient's authorization for insurance payments\n"
            "to be made to you, not them.\n"
            "Box 27 on the CMS-1500 claim form.\n"
        )
    )
    appointment_type: typing.Optional[str] = pydantic.Field(
        description=('Human-readable description of the appointment type (ex: "Acupuncture - Headaches")\n')
    )
    do_not_bill: typing.Optional[bool] = pydantic.Field(
        description=(
            "Should be set to true if Candid should not create or submit a claim but you'd\n"
            "like us to track this encounter anyway (ex: patient is paying cash)\n"
        )
    )
    existing_medications: typing.Optional[typing.List[Medication]]
    vitals: typing.Optional[Vitals]
    interventions: typing.Optional[typing.List[Intervention]]
    pay_to_address: typing.Optional[StreetAddressLongZip]
    synchronicity: typing.Optional[SynchronicityType] = pydantic.Field(
        description=(
            "Whether or not this was a synchronous or asynchronous encounter.\n"
            "Asynchronous encounters occur when providers and patients communicate online using\n"
            "forms, instant messaging, or other pre-recorded digital mediums.\n"
            "Synchronous encounters occur in live, real-time settings where the patient interacts\n"
            "directly with the provider, such as over video or a phone call.\n"
        )
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
