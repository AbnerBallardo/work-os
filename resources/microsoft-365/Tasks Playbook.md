# Tasks Playbook

Version: v1.0
Status: Active
Owner: Abner Ballardo
System: Work OS
Classification: Highly Sensitive
Role: Microsoft 365 personal-commitment playbook

Canonical boundary source: [Operating Stack.md](../../context/Operating%20Stack.md)

---

## Purpose

Define the working model for Microsoft To Do, Outlook flagged emails, waiting-for items, and personal commitment review.

This playbook supports:

* Abner-owned next actions
* Email-derived commitments
* Waiting-for visibility
* Calendar and follow-up discipline
* Separation from Jira execution tracking

Rule:

* Keep Jira as the execution tracker for project work, backlog, delivery tasks, and team-owned work.
* Keep Microsoft To Do / Tasks limited to Abner-owned commitments.
* Do not use Microsoft To Do as a team tracker, project tracker, decision log, or corporate record.

---

## Tool Roles

| Tool | Role | Not For |
|---|---|---|
| Outlook flags | Fast capture from email | Permanent task wording or team-task assignment |
| Microsoft To Do / Tasks | Abner-owned personal commitments | Team execution, Jira work, durable decisions |
| Jira | Delivery execution tracking | Personal reminder list |
| Microsoft Lists | Structured intake or lightweight governance register | Backlog or delivery execution tracking |
| Calendar | Time allocation for high-friction commitments | Task inventory |
| Work OS | Private operating logic and boundary design | Corporate task records |

Decision rule:

```text
To Do = Abner commitments
Jira = delivery execution
Lists = structured intake / governance register
Calendar = capacity allocation
Work OS = private operating logic
```

---

## Capture Rules

Create or keep a To Do item only when Abner personally must:

* Reply
* Decide
* Review
* Prepare
* Follow up
* Confirm closure
* Track a waiting-for commitment

Do not create a To Do item for:

* Team-owned delivery tasks
* Jira-owned execution work
* Committee topics that belong in Technology Committee intake
* Documentation work that belongs in Confluence
* Awareness-only material
* Read-later material without a concrete next action

Rule:

```text
If the next action is not Abner-owned, route it instead of personalizing it.
```

---

## Task Shape

Every active personal task should be action-oriented.

Minimum fields:

| Field | Rule |
|---|---|
| Verb | Start with the action: review, decide, reply, prepare, confirm, follow up |
| Object | Name the topic, artifact, or person |
| Outcome | State what closure looks like |
| Due date | Add only when timing matters |
| Source | Preserve link or reference to email, meeting, Jira, List, or document when useful |

Examples:

| Weak | Better |
|---|---|
| `Re: architecture update` | `Review architecture exception recommendation before TC triage` |
| `Follow up` | `Follow up with owner on production-risk closure evidence` |
| `Budget` | `Decide whether vendor budget issue needs escalation` |

---

## Waiting-For Model

Use waiting-for tasks when Abner has asked someone else for a response and the absence of response may affect a decision, timeline, risk, or executive commitment.

Waiting-for task naming:

```text
Waiting for [owner] on [specific response / artifact / decision]
```

Rules:

* Do not track every delegated task.
* Track only commitments where Abner needs visibility or closure.
* Use due dates sparingly.
* Close waiting-for tasks when the response arrives, the issue is routed to Jira, or it no longer affects a decision.

Copilot prompt:

```text
Find email threads from the last two weeks where I asked someone for a response, update, artifact, or decision and I have not received a clear answer. Return only items that may affect a decision, timeline, risk, or executive commitment.
```

---

## Review Rhythm

| Cadence | Review |
|---|---|
| Daily | Clear overdue and today items; decide, defer, route, or delete |
| Daily | Check flagged-email tasks created during email triage |
| Weekly | Review waiting-for items and stale commitments |
| Weekly | Convert work that belongs in Jira, Lists, Calendar, or Technology Committee |
| Monthly | Remove low-value recurring tasks and stale reminders |

Rule:

```text
The task list should represent commitments Abner can act on, not everything that matters.
```

---

## Routing Rules

| Signal | Route |
|---|---|
| Abner owns the next action | Microsoft To Do / Tasks |
| Team owns delivery execution | Jira |
| Topic needs committee triage | Technology Committee intake |
| Structured governance follow-up is needed | Microsoft Lists |
| Time must be protected | Outlook Calendar |
| Documentation must be retained by the team | Confluence |
| Quick coordination is enough | Teams |

---

## Review Trigger

Review this playbook when:

* Microsoft To Do becomes noisy or stale
* Waiting-for items are missed
* Personal tasks start duplicating Jira
* Calendar reviews reveal commitments without protected time
* Lists or Technology Committee intake changes the routing model
