# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.date import Date
from .....commons.types.regions import Regions
from .authorized_signatory import AuthorizedSignatory
from .contract_status import ContractStatus
from .insurance_types import InsuranceTypes

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ContractBase(pydantic.BaseModel):
    effective_date: Date = pydantic.Field(description="The starting day upon which the contract is effective")
    expiration_date: typing.Optional[Date] = pydantic.Field(
        default=None, description="An optional end day upon which the contract expires"
    )
    regions: Regions = pydantic.Field(
        description=(
            "The state(s) to which the contract's coverage extends.\n"
            'It may also be set to "national" for the entirety of the US.\n'
        )
    )
    contract_status: typing.Optional[ContractStatus] = None
    authorized_signatory: typing.Optional[AuthorizedSignatory] = None
    commercial_insurance_types: InsuranceTypes = pydantic.Field(
        description=("The commercial plan insurance types this contract applies.\n")
    )
    medicare_insurance_types: InsuranceTypes = pydantic.Field(
        description=("The Medicare plan insurance types this contract applies.\n")
    )
    medicaid_insurance_types: InsuranceTypes = pydantic.Field(
        description=("The Medicaid plan insurance types this contract applies.\n")
    )

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