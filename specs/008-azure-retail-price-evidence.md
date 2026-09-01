# Spec 008 — Azure retail price evidence slice

## Goal

Add one small, free, structurally different evidence source using Microsoft Azure’s official Retail Prices API.

This slice should test whether the existing weak `SourceObservation` envelope can honestly represent **source-native supply-side price evidence**: comparable cloud compute offerings whose retail prices vary across otherwise comparable regions/SKUs.

This is an empirical pricing slice, not a cloud-cost optimizer, arbitrage engine, or cross-provider comparison product.

## Why this source / why now

The project has already observed several distinct economic signals:

- Stack Exchange — articulated individual decision friction,
- CFPB — realised consumer financial pain,
- TED — institutional procurement demand and explicit budgets,
- Eurostat — market structure / economic denominator evidence,
- DataForSEO — search-demand/commercial-intent adapter implemented, but not yet run against paid production data.

The largest remaining gap is direct supply-side / price evidence:

> what suppliers actually charge for comparable economic units, and how much complexity or dispersion exists in the offer structure.

Microsoft documents the Azure Retail Prices API as an unauthenticated programmatic interface for retail rates across Azure services, regions, and SKUs. The documentation explicitly describes using the API for price comparison across SKUs and regions.

Relevant first-party reference:

- https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices

The API is public and does not require authentication.

This source is intentionally narrow. It gives us one provider’s source-native pricing surface. It does **not** establish cross-provider market fragmentation or a monetizable arbitrage by itself.

## Empirical question

> Can the same weak observation envelope represent directly comparable supplier price points without pretending that price dispersion alone proves an information asymmetry?

Secondary questions to inspect after the real run:

- Do identical or near-identical VM SKUs show material retail-price variation across European regions?
- How much additional complexity comes from meter/product/type variants even after tightly filtering the query?
- Are source-native identifiers and effective dates stable enough to treat each returned meter price as an honest observation?
- Does this source reinforce the already observed distinction between event/record evidence and changing measurement evidence?
- Does direct price evidence add enough information value to justify seeking other pricing/supply sources later?

Do not answer these questions in code. Preserve the evidence and report what the live slice shows.

## API

Use Microsoft’s official Azure Retail Prices endpoint:

`GET https://prices.azure.com/api/retail/prices`

Use anonymous access only.

Use the current documented API version that supports the required filtering reliably. Prefer a stable documented version over preview-only features because savings-plan data are not needed for this experiment.

Do not authenticate, scrape Azure pricing pages, use the Azure portal, or use third-party cloud-price datasets.

## Empirical slice

Retrieve a deliberately narrow set of **on-demand consumption prices for a few common general-purpose Azure Virtual Machine SKUs across several European regions**.

The intention is to hold the supplied compute product as constant as practical while allowing geography to vary.

Use these ARM SKU names if the live API confirms they currently return clean standard consumption prices:

- `Standard_D2s_v5`
- `Standard_D4s_v5`
- `Standard_D8s_v5`

Use these European ARM regions if the live API confirms them:

- `westeurope`
- `northeurope`
- `germanywestcentral`
- `francecentral`
- `polandcentral`

Use USD so the returned retail prices are Microsoft’s source pricing currency and no currency conversion is introduced.

Filter to standard on-demand `Consumption` pricing. Exclude reservations, dev/test, spot, and savings-plan variants from the empirical slice.

If Microsoft’s current API representation makes the exact filter names or values slightly different, Codex must confirm the current documented/source-native fields and use the closest clean equivalent. Report the exact final filter.

### Important comparability constraint

Do not assume that every row sharing an ARM SKU is economically identical.

Preserve `productName`, `skuName`, `meterName`, `type`, region, unit, and any other returned discriminator needed to see whether Windows/software-loaded variants or other meter distinctions remain.

If the API returns multiple materially different product/meter variants for the same ARM SKU/region even after the intended filter, preserve them rather than silently choosing one. Report the complication.

Do not write product-selection heuristics merely to force a cleaner answer.

## Request bounds

Use one filtered API request per CLI invocation if the documented OData filter can express the selected SKUs and regions cleanly.

The expected filtered result should remain well below the API’s 1,000-row page size.

Do not follow `NextPageLink` for this slice. If the tightly filtered live query unexpectedly exceeds one page, report that fact and stop rather than implementing pagination.

No generic Azure query builder is needed.

## Source metadata

Add a stable `SignalSource`, for example:

`azure:retail-prices`

Record at least:

- access method: official Azure Retail Prices API,
- access cost: free / unauthenticated,
- source: Microsoft Azure retail pricing,
- empirical scope: selected Dsv5 VM SKUs across selected European regions,
- currency: USD,
- evidence semantics: supplier-published retail price measurement, not observed transaction price,
- important selection/interpretation caveats:
  - this is one supplier, not a whole market,
  - retail/list price is not necessarily realized customer price,
  - enterprise agreements, negotiated discounts, taxes, support, egress and other charges are not represented by the single meter price,
  - regional differences can reflect cost structure, capacity, regulation, service availability, or product differences rather than exploitable asymmetry,
  - apparently similar rows can differ by product/meter/type,
  - prices can change while the underlying SKU/meter identity remains stable,
  - price dispersion alone does not establish information asymmetry or commercial opportunity.

The Microsoft documentation supports programmatic price analysis/comparison. Do not create a generalized licensing subsystem in this slice. Do not commit a bulk pricing corpus.

## Observation granularity

Represent each returned **source-native retail-price item / meter rate** as one `SourceObservation`.

Do not aggregate several regions into one observation.

Do not calculate a region spread or cheapest-region observation in the collector.

Use:

`item_kind=retail_price`

## Observation identity

Use the most stable combination of source-native identifiers that describes the priced meter independent of the numeric price itself.

Prefer Azure’s stable IDs where available, including concepts such as:

- `meterId`,
- `productId`,
- `skuId`,
- region,
- price type / meter type,
- reservation term only if relevant (it should not be for this on-demand slice),
- unit/tier when needed to prevent collisions.

A conceptual identity might resemble:

`azure:retail-price:<meterId>:<armRegionName>:<type>:<tier>`

but Codex should choose the simplest collision-resistant encoding based on the live response.

Do **not** include `retailPrice`, `unitPrice`, `effectiveStartDate`, or collection time merely to make revisions unique.

This is deliberate. A later price change for the same priced meter should expose the same revision/history pressure already seen with DataForSEO and Eurostat rather than being hidden by value-based identity.

Keep existing repository deduplication semantics unchanged.

## Timestamps

Use collection time as `observed_at`.

Use Azure’s source-native `effectiveStartDate` as `occurred_at` when present and parseable because it represents when that published price became effective.

If the API omits the effective date, use `occurred_at=None` rather than inventing one.

Do not use collection date as the price effective date.

## Readable `content`

`SourceObservation.content` should remain a concise source-faithful projection, including available values such as:

- service / product name,
- ARM SKU,
- SKU / meter name,
- Azure region / location,
- retail price,
- currency,
- unit of measure,
- pricing/meter type,
- effective start date,
- tier minimum units if relevant.

Do not calculate:

- cheapest region,
- percentage spread,
- monthly equivalent,
- annual equivalent,
- savings,
- arbitrage value,
- TCO,
- workload recommendation,
- opportunity score.

Those may be computed only in the completion report for empirical inspection where explicitly requested below.

## Metadata

Preserve useful source-native fields returned for each item, including where available:

- currencyCode,
- tierMinimumUnits,
- retailPrice,
- unitPrice,
- armRegionName,
- location,
- effectiveStartDate,
- meterId,
- meterName,
- productId,
- skuId,
- productName,
- skuName,
- serviceName,
- serviceId,
- serviceFamily,
- unitOfMeasure,
- type / price type,
- isPrimaryMeterRegion,
- armSkuName.

Do not introduce a generic product/offer model yet.

## CLI

Add a small command consistent with existing collectors, for example:

`asymmetry-engine collect-azure-prices --database <path>`

The SKU list, region list, currency and pricing type may remain fixed for this empirical slice.

Do not build CLI parameters for arbitrary cloud-price queries.

## Persistence and deduplication

Reuse the existing pipeline, repository, SQLite schema, source transaction semantics, and `(source_id, external_id)` deduplication behavior unchanged.

Use a fresh SQLite database for the live run.

Run the identical command twice:

- first run should insert the returned retail-price observations,
- second run should demonstrate deduplication for unchanged meter identities.

If Azure changes a price or response composition between immediate calls, report exact counts and values rather than adding snapshot/version infrastructure.

## Tests

Use mocked Azure Retail Prices responses. No live API request should be required by the automated suite.

Tests should cover at least:

- official endpoint and GET construction,
- anonymous request,
- exact intended SKU/region/currency/consumption constraints,
- one request per collector invocation,
- no `NextPageLink` crawling,
- stable source-native identity excluding numeric price,
- different regions or materially distinct meter identities do not collide,
- source `effectiveStartDate` → `occurred_at`,
- collection time → `observed_at`,
- missing effective date handled honestly,
- readable content,
- source-native prices/units/currency preserved without conversion,
- preservation of important metadata,
- multiple product/meter variants preserved rather than silently collapsed,
- malformed/network/API failure handling,
- existing pipeline deduplication behavior.

Run the full test suite.

## Real run and completion report

After tests pass, perform one real bounded run against the official Azure Retail Prices API using a fresh database, then immediately repeat the identical command.

The completion report must include:

1. commit SHA and message,
2. files changed,
3. exact official endpoint and API version,
4. exact final OData filter / query parameters,
5. exact SKUs and regions represented,
6. identity semantics,
7. timestamp semantics,
8. first-run fetched / inserted / duplicate counts,
9. second-run fetched / inserted / duplicate counts,
10. full test result,
11. whether a `NextPageLink` was returned,
12. a compact full manifest with columns such as:

   `external_id | armSkuName | productName | meterName | region | retailPrice | currency | unit | type | effectiveStartDate`

13. eight to twelve representative readable observations,
14. simple report-only empirical summaries:
   - count of returned observations by ARM SKU,
   - count by region,
   - count by product/type variant,
   - for truly comparable rows only, min / median / max retail price by SKU,
   - for truly comparable rows only, absolute and percentage max/min spread by SKU,
15. identify any cases where rows that looked comparable were actually different products/meters and therefore should not be compared,
16. identify the largest obvious regional price differences in the clean comparable subset,
17. state clearly whether those differences look economically interesting enough to justify another pricing source, without calling them asymmetries,
18. whether the weak `SourceObservation` envelope remained honest or felt strained,
19. whether changing-price semantics reinforce the need for future repeated-measurement history,
20. any material departure from this spec.

Do not persist report-only dispersion calculations as domain objects.

Do not commit the API response corpus or SQLite database.

## Explicitly out of scope

Do **not** implement:

- AWS or Google Cloud comparison,
- cross-provider matching,
- cloud instance normalization,
- CPU/RAM performance normalization,
- cloud cost calculator,
- cheapest-region recommendations,
- arbitrage detection,
- TCO modelling,
- reserved-instance analysis,
- savings-plan analysis,
- spot-price analysis,
- price-history tables,
- revision/version infrastructure,
- cross-source matching,
- asymmetry scoring,
- opportunity scoring,
- market sizing,
- LLM classification,
- clustering,
- embeddings,
- commercialization logic,
- alerts/scheduling,
- UI,
- generic source orchestration,
- generic product/offer/price abstractions,
- changes to `SourceObservation` solely to anticipate future price analytics.

## Acceptance criteria

The slice passes when:

- the official unauthenticated Azure Retail Prices API is used,
- one tightly filtered request captures the selected common VM SKUs across selected European regions,
- only the intended on-demand consumption price family is targeted,
- each source-native priced meter is represented honestly as one `SourceObservation`,
- source identifiers, region, product/meter distinctions, price, currency, unit and effective date are preserved,
- numeric price is excluded from identity,
- existing persistence/deduplication semantics remain unchanged,
- mocked tests cover the critical source and identity contract and the full suite passes,
- the real run and immediate repeat are completed,
- the requested empirical price-dispersion report is produced,
- no cloud comparison/recommendation/commercialization architecture is introduced.

After the completion report, stop. Do not begin another source or phase.
