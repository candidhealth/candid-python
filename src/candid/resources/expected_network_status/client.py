# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawExpectedNetworkStatusClient, RawExpectedNetworkStatusClient
from .resources.v_1.client import AsyncV1Client, V1Client
from .resources.v_2.client import AsyncV2Client, V2Client


class ExpectedNetworkStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExpectedNetworkStatusClient(client_wrapper=client_wrapper)
        self.v_1 = V1Client(client_wrapper=client_wrapper)

        self.v_2 = V2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExpectedNetworkStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExpectedNetworkStatusClient
        """
        return self._raw_client


class AsyncExpectedNetworkStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExpectedNetworkStatusClient(client_wrapper=client_wrapper)
        self.v_1 = AsyncV1Client(client_wrapper=client_wrapper)

        self.v_2 = AsyncV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExpectedNetworkStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExpectedNetworkStatusClient
        """
        return self._raw_client
