# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...commons.types.street_address_long_zip import StreetAddressLongZip
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class EncounterServiceFacilityUpdate(UniversalBaseModel):
    """
    Examples
    --------
    from candid.resources.commons import State, StreetAddressLongZip
    from candid.resources.service_facility import EncounterServiceFacilityUpdate

    EncounterServiceFacilityUpdate(
        organization_name="Test Organization",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    )
    """

    organization_name: typing.Optional[str] = None
    npi: typing.Optional[str] = pydantic.Field(default=None)
    """
    An NPI specific to the service facility if applicable, i.e. if it has one and is not under the billing provider's NPI.
    Box 32 section (a) of the CMS-1500 claim form.
    """

    address: typing.Optional[StreetAddressLongZip] = pydantic.Field(default=None)
    """
    zip_plus_four_code is required for service facility address. When the zip_plus_four_code is not available use "9998" as per CMS documentation.
    """

    secondary_identification: typing.Optional[str] = pydantic.Field(default=None)
    """
    An additional identifier for the service facility other than the facility's NPI. Some payers may require this field.
    Potential examples: state license number, provider commercial number, or location number.
    Box 32 section (b) of the CMS-1500 claim form.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
