# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.oauth_token_provider import OAuthTokenProvider
from .environment import CandidApiClientEnvironment
from .resources.auth.client import AsyncAuthClient, AuthClient
from .resources.billing_notes.client import AsyncBillingNotesClient, BillingNotesClient
from .resources.contracts.client import AsyncContractsClient, ContractsClient
from .resources.eligibility.client import AsyncEligibilityClient, EligibilityClient
from .resources.encounters.client import AsyncEncountersClient, EncountersClient
from .resources.expected_network_status.client import AsyncExpectedNetworkStatusClient, ExpectedNetworkStatusClient
from .resources.exports.client import AsyncExportsClient, ExportsClient
from .resources.fee_schedules.client import AsyncFeeSchedulesClient, FeeSchedulesClient
from .resources.guarantor.client import AsyncGuarantorClient, GuarantorClient
from .resources.import_invoice.client import AsyncImportInvoiceClient, ImportInvoiceClient
from .resources.insurance_adjudications.client import AsyncInsuranceAdjudicationsClient, InsuranceAdjudicationsClient
from .resources.insurance_payments.client import AsyncInsurancePaymentsClient, InsurancePaymentsClient
from .resources.insurance_refunds.client import AsyncInsuranceRefundsClient, InsuranceRefundsClient
from .resources.organization_providers.client import AsyncOrganizationProvidersClient, OrganizationProvidersClient
from .resources.organization_service_facilities.client import (
    AsyncOrganizationServiceFacilitiesClient,
    OrganizationServiceFacilitiesClient,
)
from .resources.patient_payments.client import AsyncPatientPaymentsClient, PatientPaymentsClient
from .resources.patient_refunds.client import AsyncPatientRefundsClient, PatientRefundsClient
from .resources.payers.client import AsyncPayersClient, PayersClient
from .resources.service_facility.client import AsyncServiceFacilityClient, ServiceFacilityClient
from .resources.tasks.client import AsyncTasksClient, TasksClient
from .resources.write_offs.client import AsyncWriteOffsClient, WriteOffsClient


class CandidApiClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : CandidApiClientEnvironment
        The environment to use for requests from the client. from .environment import CandidApiClientEnvironment



        Defaults to CandidApiClientEnvironment.PRODUCTION



    client_id : str
    client_secret : str
    _token_getter_override : typing.Optional[typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from candid.client import CandidApiClient

    client = CandidApiClient(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: CandidApiClientEnvironment = CandidApiClientEnvironment.PRODUCTION,
        client_id: str,
        client_secret: str,
        _token_getter_override: typing.Optional[typing.Callable[[], str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        oauth_token_provider = OAuthTokenProvider(
            client_id=client_id,
            client_secret=client_secret,
            client_wrapper=SyncClientWrapper(
                base_url=_get_base_url(base_url=base_url, environment=environment),
                httpx_client=httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
                if follow_redirects is not None
                else httpx.Client(timeout=_defaulted_timeout),
                timeout=_defaulted_timeout,
            ),
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=_token_getter_override if _token_getter_override is not None else oauth_token_provider.get_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.billing_notes = BillingNotesClient(client_wrapper=self._client_wrapper)
        self.contracts = ContractsClient(client_wrapper=self._client_wrapper)
        self.eligibility = EligibilityClient(client_wrapper=self._client_wrapper)
        self.encounters = EncountersClient(client_wrapper=self._client_wrapper)
        self.expected_network_status = ExpectedNetworkStatusClient(client_wrapper=self._client_wrapper)
        self.exports = ExportsClient(client_wrapper=self._client_wrapper)
        self.fee_schedules = FeeSchedulesClient(client_wrapper=self._client_wrapper)
        self.guarantor = GuarantorClient(client_wrapper=self._client_wrapper)
        self.import_invoice = ImportInvoiceClient(client_wrapper=self._client_wrapper)
        self.insurance_adjudications = InsuranceAdjudicationsClient(client_wrapper=self._client_wrapper)
        self.insurance_payments = InsurancePaymentsClient(client_wrapper=self._client_wrapper)
        self.insurance_refunds = InsuranceRefundsClient(client_wrapper=self._client_wrapper)
        self.organization_service_facilities = OrganizationServiceFacilitiesClient(client_wrapper=self._client_wrapper)
        self.organization_providers = OrganizationProvidersClient(client_wrapper=self._client_wrapper)
        self.patient_payments = PatientPaymentsClient(client_wrapper=self._client_wrapper)
        self.patient_refunds = PatientRefundsClient(client_wrapper=self._client_wrapper)
        self.payers = PayersClient(client_wrapper=self._client_wrapper)
        self.tasks = TasksClient(client_wrapper=self._client_wrapper)
        self.write_offs = WriteOffsClient(client_wrapper=self._client_wrapper)
        self.service_facility = ServiceFacilityClient(client_wrapper=self._client_wrapper)


class AsyncCandidApiClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : CandidApiClientEnvironment
        The environment to use for requests from the client. from .environment import CandidApiClientEnvironment



        Defaults to CandidApiClientEnvironment.PRODUCTION



    client_id : str
    client_secret : str
    _token_getter_override : typing.Optional[typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from candid.client import AsyncCandidApiClient

    client = AsyncCandidApiClient(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: CandidApiClientEnvironment = CandidApiClientEnvironment.PRODUCTION,
        client_id: str,
        client_secret: str,
        _token_getter_override: typing.Optional[typing.Callable[[], str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        oauth_token_provider = OAuthTokenProvider(
            client_id=client_id,
            client_secret=client_secret,
            client_wrapper=SyncClientWrapper(
                base_url=_get_base_url(base_url=base_url, environment=environment),
                httpx_client=httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
                if follow_redirects is not None
                else httpx.Client(timeout=_defaulted_timeout),
                timeout=_defaulted_timeout,
            ),
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=_token_getter_override if _token_getter_override is not None else oauth_token_provider.get_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.billing_notes = AsyncBillingNotesClient(client_wrapper=self._client_wrapper)
        self.contracts = AsyncContractsClient(client_wrapper=self._client_wrapper)
        self.eligibility = AsyncEligibilityClient(client_wrapper=self._client_wrapper)
        self.encounters = AsyncEncountersClient(client_wrapper=self._client_wrapper)
        self.expected_network_status = AsyncExpectedNetworkStatusClient(client_wrapper=self._client_wrapper)
        self.exports = AsyncExportsClient(client_wrapper=self._client_wrapper)
        self.fee_schedules = AsyncFeeSchedulesClient(client_wrapper=self._client_wrapper)
        self.guarantor = AsyncGuarantorClient(client_wrapper=self._client_wrapper)
        self.import_invoice = AsyncImportInvoiceClient(client_wrapper=self._client_wrapper)
        self.insurance_adjudications = AsyncInsuranceAdjudicationsClient(client_wrapper=self._client_wrapper)
        self.insurance_payments = AsyncInsurancePaymentsClient(client_wrapper=self._client_wrapper)
        self.insurance_refunds = AsyncInsuranceRefundsClient(client_wrapper=self._client_wrapper)
        self.organization_service_facilities = AsyncOrganizationServiceFacilitiesClient(
            client_wrapper=self._client_wrapper
        )
        self.organization_providers = AsyncOrganizationProvidersClient(client_wrapper=self._client_wrapper)
        self.patient_payments = AsyncPatientPaymentsClient(client_wrapper=self._client_wrapper)
        self.patient_refunds = AsyncPatientRefundsClient(client_wrapper=self._client_wrapper)
        self.payers = AsyncPayersClient(client_wrapper=self._client_wrapper)
        self.tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        self.write_offs = AsyncWriteOffsClient(client_wrapper=self._client_wrapper)
        self.service_facility = AsyncServiceFacilityClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: CandidApiClientEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
