# This file was auto-generated by Fern from our API Definition.

from .encounter_base import EncounterBase
from .....commons.types.pre_encounter_patient_id import PreEncounterPatientId
import typing
from .....commons.types.pre_encounter_appointment_id import PreEncounterAppointmentId
from .....encounter_providers.resources.v_2.types.billing_provider import BillingProvider
import pydantic
from .....encounter_providers.resources.v_2.types.rendering_provider import RenderingProvider
from .....encounter_providers.resources.v_2.types.initial_referring_provider import InitialReferringProvider
from .....encounter_providers.resources.v_2.types.supervising_provider import SupervisingProvider
from .....service_facility.types.encounter_service_facility_base import EncounterServiceFacilityBase
from .....diagnoses.types.diagnosis_create import DiagnosisCreate
from .clinical_note_category_create import ClinicalNoteCategoryCreate
from .....billing_notes.resources.v_2.types.billing_note_base import BillingNoteBase
from .....commons.types.facility_type_code import FacilityTypeCode
from .patient_history_category import PatientHistoryCategory
from .....service_lines.resources.v_2.types.service_line_create import ServiceLineCreate
from .....claim_submission.resources.v_1.types.external_claim_submission_create import ExternalClaimSubmissionCreate
from .....tags.types.tag_id import TagId
from .....custom_schemas.resources.v_1.types.schema_instance import SchemaInstance
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class EncounterCreateFromPreEncounter(EncounterBase):
    pre_encounter_patient_id: PreEncounterPatientId
    pre_encounter_appointment_ids: typing.List[PreEncounterAppointmentId]
    billing_provider: BillingProvider = pydantic.Field()
    """
    The billing provider is the provider or business entity submitting the claim. Billing provider may be, but is not necessarily, the same person/NPI as the rendering provider. From a payer's perspective, this represents the person or entity being reimbursed. When a contract exists with the target payer, the billing provider should be the entity contracted with the payer. In some circumstances, this will be an individual provider. In that case, submit that provider's NPI and the tax ID (TIN) that the provider gave to the payer during contracting. In other cases, the billing entity will be a medical group. If so, submit the group NPI and the group's tax ID. Box 33 on the CMS-1500 claim form.
    """

    rendering_provider: RenderingProvider = pydantic.Field()
    """
    The rendering provider is the practitioner -- physician, nurse practitioner, etc. -- performing the service.
    For telehealth services, the rendering provider performs the visit, asynchronous communication, or other service. The rendering provider address should generally be the same as the service facility address.
    """

    initial_referring_provider: typing.Optional[InitialReferringProvider] = pydantic.Field(default=None)
    """
    The second iteration of Loop ID-2310. Use code "P3 - Primary Care Provider" in this loop to
    indicate the initial referral from the primary care provider or whatever provider wrote the initial referral for this patient's episode of care being billed/reported in this transaction.
    """

    supervising_provider: typing.Optional[SupervisingProvider] = pydantic.Field(default=None)
    """
    Required when the rendering provider is supervised by a physician. If not required by this implementation guide, do not send.
    """

    service_facility: typing.Optional[EncounterServiceFacilityBase] = pydantic.Field(default=None)
    """
    Encounter Service facility is typically the location a medical service was rendered, such as a provider office or hospital. For telehealth, service facility can represent the provider's location when the service was delivered (e.g., home), or the location where an in-person visit would have taken place, whichever is easier to identify. If the provider is in-network, service facility may be defined in payer contracts. Box 32 on the CMS-1500 claim form. Note that for an in-network claim to be successfully adjudicated, the service facility address listed on claims must match what was provided to the payer during the credentialing process.
    """

    diagnoses: typing.List[DiagnosisCreate] = pydantic.Field()
    """
    Ideally, this field should contain no more than 12 diagnoses. However, more diagnoses
    may be submitted at this time, and coders will later prioritize the 12 that will be
    submitted to the payor.
    """

    clinical_notes: typing.Optional[typing.List[ClinicalNoteCategoryCreate]] = pydantic.Field(default=None)
    """
    Holds a collection of clinical observations made by healthcare providers during patient encounters.
    """

    billing_notes: typing.Optional[typing.List[BillingNoteBase]] = pydantic.Field(default=None)
    """
    Spot to store misc, human-readable, notes about this encounter to be used
    in the billing process.
    """

    place_of_service_code: FacilityTypeCode = pydantic.Field()
    """
    Box 24B on the CMS-1500 claim form. 837p Loop2300, CLM-05-1. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms .gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).
    """

    patient_histories: typing.Optional[typing.List[PatientHistoryCategory]] = None
    service_lines: typing.Optional[typing.List[ServiceLineCreate]] = pydantic.Field(default=None)
    """
    Each service line must be linked to a diagnosis. Concretely,
    `service_line.diagnosis_pointers`must contain at least one entry which should be
    in bounds of the diagnoses list field.
    """

    external_claim_submission: typing.Optional[ExternalClaimSubmissionCreate] = pydantic.Field(default=None)
    """
    To be included for claims that have been submitted outside of Candid.
    Candid supports posting remits and payments to these claims and working them in-platform (e.g. editing, resubmitting).
    """

    tag_ids: typing.Optional[typing.List[TagId]] = pydantic.Field(default=None)
    """
    Names of tags that should be on the encounter.
    """

    schema_instances: typing.Optional[typing.List[SchemaInstance]] = pydantic.Field(default=None)
    """
    Key-value pairs that must adhere to a schema created via the Custom Schema API. Multiple schema
    instances cannot be created for the same schema on an encounter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
