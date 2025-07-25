# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2
from .....billing_notes.resources.v_2.types.billing_note import BillingNote
from .....claims.types.claim import Claim
from .....commons.types.charge_capture_claim_creation_id import ChargeCaptureClaimCreationId
from .....commons.types.encounter_id import EncounterId
from .....commons.types.facility_type_code import FacilityTypeCode
from .....commons.types.link_url import LinkUrl
from .....commons.types.next_responsible_party import NextResponsibleParty
from .....commons.types.work_queue_id import WorkQueueId
from .....custom_schemas.resources.v_1.types.schema_instance import SchemaInstance
from .....diagnoses.types.diagnosis import Diagnosis
from .....encounter_providers.resources.v_2.types.encounter_provider import EncounterProvider
from .....guarantor.resources.v_1.types.guarantor import Guarantor
from .....individual.types.patient import Patient
from .....individual.types.subscriber import Subscriber
from .....patient_payments.resources.v_3.types.patient_payment import PatientPayment
from .....service_facility.types.encounter_service_facility import EncounterServiceFacility
from .....tags.types.tag import Tag
from .claim_supplemental_information import ClaimSupplementalInformation
from .clinical_note_category import ClinicalNoteCategory
from .coding_attribution_type import CodingAttributionType
from .encounter_base import EncounterBase
from .encounter_owner_of_next_action_type import EncounterOwnerOfNextActionType
from .encounter_submission_origin_type import EncounterSubmissionOriginType
from .epsdt_referral import EpsdtReferral
from .patient_history_category import PatientHistoryCategory
from .prior_authorization_number import PriorAuthorizationNumber
from .responsible_party_type import ResponsiblePartyType


class Encounter(EncounterBase):
    """
    Examples
    --------
    import datetime
    import uuid

    from candid.resources.billing_notes.resources.v_2 import BillingNote
    from candid.resources.claims import Claim, ClaimStatus
    from candid.resources.commons import (
        DateRangeOptionalEnd,
        FacilityTypeCode,
        InsuranceTypeCode,
        NextResponsibleParty,
        PatientRelationshipToInsuredCodeAll,
        PhoneNumber,
        PhoneNumberType,
        ProcedureModifier,
        ServiceLineUnits,
        SourceOfPaymentCode,
        State,
        StreetAddressLongZip,
        StreetAddressShortZip,
    )
    from candid.resources.custom_schemas.resources.v_1 import SchemaInstance
    from candid.resources.diagnoses import Diagnosis, DiagnosisTypeCode
    from candid.resources.encounter_providers.resources.v_2 import EncounterProvider
    from candid.resources.encounters.resources.v_4 import (
        BillableStatusType,
        ClinicalNote,
        ClinicalNoteCategory,
        CodingAttributionType,
        Encounter,
        EncounterOwnerOfNextActionType,
        EncounterSubmissionOriginType,
        IntakeFollowUp,
        IntakeQuestion,
        IntakeResponseAndFollowUps,
        Intervention,
        InterventionCategory,
        Lab,
        LabCodeType,
        Medication,
        NoteCategory,
        PatientHistoryCategory,
        PatientHistoryCategoryEnum,
        ResponsiblePartyType,
        ServiceAuthorizationExceptionCode,
        SynchronicityType,
        Vitals,
    )
    from candid.resources.era import Era
    from candid.resources.guarantor.resources.v_1 import Guarantor
    from candid.resources.individual import (
        Gender,
        Patient,
        PatientNonInsurancePayerInfo,
        Subscriber,
    )
    from candid.resources.insurance_cards.resources.v_2 import InsuranceCard
    from candid.resources.invoices import Invoice, InvoiceItem, InvoiceStatus
    from candid.resources.non_insurance_payers.resources.v_1 import (
        NonInsurancePayer,
    )
    from candid.resources.patient_payments.resources.v_3 import (
        PatientPayment,
        PatientPaymentSource,
        PatientPaymentStatus,
    )
    from candid.resources.service_facility import EncounterServiceFacility
    from candid.resources.service_lines.resources.v_2 import (
        DenialReasonContent,
        ServiceLine,
        ServiceLineAdjustment,
        ServiceLineDenialReason,
        ServiceLineEraData,
        TestResult,
        TestResultType,
    )
    from candid.resources.tags import Tag, TagColorEnum

    Encounter(
        encounter_id=uuid.UUID(
            "b2506e84-4470-4cba-8a68-6883367739e1",
        ),
        claims=[
            Claim(
                claim_id=uuid.UUID(
                    "dd9d7f82-37b5-449d-aa63-26925398335b",
                ),
                status=ClaimStatus.BILLER_RECEIVED,
                clearinghouse="Change Healthcare",
                clearinghouse_claim_id="5BA7C3AB-2BC2-496C-8B10-6CAC73D0729D",
                payer_claim_id="9BB9F259-9756-4F16-8F53-9DBB9F7EB1BB",
                service_lines=[
                    ServiceLine(
                        created_at=datetime.datetime.fromisoformat(
                            "2023-01-01 00:00:00+00:00",
                        ),
                        modifiers=[ProcedureModifier.TWENTY_TWO],
                        charge_amount_cents=10000,
                        allowed_amount_cents=8000,
                        insurance_balance_cents=0,
                        patient_balance_cents=2000,
                        paid_amount_cents=8000,
                        patient_responsibility_cents=2000,
                        diagnosis_id_zero=uuid.UUID(
                            "4ac84bcd-12f5-4f86-a57b-e06749127c98",
                        ),
                        diagnosis_id_one=uuid.UUID(
                            "eea5ca5a-8b43-45fd-8cbd-c6cc1103e759",
                        ),
                        diagnosis_id_two=uuid.UUID(
                            "5c4aa029-2db9-4202-916e-e93c708f65ff",
                        ),
                        diagnosis_id_three=uuid.UUID(
                            "81795126-a3ac-443c-b47e-7259a16ab4a2",
                        ),
                        service_line_era_data=ServiceLineEraData(
                            service_line_adjustments=[
                                ServiceLineAdjustment(
                                    created_at=datetime.datetime.fromisoformat(
                                        "2023-01-01 00:00:00+00:00",
                                    ),
                                    adjustment_group_code="CO",
                                    adjustment_reason_code="CO",
                                    adjustment_amount_cents=1000,
                                    adjustment_note="test_note",
                                )
                            ],
                            remittance_advice_remark_codes=["N362"],
                        ),
                        service_line_manual_adjustments=[
                            ServiceLineAdjustment(
                                created_at=datetime.datetime.fromisoformat(
                                    "2023-01-01 00:00:00+00:00",
                                ),
                                adjustment_group_code="CO",
                                adjustment_reason_code="CO",
                                adjustment_amount_cents=1000,
                                adjustment_note="test_note",
                            )
                        ],
                        related_invoices=[
                            Invoice(
                                id=uuid.UUID(
                                    "901be2f1-41bc-456e-9987-4fe2f84f9d75",
                                ),
                                created_at=datetime.datetime.fromisoformat(
                                    "2023-01-01 00:00:00+00:00",
                                ),
                                updated_at=datetime.datetime.fromisoformat(
                                    "2023-01-01 00:00:00+00:00",
                                ),
                                organzation_id=uuid.UUID(
                                    "f13f73d4-4344-46ea-9d93-33bcffbb9f36",
                                ),
                                source_id="9B626577-8808-4F28-9ED1-F0DFF0D49BBC",
                                source_customer_id="624D1972-8C69-4C2F-AEFA-10856F734DB3",
                                patient_external_id="10FED4D6-4C5A-48DF-838A-EEF45A74788D",
                                note="test_note",
                                due_date="2023-10-10",
                                status=InvoiceStatus.DRAFT,
                                url="https://example.com",
                                customer_invoice_url="https://example.com",
                                items=[
                                    InvoiceItem(
                                        service_line_id=uuid.UUID(
                                            "ced00f23-6e68-4678-9dbc-f5aa2969a565",
                                        ),
                                        amount_cents=500,
                                    )
                                ],
                            )
                        ],
                        denial_reason=ServiceLineDenialReason(
                            reason=DenialReasonContent.AUTHORIZATION_REQUIRED,
                        ),
                        place_of_service_code=FacilityTypeCode.PHARMACY,
                        service_line_id=uuid.UUID(
                            "ced00f23-6e68-4678-9dbc-f5aa2969a565",
                        ),
                        procedure_code="99213",
                        quantity="1",
                        units=ServiceLineUnits.MJ,
                        claim_id=uuid.UUID(
                            "026a1fb8-748e-4859-a2d7-3ea9e07d25ae",
                        ),
                        date_of_service_range=DateRangeOptionalEnd(
                            start_date="2023-01-01",
                            end_date="2023-01-03",
                        ),
                        date_of_service=datetime.date.fromisoformat(
                            "2023-01-01",
                        ),
                        end_date_of_service=datetime.date.fromisoformat(
                            "2023-01-03",
                        ),
                        test_results=[
                            TestResult(
                                result_type=TestResultType.HEMOGLOBIN,
                                value=51.0,
                            ),
                            TestResult(
                                result_type=TestResultType.LDL,
                                value=110.0,
                            ),
                        ],
                    )
                ],
                eras=[
                    Era(
                        era_id=uuid.UUID(
                            "4d844ef1-2253-43cd-a4f1-6db7e65cb54b",
                        ),
                        check_number="CHK12345",
                        check_date="2023-10-12",
                    )
                ],
            )
        ],
        patient=Patient(
            individual_id=uuid.UUID(
                "93ddbebf-4956-4482-9a6c-21499b7e4e5d",
            ),
            phone_numbers=[
                PhoneNumber(
                    number="1234567890",
                    type=PhoneNumberType.HOME,
                )
            ],
            non_insurance_payers=[
                NonInsurancePayer(
                    non_insurance_payer_id=uuid.UUID(
                        "eb7623ab-d5bc-4b25-b257-2b8fcec578de",
                    ),
                    name="Sunrise Foundation",
                    category="Foundation",
                    description="Sunrise Foundation is a non-profit organization that provides financial assistance to patients in need.",
                    enabled=True,
                    address=StreetAddressShortZip(
                        address_1="123 Main St",
                        city="San Francisco",
                        state=State.CA,
                        zip_code="94105",
                    ),
                    clinical_trials=[],
                )
            ],
            non_insurance_payers_info=[
                PatientNonInsurancePayerInfo(
                    non_insurance_payer=NonInsurancePayer(
                        non_insurance_payer_id=uuid.UUID(
                            "eb7623ab-d5bc-4b25-b257-2b8fcec578de",
                        ),
                        name="Sunrise Foundation",
                        category="Foundation",
                        description="Sunrise Foundation is a non-profit organization that provides financial assistance to patients in need.",
                        enabled=True,
                        address=StreetAddressShortZip(
                            address_1="123 Main St",
                            city="San Francisco",
                            state=State.CA,
                            zip_code="94105",
                        ),
                        clinical_trials=[],
                    ),
                    member_id="123456789",
                    clinical_trial_info=[],
                )
            ],
            phone_consent=True,
            email="johndoe@joincandidhealth.com",
            email_consent=True,
            external_id="49460F77-6456-41F1-AC6D-0AED08614D39",
            date_of_birth=datetime.date.fromisoformat(
                "2000-01-01",
            ),
            address=StreetAddressShortZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
            first_name="John",
            last_name="Doe",
            gender=Gender.MALE,
        ),
        guarantor=Guarantor(
            guarantor_id=uuid.UUID(
                "8bbdbe63-58d3-4d40-98c9-40403c050977",
            ),
            phone_numbers=[
                PhoneNumber(
                    number="1234567890",
                    type=PhoneNumberType.HOME,
                )
            ],
            phone_consent=True,
            email="johndoe@joincandidhealth.com",
            email_consent=True,
            first_name="John",
            last_name="Doe",
            external_id="49460F77-6456-41F1-AC6D-0AED08614D39",
            date_of_birth=datetime.date.fromisoformat(
                "2000-01-01",
            ),
            address=StreetAddressShortZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
        ),
        billing_provider=EncounterProvider(
            provider_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            address=StreetAddressLongZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
            tax_id="123456789",
            npi="1234567890",
            taxonomy_code="207Q00000X",
            first_name="John",
            last_name="Doe",
            organization_name="Organization Name",
        ),
        rendering_provider=EncounterProvider(
            provider_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            address=StreetAddressLongZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
            tax_id="123456789",
            npi="1234567890",
            taxonomy_code="207Q00000X",
            first_name="John",
            last_name="Doe",
            organization_name="Organization Name",
        ),
        referring_provider=EncounterProvider(
            provider_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            address=StreetAddressLongZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
            tax_id="123456789",
            npi="1234567890",
            taxonomy_code="207Q00000X",
            first_name="John",
            last_name="Doe",
            organization_name="Organization Name",
        ),
        service_facility=EncounterServiceFacility(
            service_facility_id=uuid.UUID(
                "2861487b-232c-4ded-a874-616a5db0688f",
            ),
            organization_name="Test Organization",
            address=StreetAddressLongZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
        ),
        subscriber_primary=Subscriber(
            individual_id=uuid.UUID(
                "797348a9-e7e8-4e59-8628-95390d079c0b",
            ),
            insurance_card=InsuranceCard(
                insurance_card_id=uuid.UUID(
                    "ca5b7711-4419-4161-9b7c-3494ac40c8d4",
                ),
                member_id="E85313B4-0FFC-4119-8042-8161A4ECFF0A",
                payer_name="John Doe",
                payer_id="836DDAA6-863F-4020-ACCA-205A689F0002",
                rx_bin="610014",
                rx_pcn="MEDDPRIME",
                image_url_front="https://s3.amazonaws.com/front.jpg",
                image_url_back="https://s3.amazonaws.com/back.jpg",
                group_number="ABC12345",
                plan_name="Silver PPO Plan",
                plan_type=SourceOfPaymentCode.SELF_PAY,
                insurance_type=InsuranceTypeCode.C_12,
            ),
            patient_relationship_to_subscriber_code=PatientRelationshipToInsuredCodeAll.SPOUSE,
            date_of_birth=datetime.date.fromisoformat(
                "2000-01-01",
            ),
            address=StreetAddressShortZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
            first_name="John",
            last_name="Doe",
            gender=Gender.MALE,
        ),
        subscriber_secondary=Subscriber(
            individual_id=uuid.UUID(
                "797348a9-e7e8-4e59-8628-95390d079c0b",
            ),
            insurance_card=InsuranceCard(
                insurance_card_id=uuid.UUID(
                    "ca5b7711-4419-4161-9b7c-3494ac40c8d4",
                ),
                member_id="E85313B4-0FFC-4119-8042-8161A4ECFF0A",
                payer_name="John Doe",
                payer_id="836DDAA6-863F-4020-ACCA-205A689F0002",
                rx_bin="610014",
                rx_pcn="MEDDPRIME",
                image_url_front="https://s3.amazonaws.com/front.jpg",
                image_url_back="https://s3.amazonaws.com/back.jpg",
                group_number="ABC12345",
                plan_name="Silver PPO Plan",
                plan_type=SourceOfPaymentCode.SELF_PAY,
                insurance_type=InsuranceTypeCode.C_12,
            ),
            patient_relationship_to_subscriber_code=PatientRelationshipToInsuredCodeAll.SPOUSE,
            date_of_birth=datetime.date.fromisoformat(
                "2000-01-01",
            ),
            address=StreetAddressShortZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
            first_name="John",
            last_name="Doe",
            gender=Gender.MALE,
        ),
        url="https://example.com",
        diagnoses=[
            Diagnosis(
                diagnosis_id=uuid.UUID(
                    "5c770e00-4bbf-42af-a73f-99c5e91fc0db",
                ),
                created_at=datetime.datetime.fromisoformat(
                    "2023-01-01 00:00:00+00:00",
                ),
                updated_at=datetime.datetime.fromisoformat(
                    "2023-01-01 00:00:00+00:00",
                ),
                encounter_id=uuid.UUID(
                    "3f63985b-51a4-4dd4-9418-7d50b2520792",
                ),
                name="John Doe",
                code_type=DiagnosisTypeCode.ABF,
                code="I10",
            )
        ],
        clinical_notes=[
            ClinicalNoteCategory(
                category=NoteCategory.CLINICAL,
                notes=["Patient complained of mild chest pain."],
                notes_structured=[
                    ClinicalNote(
                        text="Mild chest pain since morning.",
                        author_name="John Doe",
                        author_npi="1234567890",
                        timestamp=datetime.datetime.fromisoformat(
                            "2023-01-01 00:00:00+00:00",
                        ),
                    )
                ],
            )
        ],
        billing_notes=[
            BillingNote(
                billing_note_id=uuid.UUID(
                    "99882eea-936f-4e71-bc4f-520e4d14e3e2",
                ),
                encounter_id=uuid.UUID(
                    "8bcfb6a8-2876-4111-9e3f-602b541fcf62",
                ),
                created_at=datetime.datetime.fromisoformat(
                    "2023-01-01 00:00:00+00:00",
                ),
                author_auth_0_id="F0DE3BF9-F9A1-4FA7-BF6B-28C0B46BADD8",
                author_name="John Doe",
                text="Patient was billed for an MRI.",
            )
        ],
        place_of_service_code=FacilityTypeCode.PHARMACY,
        place_of_service_code_as_submitted=FacilityTypeCode.PHARMACY,
        patient_histories=[
            PatientHistoryCategory(
                category=PatientHistoryCategoryEnum.PRESENT_ILLNESS,
                questions=[
                    IntakeQuestion(
                        id="6E7FBCE4-A8EA-46D0-A8D8-FF83CA3BB176",
                        text="Do you have any allergies?",
                        responses=[
                            IntakeResponseAndFollowUps(
                                response="No allergies",
                                follow_ups=[
                                    IntakeFollowUp(
                                        id="4F3D57F9-AC94-49D6-87E4-E804B709917A",
                                        text="Do you have any allergies?",
                                        response="No allergies",
                                    )
                                ],
                            )
                        ],
                    )
                ],
            )
        ],
        patient_payments=[
            PatientPayment(
                patient_payment_id="CF237BE1-E793-4BBF-8958-61D5179D1D0D",
                organization_id=uuid.UUID(
                    "0788ca2a-b20d-4b8e-b8d4-07fa0b3b4907",
                ),
                source_internal_id="D1A76039-D5C5-4323-A2FC-B7C8B6AEF6A4",
                source=PatientPaymentSource.MANUAL_ENTRY,
                amount_cents=2000,
                payment_timestamp=datetime.datetime.fromisoformat(
                    "2023-01-01 00:00:00+00:00",
                ),
                status=PatientPaymentStatus.PENDING,
                payment_name="John Doe",
                payment_note="test payment note",
                patient_external_id="B7437260-D6B4-48CF-B9D7-753C09F34E76",
                encounter_external_id="0F26B9C3-199F-4CBB-A166-B87EA7C631BB",
                service_line_id=uuid.UUID(
                    "b557dc86-c629-478c-850a-02d45ac11783",
                ),
            )
        ],
        tags=[
            Tag(
                creator_id="00EB5A46-35C6-441B-9751-AF307AEF5888",
                tag_id="void-claim-submitted",
                description="to indicate claims where a void claim has been submitted",
                color=TagColorEnum.BLACK,
            )
        ],
        coding_attribution=CodingAttributionType.CANDID,
        work_queue_id="12",
        work_queue_membership_activated_at=datetime.datetime.fromisoformat(
            "2023-01-01 00:00:00+00:00",
        ),
        owner_of_next_action=EncounterOwnerOfNextActionType.CANDID,
        submission_origin=EncounterSubmissionOriginType.CANDID,
        external_id="5C21490F-A9C0-45F4-B5DB-136E3AEC617A",
        date_of_service=datetime.date.fromisoformat(
            "2023-01-01",
        ),
        end_date_of_service=datetime.date.fromisoformat(
            "2023-01-05",
        ),
        prior_authorization_number="PA1234567",
        patient_authorized_release=True,
        benefits_assigned_to_provider=True,
        provider_accepts_assignment=True,
        appointment_type="Routine Checkup",
        existing_medications=[
            Medication(
                name="Lisinopril",
                rx_cui="860975",
                dosage="10mg",
                dosage_form="Tablet",
                frequency="Once Daily",
                as_needed=True,
            )
        ],
        vitals=Vitals(
            height_in=70,
            weight_lbs=165,
            blood_pressure_systolic_mmhg=115,
            blood_pressure_diastolic_mmhg=85,
            body_temperature_f=98.0,
            hemoglobin_gdl=15.1,
            hematocrit_pct=51.2,
        ),
        interventions=[
            Intervention(
                name="Physical Therapy Session",
                category=InterventionCategory.LIFESTYLE,
                description="A session focused on improving muscular strength, flexibility, and range of motion post-injury.",
                medication=Medication(
                    name="Lisinopril",
                    rx_cui="860975",
                    dosage="10mg",
                    dosage_form="Tablet",
                    frequency="Once Daily",
                    as_needed=True,
                ),
                labs=[
                    Lab(
                        name="Genetic Health Labs",
                        code="GH12345",
                        code_type=LabCodeType.QUEST,
                    )
                ],
            )
        ],
        pay_to_address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        synchronicity=SynchronicityType.SYNCHRONOUS,
        billable_status=BillableStatusType.BILLABLE,
        responsible_party=ResponsiblePartyType.INSURANCE_PAY,
        service_authorization_exception_code=ServiceAuthorizationExceptionCode.C_1,
        admission_date=datetime.date.fromisoformat(
            "2023-01-01",
        ),
        discharge_date=datetime.date.fromisoformat(
            "2023-01-05",
        ),
        onset_of_current_illness_or_symptom_date=datetime.date.fromisoformat(
            "2023-01-01",
        ),
        schema_instances=[
            SchemaInstance(
                schema_id=uuid.UUID(
                    "ec096b13-f80a-471d-aaeb-54b021c9d582",
                ),
                content={
                    "provider_category": "internist",
                    "is_urgent_care": True,
                    "bmi": 24.2,
                    "age": 38,
                },
            )
        ],
        created_at=datetime.datetime.fromisoformat(
            "2023-01-01 00:00:00+00:00",
        ),
        next_responsible_party=NextResponsibleParty.PRIMARY,
    )
    """

    claim_creation_id: typing.Optional[ChargeCaptureClaimCreationId] = pydantic.Field(default=None)
    """
    If the encounter was created from ingested charge captures, this is the associated Charge Capture Claim Creation Id.
    """

    patient_control_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    A patient control number (PCN) is a unique identifier assigned to a patient within a healthcare system or facility.
    It's used to track and manage a patient's medical records, treatments, and other healthcare-related information.
    """

    encounter_id: EncounterId
    claims: typing.List[Claim]
    patient: Patient = pydantic.Field()
    """
    Contains the identification information of the individual receiving medical services.
    """

    guarantor: typing.Optional[Guarantor] = pydantic.Field(default=None)
    """
    Personal and contact info for the guarantor of the patient responsibility.
    """

    billing_provider: EncounterProvider = pydantic.Field()
    """
    The billing provider is the provider or business entity submitting the claim. Billing provider may be, but is not necessarily, the same person/NPI as the rendering provider. From a payer's perspective, this represents the person or entity being reimbursed. When a contract exists with the target payer, the billing provider should be the entity contracted with the payer. In some circumstances, this will be an individual provider. In that case, submit that provider's NPI and the tax ID (TIN) that the provider gave to the payer during contracting. In other cases, the billing entity will be a medical group. If so, submit the group NPI and the group's tax ID. Box 33 on the CMS-1500 claim form.
    """

    rendering_provider: EncounterProvider = pydantic.Field()
    """
    The rendering provider is the practitioner -- physician, nurse practitioner, etc. -- performing the service.
    For telehealth services, the rendering provider performs the visit, asynchronous communication, or other service. The rendering provider address should generally be the same as the service facility address.
    """

    referring_provider: typing.Optional[EncounterProvider] = None
    initial_referring_provider: typing.Optional[EncounterProvider] = None
    supervising_provider: typing.Optional[EncounterProvider] = None
    service_facility: EncounterServiceFacility = pydantic.Field()
    """
    Encounter Service facility is typically the location a medical service was rendered, such as a provider office or hospital. For telehealth, service facility can represent the provider's location when the service was delivered (e.g., home), or the location where an in-person visit would have taken place, whichever is easier to identify. If the provider is in-network, service facility may be defined in payer contracts. Box 32 on the CMS-1500 claim form. Note that for an in-network claim to be successfully adjudicated, the service facility address listed on claims must match what was provided to the payer during the credentialing process.
    """

    subscriber_primary: typing.Optional[Subscriber] = pydantic.Field(default=None)
    """
    Subscriber_primary is required when responsible_party is INSURANCE_PAY (i.e. when the claim should be billed to insurance).
    These are not required fields when responsible_party is SELF_PAY (i.e. when the claim should be billed to the patient).
    However, if you collect this for patients, even self-pay, we recommend including it when sending encounters to Candid.
    Note: Cash Pay is no longer a valid payer_id in v4, please use responsible party to define self-pay claims.
    """

    subscriber_secondary: typing.Optional[Subscriber] = pydantic.Field(default=None)
    """
    Contains details of the secondary insurance subscriber.
    """

    subscriber_tertiary: typing.Optional[Subscriber] = pydantic.Field(default=None)
    """
    Contains details of the tertiary insurance subscriber.
    """

    prior_authorization_number: typing.Optional[PriorAuthorizationNumber] = pydantic.Field(default=None)
    """
    Box 23 on the CMS-1500 claim form.
    """

    responsible_party: ResponsiblePartyType = pydantic.Field()
    """
    Defines the party to be billed with the initial balance owed on the claim.
    """

    url: LinkUrl = pydantic.Field()
    """
    URL that links directly to the claim created in Candid.
    """

    diagnoses: typing.List[Diagnosis] = pydantic.Field()
    """
    Ideally, this field should contain no more than 12 diagnoses. However, more diagnoses may be submitted at this time, and coders will later prioritize the 12 that will be submitted to the payor.
    """

    clinical_notes: typing.List[ClinicalNoteCategory] = pydantic.Field()
    """
    Holds a collection of clinical observations made by healthcare providers during patient encounters. Please note that medical records for appeals should be sent using the Encounter Attachments API.
    """

    billing_notes: typing.Optional[typing.List[BillingNote]] = pydantic.Field(default=None)
    """
    Spot to store misc, human-readable, notes about this encounter to be
    used in the billing process.
    """

    place_of_service_code: typing.Optional[FacilityTypeCode] = pydantic.Field(default=None)
    """
    Box 24B on the CMS-1500 claim form. 837p Loop2300, CLM-05-1. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).
    """

    place_of_service_code_as_submitted: typing.Optional[FacilityTypeCode] = pydantic.Field(default=None)
    """
    Box 24B on the CMS-1500 claim form. 837p Loop2300, CLM-05-1. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).
    """

    patient_histories: typing.List[PatientHistoryCategory]
    patient_payments: typing.List[PatientPayment]
    tags: typing.List[Tag]
    coding_attribution: typing.Optional[CodingAttributionType] = pydantic.Field(default=None)
    """
    The entity that performed the coding of medical services for the claim.
    """

    work_queue_id: typing.Optional[WorkQueueId] = None
    work_queue_membership_activated_at: typing.Optional[dt.datetime] = None
    owner_of_next_action: EncounterOwnerOfNextActionType = pydantic.Field()
    """
    The party who is responsible for taking the next action on an Encounter, as defined by ownership of open Tasks.
    """

    submission_origin: EncounterSubmissionOriginType = pydantic.Field()
    """
    The party who originally submitted the Claim.
    For Claims originating in Candid, this will be EncounterSubmissionOriginType.CANDID.
    For Encounters created with an external_claim_submission object, this will be EncounterSubmissionOriginType.EXTERNAL.
    """

    schema_instances: typing.List[SchemaInstance] = pydantic.Field()
    """
    Key-value pairs that must adhere to a schema created via the Custom Schema API. Multiple schema
    instances cannot be created for the same schema on an encounter.
    """

    referral_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Refers to REF*9F on the 837p. Value cannot be greater than 50 characters.
    """

    epsdt_referral: typing.Optional[EpsdtReferral] = pydantic.Field(default=None)
    """
    Refers Box 24H on the CMS1500 form and Loop 2300 CRC - EPSDT Referral on the 837P form
    """

    claim_supplemental_information: typing.Optional[typing.List[ClaimSupplementalInformation]] = pydantic.Field(
        default=None
    )
    """
    Refers to Loop 2300 - Segment PWK on the 837P form. No more than 10 entries are permitted.
    """

    secondary_payer_carrier_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    When Medicaid is billed as the secondary payer the Carrier Code is used to identify the primary payer. This is required for certain states.
    """

    last_submitted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the encounter was last submitted to a payer.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the encounter was created.
    """

    next_responsible_party: typing.Optional[NextResponsibleParty] = pydantic.Field(default=None)
    """
    The party (payer, patient, etc.) responsible for the remainder of the balance on the claim.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
