# This file was auto-generated by Fern from our API Definition.

from .....commons.types.resource_page import ResourcePage
import typing
from .organization_service_facility import OrganizationServiceFacility
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OrganizationServiceFacilityPage(ResourcePage):
    """
    Examples
    --------
    import uuid

    from candid.resources.commons import State, StreetAddressLongZip
    from candid.resources.organization_service_facilities.resources.v_2 import (
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
                operational_status=ServiceFacilityOperationalStatus.CLOSED,
                mode=ServiceFacilityMode.INSTANCE,
                type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
                physical_type=ServiceFacilityPhysicalType.SITE,
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
