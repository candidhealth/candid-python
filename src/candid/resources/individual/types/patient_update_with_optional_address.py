# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...commons.types.email import Email
from ...commons.types.phone_number_optional import PhoneNumberOptional
from ...commons.types.street_address_short_zip_optional import StreetAddressShortZipOptional
from ...non_insurance_payers.resources.v_1.types.non_insurance_payer_id import NonInsurancePayerId
from .gender import Gender
from .patient_non_insurance_payer_info_create_optional import PatientNonInsurancePayerInfoCreateOptional


class PatientUpdateWithOptionalAddress(UniversalBaseModel):
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    gender: typing.Optional[Gender] = None
    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID used to identify this individual in your system. For example, your internal patient ID or an EHR patient ID.
    """

    date_of_birth: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Box 3 on the CMS-1500 claim form. The date format should be in ISO 8601 date; formatted YYYY-MM-DD (i.e. 2012-02-01)
    """

    address: typing.Optional[StreetAddressShortZipOptional] = pydantic.Field(default=None)
    """
    Box 5 on the CMS-1500 claim form.
    """

    phone_numbers: typing.Optional[typing.List[PhoneNumberOptional]] = None
    phone_consent: typing.Optional[bool] = None
    email: typing.Optional[Email] = None
    email_consent: typing.Optional[bool] = None
    non_insurance_payers: typing.Optional[typing.List[NonInsurancePayerId]] = pydantic.Field(default=None)
    """
    On update, we will replace the existing list of non-insurance payers with the new list if populated.
    """

    non_insurance_payers_info: typing.Optional[typing.List[PatientNonInsurancePayerInfoCreateOptional]] = (
        pydantic.Field(default=None)
    )
    """
    On update, we will replace the existing list of non-insurance payers with the new list if populated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
