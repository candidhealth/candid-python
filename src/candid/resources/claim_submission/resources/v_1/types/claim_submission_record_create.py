# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.claim_submission_payer_responsibility_type import ClaimSubmissionPayerResponsibilityType
from .....commons.types.intended_submission_medium import IntendedSubmissionMedium
from .claim_frequency_type_code import ClaimFrequencyTypeCode


class ClaimSubmissionRecordCreate(pydantic.BaseModel):
    """
    Data about each external submission.

    Examples
    --------
    import datetime

    from candid.resources.claim_submission.v_1 import ClaimSubmissionRecordCreate

    ClaimSubmissionRecordCreate(
        submitted_at=datetime.datetime.fromisoformat(
            "2023-01-01 13:00:00+00:00",
        ),
        claim_frequency_code="1",
        payer_responsibility="primary",
        intended_submission_medium="electronic",
    )
    """

    submitted_at: dt.datetime = pydantic.Field()
    """
    When the claim was submitted to the payer.
    """

    claim_frequency_code: typing.Optional[ClaimFrequencyTypeCode] = None
    payer_responsibility: typing.Optional[ClaimSubmissionPayerResponsibilityType] = None
    intended_submission_medium: typing.Optional[IntendedSubmissionMedium] = pydantic.Field(default=None)
    """
    The medium by which the claim was submitted to the payer: paper or electronic.
    If omitted, defaults to electronic.
    """

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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
