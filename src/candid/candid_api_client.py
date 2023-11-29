import typing

from pydantic.v1 import BaseModel, root_validator

from candid import CandidApiEnvironment
from candid.client import CandidApi, AsyncCandidApi
from candid.resources.auth.resources.v_2 import AuthGetTokenRequest


class CandidApiClientOptions(BaseModel):
    token: typing.Optional[str]
    client_id: typing.Optional[str]
    client_secret: typing.Optional[str]

    @root_validator(pre=False)
    def token_or_client_id_and_secret_present(cls, values):
        if values.get("token") is not None:
            return values
        elif values.get("client_id") is not None and values.get("client_secret") is not None:
            return values
        raise ValueError("Either token or client_id and client_secret must be provided")


def get_token_for_options(options: CandidApiClientOptions, environment: CandidApiEnvironment) -> str:
    if options.token is not None:
        return options.token
    else:
        unauthed_client = CandidApi(environment=environment, token=None)
        response = unauthed_client.auth.v_2.get_token(request=AuthGetTokenRequest(client_id=options.client_id, client_secret=options.client_secret))
        return response.access_token


class CandidApiClient:
    def __init__(
        self, *, options: CandidApiClientOptions, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION
    ):
        candid = CandidApi(token=get_token_for_options(options, environment), environment=environment)
        self.auth = candid.auth
        self.encounters = candid.encounters
        self.billing_notes = candid.billing_notes
        self.expected_network_status = candid.expected_network_status
        self.payers = candid.payers


class AsyncCandidApiClient:
    def __init__(
        self, *, options: CandidApiClientOptions, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION
    ):
        candid = AsyncCandidApi(token=get_token_for_options(options, environment), environment=environment)
        self.auth = candid.auth
        self.encounters = candid.encounters
        self.billing_notes = candid.billing_notes
        self.expected_network_status = candid.expected_network_status
        self.payers = candid.payers
