# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.delay_reason_code import DelayReasonCode
from .....commons.types.encounter_external_id import EncounterExternalId
from .....commons.types.facility_type_code import FacilityTypeCode
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from .....custom_schemas.resources.v_1.types.schema_instance import SchemaInstance
from .....encounter_providers.resources.v_2.types.billing_provider_update import BillingProviderUpdate
from .....encounter_providers.resources.v_2.types.initial_referring_provider_update import (
    InitialReferringProviderUpdate,
)
from .....encounter_providers.resources.v_2.types.referring_provider_update import ReferringProviderUpdate
from .....encounter_providers.resources.v_2.types.rendering_provider_update import RenderingProviderUpdate
from .....encounter_providers.resources.v_2.types.supervising_provider_update import SupervisingProviderUpdate
from .....guarantor.resources.v_1.types.guarantor_update import GuarantorUpdate
from .....individual.types.patient_update import PatientUpdate
from .....individual.types.subscriber_create import SubscriberCreate
from .....service_facility.types.encounter_service_facility_update import EncounterServiceFacilityUpdate
from .....tags.types.tag_id import TagId
from .billable_status_type import BillableStatusType
from .clinical_note_category_create import ClinicalNoteCategoryCreate
from .medication import Medication
from .prior_authorization_number import PriorAuthorizationNumber
from .responsible_party_type import ResponsiblePartyType
from .service_authorization_exception_code import ServiceAuthorizationExceptionCode
from .synchronicity_type import SynchronicityType
from .vitals_update import VitalsUpdate


class EncounterOptional(pydantic.BaseModel):
    benefits_assigned_to_provider: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this patient has authorized insurance payments to be made to you, not them. If false, patient may receive reimbursement. Box 13 on the CMS-1500 claim form.
    """

    prior_authorization_number: typing.Optional[PriorAuthorizationNumber] = pydantic.Field(default=None)
    """
    Box 23 on the CMS-1500 claim form.
    """

    external_id: typing.Optional[EncounterExternalId] = pydantic.Field(default=None)
    """
    A client-specified unique ID to associate with this encounter;
    for example, your internal encounter ID or a Dr. Chrono encounter ID.
    This field should not contain PHI.
    """

    date_of_service: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date formatted as YYYY-MM-DD; eg: 2019-08-24.
    This date must be the local date in the timezone where the service occurred.
    Box 24a on the CMS-1500 claim form.
    If service occurred over a range of dates, this should be the start date.
    If service lines have distinct date_of_service values, updating the encounter's date_of_service will fail. If all service line date_of_service values are the same, updating the encounter's date_of_service will update all service line date_of_service values.
    """

    tag_ids: typing.Optional[typing.List[TagId]] = pydantic.Field(default=None)
    """
    Names of tags that should be on the encounter. Note all tags on encounter will be overridden with this list.
    """

    clinical_notes: typing.Optional[typing.List[ClinicalNoteCategoryCreate]] = pydantic.Field(default=None)
    """
    Holds a collection of clinical observations made by healthcare providers during patient encounters.
    """

    pay_to_address: typing.Optional[StreetAddressLongZip] = pydantic.Field(default=None)
    """
    Specifies the address to which payments for the claim should be sent.
    """

    billable_status: typing.Optional[BillableStatusType] = pydantic.Field(default=None)
    """
    Defines if the Encounter is to be billed by Candid to the responsible_party. Examples for when this should be set to NOT_BILLABLE include if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.
    """

    responsible_party: typing.Optional[ResponsiblePartyType] = pydantic.Field(default=None)
    """
    Defines the party to be billed with the initial balance owed on the claim. Use SELF_PAY if you intend to bill self pay/cash pay.
    """

    provider_accepts_assignment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether you have accepted the patient's authorization for insurance payments to be made to you, not them. Box 27 on the CMS-1500 claim form.
    """

    synchronicity: typing.Optional[SynchronicityType] = pydantic.Field(default=None)
    """
    Whether or not this was a synchronous or asynchronous encounter. Asynchronous encounters occur when providers and patients communicate online using forms, instant messaging, or other pre-recorded digital mediums. Synchronous encounters occur in live, real-time settings where the patient interacts directly with the provider, such as over video or a phone call.
    """

    place_of_service_code: typing.Optional[FacilityTypeCode] = pydantic.Field(default=None)
    """
    Box 24B on the CMS-1500 claim form. 837p Loop2300, CLM-05-1. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).
    """

    appointment_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the appointment type (ex: "Acupuncture - Headaches").
    """

    end_date_of_service: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date formatted as YYYY-MM-DD; eg: 2019-08-25.
    This date must be the local date in the timezone where the service occurred.
    If omitted, the Encounter is assumed to be for a single day.
    Must not be temporally before the date_of_service field.
    If service lines have distinct end_date_of_service values, updating the encounter's end_date_of_service will fail. If all service line end_date_of_service values are the same, updating the encounter's end_date_of_service will update all service line date_of_service values.
    """

    subscriber_primary: typing.Optional[SubscriberCreate] = pydantic.Field(default=None)
    """
    Contains details of the primary insurance subscriber.
    """

    subscriber_secondary: typing.Optional[SubscriberCreate] = pydantic.Field(default=None)
    """
    Contains details of the secondary insurance subscriber.
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
    Required when, in the judgment of the provider, the services on this claim are related to the patient's pregnancy.de
    """

    delay_reason_code: typing.Optional[DelayReasonCode] = pydantic.Field(default=None)
    """
    837i Loop2300, CLM-1300 Box 20
    Code indicating the reason why a request was delayed
    """

    patient: typing.Optional[PatientUpdate] = pydantic.Field(default=None)
    """
    Contains the identification information of the individual receiving medical services.
    """

    patient_authorized_release: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this patient has authorized the release of medical information
    for billing purpose.
    Box 12 on the CMS-1500 claim form.
    """

    schema_instances: typing.Optional[typing.List[SchemaInstance]] = pydantic.Field(default=None)
    """
    Key-value pairs that must adhere to a schema created via the Custom Schema API. Multiple schema
    instances cannot be created for the same schema on an encounter. Updating schema instances utilizes PUT
    semantics, so the schema instances on the encounter will be set to whatever inputs are provided. If null
    is provided as an input, then the encounter's schema instances will be cleared.
    """

    vitals: typing.Optional[VitalsUpdate] = pydantic.Field(default=None)
    """
    If a vitals entity already exists for the encounter, then all values will be updated to the provided values.
    Otherwise, a new vitals object will be created for the encounter.
    """

    existing_medications: typing.Optional[typing.List[Medication]] = pydantic.Field(default=None)
    """
    Existing medications that should be on the encounter.
    Note all current existing medications on encounter will be overridden with this list.
    """

    rendering_provider: typing.Optional[RenderingProviderUpdate] = pydantic.Field(default=None)
    """
    The rendering provider is the practitioner -- physician, nurse practitioner, etc. -- performing the service.
    For telehealth services, the rendering provider performs the visit, asynchronous communication, or other service. The rendering provider address should generally be the same as the service facility address.
    """

    service_facility: typing.Optional[EncounterServiceFacilityUpdate] = pydantic.Field(default=None)
    """
    Encounter Service facility is typically the location a medical service was rendered, such as a provider office or hospital. For telehealth, service facility can represent the provider's location when the service was delivered (e.g., home), or the location where an in-person visit would have taken place, whichever is easier to identify. If the provider is in-network, service facility may be defined in payer contracts. Box 32 on the CMS-1500 claim form. Note that for an in-network claim to be successfully adjudicated, the service facility address listed on claims must match what was provided to the payer during the credentialing process.
    """

    guarantor: typing.Optional[GuarantorUpdate] = pydantic.Field(default=None)
    """
    Personal and contact info for the guarantor of the patient responsibility.
    """

    billing_provider: typing.Optional[BillingProviderUpdate] = pydantic.Field(default=None)
    """
    The billing provider is the provider or business entity submitting the claim. Billing provider may be, but is not necessarily, the same person/NPI as the rendering provider. From a payer's perspective, this represents the person or entity being reimbursed. When a contract exists with the target payer, the billing provider should be the entity contracted with the payer. In some circumstances, this will be an individual provider. In that case, submit that provider's NPI and the tax ID (TIN) that the provider gave to the payer during contracting. In other cases, the billing entity will be a medical group. If so, submit the group NPI and the group's tax ID. Box 33 on the CMS-1500 claim form.
    """

    supervising_provider: typing.Optional[SupervisingProviderUpdate] = pydantic.Field(default=None)
    """
    Required when the rendering provider is supervised by a physician. If not required by this implementation guide, do not send.
    """

    referring_provider: typing.Optional[ReferringProviderUpdate] = pydantic.Field(default=None)
    """
    The final provider who referred the services that were rendered.
    All physicians who order services or refer Medicare beneficiaries must
    report this data.
    """

    initial_referring_provider: typing.Optional[InitialReferringProviderUpdate] = pydantic.Field(default=None)
    """
    The second iteration of Loop ID-2310. Use code "P3 - Primary Care Provider" in this loop to
    indicate the initial referral from the primary care provider or whatever provider wrote the initial referral for this patient's episode of care being billed/reported in this transaction.
    """

    referral_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Refers to REF\*9F on the 837p. Value cannot be greater than 50 characters.
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
