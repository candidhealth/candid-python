# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .....commons.types.date import Date
import pydantic
import typing
from .....commons.types.regions import Regions
from .contract_status import ContractStatus
from .authorized_signatory import AuthorizedSignatory
from .insurance_types import InsuranceTypes
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class ContractBase(UniversalBaseModel):
    effective_date: Date = pydantic.Field()
    """
    The starting day upon which the contract is effective
    """

    expiration_date: typing.Optional[Date] = pydantic.Field(default=None)
    """
    An optional end day upon which the contract expires
    """

    regions: Regions = pydantic.Field()
    """
    The state(s) to which the contract's coverage extends.
    It may also be set to "national" for the entirety of the US.
    """

    contract_status: typing.Optional[ContractStatus] = None
    authorized_signatory: typing.Optional[AuthorizedSignatory] = None
    commercial_insurance_types: InsuranceTypes = pydantic.Field()
    """
    The commercial plan insurance types this contract applies.
    """

    medicare_insurance_types: InsuranceTypes = pydantic.Field()
    """
    The Medicare plan insurance types this contract applies.
    """

    medicaid_insurance_types: InsuranceTypes = pydantic.Field()
    """
    The Medicaid plan insurance types this contract applies.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
