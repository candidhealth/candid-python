# This file was auto-generated by Fern from our API Definition.

from .individual_base import IndividualBase
import pydantic
import datetime as dt
from ...commons.types.street_address_short_zip import StreetAddressShortZip
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class PatientBase(IndividualBase):
    external_id: str = pydantic.Field()
    """
    The ID used to identify this individual in your system. For example, your internal patient ID or an EHR patient ID.
    """

    date_of_birth: dt.date = pydantic.Field()
    """
    Box 3 on the CMS-1500 claim form. The date format should be in ISO 8601 date; formatted YYYY-MM-DD (i.e. 2012-02-01)
    """

    address: StreetAddressShortZip = pydantic.Field()
    """
    Box 5 on the CMS-1500 claim form.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
