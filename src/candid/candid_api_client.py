import typing

from pydantic import BaseModel, root_validator

from candid import CandidApiEnvironment
from candid.client import CandidApi
from candid.resources.auth.client import AuthClient, AsyncAuthClient
from candid.resources.auth.resources.v_2 import AuthGetTokenRequest
from candid.resources.billing_notes.client import BillingNotesClient, AsyncBillingNotesClient
from candid.resources.encounters.client import EncountersClient, AsyncEncountersClient
from candid.resources.expected_network_status.client import ExpectedNetworkStatusClient, \
    AsyncExpectedNetworkStatusClient
from candid.resources.payers.client import PayersClient, AsyncPayersClient


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
        self._environment = environment
        self._token = get_token_for_options(options, environment)
        self.auth = AuthClient(environment=self._environment, token=self._token)
        self.encounters = EncountersClient(environment=self._environment, token=self._token)
        self.billing_notes = BillingNotesClient(environment=self._environment, token=self._token)
        self.expected_network_status = ExpectedNetworkStatusClient(environment=self._environment, token=self._token)
        self.payers = PayersClient(environment=self._environment, token=self._token)


class AsyncCandidApiClient:
    def __init__(
        self, *, options: CandidApiClientOptions, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION
    ):
        self._environment = environment
        self._token = get_token_for_options(options, environment)
        self.auth = AsyncAuthClient(environment=self._environment, token=self._token)
        self.encounters = AsyncEncountersClient(environment=self._environment, token=self._token)
        self.billing_notes = AsyncBillingNotesClient(environment=self._environment, token=self._token)
        self.expected_network_status = AsyncExpectedNetworkStatusClient(
            environment=self._environment, token=self._token
        )
        self.payers = AsyncPayersClient(environment=self._environment, token=self._token)
