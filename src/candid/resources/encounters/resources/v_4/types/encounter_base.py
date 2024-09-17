# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.delay_reason_code import DelayReasonCode
from .....commons.types.encounter_external_id import EncounterExternalId
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from .billable_status_type import BillableStatusType
from .intervention import Intervention
from .medication import Medication
from .prior_authorization_number import PriorAuthorizationNumber
from .responsible_party_type import ResponsiblePartyType
from .service_authorization_exception_code import ServiceAuthorizationExceptionCode
from .synchronicity_type import SynchronicityType
from .vitals import Vitals


class EncounterBase(pydantic.BaseModel):
    external_id: EncounterExternalId = pydantic.Field()
    """
    A client-specified unique ID to associate with this encounter;
    for example, your internal encounter ID or a Dr. Chrono encounter ID.
    This field should not contain PHI.
    """

    prior_authorization_number: typing.Optional[PriorAuthorizationNumber] = pydantic.Field(default=None)
    """
    Box 23 on the CMS-1500 claim form.
    """

    patient_authorized_release: bool = pydantic.Field()
    """
    Whether this patient has authorized the release of medical information
    for billing purpose.
    Box 12 on the CMS-1500 claim form.
    """

    benefits_assigned_to_provider: bool = pydantic.Field()
    """
    Whether this patient has authorized insurance payments to be made to you,
    not them. If false, patient may receive reimbursement.
    Box 13 on the CMS-1500 claim form.
    """

    provider_accepts_assignment: bool = pydantic.Field()
    """
    Whether you have accepted the patient's authorization for insurance payments
    to be made to you, not them.
    Box 27 on the CMS-1500 claim form.
    """

    appointment_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the appointment type (ex: "Acupuncture - Headaches").
    """

    existing_medications: typing.Optional[typing.List[Medication]] = None
    vitals: typing.Optional[Vitals] = None
    interventions: typing.Optional[typing.List[Intervention]] = None
    pay_to_address: typing.Optional[StreetAddressLongZip] = pydantic.Field(default=None)
    """
    Specifies the address to which payments for the claim should be sent.
    """

    synchronicity: typing.Optional[SynchronicityType] = pydantic.Field(default=None)
    """
    Whether or not this was a synchronous or asynchronous encounter.
    Asynchronous encounters occur when providers and patients communicate online using
    forms, instant messaging, or other pre-recorded digital mediums.
    Synchronous encounters occur in live, real-time settings where the patient interacts
    directly with the provider, such as over video or a phone call.
    """

    billable_status: BillableStatusType = pydantic.Field()
    """
    Defines if the Encounter is to be billed by Candid to the responsible_party.
    Examples for when this should be set to NOT_BILLABLE include
    if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.
    """

    responsible_party: ResponsiblePartyType = pydantic.Field()
    """
    Defines the party to be billed with the initial balance owed on the claim.
    """

    additional_information: typing.Optional[str] = pydantic.Field(default=None)
    """
    Defines additional information on the claim needed by the payer.
    Box 19 on the CMS-1500 claim form.
    """

    service_authorization_exception_code: typing.Optional[ServiceAuthorizationExceptionCode] = pydantic.Field(
        default=None
    )
    """
    837p Loop2300 REF\*4N
    Required when mandated by government law or regulation to obtain authorization for specific service(s) but, for the
    reasons listed in one of the enum values of ServiceAuthorizationExceptionCode, the service was performed without
    obtaining the authorization.
    """

    admission_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    837p Loop2300 DTP\*435, CMS-1500 Box 18
    Required on all ambulance claims when the patient was known to be admitted to the hospital.
    OR
    Required on all claims involving inpatient medical visits.
    """

    discharge_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    837p Loop2300 DTP\*096, CMS-1500 Box 18
    Required for inpatient claims when the patient was discharged from the facility and the discharge date is known.
    """

    onset_of_current_illness_or_symptom_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    837p Loop2300 DTP\*431, CMS-1500 Box 14
    Required for the initial medical service or visit performed in response to a medical emergency when the date is available and is different than the date of service.
    OR
    This date is the onset of acute symptoms for the current illness or condition.
    """

    last_menstrual_period_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    837p Loop2300 DTP\*484, CMS-1500 Box 14
    Required when, in the judgment of the provider, the services on this claim are related to the patient's pregnancy.
    """

    delay_reason_code: typing.Optional[DelayReasonCode] = pydantic.Field(default=None)
    """
    837i Loop2300, CLM-1300 Box 20
    Code indicating the reason why a request was delayed
    """

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
