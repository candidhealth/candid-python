# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .canonical_clinical_trial_id import CanonicalClinicalTrialId
import typing
from .period import Period
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CanonicalClinicalTrialAssociation(UniversalBaseModel):
    id: CanonicalClinicalTrialId
    clinical_trial_arm: typing.Optional[str] = None
    period: typing.Optional[Period] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
