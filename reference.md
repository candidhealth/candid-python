# Reference
## Auth V2
<details><summary><code>client.auth.v_2.<a href="src/candid/resources/auth/resources/v_2/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Callout intent="info">
Candid Health SDKs automatically handle authentication workflows after configuring them with the `client_id` and
`client_secret`.
</Callout>

Candid Health utilizes the [OAuth 2.0 bearer token authentication scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) in our auth flow. You obtain the bearer token for all
subsequent API requests via the `/auth/token` endpoint defined below, which requires you to provide your `client_id` and `client_secret`. Your `client_id` and `client_secret` can be [generated](https://support.joincandidhealth.com/hc/en-us/articles/23065219476244--Generating-Candid-API-Keys) from the "Users & Credentials" tab by your org admin.

The bearer token is a signed [JWT](https://jwt.io/). The public key for the JWT can be found [here](https://candidhealth.auth0.com/pem) for any verification workflows.

The bearer token should be provided in the `Authorization` header for all subsequent API calls.

<Callout intent="warning">
The bearer token expires 5 hours after it has been created. After it has expired, the client will receive an "HTTP 401
Unauthorized" error, at which point the client should generate a new token. It is important that tokens be reused between
requests; if the client attempts to generate a token too often, it will be rate-limited and will receive an `HTTP 429 Too Many Requests` error.
</Callout>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.auth.v_2.get_token(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — Your application's Client ID.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — Your application's Client Secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BillingNotes V2
<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.create(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    text="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Empty string not allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.delete(
    billing_note_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**billing_note_id:** `BillingNoteId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.update(
    billing_note_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    text="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**billing_note_id:** `BillingNoteId` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Empty string not allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contracts V2
<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.get(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import State
from candid.client import CandidApiClient
from candid.resources.contracts.v_2 import ContractStatus

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.get_multi(
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    limit=1,
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rendering_provider_ids=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payer_names="string",
    states=State.AA,
    contract_status=ContractStatus.PENDING,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of contracts returned. Defaults to 1000. Max is 1000.
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `typing.Optional[ContractingProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Optional[
    typing.Union[RenderingProviderid, typing.Sequence[RenderingProviderid]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter to contracts that include any of the included payer names.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[State, typing.Sequence[State]]]` 
    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` — The status of the contract. Defaults to `pending`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new contract within the user's current organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import Regions_States
from candid.client import CandidApiClient
from candid.resources.contracts.v_2 import (
    AuthorizedSignatory,
    ContractStatus,
    InsuranceTypes,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.create(
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rendering_provider_ids={
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    },
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    effective_date="string",
    expiration_date="string",
    regions=Regions_States(),
    contract_status=ContractStatus.PENDING,
    authorized_signatory=AuthorizedSignatory(
        first_name="string",
        last_name="string",
        title="string",
        email="string",
        phone="string",
        fax="string",
    ),
    commercial_insurance_types=InsuranceTypes(),
    medicare_insurance_types=InsuranceTypes(),
    medicaid_insurance_types=InsuranceTypes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contracting_provider_id:** `ContractingProviderId` — The UUID of the provider under agreement to the contract
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Set[RenderingProviderid]` 

A rendering provider isn't contracted directly with the payer but can render
services under the contract held by the contracting provider.
Max items is 100.

    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `uuid.UUID` — The UUID of the insurance company under agreement to the contract
    
</dd>
</dl>

<dl>
<dd>

**effective_date:** `Date` — The starting day upon which the contract is effective
    
</dd>
</dl>

<dl>
<dd>

**regions:** `Regions` 

The state(s) to which the contract's coverage extends.
It may also be set to "national" for the entirety of the US.
    
</dd>
</dl>

<dl>
<dd>

**commercial_insurance_types:** `InsuranceTypes` — The commercial plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**medicare_insurance_types:** `InsuranceTypes` — The Medicare plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**medicaid_insurance_types:** `InsuranceTypes` — The Medicaid plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[Date]` — An optional end day upon which the contract expires
    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**authorized_signatory:** `typing.Optional[AuthorizedSignatory]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.delete(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import Regions_States, State
from candid.client import CandidApiClient
from candid.resources.contracts.v_2 import (
    AuthorizedSignatoryUpdate_Set,
    ContractStatus,
    DateUpdate_Set,
    InsuranceTypes,
    RegionsUpdate_Set,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.update(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rendering_provider_ids={
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    },
    effective_date="string",
    expiration_date=DateUpdate_Set(value="string"),
    regions=RegionsUpdate_Set(
        value=Regions_States(
            states=[State.AA],
        )
    ),
    contract_status=ContractStatus.PENDING,
    authorized_signatory=AuthorizedSignatoryUpdate_Set(
        first_name="string",
        last_name="string",
        title="string",
        email="string",
        phone="string",
        fax="string",
    ),
    commercial_insurance_types=InsuranceTypes(),
    medicare_insurance_types=InsuranceTypes(),
    medicaid_insurance_types=InsuranceTypes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Optional[typing.Set[RenderingProviderid]]` 

A rendering provider isn't contracted directly with the payer but can render
services under the contract held by the contracting provider.
Max items is 100.

    
</dd>
</dl>

<dl>
<dd>

**effective_date:** `typing.Optional[Date]` — The starting day upon which the contract is effective
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[DateUpdate]` — An optional end day upon which the contract expires
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[RegionsUpdate]` 

If present, the contract's rendering providers will be patched to this exact
value, overriding what was set before.

    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**authorized_signatory:** `typing.Optional[AuthorizedSignatoryUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**commercial_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**medicare_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**medicaid_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credentialing V2
<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import Regions_States, State
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.create(
    rendering_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    start_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    end_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    regions=Regions_States(
        states=[State.AA],
    ),
    submitted_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    payer_loaded_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rendering_provider_id:** `uuid.UUID` — The ID of the rendering provider covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `uuid.UUID` — The ID of the practice location at which the rendering provider is covered by the credentialing span.

    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `uuid.UUID` — The ID of the payer covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**regions:** `Regions` — The states covered by the credentialing span. A span may be national and cover all states.

    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.date]` — Start date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.date]` — End date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**submitted_date:** `typing.Optional[dt.date]` — Date that the credential paperwork was submitted.
    
</dd>
</dl>

<dl>
<dd>

**payer_loaded_date:** `typing.Optional[dt.date]` — Date that the payer loaded the credentialing span into their system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.get(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.get_all(
    limit=1,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    as_rendering_provider=True,
    as_contracting_provider=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[uuid.UUID]` — Filter by payer.
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `typing.Optional[uuid.UUID]` — Filter to a particular provider. Use in conjunction as_rendering_provider and as_contracting_provider.
    
</dd>
</dl>

<dl>
<dd>

**as_rendering_provider:** `typing.Optional[bool]` — Filter to credentialing spans where the provider is a rendering provider. To use this filter provider_id is required.
    
</dd>
</dl>

<dl>
<dd>

**as_contracting_provider:** `typing.Optional[bool]` — Filter to credentialing spans where the provider is a contracting provider. To use this filter provider_id is required.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft deletes a credentialing span rate from the system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.delete(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import Regions_States, State
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.update(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    start_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    end_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    regions=Regions_States(
        states=[State.AA],
    ),
    submitted_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    payer_loaded_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `typing.Optional[uuid.UUID]` — The ID of the practice location at which the rendering provider is covered by the credentialing span.

    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[uuid.UUID]` — The ID of the payer doing the credentialing.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.date]` — Start date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.date]` — End date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[Regions]` — The states covered by the credentialing span. A span may be national and cover all states.

    
</dd>
</dl>

<dl>
<dd>

**submitted_date:** `typing.Optional[dt.date]` — Date that the credential paperwork was submitted.
    
</dd>
</dl>

<dl>
<dd>

**payer_loaded_date:** `typing.Optional[dt.date]` — Date that the payer loaded the credentialing span into their system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomSchemas V1
<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">get_multi</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all custom schemas.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a custom schema with a given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.get(
    schema_id=uuid.UUID(
        "ec096b13-f80a-471d-aaeb-54b021c9d582",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `SchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create custom schema with a set of typed keys. Schema keys can be referenced as inputs in user-configurable rules in the Rules
Engine, and key-value pairs can be attached to claims via the Encounters API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import Primitive
from candid.client import CandidApiClient
from candid.resources.custom_schemas.v_1 import SchemaField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.create(
    name="General Medicine",
    description="Values associated with a generic visit",
    fields=[
        SchemaField(
            key="provider_category",
            type=Primitive.STRING,
        ),
        SchemaField(
            key="is_urgent_care",
            type=Primitive.BOOLEAN,
        ),
        SchemaField(
            key="bmi",
            type=Primitive.DOUBLE,
        ),
        SchemaField(
            key="age",
            type=Primitive.INTEGER,
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Sequence[SchemaField]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name, description, or keys on a preexisting schema.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import Primitive
from candid.client import CandidApiClient
from candid.resources.custom_schemas.v_1 import SchemaField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.update(
    schema_id=uuid.UUID(
        "ec096b13-f80a-471d-aaeb-54b021c9d582",
    ),
    name="General Medicine and Health",
    description="Values collected during all visits",
    fields_to_add=[
        SchemaField(
            key="visit_type",
            type=Primitive.STRING,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `SchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fields_to_add:** `typing.Optional[typing.Sequence[SchemaField]]` — A list of typed entries to add to schema. Only additive modifications are permitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Eligibility V2
<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API is a wrapper around Change Healthcare's eligibility API. Below are some helpful documentation links:

- [Change Healthcare - Guides: Contents of the Eligibility Request Body](https://developers.changehealthcare.com/eligibilityandclaims/docs/contents-of-the-eligibility-request-body)
- [Change Healthcare - Guides: Use "Bare Minimum" Eligibility Requests](https://developers.changehealthcare.com/eligibilityandclaims/docs/use-bare-minimum-eligibility-requests)
- [Change Healthcare - Guides: Contents of the Eligibility Response](https://developers.changehealthcare.com/eligibilityandclaims/docs/contents-of-the-eligibility-response)
- [Change Healthcare - Guides: Eligibility JSON-to-EDI API Contents](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-json-to-edi-api-contents)
- [Change Healthcare - Guides: Eligibility Error Messages](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-error-messages)
- [Change Healthcare - Guides: FAQ](https://developers.changehealthcare.com/eligibilityandclaims/docs/frequently-asked-questions)
- [Change Healthcare - Guides: Eligibility FAQs](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-api-requests)
- [Change Healthcare - Guides: Sandbox API Values and Test Responses](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-sandbox-api-values-and-test-responses)
- [Change Healthcare - Guides: Sandbox Predefined Fields and Values](https://developers.changehealthcare.com/eligibilityandclaims/docs/sandbox-predefined-fields-and-values)
- [Change Healthcare - Guides: Using Test Payers in the Sandbox](https://developers.changehealthcare.com/eligibilityandclaims/docs/use-the-test-payers-in-the-sandbox-api)

A schema of the response object can be found here: [Change Healthcare Docs](https://developers.changehealthcare.com/eligibilityandclaims/reference/medicaleligibility)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check_availity</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Availity has transitioned their GET endpoint to a POST endpoint. Candid has updated their pass-through integration to enable backwards compatibility for the GET endpoint so that customers do not have to immediately update their integrations.**

**Candid recommends integrations with the [POST endpoint](https://docs.joincandidhealth.com/api-reference/eligibility/v-2/submit-eligibility-check-availity-post) to ensure the best possible integration experience. Given the transition, Availity’s documentation will be out of sync with this endpoint.**

If you'd like access to this endpoint, please reach out to support@joincandidhealth.com with the subject line "Action: Activate Availity Eligibility API Endpoint

This API is a wrapper around Availity's coverages API. Below are some helpful documentation links:

- [Availity - Coverages 1.0.0 API](https://developer.availity.com/partner/documentation#c_coverages_references)
- [Candid Availity Eligibility Integration Guide](https://support.joincandidhealth.com/hc/en-us/articles/24218441631892--Availity-Eligibility-Integration-Guide)

A schema of the response object can be found here: [Availity Docs](https://developer.availity.com/partner/product/191210/api/190898#/Coverages_100/operation/%2Fcoverages%2F{id}/get)

- Note Availity requires a free developer account to access this documentation.

Check connection status of Availity API and partners here:

- [Availity Trading Partner Connection Status](https://www.availity.com/status/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check_availity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check_availity_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If you'd like access to this endpoint, please reach out to support@joincandidhealth.com with the subject line "Action: Activate Availity Eligibility API Endpoint

This API is a wrapper around Availity's coverages API. Below are some helpful documentation links:

- [Availity - Coverages 1.0.0 API](https://developer.availity.com/partner/documentation#c_coverages_references)
- [Candid Availity Eligibility Integration Guide](https://support.joincandidhealth.com/hc/en-us/articles/24218441631892--Availity-Eligibility-Integration-Guide)

A schema of the response object can be found here: [Availity Docs](https://developer.availity.com/partner/product/191210/api/190898#/Coverages_100/operation/%2Fcoverages%2F{id}/get)

- Note Availity requires a free developer account to access this documentation.

Check connection status of Availity API and partners here:

- [Availity Trading Partner Connection Status](https://www.availity.com/status/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check_availity_post(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EncounterProviders V2
<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import ReferringProviderUpdate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ReferringProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReferringProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import QualifierCode, State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import (
    InitialReferringProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=InitialReferringProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        qualifier=QualifierCode.DQ,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `InitialReferringProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import SupervisingProviderUpdate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=SupervisingProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SupervisingProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import OrderingProviderUpdate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=OrderingProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrderingProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import ReferringProvider

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReferringProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import QualifierCode, State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import InitialReferringProvider

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=InitialReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        qualifier=QualifierCode.DQ,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `InitialReferringProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import SupervisingProvider

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=SupervisingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SupervisingProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import OrderingProvider

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=OrderingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrderingProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Encounters V4
<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import ClaimStatus
from candid.client import CandidApiClient
from candid.resources.encounters.v_4 import EncounterSortOptions

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.get_all(
    limit=100,
    claim_status=ClaimStatus.BILLER_RECEIVED,
    sort=EncounterSortOptions.CREATED_AT_ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    date_of_service_min=datetime.date.fromisoformat(
        "2019-08-24",
    ),
    date_of_service_max=datetime.date.fromisoformat(
        "2019-08-25",
    ),
    primary_payer_names="Medicare,Medicaid",
    search_term="doe",
    external_id="123456",
    diagnoses_updated_since=datetime.datetime.fromisoformat(
        "2019-08-24 14:15:22+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**claim_status:** `typing.Optional[ClaimStatus]` — Indicates the current status of an insurance claim within the billing process.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[EncounterSortOptions]` — Defaults to created_at:desc.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` — Date formatted as YYYY-MM-DD; eg: 2019-08-25.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` — Date formatted as YYYY-MM-DD; eg: 2019-08-25.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_names:** `typing.Optional[str]` — Comma delimited string.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` 

Filter by any of the following fields: encounter_id, claim_id, patient external_id,
patient date of birth, patient first name, patient last name,
or encounter external id.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[EncounterExternalId]` — Filter to an exact match on encounter external_id, if one exists.
    
</dd>
</dl>

<dl>
<dd>

**diagnoses_updated_since:** `typing.Optional[dt.datetime]` — ISO 8601 timestamp; ideally in UTC (although not required): 2019-08-24T14:15:22Z.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[TagId, typing.Sequence[TagId]]]` — Filter by name of tags on encounters.
    
</dd>
</dl>

<dl>
<dd>

**work_queue_id:** `typing.Optional[WorkQueueId]` 
    
</dd>
</dl>

<dl>
<dd>

**billable_status:** `typing.Optional[BillableStatusType]` — Defines if the Encounter is to be billed by Candid to the responsible_party. Examples for when this should be set to NOT_BILLABLE include if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.
    
</dd>
</dl>

<dl>
<dd>

**responsible_party:** `typing.Optional[ResponsiblePartyType]` — Defines the party to be billed with the initial balance owed on the claim. Use SELF_PAY if you intend to bill self pay/cash pay.
    
</dd>
</dl>

<dl>
<dd>

**owner_of_next_action:** `typing.Optional[EncounterOwnerOfNextActionType]` — The party who is responsible for taking the next action on an Encounter, as defined by ownership of open Tasks.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.get(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    ClaimSubmissionPayerResponsibilityType,
    DelayReasonCode,
    DiagnosisCreate,
    DiagnosisTypeCode,
    EmrPayerCrosswalk,
    EncounterServiceFacilityBase,
    FacilityTypeCode,
    Gender,
    InsuranceTypeCode,
    IntendedSubmissionMedium,
    PatientCreate,
    PatientNonInsurancePayerInfoCreate,
    PatientRelationshipToInsuredCodeAll,
    PhoneNumber,
    PhoneNumberType,
    ProcedureModifier,
    QualifierCode,
    ServiceLineUnits,
    SourceOfPaymentCode,
    State,
    StreetAddressLongZip,
    StreetAddressShortZip,
    SubscriberCreate,
)
from candid.client import CandidApiClient
from candid.resources.billing_notes.v_2 import BillingNoteBase
from candid.resources.claim_submission.v_1 import (
    ClaimFrequencyTypeCode,
    ClaimSubmissionRecordCreate,
    ExternalClaimSubmissionCreate,
)
from candid.resources.custom_schemas.v_1 import SchemaInstance
from candid.resources.encounter_providers.v_2 import (
    BillingProvider,
    InitialReferringProvider,
    OrderingProvider,
    ReferringProvider,
    RenderingProvider,
    SupervisingProvider,
)
from candid.resources.encounters.v_4 import (
    BillableStatusType,
    ClinicalNote,
    ClinicalNoteCategoryCreate,
    IntakeFollowUp,
    IntakeQuestion,
    IntakeResponseAndFollowUps,
    Intervention,
    InterventionCategory,
    Lab,
    LabCodeType,
    Medication,
    NoteCategory,
    PatientHistoryCategory,
    PatientHistoryCategoryEnum,
    ResponsiblePartyType,
    ServiceAuthorizationExceptionCode,
    SynchronicityType,
    Vitals,
)
from candid.resources.guarantor.v_1 import GuarantorCreate
from candid.resources.insurance_cards.v_2 import InsuranceCardCreate
from candid.resources.service_lines.v_2 import (
    DrugIdentification,
    MeasurementUnitCode,
    ServiceIdQualifier,
    ServiceLineCreate,
    TestResult,
    TestResultType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.create(
    patient=PatientCreate(
        phone_numbers=[
            PhoneNumber(
                number="1234567890",
                type=PhoneNumberType.HOME,
            )
        ],
        phone_consent=True,
        email="johndoe@joincandidhealth.com",
        non_insurance_payers=[
            uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            )
        ],
        non_insurance_payers_info=[
            PatientNonInsurancePayerInfoCreate(
                non_insurance_payer_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                member_id="string",
            )
        ],
        email_consent=True,
        external_id="string",
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        gender=Gender.MALE,
    ),
    billing_provider=BillingProvider(
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        tax_id="string",
        npi="string",
        taxonomy_code="string",
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    rendering_provider=RenderingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    referring_provider=ReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    initial_referring_provider=InitialReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        qualifier=QualifierCode.DQ,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    supervising_provider=SupervisingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    service_facility=EncounterServiceFacilityBase(
        organization_name="string",
        npi="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
    subscriber_primary=SubscriberCreate(
        insurance_card=InsuranceCardCreate(
            member_id="string",
            payer_name="string",
            payer_id="string",
            rx_bin="string",
            rx_pcn="string",
            image_url_front="string",
            image_url_back="string",
            emr_payer_crosswalk=EmrPayerCrosswalk.HEALTHIE,
            group_number="string",
            plan_name="string",
            plan_type=SourceOfPaymentCode.SELF_PAY,
            insurance_type=InsuranceTypeCode.C_01,
        ),
        patient_relationship_to_subscriber_code=PatientRelationshipToInsuredCodeAll.SPOUSE,
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        gender=Gender.MALE,
    ),
    subscriber_secondary=SubscriberCreate(
        insurance_card=InsuranceCardCreate(
            member_id="string",
            payer_name="string",
            payer_id="string",
            rx_bin="string",
            rx_pcn="string",
            image_url_front="string",
            image_url_back="string",
            emr_payer_crosswalk=EmrPayerCrosswalk.HEALTHIE,
            group_number="string",
            plan_name="string",
            plan_type=SourceOfPaymentCode.SELF_PAY,
            insurance_type=InsuranceTypeCode.C_01,
        ),
        patient_relationship_to_subscriber_code=PatientRelationshipToInsuredCodeAll.SPOUSE,
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        gender=Gender.MALE,
    ),
    prior_authorization_number="string",
    responsible_party=ResponsiblePartyType.INSURANCE_PAY,
    diagnoses=[
        DiagnosisCreate(
            name="string",
            code_type=DiagnosisTypeCode.ABF,
            code="string",
        )
    ],
    clinical_notes=[
        ClinicalNoteCategoryCreate(
            category=NoteCategory.CLINICAL,
            notes=[
                ClinicalNote(
                    text="string",
                    author_name="string",
                    author_npi="string",
                    timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                )
            ],
        )
    ],
    billing_notes=[
        BillingNoteBase(
            text="string",
        )
    ],
    place_of_service_code=FacilityTypeCode.PHARMACY,
    patient_histories=[
        PatientHistoryCategory(
            category=PatientHistoryCategoryEnum.PRESENT_ILLNESS,
            questions=[
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
            ],
        )
    ],
    service_lines=[
        ServiceLineCreate(
            modifiers=[ProcedureModifier.TWENTY_TWO],
            procedure_code="string",
            quantity="string",
            units=ServiceLineUnits.MJ,
            charge_amount_cents=1,
            diagnosis_pointers=[1],
            drug_identification=DrugIdentification(
                service_id_qualifier=ServiceIdQualifier.EAN_UCC_13,
                national_drug_code="string",
                national_drug_unit_count="string",
                measurement_unit_code=MeasurementUnitCode.MILLILITERS,
                link_sequence_number="string",
                pharmacy_prescription_number="string",
                conversion_formula="string",
                drug_description="string",
            ),
            place_of_service_code=FacilityTypeCode.PHARMACY,
            description="string",
            date_of_service=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            end_date_of_service=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            ordering_provider=OrderingProvider(
                npi="string",
                taxonomy_code="string",
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
                first_name="string",
                last_name="string",
                organization_name="string",
            ),
            test_results=[
                TestResult(
                    value=1.1,
                    result_type=TestResultType.HEMATOCRIT,
                )
            ],
        )
    ],
    guarantor=GuarantorCreate(
        phone_numbers=[
            PhoneNumber(
                number="1234567890",
                type=PhoneNumberType.HOME,
            )
        ],
        phone_consent=True,
        email="johndoe@joincandidhealth.com",
        email_consent=True,
        first_name="string",
        last_name="string",
        external_id="string",
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
    external_claim_submission=ExternalClaimSubmissionCreate(
        claim_created_at=datetime.datetime.fromisoformat(
            "2023-01-01 12:00:00+00:00",
        ),
        patient_control_number="PATIENT_CONTROL_NUMBER",
        submission_records=[
            ClaimSubmissionRecordCreate(
                submitted_at=datetime.datetime.fromisoformat(
                    "2023-01-01 13:00:00+00:00",
                ),
                claim_frequency_code=ClaimFrequencyTypeCode.ORIGINAL,
                payer_responsibility=ClaimSubmissionPayerResponsibilityType.PRIMARY,
                intended_submission_medium=IntendedSubmissionMedium.ELECTRONIC,
            ),
            ClaimSubmissionRecordCreate(
                submitted_at=datetime.datetime.fromisoformat(
                    "2023-01-04 12:00:00+00:00",
                ),
                claim_frequency_code=ClaimFrequencyTypeCode.REPLACEMENT,
                payer_responsibility=ClaimSubmissionPayerResponsibilityType.PRIMARY,
                intended_submission_medium=IntendedSubmissionMedium.PAPER,
            ),
        ],
    ),
    tag_ids=["string"],
    schema_instances=[
        SchemaInstance(
            schema_id=uuid.UUID(
                "ec096b13-f80a-471d-aaeb-54b021c9d582",
            ),
            content={
                "provider_category": "internist",
                "is_urgent_care": true,
                "bmi": 24.2,
                "age": 38,
            },
        )
    ],
    referral_number="string",
    external_id="string",
    date_of_service=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    end_date_of_service=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    patient_authorized_release=True,
    benefits_assigned_to_provider=True,
    provider_accepts_assignment=True,
    appointment_type="string",
    existing_medications=[
        Medication(
            name="Lisinopril",
            rx_cui="860975",
            dosage="10mg",
            dosage_form="Tablet",
            frequency="Once Daily",
            as_needed=True,
        )
    ],
    vitals=Vitals(
        height_in=70,
        weight_lbs=165,
        blood_pressure_systolic_mmhg=115,
        blood_pressure_diastolic_mmhg=85,
        body_temperature_f=98.0,
        hemoglobin_gdl=15.1,
        hematocrit_pct=51.2,
    ),
    interventions=[
        Intervention(
            name="Physical Therapy Session",
            category=InterventionCategory.LIFESTYLE,
            description="A session focused on improving muscular strength, flexibility, and range of motion post-injury.",
            medication=Medication(
                name="Lisinopril",
                rx_cui="860975",
                dosage="10mg",
                dosage_form="Tablet",
                frequency="Once Daily",
                as_needed=True,
            ),
            labs=[
                Lab(
                    name="Genetic Health Labs",
                    code="GH12345",
                    code_type=LabCodeType.QUEST,
                )
            ],
        )
    ],
    pay_to_address=StreetAddressLongZip(
        address_1="123 Main St",
        address_2="Apt 1",
        city="New York",
        state=State.NY,
        zip_code="10001",
        zip_plus_four_code="1234",
    ),
    synchronicity=SynchronicityType.SYNCHRONOUS,
    billable_status=BillableStatusType.BILLABLE,
    additional_information="string",
    service_authorization_exception_code=ServiceAuthorizationExceptionCode.C_1,
    admission_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    discharge_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    onset_of_current_illness_or_symptom_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    last_menstrual_period_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    delay_reason_code=DelayReasonCode.C_1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient:** `PatientCreate` — Contains the identification information of the individual receiving medical services.

    
</dd>
</dl>

<dl>
<dd>

**billing_provider:** `BillingProvider` — The billing provider is the provider or business entity submitting the claim. Billing provider may be, but is not necessarily, the same person/NPI as the rendering provider. From a payer's perspective, this represents the person or entity being reimbursed. When a contract exists with the target payer, the billing provider should be the entity contracted with the payer. In some circumstances, this will be an individual provider. In that case, submit that provider's NPI and the tax ID (TIN) that the provider gave to the payer during contracting. In other cases, the billing entity will be a medical group. If so, submit the group NPI and the group's tax ID. Box 33 on the CMS-1500 claim form.

    
</dd>
</dl>

<dl>
<dd>

**rendering_provider:** `RenderingProvider` 

The rendering provider is the practitioner -- physician, nurse practitioner, etc. -- performing the service.
For telehealth services, the rendering provider performs the visit, asynchronous communication, or other service. The rendering provider address should generally be the same as the service facility address.

    
</dd>
</dl>

<dl>
<dd>

**responsible_party:** `ResponsiblePartyType` — Defines the party to be billed with the initial balance owed on the claim.

    
</dd>
</dl>

<dl>
<dd>

**diagnoses:** `typing.Sequence[DiagnosisCreate]` 

Ideally, this field should contain no more than 12 diagnoses. However, more diagnoses
may be submitted at this time, and coders will later prioritize the 12 that will be
submitted to the payor.

    
</dd>
</dl>

<dl>
<dd>

**place_of_service_code:** `FacilityTypeCode` — Box 24B on the CMS-1500 claim form. 837p Loop2300, CLM-05-1. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).

    
</dd>
</dl>

<dl>
<dd>

**external_id:** `EncounterExternalId` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**patient_authorized_release:** `bool` 

Whether this patient has authorized the release of medical information
for billing purpose.
Box 12 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**benefits_assigned_to_provider:** `bool` 

Whether this patient has authorized insurance payments to be made to you,
not them. If false, patient may receive reimbursement.
Box 13 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**provider_accepts_assignment:** `bool` 

Whether you have accepted the patient's authorization for insurance payments
to be made to you, not them.
Box 27 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**billable_status:** `BillableStatusType` 

Defines if the Encounter is to be billed by Candid to the responsible_party.
Examples for when this should be set to NOT_BILLABLE include
if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.
    
</dd>
</dl>

<dl>
<dd>

**referring_provider:** `typing.Optional[ReferringProvider]` 

The final provider who referred the services that were rendered.
All physicians who order services or refer Medicare beneficiaries must
report this data.

    
</dd>
</dl>

<dl>
<dd>

**initial_referring_provider:** `typing.Optional[InitialReferringProvider]` 

The second iteration of Loop ID-2310. Use code "P3 - Primary Care Provider" in this loop to
indicate the initial referral from the primary care provider or whatever provider wrote the initial referral for this patient's episode of care being billed/reported in this transaction.

    
</dd>
</dl>

<dl>
<dd>

**supervising_provider:** `typing.Optional[SupervisingProvider]` — Required when the rendering provider is supervised by a physician. If not required by this implementation guide, do not send.

    
</dd>
</dl>

<dl>
<dd>

**service_facility:** `typing.Optional[EncounterServiceFacilityBase]` — Encounter Service facility is typically the location a medical service was rendered, such as a provider office or hospital. For telehealth, service facility can represent the provider's location when the service was delivered (e.g., home), or the location where an in-person visit would have taken place, whichever is easier to identify. If the provider is in-network, service facility may be defined in payer contracts. Box 32 on the CMS-1500 claim form. Note that for an in-network claim to be successfully adjudicated, the service facility address listed on claims must match what was provided to the payer during the credentialing process.

    
</dd>
</dl>

<dl>
<dd>

**subscriber_primary:** `typing.Optional[SubscriberCreate]` 

Subscriber_primary is required when responsible_party is INSURANCE_PAY (i.e. when the claim should be billed to insurance).
These are not required fields when responsible_party is SELF_PAY (i.e. when the claim should be billed to the patient).
However, if you collect this for patients, even self-pay, we recommend including it when sending encounters to Candid.
Note: Cash Pay is no longer a valid payer_id in v4, please use responsible party to define self-pay claims.

    
</dd>
</dl>

<dl>
<dd>

**subscriber_secondary:** `typing.Optional[SubscriberCreate]` — Please always include this when you have it, even for self-pay claims.

    
</dd>
</dl>

<dl>
<dd>

**prior_authorization_number:** `typing.Optional[PriorAuthorizationNumber]` — Box 23 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**clinical_notes:** `typing.Optional[typing.Sequence[ClinicalNoteCategoryCreate]]` — Holds a collection of clinical observations made by healthcare providers during patient encounters.
    
</dd>
</dl>

<dl>
<dd>

**billing_notes:** `typing.Optional[typing.Sequence[BillingNoteBase]]` 

Spot to store misc, human-readable, notes about this encounter to be used
in the billing process.

    
</dd>
</dl>

<dl>
<dd>

**patient_histories:** `typing.Optional[typing.Sequence[PatientHistoryCategory]]` 
    
</dd>
</dl>

<dl>
<dd>

**service_lines:** `typing.Optional[typing.Sequence[ServiceLineCreate]]` 

Each service line must be linked to a diagnosis. Concretely,
`service_line.diagnosis_pointers`must contain at least one entry which should be
in bounds of the diagnoses list field.

    
</dd>
</dl>

<dl>
<dd>

**guarantor:** `typing.Optional[GuarantorCreate]` — Personal and contact info for the guarantor of the patient responsibility.

    
</dd>
</dl>

<dl>
<dd>

**external_claim_submission:** `typing.Optional[ExternalClaimSubmissionCreate]` 

***This field is in beta.***
To be included for claims that have been submitted outside of Candid.
Candid supports posting remits and payments to these claims and working them in-platform (e.g. editing, resubmitting).

    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[TagId]]` — Names of tags that should be on the encounter.
    
</dd>
</dl>

<dl>
<dd>

**schema_instances:** `typing.Optional[typing.Sequence[SchemaInstance]]` 

Key-value pairs that must adhere to a schema created via the Custom Schema API. Multiple schema
instances cannot be created for the same schema on an encounter.

    
</dd>
</dl>

<dl>
<dd>

**referral_number:** `typing.Optional[str]` — Refers to REF*9F on the 837p. Value cannot be greater than 50 characters.

    
</dd>
</dl>

<dl>
<dd>

**date_of_service:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
Box 24a on the CMS-1500 claim form.
If service occurred over a range of dates, this should be the start date.
date_of_service must be defined on either the encounter or the service lines but not both.
If there are greater than zero service lines, it is recommended to specify date_of_service on the service_line instead of on the encounter to prepare for future API versions.
    
</dd>
</dl>

<dl>
<dd>

**end_date_of_service:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-25.
This date must be the local date in the timezone where the service occurred.
If omitted, the Encounter is assumed to be for a single day.
Must not be temporally before the date_of_service field.
If there are greater than zero service lines, it is recommended to specify end_date_of_service on the service_line instead of on the encounter to prepare for future API versions.
    
</dd>
</dl>

<dl>
<dd>

**appointment_type:** `typing.Optional[str]` — Human-readable description of the appointment type (ex: "Acupuncture - Headaches").
    
</dd>
</dl>

<dl>
<dd>

**existing_medications:** `typing.Optional[typing.Sequence[Medication]]` 
    
</dd>
</dl>

<dl>
<dd>

**vitals:** `typing.Optional[Vitals]` 
    
</dd>
</dl>

<dl>
<dd>

**interventions:** `typing.Optional[typing.Sequence[Intervention]]` 
    
</dd>
</dl>

<dl>
<dd>

**pay_to_address:** `typing.Optional[StreetAddressLongZip]` — Specifies the address to which payments for the claim should be sent.
    
</dd>
</dl>

<dl>
<dd>

**synchronicity:** `typing.Optional[SynchronicityType]` 

Whether or not this was a synchronous or asynchronous encounter.
Asynchronous encounters occur when providers and patients communicate online using
forms, instant messaging, or other pre-recorded digital mediums.
Synchronous encounters occur in live, real-time settings where the patient interacts
directly with the provider, such as over video or a phone call.
    
</dd>
</dl>

<dl>
<dd>

**additional_information:** `typing.Optional[str]` 

Defines additional information on the claim needed by the payer.
Box 19 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**service_authorization_exception_code:** `typing.Optional[ServiceAuthorizationExceptionCode]` 

837p Loop2300 REF\*4N
Required when mandated by government law or regulation to obtain authorization for specific service(s) but, for the
reasons listed in one of the enum values of ServiceAuthorizationExceptionCode, the service was performed without
obtaining the authorization.
    
</dd>
</dl>

<dl>
<dd>

**admission_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP\*435, CMS-1500 Box 18
Required on all ambulance claims when the patient was known to be admitted to the hospital.
OR
Required on all claims involving inpatient medical visits.
    
</dd>
</dl>

<dl>
<dd>

**discharge_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP\*096, CMS-1500 Box 18
Required for inpatient claims when the patient was discharged from the facility and the discharge date is known.
    
</dd>
</dl>

<dl>
<dd>

**onset_of_current_illness_or_symptom_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP\*431, CMS-1500 Box 14
Required for the initial medical service or visit performed in response to a medical emergency when the date is available and is different than the date of service.
OR
This date is the onset of acute symptoms for the current illness or condition.
    
</dd>
</dl>

<dl>
<dd>

**last_menstrual_period_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP\*484, CMS-1500 Box 14
Required when, in the judgment of the provider, the services on this claim are related to the patient's pregnancy.
    
</dd>
</dl>

<dl>
<dd>

**delay_reason_code:** `typing.Optional[DelayReasonCode]` 

837i Loop2300, CLM-1300 Box 20
Code indicating the reason why a request was delayed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">create_from_pre_encounter_patient</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an encounter from a pre-encounter patient and appointment. This endpoint is intended to be used by consumers who are managing
patients and appointments in the pre-encounter service and is currently under development. Consumers who are not taking advantage
of the pre-encounter service should use the standard create endpoint.

The endpoint will create an encounter from the provided fields, pulling information from the provided patient and appointment objects
where applicable. In particular, the following fields are populated from the patient and appointment objects:

- Patient
- Referring Provider
- Subscriber Primary
- Subscriber Secondary
- Referral Number
- Responsible Party
- Guarantor

Utilizing this endpoint opts you into automatic updating of the encounter when the patient or appointment is updated, assuming the
encounter has not already been submitted or adjudicated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    ClaimSubmissionPayerResponsibilityType,
    DelayReasonCode,
    DiagnosisCreate,
    DiagnosisTypeCode,
    EncounterServiceFacilityBase,
    FacilityTypeCode,
    IntendedSubmissionMedium,
    ProcedureModifier,
    QualifierCode,
    ServiceLineUnits,
    State,
    StreetAddressLongZip,
)
from candid.client import CandidApiClient
from candid.resources.billing_notes.v_2 import BillingNoteBase
from candid.resources.claim_submission.v_1 import (
    ClaimFrequencyTypeCode,
    ClaimSubmissionRecordCreate,
    ExternalClaimSubmissionCreate,
)
from candid.resources.custom_schemas.v_1 import SchemaInstance
from candid.resources.encounter_providers.v_2 import (
    BillingProvider,
    InitialReferringProvider,
    OrderingProvider,
    RenderingProvider,
    SupervisingProvider,
)
from candid.resources.encounters.v_4 import (
    BillableStatusType,
    ClinicalNote,
    ClinicalNoteCategoryCreate,
    IntakeFollowUp,
    IntakeQuestion,
    IntakeResponseAndFollowUps,
    Intervention,
    InterventionCategory,
    Lab,
    LabCodeType,
    Medication,
    NoteCategory,
    PatientHistoryCategory,
    PatientHistoryCategoryEnum,
    ServiceAuthorizationExceptionCode,
    SynchronicityType,
    Vitals,
)
from candid.resources.service_lines.v_2 import (
    DrugIdentification,
    MeasurementUnitCode,
    ServiceIdQualifier,
    ServiceLineCreate,
    TestResult,
    TestResultType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.create_from_pre_encounter_patient(
    pre_encounter_patient_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    pre_encounter_appointment_ids=[
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ],
    billing_provider=BillingProvider(
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        tax_id="string",
        npi="string",
        taxonomy_code="string",
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    rendering_provider=RenderingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    initial_referring_provider=InitialReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        qualifier=QualifierCode.DQ,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    supervising_provider=SupervisingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    service_facility=EncounterServiceFacilityBase(
        organization_name="string",
        npi="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
    diagnoses=[
        DiagnosisCreate(
            name="string",
            code_type=DiagnosisTypeCode.ABF,
            code="string",
        )
    ],
    clinical_notes=[
        ClinicalNoteCategoryCreate(
            category=NoteCategory.CLINICAL,
            notes=[
                ClinicalNote(
                    text="string",
                    author_name="string",
                    author_npi="string",
                    timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                )
            ],
        )
    ],
    billing_notes=[
        BillingNoteBase(
            text="string",
        )
    ],
    place_of_service_code=FacilityTypeCode.PHARMACY,
    patient_histories=[
        PatientHistoryCategory(
            category=PatientHistoryCategoryEnum.PRESENT_ILLNESS,
            questions=[
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
            ],
        )
    ],
    service_lines=[
        ServiceLineCreate(
            modifiers=[ProcedureModifier.TWENTY_TWO],
            procedure_code="string",
            quantity="string",
            units=ServiceLineUnits.MJ,
            charge_amount_cents=1,
            diagnosis_pointers=[1],
            drug_identification=DrugIdentification(
                service_id_qualifier=ServiceIdQualifier.EAN_UCC_13,
                national_drug_code="string",
                national_drug_unit_count="string",
                measurement_unit_code=MeasurementUnitCode.MILLILITERS,
                link_sequence_number="string",
                pharmacy_prescription_number="string",
                conversion_formula="string",
                drug_description="string",
            ),
            place_of_service_code=FacilityTypeCode.PHARMACY,
            description="string",
            date_of_service=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            end_date_of_service=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            ordering_provider=OrderingProvider(
                npi="string",
                taxonomy_code="string",
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
                first_name="string",
                last_name="string",
                organization_name="string",
            ),
            test_results=[
                TestResult(
                    value=1.1,
                    result_type=TestResultType.HEMATOCRIT,
                )
            ],
        )
    ],
    external_claim_submission=ExternalClaimSubmissionCreate(
        claim_created_at=datetime.datetime.fromisoformat(
            "2023-01-01 12:00:00+00:00",
        ),
        patient_control_number="PATIENT_CONTROL_NUMBER",
        submission_records=[
            ClaimSubmissionRecordCreate(
                submitted_at=datetime.datetime.fromisoformat(
                    "2023-01-01 13:00:00+00:00",
                ),
                claim_frequency_code=ClaimFrequencyTypeCode.ORIGINAL,
                payer_responsibility=ClaimSubmissionPayerResponsibilityType.PRIMARY,
                intended_submission_medium=IntendedSubmissionMedium.ELECTRONIC,
            ),
            ClaimSubmissionRecordCreate(
                submitted_at=datetime.datetime.fromisoformat(
                    "2023-01-04 12:00:00+00:00",
                ),
                claim_frequency_code=ClaimFrequencyTypeCode.REPLACEMENT,
                payer_responsibility=ClaimSubmissionPayerResponsibilityType.PRIMARY,
                intended_submission_medium=IntendedSubmissionMedium.PAPER,
            ),
        ],
    ),
    tag_ids=["string"],
    schema_instances=[
        SchemaInstance(
            schema_id=uuid.UUID(
                "ec096b13-f80a-471d-aaeb-54b021c9d582",
            ),
            content={
                "provider_category": "internist",
                "is_urgent_care": true,
                "bmi": 24.2,
                "age": 38,
            },
        )
    ],
    external_id="string",
    date_of_service=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    end_date_of_service=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    patient_authorized_release=True,
    benefits_assigned_to_provider=True,
    provider_accepts_assignment=True,
    appointment_type="string",
    existing_medications=[
        Medication(
            name="Lisinopril",
            rx_cui="860975",
            dosage="10mg",
            dosage_form="Tablet",
            frequency="Once Daily",
            as_needed=True,
        )
    ],
    vitals=Vitals(
        height_in=70,
        weight_lbs=165,
        blood_pressure_systolic_mmhg=115,
        blood_pressure_diastolic_mmhg=85,
        body_temperature_f=98.0,
        hemoglobin_gdl=15.1,
        hematocrit_pct=51.2,
    ),
    interventions=[
        Intervention(
            name="Physical Therapy Session",
            category=InterventionCategory.LIFESTYLE,
            description="A session focused on improving muscular strength, flexibility, and range of motion post-injury.",
            medication=Medication(
                name="Lisinopril",
                rx_cui="860975",
                dosage="10mg",
                dosage_form="Tablet",
                frequency="Once Daily",
                as_needed=True,
            ),
            labs=[
                Lab(
                    name="Genetic Health Labs",
                    code="GH12345",
                    code_type=LabCodeType.QUEST,
                )
            ],
        )
    ],
    pay_to_address=StreetAddressLongZip(
        address_1="123 Main St",
        address_2="Apt 1",
        city="New York",
        state=State.NY,
        zip_code="10001",
        zip_plus_four_code="1234",
    ),
    synchronicity=SynchronicityType.SYNCHRONOUS,
    billable_status=BillableStatusType.BILLABLE,
    additional_information="string",
    service_authorization_exception_code=ServiceAuthorizationExceptionCode.C_1,
    admission_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    discharge_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    onset_of_current_illness_or_symptom_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    last_menstrual_period_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    delay_reason_code=DelayReasonCode.C_1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pre_encounter_patient_id:** `PreEncounterPatientId` 
    
</dd>
</dl>

<dl>
<dd>

**pre_encounter_appointment_ids:** `typing.Sequence[PreEncounterAppointmentId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider:** `BillingProvider` — The billing provider is the provider or business entity submitting the claim. Billing provider may be, but is not necessarily, the same person/NPI as the rendering provider. From a payer's perspective, this represents the person or entity being reimbursed. When a contract exists with the target payer, the billing provider should be the entity contracted with the payer. In some circumstances, this will be an individual provider. In that case, submit that provider's NPI and the tax ID (TIN) that the provider gave to the payer during contracting. In other cases, the billing entity will be a medical group. If so, submit the group NPI and the group's tax ID. Box 33 on the CMS-1500 claim form.

    
</dd>
</dl>

<dl>
<dd>

**rendering_provider:** `RenderingProvider` 

The rendering provider is the practitioner -- physician, nurse practitioner, etc. -- performing the service.
For telehealth services, the rendering provider performs the visit, asynchronous communication, or other service. The rendering provider address should generally be the same as the service facility address.

    
</dd>
</dl>

<dl>
<dd>

**diagnoses:** `typing.Sequence[DiagnosisCreate]` 

Ideally, this field should contain no more than 12 diagnoses. However, more diagnoses
may be submitted at this time, and coders will later prioritize the 12 that will be
submitted to the payor.

    
</dd>
</dl>

<dl>
<dd>

**place_of_service_code:** `FacilityTypeCode` — Box 24B on the CMS-1500 claim form. 837p Loop2300, CLM-05-1. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms .gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).

    
</dd>
</dl>

<dl>
<dd>

**external_id:** `EncounterExternalId` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**patient_authorized_release:** `bool` 

Whether this patient has authorized the release of medical information
for billing purpose.
Box 12 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**benefits_assigned_to_provider:** `bool` 

Whether this patient has authorized insurance payments to be made to you,
not them. If false, patient may receive reimbursement.
Box 13 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**provider_accepts_assignment:** `bool` 

Whether you have accepted the patient's authorization for insurance payments
to be made to you, not them.
Box 27 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**billable_status:** `BillableStatusType` 

Defines if the Encounter is to be billed by Candid to the responsible_party.
Examples for when this should be set to NOT_BILLABLE include
if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.
    
</dd>
</dl>

<dl>
<dd>

**initial_referring_provider:** `typing.Optional[InitialReferringProvider]` 

The second iteration of Loop ID-2310. Use code "P3 - Primary Care Provider" in this loop to
indicate the initial referral from the primary care provider or whatever provider wrote the initial referral for this patient's episode of care being billed/reported in this transaction.

    
</dd>
</dl>

<dl>
<dd>

**supervising_provider:** `typing.Optional[SupervisingProvider]` — Required when the rendering provider is supervised by a physician. If not required by this implementation guide, do not send.

    
</dd>
</dl>

<dl>
<dd>

**service_facility:** `typing.Optional[EncounterServiceFacilityBase]` — Encounter Service facility is typically the location a medical service was rendered, such as a provider office or hospital. For telehealth, service facility can represent the provider's location when the service was delivered (e.g., home), or the location where an in-person visit would have taken place, whichever is easier to identify. If the provider is in-network, service facility may be defined in payer contracts. Box 32 on the CMS-1500 claim form. Note that for an in-network claim to be successfully adjudicated, the service facility address listed on claims must match what was provided to the payer during the credentialing process.

    
</dd>
</dl>

<dl>
<dd>

**clinical_notes:** `typing.Optional[typing.Sequence[ClinicalNoteCategoryCreate]]` — Holds a collection of clinical observations made by healthcare providers during patient encounters.
    
</dd>
</dl>

<dl>
<dd>

**billing_notes:** `typing.Optional[typing.Sequence[BillingNoteBase]]` 

Spot to store misc, human-readable, notes about this encounter to be used
in the billing process.

    
</dd>
</dl>

<dl>
<dd>

**patient_histories:** `typing.Optional[typing.Sequence[PatientHistoryCategory]]` 
    
</dd>
</dl>

<dl>
<dd>

**service_lines:** `typing.Optional[typing.Sequence[ServiceLineCreate]]` 

Each service line must be linked to a diagnosis. Concretely,
`service_line.diagnosis_pointers`must contain at least one entry which should be
in bounds of the diagnoses list field.

    
</dd>
</dl>

<dl>
<dd>

**external_claim_submission:** `typing.Optional[ExternalClaimSubmissionCreate]` 

***This field is in beta.***
To be included for claims that have been submitted outside of Candid.
Candid supports posting remits and payments to these claims and working them in-platform (e.g. editing, resubmitting).

    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[TagId]]` — Names of tags that should be on the encounter.
    
</dd>
</dl>

<dl>
<dd>

**schema_instances:** `typing.Optional[typing.Sequence[SchemaInstance]]` 

Key-value pairs that must adhere to a schema created via the Custom Schema API. Multiple schema
instances cannot be created for the same schema on an encounter.

    
</dd>
</dl>

<dl>
<dd>

**date_of_service:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
Box 24a on the CMS-1500 claim form.
If service occurred over a range of dates, this should be the start date.
date_of_service must be defined on either the encounter or the service lines but not both.
If there are greater than zero service lines, it is recommended to specify date_of_service on the service_line instead of on the encounter to prepare for future API versions.
    
</dd>
</dl>

<dl>
<dd>

**end_date_of_service:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-25.
This date must be the local date in the timezone where the service occurred.
If omitted, the Encounter is assumed to be for a single day.
Must not be temporally before the date_of_service field.
If there are greater than zero service lines, it is recommended to specify end_date_of_service on the service_line instead of on the encounter to prepare for future API versions.
    
</dd>
</dl>

<dl>
<dd>

**appointment_type:** `typing.Optional[str]` — Human-readable description of the appointment type (ex: "Acupuncture - Headaches").
    
</dd>
</dl>

<dl>
<dd>

**existing_medications:** `typing.Optional[typing.Sequence[Medication]]` 
    
</dd>
</dl>

<dl>
<dd>

**vitals:** `typing.Optional[Vitals]` 
    
</dd>
</dl>

<dl>
<dd>

**interventions:** `typing.Optional[typing.Sequence[Intervention]]` 
    
</dd>
</dl>

<dl>
<dd>

**pay_to_address:** `typing.Optional[StreetAddressLongZip]` — Specifies the address to which payments for the claim should be sent.
    
</dd>
</dl>

<dl>
<dd>

**synchronicity:** `typing.Optional[SynchronicityType]` 

Whether or not this was a synchronous or asynchronous encounter.
Asynchronous encounters occur when providers and patients communicate online using
forms, instant messaging, or other pre-recorded digital mediums.
Synchronous encounters occur in live, real-time settings where the patient interacts
directly with the provider, such as over video or a phone call.
    
</dd>
</dl>

<dl>
<dd>

**additional_information:** `typing.Optional[str]` 

Defines additional information on the claim needed by the payer.
Box 19 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**service_authorization_exception_code:** `typing.Optional[ServiceAuthorizationExceptionCode]` 

837p Loop2300 REF\*4N
Required when mandated by government law or regulation to obtain authorization for specific service(s) but, for the
reasons listed in one of the enum values of ServiceAuthorizationExceptionCode, the service was performed without
obtaining the authorization.
    
</dd>
</dl>

<dl>
<dd>

**admission_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP\*435, CMS-1500 Box 18
Required on all ambulance claims when the patient was known to be admitted to the hospital.
OR
Required on all claims involving inpatient medical visits.
    
</dd>
</dl>

<dl>
<dd>

**discharge_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP\*096, CMS-1500 Box 18
Required for inpatient claims when the patient was discharged from the facility and the discharge date is known.
    
</dd>
</dl>

<dl>
<dd>

**onset_of_current_illness_or_symptom_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP\*431, CMS-1500 Box 14
Required for the initial medical service or visit performed in response to a medical emergency when the date is available and is different than the date of service.
OR
This date is the onset of acute symptoms for the current illness or condition.
    
</dd>
</dl>

<dl>
<dd>

**last_menstrual_period_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP\*484, CMS-1500 Box 14
Required when, in the judgment of the provider, the services on this claim are related to the patient's pregnancy.
    
</dd>
</dl>

<dl>
<dd>

**delay_reason_code:** `typing.Optional[DelayReasonCode]` 

837i Loop2300, CLM-1300 Box 20
Code indicating the reason why a request was delayed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    DelayReasonCode,
    EmrPayerCrosswalk,
    EncounterServiceFacilityUpdate,
    FacilityTypeCode,
    Gender,
    InsuranceTypeCode,
    PatientNonInsurancePayerInfoCreate,
    PatientRelationshipToInsuredCodeAll,
    PatientUpdate,
    PhoneNumber,
    PhoneNumberType,
    QualifierCode,
    SourceOfPaymentCode,
    State,
    StreetAddressLongZip,
    StreetAddressShortZip,
    SubscriberCreate,
)
from candid.client import CandidApiClient
from candid.resources.custom_schemas.v_1 import SchemaInstance
from candid.resources.encounter_providers.v_2 import (
    BillingProviderUpdate,
    InitialReferringProviderUpdate,
    ReferringProviderUpdate,
    RenderingProviderUpdate,
    SupervisingProviderUpdate,
)
from candid.resources.encounters.v_4 import (
    BillableStatusType,
    ClinicalNote,
    ClinicalNoteCategoryCreate,
    Medication,
    NoteCategory,
    ResponsiblePartyType,
    ServiceAuthorizationExceptionCode,
    SynchronicityType,
    VitalsUpdate,
)
from candid.resources.guarantor.v_1 import GuarantorUpdate
from candid.resources.insurance_cards.v_2 import InsuranceCardCreate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.update(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    prior_authorization_number="string",
    external_id="string",
    date_of_service=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    diagnosis_ids=[
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ],
    tag_ids=["string"],
    clinical_notes=[
        ClinicalNoteCategoryCreate(
            category=NoteCategory.CLINICAL,
            notes=[
                ClinicalNote(
                    text="string",
                    author_name="string",
                    author_npi="string",
                    timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                )
            ],
        )
    ],
    pay_to_address=StreetAddressLongZip(
        address_1="123 Main St",
        address_2="Apt 1",
        city="New York",
        state=State.NY,
        zip_code="10001",
        zip_plus_four_code="1234",
    ),
    billable_status=BillableStatusType.BILLABLE,
    responsible_party=ResponsiblePartyType.INSURANCE_PAY,
    provider_accepts_assignment=True,
    benefits_assigned_to_provider=True,
    synchronicity=SynchronicityType.SYNCHRONOUS,
    place_of_service_code=FacilityTypeCode.PHARMACY,
    place_of_service_code_as_submitted=FacilityTypeCode.PHARMACY,
    appointment_type="string",
    end_date_of_service=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    subscriber_primary=SubscriberCreate(
        insurance_card=InsuranceCardCreate(
            member_id="string",
            payer_name="string",
            payer_id="string",
            rx_bin="string",
            rx_pcn="string",
            image_url_front="string",
            image_url_back="string",
            emr_payer_crosswalk=EmrPayerCrosswalk.HEALTHIE,
            group_number="string",
            plan_name="string",
            plan_type=SourceOfPaymentCode.SELF_PAY,
            insurance_type=InsuranceTypeCode.C_01,
        ),
        patient_relationship_to_subscriber_code=PatientRelationshipToInsuredCodeAll.SPOUSE,
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        gender=Gender.MALE,
    ),
    subscriber_secondary=SubscriberCreate(
        insurance_card=InsuranceCardCreate(
            member_id="string",
            payer_name="string",
            payer_id="string",
            rx_bin="string",
            rx_pcn="string",
            image_url_front="string",
            image_url_back="string",
            emr_payer_crosswalk=EmrPayerCrosswalk.HEALTHIE,
            group_number="string",
            plan_name="string",
            plan_type=SourceOfPaymentCode.SELF_PAY,
            insurance_type=InsuranceTypeCode.C_01,
        ),
        patient_relationship_to_subscriber_code=PatientRelationshipToInsuredCodeAll.SPOUSE,
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        gender=Gender.MALE,
    ),
    additional_information="string",
    service_authorization_exception_code=ServiceAuthorizationExceptionCode.C_1,
    admission_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    discharge_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    onset_of_current_illness_or_symptom_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    last_menstrual_period_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    delay_reason_code=DelayReasonCode.C_1,
    patient=PatientUpdate(
        first_name="string",
        last_name="string",
        gender=Gender.MALE,
        external_id="string",
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        phone_numbers=[
            PhoneNumber(
                number="1234567890",
                type=PhoneNumberType.HOME,
            )
        ],
        phone_consent=True,
        email="johndoe@joincandidhealth.com",
        email_consent=True,
        non_insurance_payers=[
            uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            )
        ],
        non_insurance_payers_info=[
            PatientNonInsurancePayerInfoCreate(
                non_insurance_payer_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                member_id="string",
            )
        ],
    ),
    patient_authorized_release=True,
    schema_instances=[
        SchemaInstance(
            schema_id=uuid.UUID(
                "ec096b13-f80a-471d-aaeb-54b021c9d582",
            ),
            content={
                "provider_category": "internist",
                "is_urgent_care": true,
                "bmi": 24.2,
                "age": 38,
            },
        )
    ],
    vitals=VitalsUpdate(
        height_in=70,
        weight_lbs=165,
        blood_pressure_systolic_mmhg=115,
        blood_pressure_diastolic_mmhg=85,
        body_temperature_f=98.0,
        hemoglobin_gdl=15.1,
        hematocrit_pct=51.2,
    ),
    existing_medications=[
        Medication(
            name="Lisinopril",
            rx_cui="860975",
            dosage="10mg",
            dosage_form="Tablet",
            frequency="Once Daily",
            as_needed=True,
        )
    ],
    rendering_provider=RenderingProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    service_facility=EncounterServiceFacilityUpdate(
        organization_name="Test Organization",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
    guarantor=GuarantorUpdate(
        first_name="string",
        last_name="string",
        external_id="string",
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        phone_numbers=[
            PhoneNumber(
                number="1234567890",
                type=PhoneNumberType.HOME,
            )
        ],
        phone_consent=True,
        email="johndoe@joincandidhealth.com",
        email_consent=True,
    ),
    billing_provider=BillingProviderUpdate(
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        tax_id="string",
        npi="string",
        taxonomy_code="string",
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    supervising_provider=SupervisingProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    referring_provider=ReferringProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    initial_referring_provider=InitialReferringProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        qualifier=QualifierCode.DQ,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    referral_number="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**prior_authorization_number:** `typing.Optional[PriorAuthorizationNumber]` — Box 23 on the CMS-1500 claim form.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[EncounterExternalId]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.

    
</dd>
</dl>

<dl>
<dd>

**date_of_service:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
Box 24a on the CMS-1500 claim form.
If service occurred over a range of dates, this should be the start date.
If service lines have distinct date_of_service values, updating the encounter's date_of_service will fail. If all service line date_of_service values are the same, updating the encounter's date_of_service will update all service line date_of_service values.

    
</dd>
</dl>

<dl>
<dd>

**diagnosis_ids:** `typing.Optional[typing.Sequence[DiagnosisId]]` 

Ideally, this field should contain no more than 12 diagnoses. However, more diagnoses
may be submitted at this time, and coders will later prioritize the 12 that will be
submitted to the payor.

    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[TagId]]` — Names of tags that should be on the encounter.  Note all tags on encounter will be overridden with this list.
    
</dd>
</dl>

<dl>
<dd>

**clinical_notes:** `typing.Optional[typing.Sequence[ClinicalNoteCategoryCreate]]` — Holds a collection of clinical observations made by healthcare providers during patient encounters.
    
</dd>
</dl>

<dl>
<dd>

**pay_to_address:** `typing.Optional[StreetAddressLongZip]` — Specifies the address to which payments for the claim should be sent.
    
</dd>
</dl>

<dl>
<dd>

**billable_status:** `typing.Optional[BillableStatusType]` — Defines if the Encounter is to be billed by Candid to the responsible_party. Examples for when this should be set to NOT_BILLABLE include if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.

    
</dd>
</dl>

<dl>
<dd>

**responsible_party:** `typing.Optional[ResponsiblePartyType]` — Defines the party to be billed with the initial balance owed on the claim. Use SELF_PAY if you intend to bill self pay/cash pay.

    
</dd>
</dl>

<dl>
<dd>

**provider_accepts_assignment:** `typing.Optional[bool]` — Whether you have accepted the patient's authorization for insurance payments to be made to you, not them. Box 27 on the CMS-1500 claim form.

    
</dd>
</dl>

<dl>
<dd>

**benefits_assigned_to_provider:** `typing.Optional[bool]` — Whether this patient has authorized insurance payments to be made to you, not them. If false, patient may receive reimbursement. Box 13 on the CMS-1500 claim form.

    
</dd>
</dl>

<dl>
<dd>

**synchronicity:** `typing.Optional[SynchronicityType]` — Whether or not this was a synchronous or asynchronous encounter. Asynchronous encounters occur when providers and patients communicate online using forms, instant messaging, or other pre-recorded digital mediums. Synchronous encounters occur in live, real-time settings where the patient interacts directly with the provider, such as over video or a phone call.

    
</dd>
</dl>

<dl>
<dd>

**place_of_service_code:** `typing.Optional[FacilityTypeCode]` — Box 24B on the CMS-1500 claim form. 837p Loop2300, CLM-05-1. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).

    
</dd>
</dl>

<dl>
<dd>

**place_of_service_code_as_submitted:** `typing.Optional[FacilityTypeCode]` — Box 24B on the CMS-1500 claim form. 837p Loop2300, CLM-05-1. 02 for telemedicine, 11 for in-person. Full list [here](https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set).

    
</dd>
</dl>

<dl>
<dd>

**appointment_type:** `typing.Optional[str]` — Human-readable description of the appointment type (ex: "Acupuncture - Headaches").

    
</dd>
</dl>

<dl>
<dd>

**end_date_of_service:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-25.
This date must be the local date in the timezone where the service occurred.
If omitted, the Encounter is assumed to be for a single day.
Must not be temporally before the date_of_service field.
If service lines have distinct end_date_of_service values, updating the encounter's end_date_of_service will fail. If all service line end_date_of_service values are the same, updating the encounter's end_date_of_service will update all service line date_of_service values.

    
</dd>
</dl>

<dl>
<dd>

**subscriber_primary:** `typing.Optional[SubscriberCreate]` — Contains details of the primary insurance subscriber.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_secondary:** `typing.Optional[SubscriberCreate]` — Contains details of the secondary insurance subscriber.
    
</dd>
</dl>

<dl>
<dd>

**additional_information:** `typing.Optional[str]` 

Defines additional information on the claim needed by the payer.
Box 19 on the CMS-1500 claim form.

    
</dd>
</dl>

<dl>
<dd>

**service_authorization_exception_code:** `typing.Optional[ServiceAuthorizationExceptionCode]` 

837p Loop2300 REF*4N
Required when mandated by government law or regulation to obtain authorization for specific service(s) but, for the
reasons listed in one of the enum values of ServiceAuthorizationExceptionCode, the service was performed without
obtaining the authorization.

    
</dd>
</dl>

<dl>
<dd>

**admission_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP*435, CMS-1500 Box 18
Required on all ambulance claims when the patient was known to be admitted to the hospital.
OR
Required on all claims involving inpatient medical visits.

    
</dd>
</dl>

<dl>
<dd>

**discharge_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP*096, CMS-1500 Box 18
Required for inpatient claims when the patient was discharged from the facility and the discharge date is known.

    
</dd>
</dl>

<dl>
<dd>

**onset_of_current_illness_or_symptom_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP*431, CMS-1500 Box 14
Required for the initial medical service or visit performed in response to a medical emergency when the date is available and is different than the date of service.
OR
This date is the onset of acute symptoms for the current illness or condition.

    
</dd>
</dl>

<dl>
<dd>

**last_menstrual_period_date:** `typing.Optional[dt.date]` 

837p Loop2300 DTP*484, CMS-1500 Box 14
Required when, in the judgment of the provider, the services on this claim are related to the patient's pregnancy.

    
</dd>
</dl>

<dl>
<dd>

**delay_reason_code:** `typing.Optional[DelayReasonCode]` 

837i Loop2300, CLM-1300 Box 20
Code indicating the reason why a request was delayed

    
</dd>
</dl>

<dl>
<dd>

**patient:** `typing.Optional[PatientUpdate]` — Contains the identification information of the individual receiving medical services.

    
</dd>
</dl>

<dl>
<dd>

**patient_authorized_release:** `typing.Optional[bool]` 

Whether this patient has authorized the release of medical information
for billing purpose.
Box 12 on the CMS-1500 claim form.

    
</dd>
</dl>

<dl>
<dd>

**schema_instances:** `typing.Optional[typing.Sequence[SchemaInstance]]` 

Key-value pairs that must adhere to a schema created via the Custom Schema API. Multiple schema
instances cannot be created for the same schema on an encounter. Updating schema instances utilizes PUT
semantics, so the schema instances on the encounter will be set to whatever inputs are provided. If null
is provided as an input, then the encounter's schema instances will be cleared.

    
</dd>
</dl>

<dl>
<dd>

**vitals:** `typing.Optional[VitalsUpdate]` 

If a vitals entity already exists for the encounter, then all values will be updated to the provided values.
Otherwise, a new vitals object will be created for the encounter.

    
</dd>
</dl>

<dl>
<dd>

**existing_medications:** `typing.Optional[typing.Sequence[Medication]]` 

Existing medications that should be on the encounter.
Note all current existing medications on encounter will be overridden with this list.

    
</dd>
</dl>

<dl>
<dd>

**rendering_provider:** `typing.Optional[RenderingProviderUpdate]` 

The rendering provider is the practitioner -- physician, nurse practitioner, etc. -- performing the service.
For telehealth services, the rendering provider performs the visit, asynchronous communication, or other service. The rendering provider address should generally be the same as the service facility address.

    
</dd>
</dl>

<dl>
<dd>

**service_facility:** `typing.Optional[EncounterServiceFacilityUpdate]` — Encounter Service facility is typically the location a medical service was rendered, such as a provider office or hospital. For telehealth, service facility can represent the provider's location when the service was delivered (e.g., home), or the location where an in-person visit would have taken place, whichever is easier to identify. If the provider is in-network, service facility may be defined in payer contracts. Box 32 on the CMS-1500 claim form. Note that for an in-network claim to be successfully adjudicated, the service facility address listed on claims must match what was provided to the payer during the credentialing process.

    
</dd>
</dl>

<dl>
<dd>

**guarantor:** `typing.Optional[GuarantorUpdate]` — Personal and contact info for the guarantor of the patient responsibility.

    
</dd>
</dl>

<dl>
<dd>

**billing_provider:** `typing.Optional[BillingProviderUpdate]` — The billing provider is the provider or business entity submitting the claim. Billing provider may be, but is not necessarily, the same person/NPI as the rendering provider. From a payer's perspective, this represents the person or entity being reimbursed. When a contract exists with the target payer, the billing provider should be the entity contracted with the payer. In some circumstances, this will be an individual provider. In that case, submit that provider's NPI and the tax ID (TIN) that the provider gave to the payer during contracting. In other cases, the billing entity will be a medical group. If so, submit the group NPI and the group's tax ID. Box 33 on the CMS-1500 claim form.

    
</dd>
</dl>

<dl>
<dd>

**supervising_provider:** `typing.Optional[SupervisingProviderUpdate]` — Required when the rendering provider is supervised by a physician. If not required by this implementation guide, do not send.

    
</dd>
</dl>

<dl>
<dd>

**referring_provider:** `typing.Optional[ReferringProviderUpdate]` 

The final provider who referred the services that were rendered.
All physicians who order services or refer Medicare beneficiaries must
report this data.

    
</dd>
</dl>

<dl>
<dd>

**initial_referring_provider:** `typing.Optional[InitialReferringProviderUpdate]` 

The second iteration of Loop ID-2310. Use code "P3 - Primary Care Provider" in this loop to
indicate the initial referral from the primary care provider or whatever provider wrote the initial referral for this patient's episode of care being billed/reported in this transaction.

    
</dd>
</dl>

<dl>
<dd>

**referral_number:** `typing.Optional[str]` — Refers to REF*9F on the 837p. Value cannot be greater than 50 characters.

    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ExpectedNetworkStatus V1
<details><summary><code>client.expected_network_status.v_1.<a href="src/candid/resources/expected_network_status/resources/v_1/client.py">compute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Computes the expected network status given the provided information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import InsuranceTypeCode, State
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.expected_network_status.v_1.compute(
    external_patient_id="string",
    subscriber_payer_id="string",
    subscriber_payer_name="string",
    subscriber_insurance_type=InsuranceTypeCode.C_01,
    subscriber_plan_name="string",
    billing_provider_npi="string",
    billing_provider_tin="string",
    rendering_provider_npi="string",
    contracted_state=State.AA,
    date_of_service="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscriber_payer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber_payer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npi:** `str` — The National Provider Identifier (NPI) of the healthcare provider responsible for billing. A unique 10-digit identification number.
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_tin:** `str` — Follow the 9-digit format of the Taxpayer Identification Number (TIN).
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_npi:** `str` — The National Provider Identifier (NPI) of the healthcare provider who delivered the services. A unique 10-digit identification number.
    
</dd>
</dl>

<dl>
<dd>

**contracted_state:** `State` — The state in which the healthcare provider has a contractual agreement with the insurance payer.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service:** `Date` — Date formatted as YYYY-MM-DD; eg: 2019-08-25.

    
</dd>
</dl>

<dl>
<dd>

**external_patient_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber_insurance_type:** `typing.Optional[InsuranceTypeCode]` 
    
</dd>
</dl>

<dl>
<dd>

**subscriber_plan_name:** `typing.Optional[str]` — The descriptive name of the insurance plan selected by the subscriber, often indicating coverage specifics or tier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ExpectedNetworkStatus V2
<details><summary><code>client.expected_network_status.v_2.<a href="src/candid/resources/expected_network_status/resources/v_2/client.py">compute_for_rendering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Computes the expected network status for a given rendering provider.
This endpoint is not available to all customers. Reach out to the Candid sales team
to discuss enabling this endpoint if it is not available for your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    FacilityTypeCode,
    InsuranceTypeCode,
    State,
    StreetAddressShortZip,
)
from candid.client import CandidApiClient
from candid.resources.expected_network_status.v_2 import (
    ExpectedNetworkStatusRequestV2,
    ExpectedNetworkStatusSubscriberInformation,
    InsuranceType,
    InsuranceTypeCodes_InsuranceTypeCode,
    LineOfBusiness,
    ServiceType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.expected_network_status.v_2.compute_for_rendering_provider(
    rendering_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ExpectedNetworkStatusRequestV2(
        service_type=ServiceType.NEW_PATIENT_VIDEO_APPT,
        place_of_service_code=FacilityTypeCode.PHARMACY,
        subscriber_information=ExpectedNetworkStatusSubscriberInformation(
            payer_uuid=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            member_id="string",
            insurance_type=InsuranceType(
                line_of_business=LineOfBusiness.MEDICARE,
                insurance_type_codes=InsuranceTypeCodes_InsuranceTypeCode(
                    value=InsuranceTypeCode.C_01
                ),
            ),
        ),
        patient_address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        billing_provider_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        organization_service_facility_id=uuid.UUID(
            "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
        ),
        date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rendering_provider_id:** `OrganizationProviderId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExpectedNetworkStatusRequestV2` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.expected_network_status.v_2.<a href="src/candid/resources/expected_network_status/resources/v_2/client.py">compute_all_in_network_providers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Computes all the in network providers for a given set of inputs.
This endpoint is not available to all customers. Reach out to the Candid sales team
to discuss enabling this endpoint if it is not available for your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    FacilityTypeCode,
    InsuranceTypeCode,
    State,
    StreetAddressShortZip,
)
from candid.client import CandidApiClient
from candid.resources.expected_network_status.v_2 import (
    ComputeAllInNetworkProvidersRequest,
    ExpectedNetworkStatusSubscriberInformation,
    InsuranceType,
    InsuranceTypeCodes_InsuranceTypeCode,
    LineOfBusiness,
    ServiceType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.expected_network_status.v_2.compute_all_in_network_providers(
    request=ComputeAllInNetworkProvidersRequest(
        service_type=ServiceType.NEW_PATIENT_VIDEO_APPT,
        place_of_service_code=FacilityTypeCode.PHARMACY,
        subscriber_information=ExpectedNetworkStatusSubscriberInformation(
            payer_uuid=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            member_id="string",
            insurance_type=InsuranceType(
                line_of_business=LineOfBusiness.MEDICARE,
                insurance_type_codes=InsuranceTypeCodes_InsuranceTypeCode(
                    value=InsuranceTypeCode.C_01
                ),
            ),
        ),
        patient_address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        billing_provider_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        organization_service_facility_id=uuid.UUID(
            "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
        ),
        date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ComputeAllInNetworkProvidersRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Exports V3
<details><summary><code>client.exports.v_3.<a href="src/candid/resources/exports/resources/v_3/client.py">get_exports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve CSV-formatted reports on claim submissions and outcomes. This endpoint returns Export objects that contain an
authenticated URL to a customer's reports with a 2min TTL. The schema for the CSV export can be found [here](https://app.joincandidhealth.com/files/exports_schema.csv).

**Schema changes:** Changing column order, removing columns, or changing the name of a column is considered a
[Breaking Change](../../../api-principles/breaking-changes). Adding new columns to the end of the Exports file is not considered a
Breaking Change and happens periodically. For this reason, it is important that any downstream automation or processes built on top
of Candid Health's export files be resilient to the addition of new columns at the end of the file.

**SLA guarantees:** Files for a given date are guaranteed to be available after 3 business days. For example, Friday's file will be
available by Wednesday at the latest. If file generation is still in progress upon request before 3 business days have passed, the
caller will receive a 422 response. If the file has already been generated, it will be served. Historic files should be available
up to 90 days in the past by default. Please email our [Support team](mailto:support@joincandidhealth.com) with any data requests
outside of these stated guarantees.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.exports.v_3.get_exports(
    start_date=datetime.date.fromisoformat(
        "2023-10-01",
    ),
    end_date=datetime.date.fromisoformat(
        "2023-10-02",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `dt.date` 

Beginning date of claim versions returned in the export, ISO 8601 date e.g. 2019-08-24.
Must be at least 1 calendar day in the past. Cannot be earlier than 2022-10-07.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `dt.date` 

Ending date of claim versions returned in the export, ISO 8601 date; e.g. 2019-08-24.
Must be within 30 days of start_date.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ExternalPaymentAccountConfig V1
<details><summary><code>client.external_payment_account_config.v_1.<a href="src/candid/resources/external_payment_account_config/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.external_payment_account_config.v_1.get_multi(
    limit=1,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FeeSchedules V3
<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_match</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the rate that matches a service line. No result means no rate exists matching the service line's dimensions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_match(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">test_match</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tests a service line against a rate to see if it matches.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.test_match(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rate_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**rate_id:** `RateId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of dimensions with their rates. The rates returned will always be the most recent versions of those rates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import FacilityTypeCode, NetworkType, ProcedureModifier, State
from candid.client import CandidApiClient
from candid.resources.organization_providers.v_2 import LicenseType

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_multi(
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    limit=1,
    active_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    organization_billing_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    states=State.AA,
    zip_codes="string",
    license_types=LicenseType.MD,
    facility_type_codes=FacilityTypeCode.PHARMACY,
    network_types=NetworkType.PPO,
    cpt_code="string",
    modifiers=ProcedureModifier.TWENTY_TWO,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of dimensions returned. Defaults to 100. Max is 100.
    
</dd>
</dl>

<dl>
<dd>

**active_date:** `typing.Optional[dt.date]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_billing_provider_id:** `typing.Optional[OrganizationProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[State, typing.Sequence[State]]]` 
    
</dd>
</dl>

<dl>
<dd>

**zip_codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**license_types:** `typing.Optional[typing.Union[LicenseType, typing.Sequence[LicenseType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**facility_type_codes:** `typing.Optional[
    typing.Union[FacilityTypeCode, typing.Sequence[FacilityTypeCode]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**network_types:** `typing.Optional[typing.Union[NetworkType, typing.Sequence[NetworkType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**cpt_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**modifiers:** `typing.Optional[
    typing.Union[ProcedureModifier, typing.Sequence[ProcedureModifier]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_unique_values_for_dimension</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets unique values for a dimension based on other selection criteria. The response is a list of dimensions with your criteria and the unique values populated. This API is useful for driving pivots on dimension values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import FacilityTypeCode, NetworkType, ProcedureModifier, State
from candid.client import CandidApiClient
from candid.resources.fee_schedules.v_3 import DimensionName
from candid.resources.organization_providers.v_2 import LicenseType

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_unique_values_for_dimension(
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    limit=1,
    pivot_dimension=DimensionName.PAYER_UUID,
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    organization_billing_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    states=State.AA,
    zip_codes="string",
    license_types=LicenseType.MD,
    facility_type_codes=FacilityTypeCode.PHARMACY,
    network_types=NetworkType.PPO,
    cpt_code="string",
    modifiers=ProcedureModifier.TWENTY_TWO,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pivot_dimension:** `DimensionName` — The name of the dimension to fetch unique values for.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of values returned. Defaults to 1000. Max is 1000.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_billing_provider_id:** `typing.Optional[OrganizationProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[State, typing.Sequence[State]]]` 
    
</dd>
</dl>

<dl>
<dd>

**zip_codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**license_types:** `typing.Optional[typing.Union[LicenseType, typing.Sequence[LicenseType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**facility_type_codes:** `typing.Optional[
    typing.Union[FacilityTypeCode, typing.Sequence[FacilityTypeCode]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**network_types:** `typing.Optional[typing.Union[NetworkType, typing.Sequence[NetworkType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**cpt_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**modifiers:** `typing.Optional[
    typing.Union[ProcedureModifier, typing.Sequence[ProcedureModifier]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_rate_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets every version of a rate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_rate_history(
    rate_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rate_id:** `RateId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">upload_fee_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a new fee schedule.\n Each rate may either be totally new as qualified by it's dimensions or a new version for an existing rate.\n If adding a new version to an existing rate, the rate must be posted with the next version number (previous version + 1) or a EntityConflictError will be returned.\n Use the dry run flag to discover already existing rates and to run validations. If validations for any rate fail, no rates will be saved to the system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import FacilityTypeCode, NetworkType, ProcedureModifier, State
from candid.client import CandidApiClient
from candid.resources.fee_schedules.v_3 import (
    Dimensions,
    RateEntry,
    RateUpload_NewRate,
)
from candid.resources.organization_providers.v_2 import LicenseType

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.upload_fee_schedule(
    dry_run=True,
    rates=[
        RateUpload_NewRate(
            dimensions=Dimensions(
                payer_uuid=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                organization_billing_provider_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                states={State.AA},
                zip_codes={"string"},
                license_types={LicenseType.MD},
                facility_type_codes={FacilityTypeCode.PHARMACY},
                network_types={NetworkType.PPO},
                cpt_code="string",
                modifiers={ProcedureModifier.TWENTY_TWO},
            ),
            entries=[
                RateEntry(
                    start_date=datetime.date.fromisoformat(
                        "2024-04-11",
                    ),
                    rate_cents=33000,
                    is_deactivated=False,
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dry_run:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**rates:** `typing.Sequence[RateUpload]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">delete_rate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft deletes a rate from the system. Only the most recent version of a rate can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.delete_rate(
    rate_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rate_id:** `RateId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_payer_thresholds_default</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the default payer threshold
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_payer_thresholds_default()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">get_payer_thresholds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of payers and thresholds by their uuids
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.get_payer_thresholds(
    payer_uuids=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_uuids:** `typing.Union[PayerUuid, typing.Sequence[PayerUuid]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fee_schedules.v_3.<a href="src/candid/resources/fee_schedules/resources/v_3/client.py">set_payer_threshold</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the threshold information for a payer
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient
from candid.resources.fee_schedules.v_3 import PayerThreshold

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.fee_schedules.v_3.set_payer_threshold(
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=PayerThreshold(
        upper_threshold_cents=1,
        lower_threshold_cents=1,
        disable_paid_incorrectly=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_uuid:** `PayerUuid` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PayerThreshold` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guarantor V1
<details><summary><code>client.guarantor.v_1.<a href="src/candid/resources/guarantor/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new guarantor and returns the newly created Guarantor object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import PhoneNumber, PhoneNumberType, State, StreetAddressShortZip
from candid.client import CandidApiClient
from candid.resources.guarantor.v_1 import GuarantorCreate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.guarantor.v_1.create(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=GuarantorCreate(
        phone_numbers=[
            PhoneNumber(
                number="1234567890",
                type=PhoneNumberType.HOME,
            )
        ],
        phone_consent=True,
        email="johndoe@joincandidhealth.com",
        email_consent=True,
        first_name="string",
        last_name="string",
        external_id="string",
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GuarantorCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guarantor.v_1.<a href="src/candid/resources/guarantor/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a guarantor by its `guarantor_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.guarantor.v_1.get(
    guarantor_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guarantor_id:** `GuarantorId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guarantor.v_1.<a href="src/candid/resources/guarantor/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a guarantor by its `guarantor_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import PhoneNumber, PhoneNumberType, State, StreetAddressShortZip
from candid.client import CandidApiClient
from candid.resources.guarantor.v_1 import GuarantorUpdate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.guarantor.v_1.update(
    guarantor_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=GuarantorUpdate(
        first_name="string",
        last_name="string",
        external_id="string",
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        phone_numbers=[
            PhoneNumber(
                number="1234567890",
                type=PhoneNumberType.HOME,
            )
        ],
        phone_consent=True,
        email="johndoe@joincandidhealth.com",
        email_consent=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guarantor_id:** `GuarantorId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GuarantorUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ImportInvoice V1
<details><summary><code>client.import_invoice.v_1.<a href="src/candid/resources/import_invoice/resources/v_1/client.py">import_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import an existing invoice from a third party service to reflect state in Candid.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.import_invoice.v_1 import CreateImportInvoiceRequest
from candid.resources.invoices.v_2 import (
    InvoiceItemAttributionCreate_ServiceLineId,
    InvoiceItemCreate,
    InvoiceStatus,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.import_invoice.v_1.import_invoice(
    request=CreateImportInvoiceRequest(
        external_payment_account_config_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        patient_external_id="string",
        external_customer_identifier="string",
        note="string",
        due_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        items=[
            InvoiceItemCreate(
                attribution=InvoiceItemAttributionCreate_ServiceLineId(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
                amount_cents=1,
            )
        ],
        status=InvoiceStatus.DRAFT,
        external_identifier="string",
        customer_invoice_url="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateImportInvoiceRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_invoice.v_1.<a href="src/candid/resources/import_invoice/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all Invoices for the authenticated user's organziation with all filters applied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import SortDirection
from candid.client import CandidApiClient
from candid.resources.invoices.v_2 import InvoiceSortField, InvoiceStatus

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.import_invoice.v_1.get_multi(
    patient_external_id="string",
    encounter_external_id="string",
    note="string",
    due_date_before=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    due_date_after=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    status=InvoiceStatus.DRAFT,
    limit=1,
    sort=InvoiceSortField.CREATED_AT,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_external_id:** `typing.Optional[PatientExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**encounter_external_id:** `typing.Optional[EncounterExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — partial match supported
    
</dd>
</dl>

<dl>
<dd>

**due_date_before:** `typing.Optional[dt.date]` — all invoices whose due date is before this due date, not inclusive
    
</dd>
</dl>

<dl>
<dd>

**due_date_after:** `typing.Optional[dt.date]` — all invoices whose due date is after this due date, not inclusive
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — all invoices that match any of the provided statuses
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[InvoiceSortField]` — Defaults to created_at
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_invoice.v_1.<a href="src/candid/resources/import_invoice/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve and view an import invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.import_invoice.v_1.get(
    invoice_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` — InvoiceId to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_invoice.v_1.<a href="src/candid/resources/import_invoice/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the information on the imported invoice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.import_invoice.v_1 import (
    ImportInvoiceUpdateRequest,
    InvoiceItemInfoUpdate,
    InvoiceItemUpdateType,
)
from candid.resources.invoices.v_2 import (
    InvoiceItemAttributionCreate_ServiceLineId,
    InvoiceItemCreate,
    InvoiceStatus,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.import_invoice.v_1.update(
    invoice_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ImportInvoiceUpdateRequest(
        customer_invoice_url="string",
        status=InvoiceStatus.DRAFT,
        note="string",
        due_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        items=InvoiceItemInfoUpdate(
            update_type=InvoiceItemUpdateType.APPEND,
            items=[
                InvoiceItemCreate(
                    attribution=InvoiceItemAttributionCreate_ServiceLineId(
                        value=uuid.UUID(
                            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                        )
                    ),
                    amount_cents=1,
                )
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `InvoiceId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ImportInvoiceUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InsuranceAdjudications V1
<details><summary><code>client.insurance_adjudications.v_1.<a href="src/candid/resources/insurance_adjudications/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created insurance adjudication by its `insurance_adjudication_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_adjudications.v_1.get(
    insurance_adjudication_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_adjudication_id:** `InsuranceAdjudicationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_adjudications.v_1.<a href="src/candid/resources/insurance_adjudications/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new insurance adjudication record and returns the newly created InsuranceAdjudication object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import ClaimStatusCodeCreate
from candid.client import CandidApiClient
from candid.resources.insurance_adjudications.v_1 import (
    ClaimAdjudicationCreate,
    InsuranceAdjudicationCreate,
)
from candid.resources.payers.v_3 import PayerIdentifier_PayerInfo
from candid.resources.remits.v_1 import Payee, PayeeIdentifier_Npi

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_adjudications.v_1.create(
    request=InsuranceAdjudicationCreate(
        payer_identifier=PayerIdentifier_PayerInfo(),
        payee=Payee(
            payee_name="string",
            payee_identifier=PayeeIdentifier_Npi(value="string"),
        ),
        post_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        check_number="string",
        check_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        note="string",
        claims={
            uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",): [
                ClaimAdjudicationCreate(
                    claim_status_code=ClaimStatusCodeCreate.PROCESSED_AS_PRIMARY,
                    service_lines={},
                    carcs=[],
                )
            ]
        },
        remit_draft_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InsuranceAdjudicationCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_adjudications.v_1.<a href="src/candid/resources/insurance_adjudications/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the insurance adjudication record matching the provided insurance_adjudication_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_adjudications.v_1.delete(
    insurance_adjudication_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_adjudication_id:** `InsuranceAdjudicationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InsurancePayments V1
<details><summary><code>client.insurance_payments.v_1.<a href="src/candid/resources/insurance_payments/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all non-ERA originated insurance payments satisfying the search criteria
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import SortDirection
from candid.client import CandidApiClient
from candid.resources.insurance_payments.v_1 import InsurancePaymentSortField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_payments.v_1.get_multi(
    limit=1,
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    claim_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    billing_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    sort=InsurancePaymentSortField.AMOUNT_CENTS,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[InsurancePaymentSortField]` — Defaults to payment_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_payments.v_1.<a href="src/candid/resources/insurance_payments/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created insurance payment by its `insurance_payment_id`.
If the payment does not exist, a `403` will be thrown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_payments.v_1.get(
    insurance_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_payment_id:** `InsurancePaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_payments.v_1.<a href="src/candid/resources/insurance_payments/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new insurance payment record and returns the newly created `InsurancePayment` object. This endpoint
should only be used for insurance payments that do not have a corresponding ERA (for example: a settlement check
from a payer). If the payment is an ERA, then you should used the insurance-adjudications API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import AllocationCreate, AllocationTargetCreate_ServiceLineById
from candid.client import CandidApiClient
from candid.resources.insurance_payments.v_1 import InsurancePaymentCreate
from candid.resources.payers.v_3 import PayerIdentifier_PayerInfo

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_payments.v_1.create(
    request=InsurancePaymentCreate(
        payer_identifier=PayerIdentifier_PayerInfo(),
        amount_cents=1,
        payment_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        payment_note="string",
        allocations=[
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InsurancePaymentCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_payments.v_1.<a href="src/candid/resources/insurance_payments/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the patient payment record matching the provided insurance_payment_id. If updating the payment amount,
then the allocations must be appropriately updated as well.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import NoteUpdate_Set
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_payments.v_1.update(
    insurance_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payment_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    payment_note=NoteUpdate_Set(value="string"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_payment_id:** `InsurancePaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**payment_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_payments.v_1.<a href="src/candid/resources/insurance_payments/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the insurance payment record matching the provided `insurance_payment_id`.
If the matching record's organization_id does not match the authenticated user's
current organization_id, then a response code of `403` will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_payments.v_1.delete(
    insurance_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_payment_id:** `InsurancePaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InsuranceRefunds V1
<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all insurance refunds satisfying the search criteria AND whose organization_id matches
the current organization_id of the authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import SortDirection
from candid.client import CandidApiClient
from candid.resources.insurance_refunds.v_1 import InsuranceRefundSortField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.get_multi(
    limit=1,
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    claim_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    billing_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    sort=InsuranceRefundSortField.AMOUNT_CENTS,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[InsuranceRefundSortField]` — Defaults to refund_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created insurance refund by its `insurance_refund_id`.
If the refund does not exist, a `403` will be thrown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.get(
    insurance_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_refund_id:** `InsuranceRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new insurance refund record and returns the newly created `InsuranceRefund` object.
The allocations can describe whether the refund is being applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    AllocationCreate,
    AllocationTargetCreate_ServiceLineById,
    RefundReason,
)
from candid.client import CandidApiClient
from candid.resources.insurance_refunds.v_1 import InsuranceRefundCreate
from candid.resources.payers.v_3 import PayerIdentifier_PayerInfo

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.create(
    request=InsuranceRefundCreate(
        payer_identifier=PayerIdentifier_PayerInfo(),
        amount_cents=1,
        refund_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        refund_note="string",
        allocations=[
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            )
        ],
        refund_reason=RefundReason.OVERCHARGED,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InsuranceRefundCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the patient refund record matching the provided insurance_refund_id. If updating the refund amount,
then the allocations must be appropriately updated as well.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import NoteUpdate_Set, RefundReason, RefundReasonUpdate_Set
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.update(
    insurance_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    refund_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    refund_note=NoteUpdate_Set(value="string"),
    refund_reason=RefundReasonUpdate_Set(value=RefundReason.OVERCHARGED),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_refund_id:** `InsuranceRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**refund_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_reason:** `typing.Optional[RefundReasonUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insurance_refunds.v_1.<a href="src/candid/resources/insurance_refunds/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the insurance refund record matching the provided `insurance_refund_id`.
If the matching record's organization_id does not match the authenticated user's
current organization_id, then a response code of `403` will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.insurance_refunds.v_1.delete(
    insurance_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**insurance_refund_id:** `InsuranceRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## MedicationDispense V1
<details><summary><code>client.medication_dispense.v_1.<a href="src/candid/resources/medication_dispense/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import ProcedureModifier, ServiceLineUnits
from candid.client import CandidApiClient
from candid.resources.medication_dispense.v_1 import MedicationDispenseCreate
from candid.resources.service_lines.v_2 import (
    DrugIdentification,
    MeasurementUnitCode,
    ServiceIdQualifier,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.medication_dispense.v_1.create(
    request=MedicationDispenseCreate(
        medication_dispense_external_id="string",
        patient_external_id="string",
        procedure_code="string",
        quantity="string",
        units=ServiceLineUnits.MJ,
        date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        drug_identification=DrugIdentification(
            service_id_qualifier=ServiceIdQualifier.EAN_UCC_13,
            national_drug_code="string",
            national_drug_unit_count="string",
            measurement_unit_code=MeasurementUnitCode.MILLILITERS,
            link_sequence_number="string",
            pharmacy_prescription_number="string",
            conversion_formula="string",
            drug_description="string",
        ),
        description="string",
        modifiers=[ProcedureModifier.TWENTY_TWO],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MedicationDispenseCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NonInsurancePayerPayments V1
<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all non-insurance payer payments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import SortDirection
from candid.client import CandidApiClient
from candid.resources.non_insurance_payer_payments.v_1 import (
    NonInsurancePayerPaymentSortField,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.get_multi(
    limit=1,
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    check_number="string",
    invoice_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    sort=NonInsurancePayerPaymentSortField.AMOUNT_CENTS,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**non_insurance_payer_id:** `typing.Optional[NonInsurancePayerId]` 
    
</dd>
</dl>

<dl>
<dd>

**check_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[NonInsurancePayerPaymentSortField]` — Defaults to refund_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created non-insurance payer payment by its `non_insurance_payer_payment_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.get(
    non_insurance_payer_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_payment_id:** `NonInsurancePayerPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import AllocationCreate, AllocationTargetCreate_ServiceLineById
from candid.client import CandidApiClient
from candid.resources.non_insurance_payer_payments.v_1 import (
    NonInsurancePayerPaymentCreate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.create(
    request=NonInsurancePayerPaymentCreate(
        non_insurance_payer_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        amount_cents=1,
        payment_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        payment_note="string",
        check_number="string",
        allocations=[
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            )
        ],
        invoice_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `NonInsurancePayerPaymentCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import InvoiceUpdate_Set, NoteUpdate_Set
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.update(
    non_insurance_payer_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payment_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    payment_note=NoteUpdate_Set(value="string"),
    invoice_id=InvoiceUpdate_Set(
        value=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_payment_id:** `NonInsurancePayerPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**payment_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_payments.v_1.<a href="src/candid/resources/non_insurance_payer_payments/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the non-insurance payer payment record matching the provided `non_insurance_payer_payment_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_payments.v_1.delete(
    non_insurance_payer_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_payment_id:** `NonInsurancePayerPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NonInsurancePayerRefunds V1
<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all non-insurance payer refunds satisfying the search criteria
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import SortDirection
from candid.client import CandidApiClient
from candid.resources.non_insurance_payer_refunds.v_1 import (
    NonInsurancePayerRefundSortField,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.get_multi(
    limit=1,
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    check_number="string",
    invoice_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    sort=NonInsurancePayerRefundSortField.AMOUNT_CENTS,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**non_insurance_payer_id:** `typing.Optional[NonInsurancePayerId]` 
    
</dd>
</dl>

<dl>
<dd>

**check_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[NonInsurancePayerRefundSortField]` — Defaults to refund_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created non-insurance payer refund by its `non_insurance_payer_refund_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.get(
    non_insurance_payer_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_refund_id:** `NonInsurancePayerRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new non-insurance payer refund record and returns the newly created `NonInsurancePayerRefund` object.
The allocations can describe whether the refund is being applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    AllocationCreate,
    AllocationTargetCreate_ServiceLineById,
    RefundReason,
)
from candid.client import CandidApiClient
from candid.resources.non_insurance_payer_refunds.v_1 import (
    NonInsurancePayerRefundCreate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.create(
    request=NonInsurancePayerRefundCreate(
        non_insurance_payer_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        invoice_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        amount_cents=1,
        refund_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        refund_note="string",
        check_number="string",
        allocations=[
            AllocationCreate(
                amount_cents=1,
                target=AllocationTargetCreate_ServiceLineById(
                    value=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    )
                ),
            )
        ],
        refund_reason=RefundReason.OVERCHARGED,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `NonInsurancePayerRefundCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the non-insurance payer refund record matching the provided non_insurance_payer_refund_id. If updating the refund amount,
then the allocations must be appropriately updated as well.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    InvoiceUpdate_Set,
    NoteUpdate_Set,
    RefundReason,
    RefundReasonUpdate_Set,
)
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.update(
    non_insurance_payer_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    refund_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    refund_note=NoteUpdate_Set(value="string"),
    refund_reason=RefundReasonUpdate_Set(value=RefundReason.OVERCHARGED),
    invoice_id=InvoiceUpdate_Set(
        value=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_refund_id:** `NonInsurancePayerRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**refund_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_reason:** `typing.Optional[RefundReasonUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payer_refunds.v_1.<a href="src/candid/resources/non_insurance_payer_refunds/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the non-insurance payer refund record matching the provided `non_insurance_payer_refund_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payer_refunds.v_1.delete(
    non_insurance_payer_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_refund_id:** `NonInsurancePayerRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NonInsurancePayers V1
<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import State, StreetAddressShortZip
from candid.client import CandidApiClient
from candid.resources.non_insurance_payers.v_1 import (
    CreateNonInsurancePayerRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.create(
    request=CreateNonInsurancePayerRequest(
        name="string",
        description="string",
        category="string",
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateNonInsurancePayerRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">toggle_enablement</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient
from candid.resources.non_insurance_payers.v_1 import (
    ToggleNonInsurancePayerEnablementRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.toggle_enablement(
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ToggleNonInsurancePayerEnablementRequest(
        enabled=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_id:** `NonInsurancePayerId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ToggleNonInsurancePayerEnablementRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import SortDirection
from candid.client import CandidApiClient
from candid.resources.non_insurance_payers.v_1 import NonInsurancePayerSortField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.get_multi(
    name="string",
    category="string",
    enabled=True,
    sort=NonInsurancePayerSortField.NAME,
    sort_direction=SortDirection.ASC,
    limit=1,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[NonInsurancePayerSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.get(
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_id:** `NonInsurancePayerId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient
from candid.resources.non_insurance_payers.v_1 import (
    NonInsurancePayerAddressUpdate,
    NonInsurancePayerCategoryUpdate,
    NonInsurancePayerDescriptionUpdate,
    NonInsurancePayerUpdateRequest,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.update(
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=NonInsurancePayerUpdateRequest(
        name="string",
        description=NonInsurancePayerDescriptionUpdate(),
        category=NonInsurancePayerCategoryUpdate(),
        address=NonInsurancePayerAddressUpdate(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_id:** `NonInsurancePayerId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NonInsurancePayerUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.non_insurance_payers.v_1.<a href="src/candid/resources/non_insurance_payers/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.non_insurance_payers.v_1.delete(
    non_insurance_payer_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**non_insurance_payer_id:** `NonInsurancePayerId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrganizationServiceFacilities V2
<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.get(
    organization_service_facility_id=uuid.UUID(
        "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_service_facility_id:** `OrganizationServiceFacilityId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.get_multi(
    limit=100,
    name="Test Service Facility",
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of results returned. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter to a name or a part of a name.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` — The page token to continue paging through a previous request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.organization_service_facilities.v_2 import (
    OrganizationServiceFacilityCreate,
    ServiceFacilityMode,
    ServiceFacilityOperationalStatus,
    ServiceFacilityPhysicalType,
    ServiceFacilityStatus,
    ServiceFacilityType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.create(
    request=OrganizationServiceFacilityCreate(
        name="Test Service Facility",
        aliases=["Test Service Facility Alias"],
        description="Test Service Facility Description",
        status=ServiceFacilityStatus.ACTIVE,
        operational_status=ServiceFacilityOperationalStatus.CLOSED,
        mode=ServiceFacilityMode.INSTANCE,
        type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
        physical_type=ServiceFacilityPhysicalType.SITE,
        telecoms=["555-555-5555"],
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OrganizationServiceFacilityCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import State, StreetAddressLongZip
from candid.client import CandidApiClient
from candid.resources.organization_service_facilities.v_2 import (
    OrganizationServiceFacilityUpdate,
    ServiceFacilityMode,
    ServiceFacilityOperationalStatus,
    ServiceFacilityPhysicalType,
    ServiceFacilityStatus,
    ServiceFacilityType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.update(
    organization_service_facility_id=uuid.UUID(
        "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
    ),
    request=OrganizationServiceFacilityUpdate(
        name="Test Service Facility",
        aliases=["Test Service Facility Alias"],
        description="Test Service Facility Description",
        status=ServiceFacilityStatus.ACTIVE,
        operational_status=ServiceFacilityOperationalStatus.CLOSED,
        mode=ServiceFacilityMode.INSTANCE,
        type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
        physical_type=ServiceFacilityPhysicalType.SITE,
        telecoms=["555-555-5555"],
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_service_facility_id:** `OrganizationServiceFacilityId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationServiceFacilityUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_service_facilities.v_2.<a href="src/candid/resources/organization_service_facilities/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_service_facilities.v_2.delete(
    organization_service_facility_id=uuid.UUID(
        "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_service_facility_id:** `OrganizationServiceFacilityId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrganizationProviders V3
<details><summary><code>client.organization_providers.v_3.<a href="src/candid/resources/organization_providers/resources/v_3/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_providers.v_3.get(
    organization_provider_id=uuid.UUID(
        "965a563a-0285-4910-9569-e3739c0f6eab",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_provider_id:** `OrganizationProviderId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_providers.v_3.<a href="src/candid/resources/organization_providers/resources/v_3/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient
from candid.resources.organization_providers.v_2 import (
    OrganizationProviderSortOptions,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_providers.v_3.get_multi(
    limit=100,
    search_term="john",
    npi="1234567890",
    is_rendering=True,
    is_billing=True,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    sort=OrganizationProviderSortOptions.PROVIDER_NAME_ASC,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of results returned. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` — Filter to a name or a part of a name.
    
</dd>
</dl>

<dl>
<dd>

**npi:** `typing.Optional[str]` — Filter to a specific NPI.
    
</dd>
</dl>

<dl>
<dd>

**is_rendering:** `typing.Optional[bool]` — Filter to only rendering providers.
    
</dd>
</dl>

<dl>
<dd>

**is_billing:** `typing.Optional[bool]` — Filter to only billing providers.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` — The page token to continue paging through a previous request.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[OrganizationProviderSortOptions]` — Defaults to PROVIDER_NAME_ASC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_providers.v_3.<a href="src/candid/resources/organization_providers/resources/v_3/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import (
    DateRangeOptionalEnd,
    IdentifierCode,
    IdentifierCreate,
    IdentifierValue_MedicareProviderIdentifier,
    State,
    StreetAddressLongZip,
)
from candid.client import CandidApiClient
from candid.resources.organization_providers.v_2 import (
    AddressType,
    LicenseType,
    OrganizationProviderAddress,
    ProviderType,
)
from candid.resources.organization_providers.v_3 import (
    OrganizationProviderCreateV2,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_providers.v_3.create(
    request=OrganizationProviderCreateV2(
        npi="string",
        is_rendering=True,
        is_billing=True,
        first_name="string",
        last_name="string",
        organization_name="string",
        provider_type=ProviderType.INDIVIDUAL,
        tax_id="string",
        taxonomy_code="string",
        license_type=LicenseType.MD,
        addresses=[
            OrganizationProviderAddress(
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
                address_type=AddressType.DEFAULT,
            )
        ],
        employment_start_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        employment_termination_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        qualifications=[
            IdentifierCreate(
                period=DateRangeOptionalEnd(
                    start_date="string",
                ),
                identifier_code=IdentifierCode.MCR,
                identifier_value=IdentifierValue_MedicareProviderIdentifier(),
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OrganizationProviderCreateV2` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_providers.v_3.<a href="src/candid/resources/organization_providers/resources/v_3/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import (
    DateRangeOptionalEnd,
    IdentifierCode,
    IdentifierValue_MedicareProviderIdentifier,
    State,
    StreetAddressLongZip,
    UpdatableIdentifier_Add,
)
from candid.client import CandidApiClient
from candid.resources.organization_providers.v_2 import (
    AddressType,
    LicenseType,
    OrganizationProviderAddress,
    ProviderType,
)
from candid.resources.organization_providers.v_3 import (
    OrganizationProviderUpdateV2,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.organization_providers.v_3.update(
    organization_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=OrganizationProviderUpdateV2(
        npi="string",
        is_rendering=True,
        is_billing=True,
        first_name="string",
        last_name="string",
        organization_name="string",
        provider_type=ProviderType.INDIVIDUAL,
        tax_id="string",
        taxonomy_code="string",
        license_type=LicenseType.MD,
        addresses=[
            OrganizationProviderAddress(
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
                address_type=AddressType.DEFAULT,
            )
        ],
        employment_start_date="string",
        employment_termination_date="string",
        qualifications=[
            UpdatableIdentifier_Add(
                period=DateRangeOptionalEnd(
                    start_date="string",
                ),
                identifier_code=IdentifierCode.MCR,
                identifier_value=IdentifierValue_MedicareProviderIdentifier(),
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_provider_id:** `OrganizationProviderId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationProviderUpdateV2` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PatientPayments V4
<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all patient payments satisfying the search criteria AND whose organization_id matches
the current organization_id of the authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import PatientTransactionSource, SortDirection
from candid.client import CandidApiClient
from candid.resources.patient_payments.v_4 import PatientPaymentSortField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.get_multi(
    limit=1,
    patient_external_id="string",
    claim_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    billing_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    unattributed=True,
    invoice_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    sources=PatientTransactionSource.MANUAL_ENTRY,
    sort=PatientPaymentSortField.PAYMENT_SOURCE,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[PatientExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**unattributed:** `typing.Optional[bool]` — returns payments with unattributed allocations if set to true
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[
    typing.Union[
        PatientTransactionSource, typing.Sequence[PatientTransactionSource]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PatientPaymentSortField]` — Defaults to payment_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created patient payment by its `patient_payment_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.get(
    patient_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_payment_id:** `PatientPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new patient payment record and returns the newly created PatientPayment object.
The allocations can describe whether the payment is being applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import AllocationCreate, AllocationTargetCreate_ServiceLineById
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.create(
    amount_cents=1,
    payment_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    payment_note="string",
    patient_external_id="string",
    allocations=[
        AllocationCreate(
            amount_cents=1,
            target=AllocationTargetCreate_ServiceLineById(
                value=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ),
        )
    ],
    invoice=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount_cents:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `PatientExternalId` 
    
</dd>
</dl>

<dl>
<dd>

**allocations:** `typing.Sequence[AllocationCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the patient payment record matching the provided patient_payment_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import InvoiceUpdate_Set, NoteUpdate_Set
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.update(
    patient_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payment_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    payment_note=NoteUpdate_Set(value="string"),
    invoice=InvoiceUpdate_Set(
        value=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_payment_id:** `PatientPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**payment_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[InvoiceUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_payments.v_4.<a href="src/candid/resources/patient_payments/resources/v_4/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the patient payment record matching the provided patient_payment_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_payments.v_4.delete(
    patient_payment_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_payment_id:** `PatientPaymentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PatientRefunds V1
<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all patient refunds satisfying the search criteria AND whose organization_id matches
the current organization_id of the authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import PatientTransactionSource, SortDirection
from candid.client import CandidApiClient
from candid.resources.patient_refunds.v_1 import PatientRefundSortField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.get_multi(
    limit=1,
    patient_external_id="string",
    claim_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    billing_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    unattributed=True,
    invoice_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    sources=PatientTransactionSource.MANUAL_ENTRY,
    sort=PatientRefundSortField.REFUND_SOURCE,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[PatientExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**unattributed:** `typing.Optional[bool]` — returns payments with unattributed allocations if set to true
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[
    typing.Union[
        PatientTransactionSource, typing.Sequence[PatientTransactionSource]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PatientRefundSortField]` — Defaults to refund_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created patient refund by its `patient_refund_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.get(
    patient_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_refund_id:** `PatientRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new patient refund record and returns the newly created PatientRefund object.
The allocations can describe whether the refund is being applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    AllocationCreate,
    AllocationTargetCreate_ServiceLineById,
    RefundReason,
)
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.create(
    amount_cents=1,
    refund_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    refund_note="string",
    patient_external_id="string",
    allocations=[
        AllocationCreate(
            amount_cents=1,
            target=AllocationTargetCreate_ServiceLineById(
                value=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ),
        )
    ],
    invoice=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    refund_reason=RefundReason.OVERCHARGED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount_cents:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `PatientExternalId` 
    
</dd>
</dl>

<dl>
<dd>

**allocations:** `typing.Sequence[AllocationCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[InvoiceId]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_reason:** `typing.Optional[RefundReason]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the patient refund record matching the provided patient_refund_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    InvoiceUpdate_Set,
    NoteUpdate_Set,
    RefundReason,
    RefundReasonUpdate_Set,
)
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.update(
    patient_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    refund_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    refund_note=NoteUpdate_Set(value="string"),
    invoice=InvoiceUpdate_Set(
        value=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ),
    refund_reason=RefundReasonUpdate_Set(value=RefundReason.OVERCHARGED),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_refund_id:** `PatientRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**refund_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_note:** `typing.Optional[NoteUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[InvoiceUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**refund_reason:** `typing.Optional[RefundReasonUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_refunds.v_1.<a href="src/candid/resources/patient_refunds/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the patient refund record matching the provided patient_refund_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.patient_refunds.v_1.delete(
    patient_refund_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_refund_id:** `PatientRefundId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payers V3
<details><summary><code>client.payers.v_3.<a href="src/candid/resources/payers/resources/v_3/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payers.v_3.get(
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payer_uuid:** `PayerUuid` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payers.v_3.<a href="src/candid/resources/payers/resources/v_3/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.payers.v_3.get_all(
    limit=100,
    search_term="john",
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ServiceLines V2
<details><summary><code>client.service_lines.v_2.<a href="src/candid/resources/service_lines/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import (
    FacilityTypeCode,
    ProcedureModifier,
    ServiceLineUnits,
    State,
    StreetAddressLongZip,
)
from candid.client import CandidApiClient
from candid.resources.encounter_providers.v_2 import OrderingProvider
from candid.resources.service_lines.v_2 import (
    DenialReasonContent,
    DrugIdentification,
    MeasurementUnitCode,
    ServiceIdQualifier,
    ServiceLineCreateStandalone,
    ServiceLineDenialReason,
    TestResult,
    TestResultType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_lines.v_2.create(
    request=ServiceLineCreateStandalone(
        modifiers=[ProcedureModifier.TWENTY_TWO],
        charge_amount_cents=1,
        diagnosis_id_zero=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        diagnosis_id_one=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        diagnosis_id_two=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        diagnosis_id_three=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        denial_reason=ServiceLineDenialReason(
            reason=DenialReasonContent.AUTHORIZATION_REQUIRED,
        ),
        place_of_service_code=FacilityTypeCode.PHARMACY,
        procedure_code="string",
        quantity="string",
        units=ServiceLineUnits.MJ,
        claim_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        description="string",
        date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        end_date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        drug_identification=DrugIdentification(
            service_id_qualifier=ServiceIdQualifier.EAN_UCC_13,
            national_drug_code="string",
            national_drug_unit_count="string",
            measurement_unit_code=MeasurementUnitCode.MILLILITERS,
            link_sequence_number="string",
            pharmacy_prescription_number="string",
            conversion_formula="string",
            drug_description="string",
        ),
        ordering_provider=OrderingProvider(
            npi="string",
            taxonomy_code="string",
            address=StreetAddressLongZip(
                address_1="123 Main St",
                address_2="Apt 1",
                city="New York",
                state=State.NY,
                zip_code="10001",
                zip_plus_four_code="1234",
            ),
            first_name="string",
            last_name="string",
            organization_name="string",
        ),
        test_results=[
            TestResult(
                value=1.1,
                result_type=TestResultType.HEMATOCRIT,
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ServiceLineCreateStandalone` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_lines.v_2.<a href="src/candid/resources/service_lines/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import FacilityTypeCode, ProcedureModifier, ServiceLineUnits
from candid.client import CandidApiClient
from candid.resources.service_lines.v_2 import (
    DenialReasonContent,
    DrugIdentification,
    MeasurementUnitCode,
    ServiceIdQualifier,
    ServiceLineDenialReason,
    ServiceLineUpdate,
    TestResult,
    TestResultType,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_lines.v_2.update(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ServiceLineUpdate(
        edit_reason="string",
        modifiers=[ProcedureModifier.TWENTY_TWO],
        charge_amount_cents=1,
        diagnosis_id_zero=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        diagnosis_id_one=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        diagnosis_id_two=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        diagnosis_id_three=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        drug_identification=DrugIdentification(
            service_id_qualifier=ServiceIdQualifier.EAN_UCC_13,
            national_drug_code="string",
            national_drug_unit_count="string",
            measurement_unit_code=MeasurementUnitCode.MILLILITERS,
            link_sequence_number="string",
            pharmacy_prescription_number="string",
            conversion_formula="string",
            drug_description="string",
        ),
        denial_reason=ServiceLineDenialReason(
            reason=DenialReasonContent.AUTHORIZATION_REQUIRED,
        ),
        place_of_service_code=FacilityTypeCode.PHARMACY,
        units=ServiceLineUnits.MJ,
        procedure_code="string",
        quantity="string",
        description="string",
        date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        end_date_of_service=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        test_results=[
            TestResult(
                value=1.1,
                result_type=TestResultType.HEMATOCRIT,
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ServiceLineUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_lines.v_2.<a href="src/candid/resources/service_lines/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_lines.v_2.delete(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks V3
<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">get_actions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.get_actions(
    task_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `TaskId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.tasks import TaskStatus, TaskType
from candid.resources.tasks.v_3 import TaskSortOptions

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.get_multi(
    limit=1,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    status=TaskStatus.FINISHED,
    task_type=TaskType.CUSTOMER_DATA_REQUEST,
    categories="string",
    updated_since=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    search_term="string",
    assigned_to_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    date_of_service_min=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    date_of_service_max=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    billing_provider_npi="string",
    sort=TaskSortOptions.UPDATED_AT_ASC,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaskStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[TaskType]` 
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[str]` — Only return tasks with categories that match one in this comma-separated list.
    
</dd>
</dl>

<dl>
<dd>

**updated_since:** `typing.Optional[dt.datetime]` — Only return tasks updated on or after this date-time
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `typing.Optional[EncounterId]` — Only return tasks associated with this encounter
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` — Query tasks by encounter_id, claim_id, task_id, or external_id
    
</dd>
</dl>

<dl>
<dd>

**assigned_to_id:** `typing.Optional[UserId]` — Only return tasks assigned to this user
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` — The minimum date of service for the linked encounter
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` — The maximum date of service for the linked encounter
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npi:** `typing.Optional[str]` — The NPI of the billing provider associated with the task's claim
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[TaskSortOptions]` — Defaults to updated_at:desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.get(
    task_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `TaskId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient
from candid.resources.tasks import TaskCategory, TaskType
from candid.resources.tasks.v_3 import TaskCreateV3

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.create(
    request=TaskCreateV3(
        encounter_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        task_type=TaskType.CUSTOMER_DATA_REQUEST,
        description="string",
        blocks_claim_submission=True,
        assignee_user_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        category=TaskCategory.OTHER,
        work_queue_id="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `TaskCreateV3` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.v_3.<a href="src/candid/resources/tasks/resources/v_3/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient
from candid.resources.tasks import TaskStatus
from candid.resources.tasks.v_3 import TaskUpdateV3

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tasks.v_3.update(
    task_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=TaskUpdateV3(
        status=TaskStatus.FINISHED,
        assignee_user_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        blocks_claim_submission=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `TaskId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TaskUpdateV3` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WriteOffs V1
<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all write-offs satisfying the search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import AccountType, SortDirection
from candid.client import CandidApiClient
from candid.resources.write_offs.v_1 import WriteOffSortField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.get_multi(
    limit=1,
    patient_external_id="string",
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    claim_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    billing_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    sort=WriteOffSortField.AMOUNT_CENTS,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    account_types=AccountType.PATIENT,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100. The value must be greater than 0 and less than 1000.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[PatientExternalId]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[PayerUuid]` 
    
</dd>
</dl>

<dl>
<dd>

**service_line_id:** `typing.Optional[ServiceLineId]` 
    
</dd>
</dl>

<dl>
<dd>

**claim_id:** `typing.Optional[ClaimId]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_id:** `typing.Optional[ProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[WriteOffSortField]` — Defaults to write_off_timestamp
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**account_types:** `typing.Optional[typing.Union[AccountType, typing.Sequence[AccountType]]]` — Filters the returned values to include only the provided account types.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a previously created write off by its `write_off_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.get(
    write_off_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**write_off_id:** `WriteOffId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one or many write-offs applied toward a specific service line,
claim, or billing provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.write_offs.v_1 import (
    PatientWriteOffReason,
    WriteOffCreate_Patient,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.create(
    write_offs=[
        WriteOffCreate_Patient(
            write_off_timestamp=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            write_off_note="string",
            write_off_reason=PatientWriteOffReason.SMALL_BALANCE,
            service_line_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            amount_cents=1,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**write_offs:** `typing.Sequence[WriteOffCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.write_offs.v_1.<a href="src/candid/resources/write_offs/resources/v_1/client.py">revert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reverts a write off given a `write_off_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.write_offs.v_1.revert(
    write_off_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**write_off_id:** `WriteOffId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Appointments V1
<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds an appointment. VersionConflictError is returned when the placer_appointment_id is already in use.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid.client import CandidApiClient
from candid.resources.pre_encounter import (
    ContactPoint,
    ContactPointUse,
    ExternalProvider,
    ExternalProviderType,
    HumanName,
    NameUse,
    Period,
)
from candid.resources.pre_encounter.appointments.v_1 import (
    AppointmentStatus,
    AppointmentWorkQueue,
    MutableAppointment,
    Service,
    UniversalServiceIdentifier,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.create(
    request=MutableAppointment(
        patient_id="string",
        start_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        status=AppointmentStatus.PENDING,
        service_duration=1,
        services=[
            Service(
                universal_service_identifier=UniversalServiceIdentifier.MD_VISIT,
                start_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )
        ],
        placer_appointment_id="string",
        attending_doctor=ExternalProvider(
            name=HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            ),
            type=ExternalProviderType.PRIMARY,
            npi="string",
            telecoms=[
                ContactPoint(
                    value="string",
                    use=ContactPointUse.HOME,
                )
            ],
            addresses=[],
            period=Period(),
            canonical_id="string",
        ),
        estimated_copay_cents=1,
        estimated_patient_responsibility_cents=1,
        patient_deposit_cents=1,
        checked_in_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        notes="string",
        location_resource_id="string",
        automated_eligibility_check_complete=True,
        work_queue=AppointmentWorkQueue.EMERGENT_ISSUE,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableAppointment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an appointment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.get(
    id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AppointmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an appointment along with it's full history. The return list is ordered by version ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.get_history(
    id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AppointmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an appointment. The path must contain the most recent version to prevent race conditions. Updating historic versions is not supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid.client import CandidApiClient
from candid.resources.pre_encounter import (
    ContactPoint,
    ContactPointUse,
    ExternalProvider,
    ExternalProviderType,
    HumanName,
    NameUse,
    Period,
)
from candid.resources.pre_encounter.appointments.v_1 import (
    AppointmentStatus,
    AppointmentWorkQueue,
    MutableAppointment,
    Service,
    UniversalServiceIdentifier,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.update(
    id="string",
    version="string",
    request=MutableAppointment(
        patient_id="string",
        start_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        status=AppointmentStatus.PENDING,
        service_duration=1,
        services=[
            Service(
                universal_service_identifier=UniversalServiceIdentifier.MD_VISIT,
                start_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )
        ],
        placer_appointment_id="string",
        attending_doctor=ExternalProvider(
            name=HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            ),
            type=ExternalProviderType.PRIMARY,
            npi="string",
            telecoms=[
                ContactPoint(
                    value="string",
                    use=ContactPointUse.HOME,
                )
            ],
            addresses=[],
            period=Period(),
            canonical_id="string",
        ),
        estimated_copay_cents=1,
        estimated_patient_responsibility_cents=1,
        patient_deposit_cents=1,
        checked_in_timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        notes="string",
        location_resource_id="string",
        automated_eligibility_check_complete=True,
        work_queue=AppointmentWorkQueue.EMERGENT_ISSUE,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AppointmentId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableAppointment` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">scan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scans up to 100 appointment updates. The since query parameter is inclusive, and the result list is ordered by updatedAt ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.scan(
    since=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.appointments.v_1.<a href="src/candid/resources/pre_encounter/resources/appointments/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets an appointment as deactivated. The path must contain the most recent version to prevent race conditions. Deactivating historic versions is not supported. Subsequent updates via PUT to the appointment will "reactivate" the appointment and set the deactivated flag to false.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.appointments.v_1.deactivate(
    id="string",
    version="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AppointmentId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Coverages V1
<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new Coverage. A Coverage provides the high-level identifiers and descriptors of a specific insurance plan for a specific individual - typically the information you can find on an insurance card. Additionally a coverage will include detailed benefits information covered by the specific plan for the individual.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid.client import CandidApiClient
from candid.resources.pre_encounter import (
    AdditionalPayerInformation,
    Address,
    AddressUse,
    HumanName,
    NameUse,
    Period,
    Relationship,
    Sex,
)
from candid.resources.pre_encounter.coverages.v_1 import (
    CoverageBenefits,
    CoverageStatus,
    EligibilityCheckMetadata,
    EligibilityCheckStatus,
    EligibilityStatus,
    InsurancePlan,
    InsuranceTypeCode,
    LatestEligibilityCheck,
    MutableCoverage,
    NetworkType,
    ServiceTypeCode,
    Subscriber,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.create(
    request=MutableCoverage(
        status=CoverageStatus.ACTIVE,
        subscriber=Subscriber(
            name=HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            ),
            date_of_birth=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            biological_sex=Sex.FEMALE,
            address=Address(
                use=AddressUse.HOME,
                line=["string"],
                city="string",
                state="string",
                postal_code="string",
                country="string",
                period=Period(),
            ),
        ),
        relationship=Relationship.SELF,
        patient="string",
        insurance_plan=InsurancePlan(
            member_id="string",
            payer_id="string",
            payer_name="string",
            additional_payer_information=AdditionalPayerInformation(
                availity_eligibility_id="string",
                availity_payer_id="string",
                availity_payer_name="string",
                availity_remittance_payer_id="string",
            ),
            group_number="string",
            name="string",
            plan_type=NetworkType.SELF_PAY,
            type=InsuranceTypeCode.C_01,
            period=Period(),
            insurance_card_image_locator="string",
        ),
        verified=True,
        eligibility_checks=[
            EligibilityCheckMetadata(
                check_id="string",
                service_code=ServiceTypeCode.MEDICAL_CARE,
                status=EligibilityCheckStatus.CREATED,
                initiated_by="string",
                initiated_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )
        ],
        latest_eligibility_check=LatestEligibilityCheck(
            check_id="string",
            status=EligibilityStatus.ACTIVE,
            initiated_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        ),
        benefits=CoverageBenefits(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableCoverage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Coverage. The path must contain the most recent version to prevent race conditions. Updating historic versions is not supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.pre_encounter import (
    AdditionalPayerInformation,
    Address,
    AddressUse,
    HumanName,
    NameUse,
    Period,
    Relationship,
    Sex,
)
from candid.resources.pre_encounter.coverages.v_1 import (
    CoverageBenefits,
    CoverageStatus,
    EligibilityCheckMetadata,
    EligibilityCheckStatus,
    EligibilityStatus,
    InsurancePlan,
    InsuranceTypeCode,
    LatestEligibilityCheck,
    MutableCoverage,
    NetworkType,
    ServiceTypeCode,
    Subscriber,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.update(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    version="string",
    request=MutableCoverage(
        status=CoverageStatus.ACTIVE,
        subscriber=Subscriber(
            name=HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            ),
            date_of_birth=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            biological_sex=Sex.FEMALE,
            address=Address(
                use=AddressUse.HOME,
                line=["string"],
                city="string",
                state="string",
                postal_code="string",
                country="string",
                period=Period(),
            ),
        ),
        relationship=Relationship.SELF,
        patient="string",
        insurance_plan=InsurancePlan(
            member_id="string",
            payer_id="string",
            payer_name="string",
            additional_payer_information=AdditionalPayerInformation(
                availity_eligibility_id="string",
                availity_payer_id="string",
                availity_payer_name="string",
                availity_remittance_payer_id="string",
            ),
            group_number="string",
            name="string",
            plan_type=NetworkType.SELF_PAY,
            type=InsuranceTypeCode.C_01,
            period=Period(),
            insurance_card_image_locator="string",
        ),
        verified=True,
        eligibility_checks=[
            EligibilityCheckMetadata(
                check_id="string",
                service_code=ServiceTypeCode.MEDICAL_CARE,
                status=EligibilityCheckStatus.CREATED,
                initiated_by="string",
                initiated_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )
        ],
        latest_eligibility_check=LatestEligibilityCheck(
            check_id="string",
            status=EligibilityStatus.ACTIVE,
            initiated_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        ),
        benefits=CoverageBenefits(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableCoverage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

gets a specific Coverage
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a coverage along with it's full history. The return list is ordered by version ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get_history(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Coverages based on the search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get_multi(
    patient_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patient_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">scan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scans up to 100 coverage updates. The since query parameter is inclusive, and the result list is ordered by updatedAt ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.scan(
    since=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">check_eligibility</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an eligibility check. Returns the metadata of the check if successfully initiated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.pre_encounter.coverages.v_1 import ServiceTypeCode

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.check_eligibility(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    service_code=ServiceTypeCode.MEDICAL_CARE,
    date_of_service=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    npi="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**service_code:** `ServiceTypeCode` 
    
</dd>
</dl>

<dl>
<dd>

**date_of_service:** `dt.date` 
    
</dd>
</dl>

<dl>
<dd>

**npi:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.coverages.v_1.<a href="src/candid/resources/pre_encounter/resources/coverages/resources/v_1/client.py">get_eligibility</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the eligibility of a patient for a specific coverage if successful.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.coverages.v_1.get_eligibility(
    id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    check_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `CoverageId` 
    
</dd>
</dl>

<dl>
<dd>

**check_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Lists V1
<details><summary><code>client.pre_encounter.lists.v_1.<a href="src/candid/resources/pre_encounter/resources/lists/resources/v_1/client.py">get_patient_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets patients with dependent objects for patients that match the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient
from candid.resources.pre_encounter import SortDirection

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.lists.v_1.get_patient_list(
    page_token="string",
    limit=1,
    sort_field="string",
    sort_direction=SortDirection.ASC,
    filters="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[SortFieldString]` — Defaults to patient.updatedAt.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Defaults to ascending.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[FilterQueryString]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.lists.v_1.<a href="src/candid/resources/pre_encounter/resources/lists/resources/v_1/client.py">get_appointment_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for appointments that match the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient
from candid.resources.pre_encounter import SortDirection

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.lists.v_1.get_appointment_list(
    sort_field="string",
    sort_direction=SortDirection.ASC,
    limit=1,
    page_token="string",
    filters="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sort_field:** `typing.Optional[SortFieldString]` — Defaults to appointment.startTimestamp.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[FilterQueryString]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Notes V1
<details><summary><code>client.pre_encounter.notes.v_1.<a href="src/candid/resources/pre_encounter/resources/notes/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a note by NoteId.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.notes.v_1.get(
    id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `NoteId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.notes.v_1.<a href="src/candid/resources/pre_encounter/resources/notes/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new note.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient
from candid.resources.pre_encounter.notes.v_1 import MutableNote

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.notes.v_1.create(
    request=MutableNote(
        value="string",
        author_email="string",
        author_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableNote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.notes.v_1.<a href="src/candid/resources/pre_encounter/resources/notes/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a note. The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient
from candid.resources.pre_encounter.notes.v_1 import MutableNote

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.notes.v_1.update(
    id="string",
    version="string",
    request=MutableNote(
        value="string",
        author_email="string",
        author_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `NoteId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableNote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.notes.v_1.<a href="src/candid/resources/pre_encounter/resources/notes/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a note as deactivated. The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.notes.v_1.deactivate(
    id="string",
    version="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `NoteId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Patients V1
<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a patient. VersionConflictError is returned when the patient's external ID is already in use.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.pre_encounter import (
    Address,
    AddressUse,
    CanonicalNonInsurancePayerAssociation,
    ContactPoint,
    ContactPointUse,
    DisabilityStatus,
    Ethnicity,
    ExternalProvider,
    ExternalProviderType,
    Gender,
    HumanName,
    NameUse,
    Period,
    Race,
    Relationship,
    Sex,
    SexualOrientation,
)
from candid.resources.pre_encounter.patients.v_1 import (
    Authorization,
    AuthorizationUnit,
    Contact,
    DoNotInvoiceReason,
    ExternalProvenance,
    FilingOrder,
    Guarantor,
    MaritalStatus,
    MutablePatient,
    Referral,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.create(
    skip_duplicate_check=True,
    request=MutablePatient(
        name=HumanName(
            family="string",
            given=["string"],
            use=NameUse.USUAL,
            period=Period(),
        ),
        other_names=[
            HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            )
        ],
        gender=Gender.MAN,
        birth_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        social_security_number="string",
        biological_sex=Sex.FEMALE,
        sexual_orientation=SexualOrientation.HETEROSEXUAL,
        race=Race.AMERICAN_INDIAN_OR_ALASKA_NATIVE,
        ethnicity=Ethnicity.HISPANIC_OR_LATINO,
        disability_status=DisabilityStatus.DISABLED,
        marital_status=MaritalStatus.ANNULLED,
        deceased=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        multiple_birth=1,
        primary_address=Address(
            use=AddressUse.HOME,
            line=["string"],
            city="string",
            state="string",
            postal_code="string",
            country="string",
            period=Period(),
        ),
        other_addresses=[
            Address(
                use=AddressUse.HOME,
                line=["string"],
                city="string",
                state="string",
                postal_code="string",
                country="string",
                period=Period(),
            )
        ],
        primary_telecom=ContactPoint(
            value="string",
            use=ContactPointUse.HOME,
        ),
        other_telecoms=[
            ContactPoint(
                value="string",
                use=ContactPointUse.HOME,
            )
        ],
        email="string",
        electronic_communication_opt_in=True,
        photo="string",
        language="string",
        external_provenance=ExternalProvenance(
            external_id="string",
            system_name="string",
        ),
        contacts=[
            Contact(
                relationship=[Relationship.SELF],
                name=HumanName(
                    family="string",
                    given=["string"],
                    use=NameUse.USUAL,
                    period=Period(),
                ),
                telecoms=[
                    ContactPoint(
                        value="string",
                        use=ContactPointUse.HOME,
                    )
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["string"],
                        city="string",
                        state="string",
                        postal_code="string",
                        country="string",
                        period=Period(),
                    )
                ],
                period=Period(),
                hipaa_authorization=True,
            )
        ],
        general_practitioners=[
            ExternalProvider(
                name=HumanName(
                    family="string",
                    given=["string"],
                    use=NameUse.USUAL,
                    period=Period(),
                ),
                type=ExternalProviderType.PRIMARY,
                npi="string",
                telecoms=[
                    ContactPoint(
                        value="string",
                        use=ContactPointUse.HOME,
                    )
                ],
                addresses=[],
                period=Period(),
                canonical_id="string",
            )
        ],
        filing_order=FilingOrder(
            coverages=[
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ],
        ),
        non_insurance_payers=["string"],
        non_insurance_payer_associations=[
            CanonicalNonInsurancePayerAssociation(
                id="string",
            )
        ],
        guarantor=Guarantor(
            name=HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            ),
            telecom=ContactPoint(
                value="string",
                use=ContactPointUse.HOME,
            ),
            email="string",
            birth_date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            address=Address(
                use=AddressUse.HOME,
                line=["string"],
                city="string",
                state="string",
                postal_code="string",
                country="string",
                period=Period(),
            ),
        ),
        self_pay=True,
        authorizations=[
            Authorization(
                payer_id="string",
                payer_name="string",
                authorization_number="string",
                cpt_code="string",
                units=AuthorizationUnit.VISIT,
            )
        ],
        referrals=[
            Referral(
                provider=ExternalProvider(
                    name=HumanName(
                        family="string",
                        given=["string"],
                        use=NameUse.USUAL,
                        period=Period(),
                    ),
                    type=ExternalProviderType.PRIMARY,
                    npi="string",
                    telecoms=[
                        ContactPoint(
                            value="string",
                            use=ContactPointUse.HOME,
                        )
                    ],
                    addresses=[],
                    period=Period(),
                    canonical_id="string",
                ),
                referral_number="string",
            )
        ],
        primary_service_facility_id="string",
        do_not_invoice_reason=DoNotInvoiceReason.BANKRUPTCY,
        note_ids=["string"],
        tag_ids=["string"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutablePatient` 
    
</dd>
</dl>

<dl>
<dd>

**skip_duplicate_check:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">create_with_mrn</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a patient and hydrates their MRN with a pre-existing MRN. Once this patient is created their MRN will not be editable. BadRequestError is returned when the MRN is greater than 20 characters. VersionConflictError is returned when the patient's external ID is already in use.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.pre_encounter import (
    Address,
    AddressUse,
    CanonicalNonInsurancePayerAssociation,
    ContactPoint,
    ContactPointUse,
    DisabilityStatus,
    Ethnicity,
    ExternalProvider,
    ExternalProviderType,
    Gender,
    HumanName,
    NameUse,
    Period,
    Race,
    Relationship,
    Sex,
    SexualOrientation,
)
from candid.resources.pre_encounter.patients.v_1 import (
    Authorization,
    AuthorizationUnit,
    Contact,
    DoNotInvoiceReason,
    ExternalProvenance,
    FilingOrder,
    Guarantor,
    MaritalStatus,
    MutablePatientWithMrn,
    Referral,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.create_with_mrn(
    skip_duplicate_check=True,
    request=MutablePatientWithMrn(
        mrn="string",
        name=HumanName(
            family="string",
            given=["string"],
            use=NameUse.USUAL,
            period=Period(),
        ),
        other_names=[
            HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            )
        ],
        gender=Gender.MAN,
        birth_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        social_security_number="string",
        biological_sex=Sex.FEMALE,
        sexual_orientation=SexualOrientation.HETEROSEXUAL,
        race=Race.AMERICAN_INDIAN_OR_ALASKA_NATIVE,
        ethnicity=Ethnicity.HISPANIC_OR_LATINO,
        disability_status=DisabilityStatus.DISABLED,
        marital_status=MaritalStatus.ANNULLED,
        deceased=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        multiple_birth=1,
        primary_address=Address(
            use=AddressUse.HOME,
            line=["string"],
            city="string",
            state="string",
            postal_code="string",
            country="string",
            period=Period(),
        ),
        other_addresses=[
            Address(
                use=AddressUse.HOME,
                line=["string"],
                city="string",
                state="string",
                postal_code="string",
                country="string",
                period=Period(),
            )
        ],
        primary_telecom=ContactPoint(
            value="string",
            use=ContactPointUse.HOME,
        ),
        other_telecoms=[
            ContactPoint(
                value="string",
                use=ContactPointUse.HOME,
            )
        ],
        email="string",
        electronic_communication_opt_in=True,
        photo="string",
        language="string",
        external_provenance=ExternalProvenance(
            external_id="string",
            system_name="string",
        ),
        contacts=[
            Contact(
                relationship=[Relationship.SELF],
                name=HumanName(
                    family="string",
                    given=["string"],
                    use=NameUse.USUAL,
                    period=Period(),
                ),
                telecoms=[
                    ContactPoint(
                        value="string",
                        use=ContactPointUse.HOME,
                    )
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["string"],
                        city="string",
                        state="string",
                        postal_code="string",
                        country="string",
                        period=Period(),
                    )
                ],
                period=Period(),
                hipaa_authorization=True,
            )
        ],
        general_practitioners=[
            ExternalProvider(
                name=HumanName(
                    family="string",
                    given=["string"],
                    use=NameUse.USUAL,
                    period=Period(),
                ),
                type=ExternalProviderType.PRIMARY,
                npi="string",
                telecoms=[
                    ContactPoint(
                        value="string",
                        use=ContactPointUse.HOME,
                    )
                ],
                addresses=[],
                period=Period(),
                canonical_id="string",
            )
        ],
        filing_order=FilingOrder(
            coverages=[
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ],
        ),
        non_insurance_payers=["string"],
        non_insurance_payer_associations=[
            CanonicalNonInsurancePayerAssociation(
                id="string",
            )
        ],
        guarantor=Guarantor(
            name=HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            ),
            telecom=ContactPoint(
                value="string",
                use=ContactPointUse.HOME,
            ),
            email="string",
            birth_date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            address=Address(
                use=AddressUse.HOME,
                line=["string"],
                city="string",
                state="string",
                postal_code="string",
                country="string",
                period=Period(),
            ),
        ),
        self_pay=True,
        authorizations=[
            Authorization(
                payer_id="string",
                payer_name="string",
                authorization_number="string",
                cpt_code="string",
                units=AuthorizationUnit.VISIT,
            )
        ],
        referrals=[
            Referral(
                provider=ExternalProvider(
                    name=HumanName(
                        family="string",
                        given=["string"],
                        use=NameUse.USUAL,
                        period=Period(),
                    ),
                    type=ExternalProviderType.PRIMARY,
                    npi="string",
                    telecoms=[
                        ContactPoint(
                            value="string",
                            use=ContactPointUse.HOME,
                        )
                    ],
                    addresses=[],
                    period=Period(),
                    canonical_id="string",
                ),
                referral_number="string",
            )
        ],
        primary_service_facility_id="string",
        do_not_invoice_reason=DoNotInvoiceReason.BANKRUPTCY,
        note_ids=["string"],
        tag_ids=["string"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutablePatientWithMrn` 
    
</dd>
</dl>

<dl>
<dd>

**skip_duplicate_check:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for patients that match the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient
from candid.resources.pre_encounter import SortDirection

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.get_multi(
    limit=1,
    mrn="string",
    page_token="string",
    sort_field="string",
    sort_direction=SortDirection.ASC,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mrn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[PatientSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Defaults to ascending.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.get(
    id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient along with it's full history. The return list is ordered by version ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.get_history(
    id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient. The path must contain the most recent version to prevent race conditions. Updating historic versions is not supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid.client import CandidApiClient
from candid.resources.pre_encounter import (
    Address,
    AddressUse,
    CanonicalNonInsurancePayerAssociation,
    ContactPoint,
    ContactPointUse,
    DisabilityStatus,
    Ethnicity,
    ExternalProvider,
    ExternalProviderType,
    Gender,
    HumanName,
    NameUse,
    Period,
    Race,
    Relationship,
    Sex,
    SexualOrientation,
)
from candid.resources.pre_encounter.patients.v_1 import (
    Authorization,
    AuthorizationUnit,
    Contact,
    DoNotInvoiceReason,
    ExternalProvenance,
    FilingOrder,
    Guarantor,
    MaritalStatus,
    MutablePatient,
    Referral,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.update(
    id="string",
    version="string",
    request=MutablePatient(
        name=HumanName(
            family="string",
            given=["string"],
            use=NameUse.USUAL,
            period=Period(),
        ),
        other_names=[
            HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            )
        ],
        gender=Gender.MAN,
        birth_date=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        social_security_number="string",
        biological_sex=Sex.FEMALE,
        sexual_orientation=SexualOrientation.HETEROSEXUAL,
        race=Race.AMERICAN_INDIAN_OR_ALASKA_NATIVE,
        ethnicity=Ethnicity.HISPANIC_OR_LATINO,
        disability_status=DisabilityStatus.DISABLED,
        marital_status=MaritalStatus.ANNULLED,
        deceased=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        multiple_birth=1,
        primary_address=Address(
            use=AddressUse.HOME,
            line=["string"],
            city="string",
            state="string",
            postal_code="string",
            country="string",
            period=Period(),
        ),
        other_addresses=[
            Address(
                use=AddressUse.HOME,
                line=["string"],
                city="string",
                state="string",
                postal_code="string",
                country="string",
                period=Period(),
            )
        ],
        primary_telecom=ContactPoint(
            value="string",
            use=ContactPointUse.HOME,
        ),
        other_telecoms=[
            ContactPoint(
                value="string",
                use=ContactPointUse.HOME,
            )
        ],
        email="string",
        electronic_communication_opt_in=True,
        photo="string",
        language="string",
        external_provenance=ExternalProvenance(
            external_id="string",
            system_name="string",
        ),
        contacts=[
            Contact(
                relationship=[Relationship.SELF],
                name=HumanName(
                    family="string",
                    given=["string"],
                    use=NameUse.USUAL,
                    period=Period(),
                ),
                telecoms=[
                    ContactPoint(
                        value="string",
                        use=ContactPointUse.HOME,
                    )
                ],
                addresses=[
                    Address(
                        use=AddressUse.HOME,
                        line=["string"],
                        city="string",
                        state="string",
                        postal_code="string",
                        country="string",
                        period=Period(),
                    )
                ],
                period=Period(),
                hipaa_authorization=True,
            )
        ],
        general_practitioners=[
            ExternalProvider(
                name=HumanName(
                    family="string",
                    given=["string"],
                    use=NameUse.USUAL,
                    period=Period(),
                ),
                type=ExternalProviderType.PRIMARY,
                npi="string",
                telecoms=[
                    ContactPoint(
                        value="string",
                        use=ContactPointUse.HOME,
                    )
                ],
                addresses=[],
                period=Period(),
                canonical_id="string",
            )
        ],
        filing_order=FilingOrder(
            coverages=[
                uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                )
            ],
        ),
        non_insurance_payers=["string"],
        non_insurance_payer_associations=[
            CanonicalNonInsurancePayerAssociation(
                id="string",
            )
        ],
        guarantor=Guarantor(
            name=HumanName(
                family="string",
                given=["string"],
                use=NameUse.USUAL,
                period=Period(),
            ),
            telecom=ContactPoint(
                value="string",
                use=ContactPointUse.HOME,
            ),
            email="string",
            birth_date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            address=Address(
                use=AddressUse.HOME,
                line=["string"],
                city="string",
                state="string",
                postal_code="string",
                country="string",
                period=Period(),
            ),
        ),
        self_pay=True,
        authorizations=[
            Authorization(
                payer_id="string",
                payer_name="string",
                authorization_number="string",
                cpt_code="string",
                units=AuthorizationUnit.VISIT,
            )
        ],
        referrals=[
            Referral(
                provider=ExternalProvider(
                    name=HumanName(
                        family="string",
                        given=["string"],
                        use=NameUse.USUAL,
                        period=Period(),
                    ),
                    type=ExternalProviderType.PRIMARY,
                    npi="string",
                    telecoms=[
                        ContactPoint(
                            value="string",
                            use=ContactPointUse.HOME,
                        )
                    ],
                    addresses=[],
                    period=Period(),
                    canonical_id="string",
                ),
                referral_number="string",
            )
        ],
        primary_service_facility_id="string",
        do_not_invoice_reason=DoNotInvoiceReason.BANKRUPTCY,
        note_ids=["string"],
        tag_ids=["string"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutablePatient` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a patient as deactivated. The path must contain the most recent version to prevent race conditions. Deactivating historic versions is not supported. Subsequent updates via PUT to the patient will "reactivate" the patient and set the deactivated flag to false.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.deactivate(
    id="string",
    version="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PatientId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Patients based on the search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.search(
    mrn="string",
    similar_name_ordering="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mrn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**similar_name_ordering:** `typing.Optional[str]` — A string that is used to order similar names in search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.patients.v_1.<a href="src/candid/resources/pre_encounter/resources/patients/resources/v_1/client.py">scan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scans up to 100 patient updates. The since query parameter is inclusive, and the result list is ordered by updatedAt ascending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.patients.v_1.scan(
    since=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PreEncounter Tags V1
<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a tag by TagId.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.get(
    id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `TagId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets all tags. Defaults to page size of 1000.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.get_all(
    limit=1,
    page_token="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new tag if it does not already exist, otherwise, returns the existing tag.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient
from candid.resources.pre_encounter.tags.v_1 import MutableTag

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.create(
    request=MutableTag(
        value="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `MutableTag` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a tag. The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient
from candid.resources.pre_encounter.tags.v_1 import MutableTag

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.update(
    id="string",
    version="string",
    request=MutableTag(
        value="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `TagId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutableTag` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pre_encounter.tags.v_1.<a href="src/candid/resources/pre_encounter/resources/tags/resources/v_1/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a tag as deactivated. The path must contain the most recent version to prevent races.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.pre_encounter.tags.v_1.deactivate(
    id="string",
    version="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `TagId` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Diagnoses
<details><summary><code>client.diagnoses.<a href="src/candid/resources/diagnoses/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new diagnosis for an encounter
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import DiagnosisTypeCode, StandaloneDiagnosisCreate
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.diagnoses.create(
    request=StandaloneDiagnosisCreate(
        encounter_id=uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        ),
        name="string",
        code_type=DiagnosisTypeCode.ABF,
        code="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `StandaloneDiagnosisCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.diagnoses.<a href="src/candid/resources/diagnoses/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the diagnosis record matching the provided `diagnosis_id`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import DiagnosisTypeCode
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.diagnoses.update(
    diagnosis_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    name="string",
    code_type=DiagnosisTypeCode.ABF,
    code="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**diagnosis_id:** `DiagnosisId` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Empty string not allowed.
    
</dd>
</dl>

<dl>
<dd>

**code_type:** `typing.Optional[DiagnosisTypeCode]` — Typically, providers submitting claims to Candid are using ICD-10 diagnosis codes. If you are using ICD-10 codes, the primary diagnosis code listed on the claim should use the ABK code_type. If more than one diagnosis is being submitted on a claim, please use ABF for the rest of the listed diagnoses. If you are using ICD-9 diagnosis codes, use BK and BF for the principal and following diagnosis code(s) respectively.

    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 

Empty string not allowed.
Should be of the appropriate format for the provided `code_type`.
Must obey the ICD-10 format if an ICD-10 code_type is provided, specifically:
  - Letter
  - Digit
  - Digit or the letter `A` or `B`
  - (Optional) Period `.`
  - Up to 4 (or as few as 0) letters and digits

    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.diagnoses.<a href="src/candid/resources/diagnoses/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the diagnosis record associated with the provided `diagnosis_id`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.diagnoses.delete(
    diagnosis_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**diagnosis_id:** `DiagnosisId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ServiceFacility
<details><summary><code>client.service_facility.<a href="src/candid/resources/service_facility/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import EncounterServiceFacilityUpdate, State, StreetAddressLongZip
from candid.client import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.service_facility.update(
    service_facility_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=EncounterServiceFacilityUpdate(
        organization_name="Test Organization",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_facility_id:** `ServiceFacilityId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EncounterServiceFacilityUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

