# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .clinical_note import ClinicalNote
from .note_category import NoteCategory


class ClinicalNoteCategory(pydantic.BaseModel):
    """
    Examples
    --------
    import datetime

    from candid.resources.encounters.v_4 import ClinicalNote, ClinicalNoteCategory

    ClinicalNoteCategory(
        category="clinical",
        notes=["Patient complained of mild chest pain."],
        notes_structured=[
            ClinicalNote(
                text="Mild chest pain since morning.",
                author_name="John Doe",
                author_npi="1234567890",
                timestamp=datetime.datetime.fromisoformat(
                    "2023-01-01 00:00:00+00:00",
                ),
            )
        ],
    )
    """

    category: NoteCategory
    notes: typing.List[str]
    notes_structured: typing.Optional[typing.List[ClinicalNote]] = None

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
