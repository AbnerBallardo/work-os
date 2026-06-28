# Context

Version: v1.1
Status: Active
Owner: Abner Ballardo
System: Work OS
Classification: Highly Sensitive
Role: Context folder authority map

---

## Purpose

Define the canonical context layer for Work OS.

This folder contains stable Work operating context, execution constraints, corporate tool boundaries, political context, leadership context, and information-handling rules needed for private Work judgment and controlled Work support.

---

## Context Contract

Every context file should make clear:

* Purpose
* Scope or constraint
* Role in the system
* Authority boundary
* Review trigger

Context files should not contain raw corporate exports, meeting logs, short-lived delivery noise, credentials, or Work-facing runtime material unless explicitly sanitized.

---

## Authority Map

| File | Role | Authority |
|---|---|---|
| `Context.md` | Stable Work operating context | Defines role reality, organizational constraints, strategic direction, and operating principles |
| `PARA.md` | Work-specific execution model | Defines Work execution, narrative PARA, coordination rules, and Work-specific constraints |
| `Operating Stack.md` | Corporate tool and system boundary model | Defines Work tool roles, official systems of record, AI boundaries, and device constraints |
| `Microsoft 365 Email and Calendar Working Reference.md` | Microsoft 365 implementation guidance | Non-canonical working reference for Outlook folders, categories, rules, calendar patterns, and Copilot prompts |
| `Political.md` | Private political landscape | Defines stakeholder dynamics, power structures, tactical patterns, and failure signals |
| `Leadership Map.md` | Private leadership landscape | Defines leadership coverage, delegation implications, reset implications, and role-risk context |
| `Information Handling Policy.md` | Exposure and sensitivity policy | Defines repository classification, externalization rules, and runtime exposure boundaries |

---

## Folder Rules

* Keep detailed Work operating truth in Work OS, not Personal OS.
* Keep official records in corporate systems, not Work OS.
* Keep detailed Microsoft 365 implementation examples subordinate to `Operating Stack.md`.
* Keep Work-facing runtime behavior in `/agents/` after source-boundary review.
* Keep committee governance in `/committees/`.
* Keep durable Work decisions in `/systems/decisions/work/`.
* Treat generated runtime packages as outputs, not context sources.

---

## Admission Criteria

Material belongs in `context/` only if it is:

* Stable enough to govern repeated Work judgment
* Useful for private Work reasoning or source-boundary decisions
* Generalizable beyond one event, meeting, person, or short-lived project
* Needed to interpret Work execution, governance, narrative, or tool constraints

Otherwise, route it to corporate systems, Work execution material, Work memory, decision records, agent packages, committee files, archive, or delete it.

---

## Review Trigger

Review this folder when:

* Work role scope materially changes
* Political or leadership context changes enough to affect decisions
* Corporate tool or system-of-record boundaries change
* Work-facing agent source packages need a new boundary model
* Personal OS / Work OS boundaries drift
