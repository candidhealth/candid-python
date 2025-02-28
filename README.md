# Candid Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fcandidhealth%2Fcandid-python)
[![pypi](https://img.shields.io/pypi/v/candidhealth)](https://pypi.python.org/pypi/candidhealth)

The Candid Python library provides convenient access to the Candid API from Python.

## Installation

```sh
pip install candidhealth
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
import datetime

from candid import CandidApiClient
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    MemberInfo,
)
from candid.resources.pre_encounter.resources.eligibility_checks.resources.v_1 import (
    EligibilityRequest,
    Encounter,
    IndividualProvider,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.eligibility_checks.v_1.post(
    request=EligibilityRequest(
        payer_id="string",
        provider=IndividualProvider(
            first_name="string",
            last_name="string",
            npi="string",
        ),
        subscriber=MemberInfo(
            member_id="string",
            first_name="string",
            last_name="string",
            date_of_birth=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        ),
        dependent=MemberInfo(
            member_id="string",
            first_name="string",
            last_name="string",
            date_of_birth=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        ),
        encounter=Encounter(
            date_of_service=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            service_type_codes=["string"],
        ),
    ),
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio
import datetime

from candid import AsyncCandidApiClient
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    MemberInfo,
)
from candid.resources.pre_encounter.resources.eligibility_checks.resources.v_1 import (
    EligibilityRequest,
    Encounter,
    IndividualProvider,
)

client = AsyncCandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main() -> None:
    await client.pre_encounter.eligibility_checks.v_1.post(
        request=EligibilityRequest(
            payer_id="string",
            provider=IndividualProvider(
                first_name="string",
                last_name="string",
                npi="string",
            ),
            subscriber=MemberInfo(
                member_id="string",
                first_name="string",
                last_name="string",
                date_of_birth=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            ),
            dependent=MemberInfo(
                member_id="string",
                first_name="string",
                last_name="string",
                date_of_birth=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            ),
            encounter=Encounter(
                date_of_service=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                service_type_codes=["string"],
            ),
        ),
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from candid.core.api_error import ApiError

try:
    client.pre_encounter.eligibility_checks.v_1.post(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retriable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.pre_encounter.eligibility_checks.v_1.post(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from candid import CandidApiClient

client = CandidApiClient(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.pre_encounter.eligibility_checks.v_1.post(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.
```python
import httpx
from candid import CandidApiClient

client = CandidApiClient(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
