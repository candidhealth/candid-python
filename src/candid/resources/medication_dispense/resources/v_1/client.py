# This file was auto-generated by Fern from our API Definition.

import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ....encounters.resources.v_4.types.encounter import Encounter
from .raw_client import AsyncRawV1Client, RawV1Client
from .types.medication_dispense_create import MedicationDispenseCreate

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV1Client
        """
        return self._raw_client

    def create(
        self, *, request: MedicationDispenseCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> Encounter:
        """
        Parameters
        ----------
        request : MedicationDispenseCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Encounter

        Examples
        --------
        import datetime

        from candid import CandidApiClient
        from candid.resources.commons import ServiceLineUnits
        from candid.resources.medication_dispense.resources.v_1 import (
            MedicationDispenseCreate,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.medication_dispense.v_1.create(
            request=MedicationDispenseCreate(
                medication_dispense_external_id="medication_dispense_external_id",
                patient_external_id="patient_external_id",
                procedure_code="procedure_code",
                quantity="quantity",
                units=ServiceLineUnits.MJ,
                date_of_service=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            ),
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV1Client
        """
        return self._raw_client

    async def create(
        self, *, request: MedicationDispenseCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> Encounter:
        """
        Parameters
        ----------
        request : MedicationDispenseCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Encounter

        Examples
        --------
        import asyncio
        import datetime

        from candid import AsyncCandidApiClient
        from candid.resources.commons import ServiceLineUnits
        from candid.resources.medication_dispense.resources.v_1 import (
            MedicationDispenseCreate,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.medication_dispense.v_1.create(
                request=MedicationDispenseCreate(
                    medication_dispense_external_id="medication_dispense_external_id",
                    patient_external_id="patient_external_id",
                    procedure_code="procedure_code",
                    quantity="quantity",
                    units=ServiceLineUnits.MJ,
                    date_of_service=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data
