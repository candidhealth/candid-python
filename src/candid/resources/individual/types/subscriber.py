# This file was auto-generated by Fern from our API Definition.

from .subscriber_base import SubscriberBase
from .individual_id import IndividualId
from ...insurance_cards.resources.v_2.types.insurance_card import InsuranceCard
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class Subscriber(SubscriberBase):
    """
    Examples
    --------
    import datetime
    import uuid

    from candid.resources.commons import StreetAddressShortZip
    from candid.resources.individual import Subscriber
    from candid.resources.insurance_cards.resources.v_2 import InsuranceCard

    Subscriber(
        individual_id=uuid.UUID(
            "797348a9-e7e8-4e59-8628-95390d079c0b",
        ),
        insurance_card=InsuranceCard(
            insurance_card_id=uuid.UUID(
                "ca5b7711-4419-4161-9b7c-3494ac40c8d4",
            ),
            member_id="E85313B4-0FFC-4119-8042-8161A4ECFF0A",
            payer_name="John Doe",
            payer_id="836DDAA6-863F-4020-ACCA-205A689F0002",
            rx_bin="610014",
            rx_pcn="MEDDPRIME",
            image_url_front="https://s3.amazonaws.com/front.jpg",
            image_url_back="https://s3.amazonaws.com/back.jpg",
            group_number="ABC12345",
            plan_name="Silver PPO Plan",
            plan_type="09",
            insurance_type="12",
        ),
        patient_relationship_to_subscriber_code="01",
        date_of_birth=datetime.date.fromisoformat(
            "2000-01-01",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state="NY",
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="John",
        last_name="Doe",
        gender="male",
    )
    """

    individual_id: IndividualId
    insurance_card: InsuranceCard

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
