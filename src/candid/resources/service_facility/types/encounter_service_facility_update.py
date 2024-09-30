# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts
from ...commons.types.street_address_long_zip import StreetAddressLongZip


class EncounterServiceFacilityUpdate(pydantic.BaseModel):
    """
    Examples
    --------
    from candid import EncounterServiceFacilityUpdate, State, StreetAddressLongZip

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

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
