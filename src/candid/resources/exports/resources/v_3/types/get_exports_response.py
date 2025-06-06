# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetExportsResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from candid.resources.exports.resources.v_3 import GetExportsResponse

    GetExportsResponse(
        name="John Doe",
        created_at=datetime.datetime.fromisoformat(
            "2021-10-07 00:00:00+00:00",
        ),
        authenticated_download_url="https://example.com",
        authenticated_download_url_expiration=datetime.datetime.fromisoformat(
            "2021-10-07 00:02:00+00:00",
        ),
    )
    """

    name: str = pydantic.Field()
    """
    Report name; contains date strings representing the start and end date of the export.
    """

    created_at: dt.datetime
    authenticated_download_url: str = pydantic.Field()
    """
    Authenticated URL where a customer's report can be retrieved.
    """

    authenticated_download_url_expiration: dt.datetime = pydantic.Field()
    """
    Expiration datetime of the authenticated URL. URLs expire after 2 minutes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
