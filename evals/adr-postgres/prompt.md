---
description: The ADR skill writes a MADR-format record in docs/decisions.
tags: [adr]
max_turns: 25
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

We decided to store orders in PostgreSQL instead of MongoDB, because order and payment updates must happen in a single transaction. The team (Ana, Ben) made the call today. Please document this decision as an architecture decision record in this repository.
