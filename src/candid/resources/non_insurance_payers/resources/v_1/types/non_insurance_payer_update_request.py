# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .non_insurance_payer_description_update import NonInsurancePayerDescriptionUpdate
from .non_insurance_payer_category_update import NonInsurancePayerCategoryUpdate
from .non_insurance_payer_address_update import NonInsurancePayerAddressUpdate
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class NonInsurancePayerUpdateRequest(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Max 50 characters allowed
    """

    description: typing.Optional[NonInsurancePayerDescriptionUpdate] = None
    category: typing.Optional[NonInsurancePayerCategoryUpdate] = None
    address: typing.Optional[NonInsurancePayerAddressUpdate] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
