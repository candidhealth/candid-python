# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import typing
from .....commons.types.procedure_modifier import ProcedureModifier
from .....diagnoses.types.diagnosis_id import DiagnosisId
from .drug_identification import DrugIdentification
from .service_line_denial_reason import ServiceLineDenialReason
from .....commons.types.facility_type_code import FacilityTypeCode
import pydantic
from .....commons.types.service_line_units import ServiceLineUnits
from .....commons.types.decimal import Decimal
import datetime as dt
from .test_result import TestResult
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class ServiceLineUpdate(UniversalBaseModel):
    edit_reason: typing.Optional[str] = None
    modifiers: typing.Optional[typing.List[ProcedureModifier]] = None
    charge_amount_cents: typing.Optional[int] = None
    diagnosis_id_zero: typing.Optional[DiagnosisId] = None
    diagnosis_id_one: typing.Optional[DiagnosisId] = None
    diagnosis_id_two: typing.Optional[DiagnosisId] = None
    diagnosis_id_three: typing.Optional[DiagnosisId] = None
    drug_identification: typing.Optional[DrugIdentification] = None
    denial_reason: typing.Optional[ServiceLineDenialReason] = None
    place_of_service_code: typing.Optional[FacilityTypeCode] = pydantic.Field(default=None)
    """
    837p Loop2300, SV105. If your organization does not intend to submit claims with a different place of service at the service line level, this field should not be populated. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).
    """

    units: typing.Optional[ServiceLineUnits] = None
    procedure_code: typing.Optional[str] = None
    quantity: typing.Optional[Decimal] = pydantic.Field(default=None)
    """
    String representation of a Decimal that can be parsed by most libraries.
    A ServiceLine quantity cannot contain more than one digit of precision.
    Example: 1.1 is valid, 1.11 is not.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A free-form description to clarify the related data elements and their content. Maps to SV1-01, C003-07 on the 837-P.
    """

    date_of_service: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    date_of_service must be defined on either the encounter or the service lines but not both.
    """

    end_date_of_service: typing.Optional[dt.date] = None
    test_results: typing.Optional[typing.List[TestResult]] = pydantic.Field(default=None)
    """
    Maps to MEA-02 on the 837-P. Updating test results utilizes PUT semantics,
    so the test results on the service line will be set to whatever inputs are provided. No more than 5 test
    results may be submitted per service line.
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
