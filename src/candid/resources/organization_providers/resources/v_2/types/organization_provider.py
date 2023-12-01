# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.date import Date
from .employment_status import EmploymentStatus
from .organization_provider_base import OrganizationProviderBase
from .organization_provider_id import OrganizationProviderId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OrganizationProvider(OrganizationProviderBase):
    organization_provider_id: OrganizationProviderId = pydantic.Field(description="Auto-generated ID set on creation")
    employment_status: EmploymentStatus = pydantic.Field(description="The employment status for the provider.")
    employment_start_date: typing.Optional[Date] = pydantic.Field(
        default=None, description="The employment start date for the provider."
    )
    employment_termination_date: typing.Optional[Date] = pydantic.Field(
        default=None, description="The employment termination date for the provider."
    )

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
