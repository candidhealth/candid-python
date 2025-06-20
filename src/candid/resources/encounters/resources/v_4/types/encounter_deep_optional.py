# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2
from .....billing_notes.resources.v_2.types.billing_note_base_optional import BillingNoteBaseOptional
from .....claim_submission.resources.v_1.types.external_claim_submission_create_optional import (
    ExternalClaimSubmissionCreateOptional,
)
from .....commons.types.street_address_short_zip_optional import StreetAddressShortZipOptional
from .....custom_schemas.resources.v_1.types.schema_instance_optional import SchemaInstanceOptional
from .....diagnoses.types.diagnosis_create_optional import DiagnosisCreateOptional
from .....encounter_providers.resources.v_2.types.billing_provider_update_with_optional_address import (
    BillingProviderUpdateWithOptionalAddress,
)
from .....encounter_providers.resources.v_2.types.initial_referring_provider_update_with_optional_address import (
    InitialReferringProviderUpdateWithOptionalAddress,
)
from .....encounter_providers.resources.v_2.types.referring_provider_update_with_optional_address import (
    ReferringProviderUpdateWithOptionalAddress,
)
from .....encounter_providers.resources.v_2.types.rendering_provider_update_with_optional_address import (
    RenderingProviderUpdateWithOptionalAddress,
)
from .....encounter_providers.resources.v_2.types.supervising_provider_update_with_optional_address import (
    SupervisingProviderUpdateWithOptionalAddress,
)
from .....guarantor.resources.v_1.types.guarantor_optional import GuarantorOptional
from .....individual.types.patient_update_with_optional_address import PatientUpdateWithOptionalAddress
from .....individual.types.subscriber_create_optional import SubscriberCreateOptional
from .....service_facility.types.encounter_service_facility_update_with_optional_address import (
    EncounterServiceFacilityUpdateWithOptionalAddress,
)
from .....service_lines.resources.v_2.types.service_line_create_optional import ServiceLineCreateOptional
from .claim_supplemental_information_optional import ClaimSupplementalInformationOptional
from .clinical_note_category_create_optional import ClinicalNoteCategoryCreateOptional
from .encounter_optional import EncounterOptional
from .epsdt_referral_optional import EpsdtReferralOptional
from .intervention_optional import InterventionOptional
from .medication_optional import MedicationOptional
from .patient_history_category_optional import PatientHistoryCategoryOptional


class EncounterDeepOptional(EncounterOptional):
    diagnoses: typing.Optional[typing.List[DiagnosisCreateOptional]] = pydantic.Field(default=None)
    """
    Ideally, this field should contain no more than 12 diagnoses. However, more diagnoses
    may be submitted at this time, and coders will later prioritize the 12 that will be
    submitted to the payor.
    """

    clinical_notes: typing.Optional[typing.List[ClinicalNoteCategoryCreateOptional]] = pydantic.Field(default=None)
    """
    Holds a collection of clinical observations made by healthcare providers during patient encounters. Please note that medical records for appeals should be sent using the Encounter Attachments API.
    """

    claim_supplemental_information: typing.Optional[typing.List[ClaimSupplementalInformationOptional]] = pydantic.Field(
        default=None
    )
    """
    Refers to Loop 2300 - Segment PWK on the 837P form. No more than 10 entries are permitted.
    """

    epsdt_referral: typing.Optional[EpsdtReferralOptional] = pydantic.Field(default=None)
    """
    Refers Box 24H on the CMS1500 form and Loop 2300 CRC - EPSDT Referral on the 837P form
    """

    existing_medications: typing.Optional[typing.List[MedicationOptional]] = pydantic.Field(default=None)
    """
    Existing medications that should be on the encounter.
    Note all current existing medications on encounter will be overridden with this list.
    """

    guarantor: typing.Optional[GuarantorOptional] = pydantic.Field(default=None)
    """
    Personal and contact info for the guarantor of the patient responsibility.
    """

    subscriber_primary: typing.Optional[SubscriberCreateOptional] = pydantic.Field(default=None)
    """
    Contains details of the primary insurance subscriber.
    """

    subscriber_secondary: typing.Optional[SubscriberCreateOptional] = pydantic.Field(default=None)
    """
    Contains details of the secondary insurance subscriber.
    """

    subscriber_tertiary: typing.Optional[SubscriberCreateOptional] = pydantic.Field(default=None)
    """
    Contains details of the tertiary insurance subscriber.
    """

    interventions: typing.Optional[typing.List[InterventionOptional]] = None
    schema_instances: typing.Optional[typing.List[SchemaInstanceOptional]] = pydantic.Field(default=None)
    """
    Key-value pairs that must adhere to a schema created via the Custom Schema API. Multiple schema
    instances cannot be created for the same schema on an encounter. Updating schema instances utilizes PUT
    semantics, so the schema instances on the encounter will be set to whatever inputs are provided. If null
    is provided as an input, then the encounter's schema instances will be cleared.
    """

    external_claim_submission: typing.Optional[ExternalClaimSubmissionCreateOptional] = pydantic.Field(default=None)
    """
    ***This field is in beta.***
    To be included for claims that have been submitted outside of Candid.
    Candid supports posting remits and payments to these claims and working them in-platform (e.g. editing, resubmitting).
    """

    service_lines: typing.Optional[typing.List[ServiceLineCreateOptional]] = pydantic.Field(default=None)
    """
    Each service line must be linked to a diagnosis. Concretely,
    `service_line.diagnosis_pointers`must contain at least one entry which should be
    in bounds of the diagnoses list field.
    """

    patient_histories: typing.Optional[typing.List[PatientHistoryCategoryOptional]] = None
    billing_notes: typing.Optional[typing.List[BillingNoteBaseOptional]] = pydantic.Field(default=None)
    """
    Spot to store misc, human-readable, notes about this encounter to be
    used in the billing process.
    """

    patient: typing.Optional[PatientUpdateWithOptionalAddress] = pydantic.Field(default=None)
    """
    Contains the identification information of the individual receiving medical services.
    """

    service_facility: typing.Optional[EncounterServiceFacilityUpdateWithOptionalAddress] = pydantic.Field(default=None)
    """
    Encounter Service facility is typically the location a medical service was rendered, such as a provider office or hospital. For telehealth, service facility can represent the provider's location when the service was delivered (e.g., home), or the location where an in-person visit would have taken place, whichever is easier to identify. If the provider is in-network, service facility may be defined in payer contracts. Box 32 on the CMS-1500 claim form. Note that for an in-network claim to be successfully adjudicated, the service facility address listed on claims must match what was provided to the payer during the credentialing process.
    """

    rendering_provider: typing.Optional[RenderingProviderUpdateWithOptionalAddress] = pydantic.Field(default=None)
    """
    The rendering provider is the practitioner -- physician, nurse practitioner, etc. -- performing the service. For telehealth services, the rendering provider performs the visit, asynchronous communication, or other service. The rendering provider address should generally be the same as the service facility address.
    """

    initial_referring_provider: typing.Optional[InitialReferringProviderUpdateWithOptionalAddress] = pydantic.Field(
        default=None
    )
    """
    The second iteration of Loop ID-2310. Use code "P3 - Primary Care Provider" in this loop to
    indicate the initial referral from the primary care provider or whatever provider wrote the initial referral for this patient's episode of care being billed/reported in this transaction.
    """

    referring_provider: typing.Optional[ReferringProviderUpdateWithOptionalAddress] = pydantic.Field(default=None)
    """
    The final provider who referred the services that were rendered.
    All physicians who order services or refer Medicare beneficiaries must
    report this data.
    """

    supervising_provider: typing.Optional[SupervisingProviderUpdateWithOptionalAddress] = pydantic.Field(default=None)
    """
    Required when the rendering provider is supervised by a physician. If not required by this implementation guide, do not send.
    """

    billing_provider: typing.Optional[BillingProviderUpdateWithOptionalAddress] = pydantic.Field(default=None)
    """
    The billing provider is the provider or business entity submitting the claim. Billing provider may be, but is not necessarily, the same person/NPI as the rendering provider. From a payer's perspective, this represents the person or entity being reimbursed. When a contract exists with the target payer, the billing provider should be the entity contracted with the payer. In some circumstances, this will be an individual provider. In that case, submit that provider's NPI and the tax ID (TIN) that the provider gave to the payer during contracting. In other cases, the billing entity will be a medical group. If so, submit the group NPI and the group's tax ID. Box 33 on the CMS-1500 claim form.
    """

    pay_to_address: typing.Optional[StreetAddressShortZipOptional] = pydantic.Field(default=None)
    """
    Specifies the address to which payments for the claim should be sent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
