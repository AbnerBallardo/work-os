# Teams Playbook

Version: v1.0
Status: Active
Owner: Abner Ballardo
System: Work OS
Classification: Highly Sensitive
Role: Microsoft Teams coordination playbook

Canonical boundary source: [Operating Stack.md](../../context/Operating%20Stack.md)

---

## Purpose

Define the working model for Microsoft Teams coordination, channel usage, thread discipline, meeting follow-up, and promotion into the correct system of record.

This playbook supports:

* Fast coordination
* Short-form executive alignment
* Technology Committee intake
* Narrative PARA reflection
* Source-boundary discipline

Rule:

* Teams is a coordination layer.
* Teams is not a durable decision log, project tracker, documentation system, or Work OS memory source by default.
* Do not create a new Microsoft Team only to support a lightweight workflow when existing Teams, channels, Lists, Jira, or Confluence can carry the work.

---

## Tool Roles

| Tool | Role | Not For |
|---|---|---|
| Teams chat | Fast clarification, pre-alignment, and low-friction follow-up | Durable decisions or broad visibility |
| Teams channel | Shared coordination, committee intake, incident updates, or group-visible alignment | Long-form documentation |
| Teams meeting recap / Copilot output | Draft recall and action extraction when available | Source of truth without review |
| Microsoft Lists | Structured intake, decision follow-up, exceptions, and request queues | Delivery execution backlog |
| Jira | Delivery execution tracking | Governance register |
| Confluence | Team and delivery documentation | Live coordination |
| Narrative PARA | Selected executive project narrative | Full project inventory |

Decision rule:

```text
Teams coordinates.
Jira executes.
Confluence documents.
Lists structures.
Narrative PARA explains selected executive movement.
```

---

## Channel Decision

Use Teams when the goal is:

* Fast coordination
* Short-form alignment
* Clarifying ownership
* Closing a small fact gap
* Posting Technology Committee triage
* Coordinating around an active incident or escalation
* Confirming next visible action after a meeting

Do not use Teams as the final destination when the output is:

* Delivery task or backlog item -> Jira
* Team documentation -> Confluence
* Committee decision record -> Technology Committee decision log
* Structured intake or follow-up queue -> Microsoft Lists
* Selected executive project movement -> Narrative PARA
* Personal commitment for Abner -> Microsoft To Do / Tasks

---

## Thread Rules

Rules:

* One topic per thread where possible.
* Use a direct title or first sentence that names the issue and desired outcome.
* Keep the ask explicit: decide, confirm, route, review, unblock, or inform.
* Prefer replying in the existing thread over creating a parallel thread.
* Promote the outcome when the thread creates a durable action, decision, risk, or narrative change.

Technology Committee intake:

* Use the existing `Technology Committee - Intake` channel when applicable.
* Keep one topic per Teams post / thread.
* Do not use email as the default intake path unless urgency requires it.

---

## Promotion Rules

Promote a Teams signal when it changes:

* Decision
* Owner
* Due date
* Status color
* Timeline or milestone
* Scope
* Critical dependency
* Risk or blocker
* Executive visibility
* Architecture, security, vendor, regulator, or cross-domain implication

Promotion destinations:

| Signal | Destination |
|---|---|
| Execution action | Jira |
| Team documentation or retained explanation | Confluence |
| Structured governance queue or follow-up register | Microsoft Lists |
| Committee decision | Technology Committee decision log |
| Selected executive project narrative movement | Narrative PARA |
| Abner personal follow-up | Microsoft To Do / Tasks |
| Meeting preparation or working note | OneNote, when it belongs inside the corporate environment |

Rule:

```text
Teams moves the work; the destination system retains the outcome.
```

---

## Meeting Follow-Up

After material meetings, use Teams only for concise alignment or visible next action.

Minimum follow-up shape:

```text
Decision / alignment:
Owner:
Next action:
Due date:
Record destination:
```

If meeting recap or Copilot output is available:

* Use it to identify actions, decisions, risks, and owners.
* Validate facts, dates, owners, and confidentiality.
* Promote only reviewed outputs into Jira, Lists, Confluence, OneNote, decision logs, or Narrative PARA.

---

## Loop Use

Use Loop only when live co-editing reduces coordination cost.

Good uses:

* Meeting agenda
* Live action list
* Draft decision bullets
* Pre-read comments
* Quick alignment table

Do not use Loop for:

* Durable documentation
* Jira-owned execution
* Confluence-owned knowledge
* Official decision records
* Private Work OS reasoning
* Sensitive unreviewed context

Rule:

```text
Loop is a temporary collaboration surface; promote the result or discard it.
```

---

## Review Trigger

Review this playbook when:

* Teams threads become hard to reconstruct
* Decisions remain trapped in chat
* Committee intake becomes inconsistent
* Meeting follow-up creates duplicate work
* Loop begins to compete with Confluence, Jira, Lists, or decision logs
* A new Microsoft Team or channel is proposed
