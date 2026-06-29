# Calendar Playbook

Version: v1.0
Status: Active
Owner: Abner Ballardo
System: Work OS
Classification: Highly Sensitive
Role: Microsoft 365 calendar capacity playbook

Canonical boundary source: [Operating Stack.md](../../context/Operating%20Stack.md)

---

## Purpose

Define the working model for Outlook Calendar capacity allocation, meeting admission, preparation, follow-up, and calendar-oriented Microsoft 365 Copilot usage.

This playbook supports:

* Capacity allocation
* Meeting preparation
* Delegation and routing
* Protected executive work
* Source-boundary discipline

Rule:

* Keep durable calendar authority in [Operating Stack.md](../../context/Operating%20Stack.md).
* Keep changing calendar cadences, categories, preparation patterns, and prompt examples here.
* Do not treat this file as a calendar log, meeting record, task list, corporate record, or Work-facing agent source package.

---

## Calendar Model

The calendar is the capacity contract.

Calendar should protect:

* Executive meetings
* Decision forums
* Preparation time
* Deep work
* Follow-up blocks
* Recovery / buffer time
* Weekly review
* Technology Committee preparation
* Sebastián / Luis Alfredo preparation

Recommended calendar categories:

```text
Personal Buffer
Time Blocking
Optional
```

Calendar-only category rules:

* Use `Time Blocking` for protected work blocks that represent capacity allocation, not a meeting commitment.
* Use `Optional` for events where attendance is genuinely discretionary and should not be treated as committed capacity.
* Do not use `Time Blocking` or `Optional` as email categories.

Minimum working structure:

| Cadence | Pattern |
|---|---|
| Daily | Two email triage windows |
| Daily | One executive signal scan |
| Daily | One protected decision or thinking block where possible |
| Weekly | Calendar and task review |
| Weekly | Email rules and category cleanup |
| Weekly | Sebastián / Luis Alfredo preparation |
| Weekly | Technology Committee preparation and decision-log review |

Meeting admission rule:

```text
A meeting should exist only when it requires decision, alignment, escalation, commitment, cross-domain coordination, sensitive discussion, high-context preparation, or governance record.
```

Otherwise prefer Teams, email, async update, document review, or delegated working session.

---

## Microsoft 365 Copilot Calendar Model

Microsoft 365 Copilot is a compression, preparation, and drafting layer.

Use it for:

* Meeting preparation
* Meeting agenda drafting
* Calendar and inbox questions
* Cross-surface catch-up across email, meetings, chats, and files
* Preparing Sebastián / Luis Alfredo interactions
* Preparing Technology Committee intake drafts
* Calendar cleanup and delegation review

Do not use it to:

* Make final executive decisions
* Replace risk acceptance ownership
* Create corporate records outside approved systems
* Store private Work OS context
* Expose private political or leadership notes
* Connect broad Work OS sources to Work-facing agents
* Treat generated summaries as source of truth without checking primary messages or documents

Review Copilot output before sending or acting.

Validate:

* Facts
* Dates
* Owners
* Decision asked
* Risk language
* External narrative
* Attachments / references
* Confidentiality
* Source boundary
* Whether a committee or governance route is required

---

## Copilot Prompt Patterns

Meeting preparation:

```text
Prepare me for this meeting using relevant emails, calendar context, chats, and files I can access. Focus on decisions, open risks, commitments, unresolved dependencies, and likely asks.
```

Calendar cleanup:

```text
Review my calendar for the next two weeks and identify meetings that may be delegated, shortened, converted to async, or require preparation blocks.
```

Executive interaction preparation:

```text
Review upcoming meetings with Sebastián or Luis Alfredo and identify preparation needs, open decisions, risks, likely asks, and follow-up commitments.
```

Technology Committee preparation:

```text
Review upcoming Technology Committee-related meetings and identify agenda readiness, decision gaps, unresolved owners, and preparation blocks needed before the meeting.
```

---

## Review Trigger

Review this playbook when:

* Calendar practices stop protecting decision, preparation, or follow-up time
* Executive support changes the scheduling workflow
* Microsoft 365 Copilot behavior changes materially
* Meeting load increases without clear decision or alignment value
* Technology Committee preparation requires a different calendar pattern
