# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.resource_page import ResourcePage
from .organization_service_facility import OrganizationServiceFacility


class OrganizationServiceFacilityPage(ResourcePage):
    """
    import uuid

    from candid import State, StreetAddressLongZip
    from candid.resources.organization_service_facilities.v_2 import (
        OrganizationServiceFacility,
        OrganizationServiceFacilityPage,
        ServiceFacilityMode,
        ServiceFacilityOperationalStatus,
        ServiceFacilityPhysicalType,
        ServiceFacilityStatus,
        ServiceFacilityType,
    )

    OrganizationServiceFacilityPage(
        items=[
            OrganizationServiceFacility(
                organization_service_facility_id=uuid.UUID(
                    "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
                ),
                name="Test Service Facility",
                aliases=["Test Service Facility Alias"],
                description="Test Service Facility Description",
                status=ServiceFacilityStatus.ACTIVE,
                operational_status=ServiceFacilityOperationalStatus.C,
                mode=ServiceFacilityMode.INSTANCE,
                type=ServiceFacilityType.DX,
                physical_type=ServiceFacilityPhysicalType.SI,
                telecoms=["555-555-5555"],
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
            )
        ],
    )
    """

    items: typing.List[OrganizationServiceFacility]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
