# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .non_insurance_payer_id import NonInsurancePayerId
import typing
from .....commons.types.street_address_short_zip import StreetAddressShortZip
from .....clinical_trials.resources.v_1.types.clinical_trial import ClinicalTrial
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class NonInsurancePayer(UniversalBaseModel):
    """
    Examples
    --------
    import uuid

    from candid.resources.commons import State, StreetAddressShortZip
    from candid.resources.non_insurance_payers.resources.v_1 import (
        NonInsurancePayer,
    )

    NonInsurancePayer(
        non_insurance_payer_id=uuid.UUID(
            "eb7623ab-d5bc-4b25-b257-2b8fcec578de",
        ),
        name="Sunrise Foundation",
        category="Foundation",
        description="Sunrise Foundation is a non-profit organization that provides financial assistance to patients in need.",
        enabled=True,
        address=StreetAddressShortZip(
            address_1="123 Main St",
            city="San Francisco",
            state=State.CA,
            zip_code="94105",
        ),
        clinical_trials=[],
    )
    """

    non_insurance_payer_id: NonInsurancePayerId
    name: str
    description: typing.Optional[str] = None
    category: typing.Optional[str] = None
    enabled: bool
    address: typing.Optional[StreetAddressShortZip] = None
    clinical_trials: typing.List[ClinicalTrial]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
