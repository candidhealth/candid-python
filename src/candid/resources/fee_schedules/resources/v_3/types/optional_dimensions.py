# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import typing
from .....payers.resources.v_3.types.payer_uuid import PayerUuid
from .....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from .....commons.types.state import State
from .....organization_providers.resources.v_2.types.license_type import LicenseType
from .....commons.types.facility_type_code import FacilityTypeCode
from .....commons.types.network_type import NetworkType
from .....commons.types.payer_plan_group_id import PayerPlanGroupId
from .....commons.types.procedure_modifier import ProcedureModifier
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OptionalDimensions(UniversalBaseModel):
    """
    A dimensions object where all properties are optional.
    """

    payer_uuid: typing.Optional[PayerUuid] = None
    organization_billing_provider_id: typing.Optional[OrganizationProviderId] = None
    states: typing.Set[State]
    zip_codes: typing.Set[str]
    license_types: typing.Set[LicenseType]
    facility_type_codes: typing.Set[FacilityTypeCode]
    network_types: typing.Set[NetworkType]
    payer_plan_group_ids: typing.Set[PayerPlanGroupId]
    cpt_code: typing.Optional[str] = None
    modifiers: typing.Set[ProcedureModifier]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
