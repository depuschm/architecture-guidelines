---
name: architecture-decision-record
description: Write an architecture decision record (ADR) for a technical decision, using the project's existing ADR convention or, if there is none, the MADR template in docs/decisions/. Also handles superseding an earlier ADR. Use when the user asks to write, draft, record or document an ADR or architecture decision, or when a review or discussion ends with a decision worth recording.
argument-hint: "[decision title]"
---

# Architecture decision record

Record one decision per ADR, following [general/decisions.md](../../general/decisions.md).

## 1. Find the existing convention

Look for existing ADRs in `docs/decisions/`, `docs/adr/`, `doc/adr/`, `adr/`, `docs/architecture/decisions/`, or the directory named in an `.adr-dir` file (used by adr-tools).

- **If ADRs exist**, follow their template, filename pattern, numbering and status values exactly.
- **If none exist**, create `docs/decisions/` and use [template.md](template.md), which is the MADR template.

## 2. Number and name

- Number = highest existing number + 1, zero-padded to four digits (`0001`, `0002`, …).
- Filename: `NNNN-short-title-in-kebab-case.md`.
- Title: name both the problem and the chosen solution, for example "Use PostgreSQL for order storage".

## 3. Collect the content

Fill in the template from the conversation and the code. **Ask the user for anything you can't find.** Don't invent decision-makers, dates, measurements or constraints.

- **Context and problem**: what forces the decision now, and its scope.
- **Decision drivers**: the quality attributes and constraints that matter (see [general/quality-attributes.md](../../general/quality-attributes.md)).
- **Considered options**: at least two real options. Include "keep the current approach" when that's realistic.
- **Decision outcome**: the chosen option and why it wins against the drivers.
- **Consequences**: both the good and the bad. An ADR with no downsides is incomplete.
- **Confirmation**: how compliance will be checked, for example an architecture test, fitness function or review.
- **More information**: links to relevant guidelines in this repository (with their source links), issues and earlier ADRs.

Set `status: proposed` unless the user says the decision is already made. Set `date` to today.

## 4. Superseding

When the new ADR replaces an earlier one:

- Write the new ADR with a link to the old one.
- In the old ADR, change only the status to `superseded by [ADR-NNNN](NNNN-new-title.md)`. Leave the rest of the accepted text as it is.

## 5. Finish

Show the path to the new file, the chosen option, and any open questions the user still needs to answer.
