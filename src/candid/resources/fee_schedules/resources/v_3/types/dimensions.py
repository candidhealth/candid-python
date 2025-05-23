# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.facility_type_code import FacilityTypeCode
from .....commons.types.network_type import NetworkType
from .....commons.types.payer_plan_group_id import PayerPlanGroupId
from .....commons.types.procedure_modifier import ProcedureModifier
from .....commons.types.state import State
from .....organization_providers.resources.v_2.types.license_type import LicenseType
from .....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from .....payers.resources.v_3.types.payer_uuid import PayerUuid


class Dimensions(UniversalBaseModel):
    """
    Dimension values that qualify a rate. For the optional dimensions, a null value signifies "all apply". For set-type dimensions, an empty set signifies "all apply". Only one of, but not both, of `network_types` and `payer_plan_group_id` may be populated.
    """

    payer_uuid: PayerUuid
    organization_billing_provider_id: OrganizationProviderId
    states: typing.Set[State]
    zip_codes: typing.Set[str]
    license_types: typing.Set[LicenseType]
    facility_type_codes: typing.Set[FacilityTypeCode]
    network_types: typing.Set[NetworkType]
    payer_plan_group_ids: typing.Set[PayerPlanGroupId]
    cpt_code: str
    modifiers: typing.Set[ProcedureModifier]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
