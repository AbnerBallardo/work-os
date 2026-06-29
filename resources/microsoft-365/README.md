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

Provide reusable working guidance for Microsoft 365 email, calendar, notes, tasks, Teams, and Copilot usage.

This folder is not a source of truth for corporate records, Work decisions, or agent runtime source packages. It contains Work OS-owned execution guidance that may change as Microsoft 365 usage matures.

---

## Playbook Map

| File | Role | Boundary |
|---|---|---|
| [Email Playbook.md](Email%20Playbook.md) | Outlook signal intake, folder/category model, flags, email routing, and email-oriented Copilot prompts | Working guidance only |
| [Calendar Playbook.md](Calendar%20Playbook.md) | Calendar capacity allocation, meeting admission, preparation, follow-up, and calendar-oriented Copilot prompts | Working guidance only |
| [Notes Playbook.md](Notes%20Playbook.md) | OneNote, Teams, and meeting-note capture boundaries | Thin until the notes workflow stabilizes |

---

## Boundary Rules

* Keep durable tool roles and system boundaries in [Operating Stack.md](../../context/Operating%20Stack.md).
* Keep changing folder names, category labels, rule logic, calendar cadences, notes patterns, and prompt examples here.
* Do not treat these playbooks as Outlook mirrors, calendar logs, task lists, project trackers, corporate records, or agent source packages.
* Do not copy private Work OS context, political notes, leadership assessments, or unreviewed working notes into Microsoft 365.
* If a private insight is needed for M365 runtime behavior, generalize it into safe routing, drafting, review, or source-boundary rules.

---

## Decision Rule

```text
Operating Stack = durable tool authority
Microsoft 365 playbooks = changing execution guidance
Agent Instructions = deployable runtime behavior
Corporate systems = official records
```

---

## Review Trigger

Review this folder when:

* Outlook folders or categories become hard to maintain
* Rules hide executive signal or create duplicate work
* Calendar practices stop protecting decision, preparation, or follow-up time
* OneNote or Teams note-taking becomes stable enough to govern
* Microsoft To Do becomes ineffective as a personal commitment layer
* Microsoft 365 Copilot behavior changes materially
* AB-Gatekeeper or AB-Executive Drafter source boundaries change
* A new M365 agent is proposed
