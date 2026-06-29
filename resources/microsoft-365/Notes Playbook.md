# Notes Playbook

Version: v0.1
Status: Draft
Owner: Abner Ballardo
System: Work OS
Classification: Highly Sensitive
Role: Microsoft 365 notes boundary playbook

Canonical boundary source: [Operating Stack.md](../../context/Operating%20Stack.md)

---

## Purpose

Define the current boundary for Microsoft-native working notes.

This playbook stays intentionally thin because OneNote is a working-note layer, not a corporate documentation authority.

---

## Current Boundary

OneNote is the preferred Microsoft-native candidate for Work notes that belong inside the corporate environment.

Microsoft Teams is the fast coordination layer. It is not a durable decision log.

Confluence is the team and delivery documentation authority where teams already document there.

Apple Notes is not the primary Work note system because Work devices do not synchronize notes reliably across the device set.

Rule:

* Use corporate systems for official records.
* Use Teams for live coordination and short-form alignment.
* Use OneNote only for Microsoft-native working notes when the note belongs inside the corporate environment and does not already belong in Jira, Confluence, Lists, or a decision log.
* Use Confluence for retained team and delivery documentation.
* Do not recreate corporate records, meeting logs, or raw conversation exports in Work OS.
* Do not copy private Work OS reasoning, political context, leadership assessments, or unreviewed working notes into administrative or Microsoft-native note workflows.

---

## Minimal OneNote Model

Use OneNote only when a lightweight corporate working note reduces reconstruction.

Recommended sections:

| Section | Use |
|---|---|
| Meeting Prep | Temporary preparation notes for material meetings |
| 1:1 Notes | Reviewed working notes from recurring leadership conversations |
| Committee Working Notes | Preparation notes that support Technology Committee triage or follow-up |

Do not create OneNote sections for:

* Every project
* Every stakeholder
* Jira-owned execution work
* Confluence-owned documentation
* Raw Teams transcripts
* Private Work OS reasoning

Minimum note shape:

```text
Date:
Context:
Decision / issue:
Owner:
Next action:
Destination system:
```

Rule:

```text
OneNote may hold working context; Jira, Confluence, Lists, decision logs, and Narrative PARA hold promoted outcomes.
```

---

## Promotion Rule

A note pattern may be promoted into a stronger playbook rule only when it:

* Repeats across multiple executive workflows
* Clarifies where a decision, commitment, or preparation artifact should live
* Reduces reconstruction or coordination load
* Improves source-boundary discipline
* Does not duplicate corporate records

Do not promote:

* Meeting transcripts
* Raw Teams chats
* Personal scratch notes
* One-off meeting preparation
* Short-lived operational noise

---

## Review Trigger

Review this playbook when:

* The OneNote workflow becomes stable
* Teams-to-narrative reflection rules change
* Meeting-note capture creates duplication or exposure risk
* Microsoft 365 Copilot notes behavior changes materially
* A Microsoft-native notes agent or workflow is proposed
