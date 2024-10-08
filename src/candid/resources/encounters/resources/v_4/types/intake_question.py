# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .intake_question_id import IntakeQuestionId
from .intake_response_and_follow_ups import IntakeResponseAndFollowUps


class IntakeQuestion(pydantic.BaseModel):
    """
    Examples
    --------
    from candid.resources.encounters.v_4 import (
        IntakeFollowUp,
        IntakeQuestion,
        IntakeResponseAndFollowUps,
    )

    IntakeQuestion(
        id="6E7FBCE4-A8EA-46D0-A8D8-FF83CA3BB176",
        text="Do you have any allergies?",
        responses=[
            IntakeResponseAndFollowUps(
                response="No allergies",
                follow_ups=[
                    IntakeFollowUp(
                        id="4F3D57F9-AC94-49D6-87E4-E804B709917A",
                        text="Do you have any allergies?",
                        response="No allergies",
                    )
                ],
            )
        ],
    )
    """

    id: IntakeQuestionId
    text: str
    responses: typing.Optional[typing.List[IntakeResponseAndFollowUps]] = None

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
