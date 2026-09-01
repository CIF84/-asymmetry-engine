# Spec 003 — Stack Exchange Richer Evidence

## Goal

Increase the fidelity of the existing Stack Exchange empirical slice so that `SourceObservation` preserves enough of each question to support meaningful inspection of economic decision friction.

Then run a larger bounded sample from Money Stack Exchange and produce an inspection manifest for ChatGPT review.

This is still an observation-layer experiment. Do not classify, score, interpret, or commercialize observations in code.

## Why this specification exists

Spec 001 proved that the basic source-independent observation envelope works:

```text
Stack Exchange API
    → StackExchangeCollector
    → SourceObservation
    → SQLite
```

The first real observations also exposed an important weakness: `SourceObservation.content` currently contains only the question title.

That is too lossy for the next empirical step.

For example, a title can tell us that someone is asking about life-insurance coverage or a foreign-transaction fee, but the economically useful structure often appears only in the body:

- personal constraints and variables
- competing alternatives
- conflicting information
- uncertainty about consequences
- existing attempts to solve the problem
- contextual details that make the decision difficult

The schema itself does not need to become more interpretive. The collector simply needs to preserve richer source evidence.

The purpose of this change is to answer:

> When we preserve enough of the original question, what recurring forms of economic information friction actually appear in a real sample?

## Current implementation pressure

The existing Stack Exchange collector uses the official `/2.3/questions` endpoint and normalizes the title into `SourceObservation.content`.

The next version should request the question body from the official API as part of the same bounded collection flow.

Use an official API filter/mechanism that returns the body. Do not scrape Stack Exchange pages.

Do not introduce pagination or crawler behavior merely to satisfy this spec. A single bounded sample of up to 100 questions remains sufficient.

## Scope

### 1. Capture the question body

Update the Stack Exchange request so that returned question objects include their body.

Use the official Stack Exchange API and an appropriate supported filter such as `withbody` or an equivalent official mechanism.

The collector must continue to:

- use the official API
- remain bounded by `sample_size`
- respect API backoff
- preserve stable identity
- use one observation timestamp for the collected batch
- remain independent of SQLite

### 2. Make `SourceObservation.content` meaningfully inspectable

For Stack Exchange questions, `content` should no longer be title-only.

It should contain a readable representation of:

```text
title
+
question body
```

The exact local formatting is an implementation detail, but the result must be useful to a human or downstream analysis without requiring another network request.

Do not summarize, classify, paraphrase, or otherwise semantically reinterpret the question.

If the API returns HTML and the implementation converts it into readable text, preserve the original source body in source-specific metadata when reasonably simple so that the transformation is not irreversibly lossy.

If the implementation instead preserves the original body directly in `content`, that is acceptable only if the resulting content remains practical to inspect.

Do not add title/body fields to the generic `SourceObservation` model solely for Stack Exchange unless an actual implementation constraint makes that necessary. Prefer keeping the generic observation envelope weak.

### 3. Preserve existing source-native metadata

Continue preserving the existing useful Stack Exchange metadata such as:

- tags
- score
- view count
- answer count
- answered state
- accepted answer ID when present
- last activity timestamp when present
- content licence when present

Additional source-native metadata may be retained if it is directly useful and does not turn this into a general Stack Exchange ingestion project.

### 4. Existing identity and deduplication semantics remain unchanged

Stable identity remains:

```text
source_id + external_id
```

For example:

```text
stackexchange:money
money:question:<question_id>
```

Do not introduce content hashes, semantic deduplication, title matching, or observation version history.

Because existing Spec 001 databases may already contain title-only observations with the same stable identities, the empirical Spec 003 run should use a **fresh SQLite database**.

Do not mutate or retrofit old observations just to enrich them. We have deliberately deferred mutable-source history/versioning.

### 5. Run a larger real sample

After implementation and automated tests pass, perform one manual real-source collection from Money Stack Exchange using a fresh database and a bounded sample of **75 questions**.

The purpose is empirical inspection, not scale testing.

Run the same command a second time against that same fresh database to reconfirm identity-based deduplication still behaves correctly with richer content.

### 6. Produce an inspection manifest in the completion report

Do not commit a corpus of Stack Exchange question bodies to the repository.

Instead, the Codex completion report should include a compact manifest for the real 75-question run so ChatGPT can independently select and inspect source questions.

For each collected question include:

```text
external_id | title | canonical_url | tags | score | view_count | answer_count
```

Do not paste all 75 full question bodies into the completion report.

Also include **8 representative stored observations** showing:

- external identity
- title
- a short body excerpt sufficient to verify richer evidence capture
- canonical URL
- tags
- engagement metadata

Choose the eight for variety rather than for presumed commercial quality. Do not classify them as good/bad opportunities.

## Tests

Update or add focused automated tests proving:

- the collector requests a body-bearing API response/filter
- normalization preserves stable identity and timestamps
- `SourceObservation.content` contains both title and meaningful body content
- any body-to-readable-text transformation behaves deterministically on a small fixture
- existing useful metadata remains preserved
- existing bounded-query/backoff behavior remains intact
- existing pipeline and deduplication tests continue to pass

Do not use live Stack Exchange requests in automated tests.

Use mocks/fixtures as in the existing suite.

## Important semantics

### Preserve evidence; do not interpret it

This phase is about increasing observation fidelity.

Do not add fields such as:

- decision type
- friction type
- economic consequence
- asymmetry strength
- commercial attractiveness
- commercialization distance
- opportunity score
- product idea
- monetization mechanism

Those are hypotheses for later interpretation, not properties of source evidence.

### `Friction Pattern` is still only a hypothesis

Recent inspection suggests observations may contain recurring structures such as:

- factual information gaps
- operational problems
- consequential decisions
- conflicting information
- hidden system mechanics

Do not encode those categories yet.

The purpose of the richer sample is to discover whether a useful intermediate abstraction actually survives real evidence.

### Do not assume SaaS

The broader project may eventually monetize an asymmetry through many mechanisms: digital products, generated reports, interactive tools, programmatic content, affiliate assets, advertising, lead generation, micro-SaaS, licensing, data products, or other automated workflows.

None of those belong in this implementation slice.

The observation layer should remain neutral about eventual commercialization mechanism.

## Explicitly out of scope

Do not introduce:

- CFPB or another source
- LLM calls
- classification
- `DecisionSignal`
- `DecisionProblem`
- `FrictionPattern` as a persisted model
- generic `Evidence` taxonomy
- asymmetry detection
- clustering
- embeddings
- vector database
- scoring
- Asymmetry Strength
- Commercial Attractiveness
- Commercialization Distance
- monetization models
- product generation
- agent orchestration
- workflow execution
- scheduling
- crawling/pagination beyond the bounded sample needed here
- UI/web app
- observation version history
- migrations framework
- speculative architecture refactors

Do not update README.md, ARCHITECTURE.md, or ROADMAP.md merely to mirror this implementation unless a genuine contradiction is discovered. If so, report it rather than broadening the change silently.

## Acceptance criteria

This specification is complete when:

1. Stack Exchange collection still uses the official API and now requests question bodies.
2. A normalized Stack Exchange `SourceObservation` contains readable title + body evidence rather than title alone.
3. No semantic interpretation/classification is introduced into `SourceObservation`.
4. Stable identity and Spec 002 deduplication semantics remain unchanged.
5. Existing Stack Exchange metadata remains available.
6. Automated tests cover richer body capture and all tests pass.
7. A fresh SQLite database successfully collects a bounded real sample of 75 Money Stack Exchange questions.
8. Re-running the same collection against that database produces no duplicate observation rows and reports the expected duplicate count.
9. The completion report contains the requested 75-question inspection manifest and eight representative richer observations.
10. No corpus of full Stack Exchange bodies is committed to GitHub.

## Requested completion report

When complete, Codex should report:

1. Commit SHA and commit message.
2. Files changed.
3. Exact API/filter change used to obtain question bodies.
4. Exact representation chosen for `SourceObservation.content`, including how HTML/source formatting is handled.
5. Whether the original source body is additionally preserved anywhere and why.
6. Test command and result/count.
7. Exact CLI command used for the fresh 75-question real run.
8. First-run fetched/inserted/duplicate counts.
9. Second-run fetched/inserted/duplicate counts.
10. Eight representative stored observations with short body excerpts and source metadata.
11. The compact 75-question inspection manifest:

```text
external_id | title | canonical_url | tags | score | view_count | answer_count
```

12. Any API, content-format, licensing, or storage behavior that differed materially from assumptions.
13. Any pressure discovered on the `SourceObservation` abstraction.
14. Any material departure from this specification and why.

Then stop.

Do not select the next source, design a friction taxonomy, or implement downstream analysis. The next step is ChatGPT inspection of the real evidence and a decision about what the data just taught us.