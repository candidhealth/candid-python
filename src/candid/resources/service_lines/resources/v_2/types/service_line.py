# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import typing
from .....commons.types.procedure_modifier import ProcedureModifier
from .....diagnoses.types.diagnosis_id import DiagnosisId
from .drug_identification import DrugIdentification
from .service_line_era_data import ServiceLineEraData
from .service_line_adjustment import ServiceLineAdjustment
from .....invoices.types.invoice import Invoice
from .....invoices.resources.v_2.types.invoice_info import InvoiceInfo
from .service_line_denial_reason import ServiceLineDenialReason
from .....commons.types.facility_type_code import FacilityTypeCode
import pydantic
from .....commons.types.service_line_id import ServiceLineId
from .....encounter_providers.resources.v_2.types.encounter_provider import EncounterProvider
from .....commons.types.decimal import Decimal
from .....commons.types.service_line_units import ServiceLineUnits
from .....commons.types.claim_id import ClaimId
from .....commons.types.date_range_optional_end import DateRangeOptionalEnd
import datetime as dt
from .test_result import TestResult
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class ServiceLine(UniversalBaseModel):
    """
    Examples
    --------
    import datetime
    import uuid

    from candid.resources.commons import (
        DateRangeOptionalEnd,
        FacilityTypeCode,
        ProcedureModifier,
        ServiceLineUnits,
    )
    from candid.resources.invoices import Invoice, InvoiceItem, InvoiceStatus
    from candid.resources.service_lines.resources.v_2 import (
        DenialReasonContent,
        ServiceLine,
        ServiceLineAdjustment,
        ServiceLineDenialReason,
        ServiceLineEraData,
        TestResult,
        TestResultType,
    )

    ServiceLine(
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
            )
        ],
    )
    """

    modifiers: typing.Optional[typing.List[ProcedureModifier]] = None
    charge_amount_cents: typing.Optional[int] = None
    allowed_amount_cents: typing.Optional[int] = None
    insurance_balance_cents: typing.Optional[int] = None
    patient_balance_cents: typing.Optional[int] = None
    paid_amount_cents: typing.Optional[int] = None
    primary_paid_amount_cents: typing.Optional[int] = None
    secondary_paid_amount_cents: typing.Optional[int] = None
    tertiary_paid_amount_cents: typing.Optional[int] = None
    patient_responsibility_cents: typing.Optional[int] = None
    diagnosis_id_zero: typing.Optional[DiagnosisId] = None
    diagnosis_id_one: typing.Optional[DiagnosisId] = None
    diagnosis_id_two: typing.Optional[DiagnosisId] = None
    diagnosis_id_three: typing.Optional[DiagnosisId] = None
    drug_identification: typing.Optional[DrugIdentification] = None
    service_line_era_data: typing.Optional[ServiceLineEraData] = None
    service_line_manual_adjustments: typing.Optional[typing.List[ServiceLineAdjustment]] = None
    related_invoices: typing.Optional[typing.List[Invoice]] = None
    related_invoice_info: typing.Optional[typing.List[InvoiceInfo]] = None
    denial_reason: typing.Optional[ServiceLineDenialReason] = None
    place_of_service_code: typing.Optional[FacilityTypeCode] = pydantic.Field(default=None)
    """
    837p Loop2300, SV105. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).
    """

    place_of_service_code_as_submitted: typing.Optional[FacilityTypeCode] = pydantic.Field(default=None)
    """
    837p Loop2300, SV105. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).
    """

    service_line_id: ServiceLineId
    procedure_code: str
    ordering_provider: typing.Optional[EncounterProvider] = None
    quantity: Decimal = pydantic.Field()
    """
    String representation of a Decimal that can be parsed by most libraries.
    A ServiceLine quantity cannot contain more than one digit of precision.
    Example: 1.1 is valid, 1.11 is not.
    """

    units: ServiceLineUnits
    claim_id: ClaimId
    date_of_service_range: DateRangeOptionalEnd = pydantic.Field()
    """
    A range of dates of service for this service line. If the service line is for a single date, the end date
    will be empty.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A free-form description to clarify the related data elements and their content. Maps to SV1-01, C003-07 on the 837-P.
    """

    date_of_service: dt.date
    end_date_of_service: typing.Optional[dt.date] = None
    test_results: typing.Optional[typing.List[TestResult]] = pydantic.Field(default=None)
    """
    Maps to MEA-02 on the 837-P. No more than 5 test results may be submitted per service line.
    """

    has_epsdt_indicator: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Maps to SV1-11 on the 837-P and Box 24H on the CMS-1500.
    If the value is true, the box will be populated with "Y". Otherwise, the box will not be populated.
    """

    has_family_planning_indicator: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Maps to SV1-12 on the 837-P and Box 24I on the CMS-1500.
    If the value is true, the box will be populated with "Y". Otherwise, the box will not be populated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
