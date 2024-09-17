# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.facility_type_code import FacilityTypeCode
from .....commons.types.network_type import NetworkType
from .....commons.types.procedure_modifier import ProcedureModifier
from .....commons.types.state import State
from .....organization_providers.resources.v_2.types.license_type import LicenseType
from .....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from .....payers.resources.v_3.types.payer_uuid import PayerUuid


class Dimensions(pydantic.BaseModel):
    """
    Dimension values that qualify a rate. For the optional dimensions, a null value signifies "all apply". For set-type dimensions, an empty set signifies "all apply".
    """

    payer_uuid: PayerUuid
    organization_billing_provider_id: OrganizationProviderId
    states: typing.Set[State]
    zip_codes: typing.Set[str]
    license_types: typing.Set[LicenseType]
    facility_type_codes: typing.Set[FacilityTypeCode]
    network_types: typing.Set[NetworkType]
    cpt_code: str
    modifiers: typing.Set[ProcedureModifier]

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
