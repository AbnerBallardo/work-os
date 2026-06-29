# Microsoft 365 Resources

Version: v1.0
Status: Active
Owner: Abner Ballardo
System: Work OS
Classification: Highly Sensitive
Role: Microsoft 365 working-playbook index

Canonical boundary source: [Operating Stack.md](../../context/Operating%20Stack.md)

---

## Purpose

Provide reusable working guidance for Microsoft 365 email, calendar, notes, tasks, Teams, Lists, Loop, and Copilot usage.

This folder is not a source of truth for corporate records, Work decisions, or agent runtime source packages. It contains Work OS-owned execution guidance that may change as Microsoft 365 usage matures.

---

## Playbook Map

| File | Role | Boundary |
|---|---|---|
| [Email Playbook.md](Email%20Playbook.md) | Outlook signal intake, folder/category model, flags, email routing, and email-oriented Copilot prompts | Working guidance only |
| [Calendar Playbook.md](Calendar%20Playbook.md) | Calendar capacity allocation, meeting admission, preparation, follow-up, and calendar-oriented Copilot prompts | Working guidance only |
| [Tasks Playbook.md](Tasks%20Playbook.md) | Microsoft To Do, Outlook flagged emails, waiting-for items, and personal commitment review | Abner-owned commitments only |
| [Teams Playbook.md](Teams%20Playbook.md) | Teams coordination, thread discipline, meeting follow-up, Lists, Loop, and promotion rules | Coordination and working guidance only |
| [Notes Playbook.md](Notes%20Playbook.md) | OneNote, Teams, Confluence, and meeting-note capture boundaries | Minimal working-note model |

---

## Boundary Rules

* Keep durable tool roles and system boundaries in [Operating Stack.md](../../context/Operating%20Stack.md).
* Keep changing folder names, category labels, rule logic, calendar cadences, notes patterns, and prompt examples here.
* Do not treat these playbooks as Outlook mirrors, calendar logs, task lists, project trackers, corporate records, or agent source packages.
* Keep Jira as the execution tracker for delivery work and team-owned tasks.
* Keep Confluence as the documentation authority where teams already document there.
* Use Microsoft Lists only for structured intake, decision follow-up, exceptions, and lightweight governance registers that do not belong in Jira.
* Use Loop only for temporary collaborative agendas, action lists, draft decision bullets, and alignment tables.
* Do not copy private Work OS context, political notes, leadership assessments, or unreviewed working notes into Microsoft 365.
* If a private insight is needed for M365 runtime behavior, generalize it into safe routing, drafting, review, or source-boundary rules.

---

## Decision Rule

```text
Operating Stack = durable tool authority
Microsoft 365 playbooks = changing execution guidance
Jira = delivery execution tracking
Confluence = team and delivery documentation
Agent Instructions = deployable runtime behavior
Corporate systems = official records
```

---

## Operating Loop

| Cadence | Action |
|---|---|
| Daily | Use Outlook and Copilot to scan decision, action, risk, escalation, and waiting-for signals |
| Daily | Convert only Abner-owned commitments into Microsoft To Do / Tasks |
| Daily | Route team-owned delivery work to Jira and retained documentation to Confluence |
| Weekly | Review calendar, To Do, waiting-for items, Technology Committee preparation, and selected Narrative PARA changes |
| Monthly | Review Outlook rules, categories, Lists, Loop usage, and stale Microsoft 365 working surfaces |

---

## Review Trigger

Review this folder when:

* Outlook folders or categories become hard to maintain
* Rules hide executive signal or create duplicate work
* Calendar practices stop protecting decision, preparation, or follow-up time
* OneNote or Teams note-taking becomes stable enough to govern
* Microsoft To Do becomes ineffective as a personal commitment layer
* Microsoft Lists becomes a governance register or starts duplicating Jira
* Loop begins competing with Confluence, Jira, Lists, or decision logs
* Microsoft 365 Copilot behavior changes materially
* AB-Gatekeeper or AB-Executive Drafter source boundaries change
* A new M365 agent is proposed
