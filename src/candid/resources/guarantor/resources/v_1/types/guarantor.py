# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.email import Email
from .....commons.types.phone_number import PhoneNumber
from .guarantor_base import GuarantorBase
from .guarantor_id import GuarantorId


class Guarantor(GuarantorBase):
    """
    Examples
    --------
    import datetime
    import uuid

    from candid import PhoneNumber, PhoneNumberType, State, StreetAddressShortZip
    from candid.resources.guarantor.v_1 import Guarantor

    Guarantor(
        guarantor_id=uuid.UUID(
            "8bbdbe63-58d3-4d40-98c9-40403c050977",
        ),
        phone_numbers=[
            PhoneNumber(
                number="1234567890",
                type=PhoneNumberType.HOME,
            )
        ],
        phone_consent=True,
        email="johndoe@joincandidhealth.com",
        email_consent=True,
        first_name="John",
        last_name="Doe",
        external_id="49460F77-6456-41F1-AC6D-0AED08614D39",
        date_of_birth=datetime.date.fromisoformat(
            "2000-01-01",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    )
    """

    guarantor_id: GuarantorId
    phone_numbers: typing.List[PhoneNumber]
    phone_consent: bool
    email: typing.Optional[Email] = None
    email_consent: bool

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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
