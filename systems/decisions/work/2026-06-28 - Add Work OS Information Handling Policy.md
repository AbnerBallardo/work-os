# Add Work OS Information Handling Policy

Date: 2026-06-28

Status: Accepted

---

## Decision

Add `/context/Information Handling Policy.md` as the canonical Work OS source for repository sensitivity, exposure, externalization, AI usage, and runtime-package handling rules.

Keep Work OS canonical context in `context/`; no folder rename is required.

---

## Rationale

* Align Work OS with the sibling OS pattern where durable information-handling rules live under `context/`.
* Reduce duplication between README, AGENTS, runtime templates, and agent-package rules.
* Make exposure policy directly referenceable by ChatGPT Project runtime builds and future Work-facing source-boundary reviews.
* Preserve Work OS as the private Work operating system while keeping Work-facing agent packages sanitized and least-privilege.

---

## Consequences

* README and AGENTS reference the policy instead of carrying the full policy inline.
* ChatGPT Project runtime package scope includes a selected policy excerpt.
* Work-facing AI agent runtime-package decisions depend on the policy.
* Future information-handling changes must update the policy first, then companion references and build configuration.
