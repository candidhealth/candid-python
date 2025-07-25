# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.claim_id import ClaimId
from .....commons.types.decimal import Decimal
from .....commons.types.facility_type_code import FacilityTypeCode
from .....commons.types.procedure_modifier import ProcedureModifier
from .....commons.types.service_line_units import ServiceLineUnits
from .....diagnoses.types.diagnosis_id import DiagnosisId
from .....encounter_providers.resources.v_2.types.ordering_provider import OrderingProvider
from .drug_identification import DrugIdentification
from .service_line_denial_reason import ServiceLineDenialReason
from .test_result import TestResult


class ServiceLineCreateStandalone(UniversalBaseModel):
    modifiers: typing.Optional[typing.List[ProcedureModifier]] = None
    charge_amount_cents: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total amount charged for this service line, factoring in quantity. If left unfilled, the system will attempt to set it based on
    chargemasters entries and the service line's quantity. For example, if a single unit has an entry of 100 cents and 2 units were rendered,
    the `charge_amount_cents` will be set to 200, if this field is unfilled.
    """

    diagnosis_id_zero: typing.Optional[DiagnosisId] = None
    diagnosis_id_one: typing.Optional[DiagnosisId] = None
    diagnosis_id_two: typing.Optional[DiagnosisId] = None
    diagnosis_id_three: typing.Optional[DiagnosisId] = None
    denial_reason: typing.Optional[ServiceLineDenialReason] = None
    place_of_service_code: typing.Optional[FacilityTypeCode] = pydantic.Field(default=None)
    """
    837p Loop2300, SV105. If your organization does not intend to submit claims with a different place of service at the service line level, this field should not be populated. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).
    """

    procedure_code: str
    quantity: Decimal = pydantic.Field()
    """
    String representation of a Decimal that can be parsed by most libraries.
    A ServiceLine quantity cannot contain more than one digit of precision.
    Example: 1.1 is valid, 1.11 is not.
    """

    units: ServiceLineUnits
    claim_id: ClaimId
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A free-form description to clarify the related data elements and their content. Maps to SV1-01, C003-07 on the 837-P.
    """

    date_of_service: typing.Optional[dt.date] = None
    end_date_of_service: typing.Optional[dt.date] = None
    drug_identification: typing.Optional[DrugIdentification] = None
    ordering_provider: typing.Optional[OrderingProvider] = pydantic.Field(default=None)
    """
    Required when the service or supply was ordered by a provider who is different than the rendering provider for this service line.
    If not required by this implementation guide, do not send.
    """

    test_results: typing.Optional[typing.List[TestResult]] = pydantic.Field(default=None)
    """
    Contains a list of test results. Test result types may map to MEA-02 on the 837-P (ex: Hemoglobin, Hematocrit).
    No more than 5 MEA-02 test results may be submitted per service line.
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

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Maps to NTE02 loop 2400 on the EDI 837.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
