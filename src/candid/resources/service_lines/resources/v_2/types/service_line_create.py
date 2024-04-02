# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.decimal import Decimal
from .....commons.types.facility_type_code import FacilityTypeCode
from .....commons.types.procedure_modifier import ProcedureModifier
from .....commons.types.service_line_units import ServiceLineUnits
from .drug_identification import DrugIdentification

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ServiceLineCreate(pydantic.BaseModel):
    modifiers: typing.Optional[typing.List[ProcedureModifier]] = None
    procedure_code: str
    quantity: Decimal = pydantic.Field(
        description=(
            "String representation of a Decimal that can be parsed by most libraries.\n"
            "A ServiceLine quantity cannot contain more than one digit of precision.\n"
            "Example: 1.1 is valid, 1.11 is not.\n"
        )
    )
    units: ServiceLineUnits
    charge_amount_cents: typing.Optional[int] = pydantic.Field(
        default=None,
        description=(
            "The total amount charged for this service line taking quantity into account. For example, if a single unit\n"
            "costs 100 cents and 2 units were rendered, the charge_amount_cents should be 200. Should be greater than or\n"
            "equal to 0.\n"
        ),
    )
    diagnosis_pointers: typing.List[int] = pydantic.Field(
        description="Indices (zero-indexed) of all the diagnoses this service line references"
    )
    drug_identification: typing.Optional[DrugIdentification] = None
    place_of_service_code: typing.Optional[FacilityTypeCode] = None
    description: typing.Optional[str] = pydantic.Field(
        default=None,
        description="A free-form description to clarify the related data elements and their content. Maps to SV1-01, C003-07 on the 837-P.",
    )
    date_of_service: typing.Optional[dt.date] = None
    end_date_of_service: typing.Optional[dt.date] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
