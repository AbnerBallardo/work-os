# Microsoft 365 Email and Calendar Working Reference

Version: v0.2
Status: Working Reference
Owner: Abner Ballardo
System: Work OS
Classification: Highly Sensitive
Role: Implementation guidance for Microsoft 365 signal intake and capacity management

Canonical source: [Operating Stack.md](Operating%20Stack.md)

This file is not a source of truth for corporate records, Work decisions, or agent runtime source packages. It captures implementation examples that may change as Outlook, Calendar, Microsoft To Do, Teams, and Microsoft 365 Copilot usage matures.

---

## Purpose

Provide reusable working guidance for Microsoft 365 email, calendar, tasks, Teams, and Copilot usage.

The goal is to support:

* Executive signal intake
* Capacity allocation
* Personal next-action tracking
* Delegation and routing
* Meeting preparation
* Technology Committee triage
* Source-boundary discipline

Rule:

* Keep durable tool roles and system boundaries in [Operating Stack.md](Operating%20Stack.md).
* Keep changing folder names, category labels, rule logic, calendar cadences, and prompt examples here.
* Do not treat this file as an Outlook mirror, calendar log, task list, project tracker, or corporate record.

---

## Microsoft 365 Tool Roles

| Tool | Role | Not For |
|---|---|---|
| Outlook Inbox | Executive signal intake | Project tracking, decision logs, knowledge storage |
| Outlook Folders | Noise reduction | Encoding durable meaning |
| Outlook Categories | Signal classification | Long-term truth or project taxonomy |
| Outlook Flags / Microsoft To Do | Abner-owned personal commitments | Team tasks, project work owned by others |
| Outlook Calendar | Capacity allocation | Passive meeting accumulation |
| Microsoft Teams | Fast coordination | Durable decisions or controlled executive records |
| Microsoft 365 Copilot | Compression, preparation, search, and drafting support | Final judgment, source of truth, private Work OS context storage |
| Work OS | Private reasoning and source-boundary control | Corporate records or raw Microsoft 365 export storage |

Decision rule:

```text
Email = signal intake
Calendar = capacity allocation
Tasks = personal commitments
Teams = fast coordination
Copilot = compression and drafting
Work OS = private reasoning and source-boundary control
Corporate systems = official records
```

---

## Inbox Model

The Inbox should contain only messages that may require decision, action, review, delegation, risk awareness, executive awareness, calendar impact, governance routing, escalation, or formal approval.

Keep in Inbox when a message is:

* Sent directly to Abner
* From Sebastian or Luis Alfredo
* From local CEO, regional, corporate, regulatory, audit, risk, security, or executive stakeholders
* A meeting request or material calendar change
* An approval, risk acceptance, or formal review request
* A production, security, regulatory, audit, incident, vulnerability, or service degradation signal
* A cross-domain blocker
* A Technology Committee candidate topic
* A material vendor, platform, architecture, infrastructure, or ownership issue
* A message where Abner owns the next visible action

Move or archive when a message is:

* Awareness-only and low consequence
* Distribution-list traffic
* Automated report or alert without executive action
* Vendor newsletter
* Meeting response without comments
* System notification already visible in a corporate system of record
* Team chatter better handled in Teams
* A message where no decision, action, risk, ownership, or timeline changes

---

## Folder Model

Folders reduce active noise. They do not encode durable meaning.

Recommended small folder set:

```text
1-Reference
2-Executive
3-Approvals
4-Risk-Security-Regulatory
5-Technology Committee
6-Distribution Lists
7-Automated Notifications
8-Vendors
Archive
```

Rules:

* Keep folder count low.
* Do not create folders for every project.
* Do not create folders for every stakeholder.
* Prefer search over manual filing.
* Use folders only when they reduce active Inbox noise.
* Use categories to preserve why a message matters.
* Use Archive for messages that no longer require action but may be useful later.

---

## Rule Model

Rules remove predictable low-signal noise. They must not hide executive signal.

Rule safety order:

```text
1. Preserve executive senders and direct-to-Abner messages.
2. Preserve risk, approval, security, regulatory, production, and committee signals.
3. Categorize known executive or governance messages.
4. Move distribution-list and automated traffic.
5. Archive or delete low-value responses and notifications.
```

Do not automatically move out of Inbox:

* Sebastian or Luis Alfredo
* Direct manager, local CEO, regional, or International Banking executive senders
* Direct-to-Abner messages
* Approval or risk acceptance requests
* Security, regulatory, audit, production, incident, or vulnerability signals
* Meeting invitations or major meeting changes
* Threads where Abner has participated and may owe a response

Safe candidates for folder rules:

* Distribution lists
* Automated notifications
* System reports
* Vendor newsletters
* Meeting responses without comments
* Low-value broadcast communications
* Notifications duplicated in another official system

Review Outlook rules quarterly and after major Outlook client changes.

Remove or revise any rule that:

* Hides executive signal
* Creates duplicate review work
* Moves messages that later require urgent search
* Depends on fragile wording
* Routes messages into a folder that is not reviewed

---

## Category Model

Categories encode the primary operational reason a message matters.

Decision rule:

```text
Folders answer where the message lives.
Categories answer why the message matters.
Flags answer whether Abner owns a personal next action.
Agent classification answers how the signal should be interpreted, routed, and drafted.
```

Primary workflow:

```text
Intent -> Context Depth -> Routing
```

Recommended Outlook Categories:

* `DECISION`
* `ACTION`
* `REVIEW`
* `FYI`
* `RISK`
* `BLOCKED`
* `ESCALATION`

Optional Outlook Domain Categories, only if they improve scanning and routing:

* `ENG`
* `ARCH`
* `SEC`
* `SRE`
* `INFRA`
* `DATA`
* `DELIVERY`
* `FIN`
* `VENDOR`
* `PROD`
* `REG`

Do not create Outlook Categories for:

* C-level
* Executive / Stakeholder sensitivity
* Governance
* TC tier
* Full Risk / Exposure taxonomy

These belong mostly in AB-Gatekeeper assessment, email body metadata, routing logic, or committee triage.

Rules:

* Use a small and stable category set.
* Do not use categories as project folders.
* Do not create temporary categories for short-lived issues.
* Intent is the primary category.
* Domain is optional and visible only when it improves scanning.
* Do not require humans to manually classify every message across all agent facets.
* Use flags or Microsoft To Do, not a category, when Abner is waiting for someone else or owns a personal follow-up.
* Use `BLOCKED` only when execution cannot proceed without intervention.
* Use `ACTION` only when Abner must personally do something.
* Use `DECISION` only when Abner must choose, approve, reject, or accept risk.
* Use `REVIEW` only when Abner must validate content or direction before it moves forward.
* Use `FYI` only when awareness matters and the next visible signal is clear.
* Use `RISK` when the primary reason to preserve the signal is possible downside.
* Use `ESCALATION` when senior intervention, narrative control, or authority beyond normal ownership is required.

Decision rule:

```text
If a message cannot be categorized by intent, it probably should be archived, ignored, delegated, or handled outside the Inbox.
```

---

## Flags and Tasks Model

Email is not the task system.

Flag an email only when Abner must personally:

* Reply
* Decide
* Review
* Follow up
* Track a waiting-for response
* Convert the email into a Microsoft To Do task

Do not flag:

* Team tasks owned by others
* Project work that belongs in a project tracker
* Committee topics that belong in Technology Committee intake
* Messages kept only for reference
* Awareness-only messages
* Broad read-later material with no concrete next action

Task naming rule:

```text
Rename flagged-email tasks into action-oriented language.
```

Example:

| Weak | Better |
|---|---|
| `Re: Valinor update` | `Review Valinor decision ask before Monday Technology Committee` |

Ownership rule:

```text
If Abner does not personally own the next action, do not convert the email into a personal task.
```

Instead:

* Delegate
* Reply with owner and deadline
* Move to project tracker
* Route to Technology Committee
* Archive

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
* Sebastian / Luis Alfredo preparation

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
| Weekly | Sebastian / Luis Alfredo preparation |
| Weekly | Technology Committee preparation and decision-log review |

Meeting admission rule:

```text
A meeting should exist only when it requires decision, alignment, escalation, commitment, cross-domain coordination, sensitive discussion, high-context preparation, or governance record.
```

Otherwise prefer Teams, email, async update, document review, or delegated working session.

---

## Microsoft 365 Copilot Model

Microsoft 365 Copilot is a compression, preparation, and drafting layer.

Use it for:

* Morning executive signal scan
* Inbox prioritization
* Email thread summarization
* Email drafting and coaching
* Meeting preparation
* Meeting agenda drafting
* Calendar and inbox questions
* Cross-surface catch-up across email, meetings, chats, and files
* Preparing concise executive replies
* Preparing Sebastian / Luis Alfredo interactions
* Preparing Technology Committee intake drafts
* Summarizing long threads into decision-ready structure

Do not use it to:

* Make final executive decisions
* Replace risk acceptance ownership
* Create corporate records outside approved systems
* Store private Work OS context
* Expose private political or leadership notes
* Connect broad Work OS sources to work-facing agents
* Produce final messages without Abner review when exposure exists
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

Morning signal scan:

```text
Review my emails from the last 24 hours and summarize only items that require my decision, action, executive awareness, risk attention, or delegation. Group by sender, topic, risk, owner, and deadline.
```

Executive sender scan:

```text
Show open threads involving Sebastian or Luis Alfredo where I owe a response, decision, review, or follow-up. Separate direct asks from FYI messages.
```

Decision extraction:

```text
Summarize this thread into: decision needed, recommendation, alternatives, risks, owner, deadline, and next visible signal.
```

Meeting preparation:

```text
Prepare me for this meeting using relevant emails, calendar context, chats, and files I can access. Focus on decisions, open risks, commitments, unresolved dependencies, and likely asks.
```

Draft executive reply:

```text
Draft a concise executive reply using this structure: what changed, why it matters, recommendation, decision/action required, owner, deadline, next visible signal.
```

Technology Committee triage:

```text
Convert this thread into a Technology Committee triage submission. Include topic, executive signal, decision needed, requested committee outcome, decision owner, why it matters, recommendation, urgency, consequence of no decision, and recommended routing.
```

Long-thread compression:

```text
Summarize this thread for executive review. Exclude history unless it changes the decision. Include only current state, decision needed, risk, owner, deadline, and unresolved assumptions.
```

Calendar cleanup:

```text
Review my calendar for the next two weeks and identify meetings that may be delegated, shortened, converted to async, or require preparation blocks.
```

Waiting-for review:

```text
Find emails from the last two weeks where I asked someone for a response, decision, update, or action and I have not received a clear answer.
```

---

## Technology Committee Routing

Route toward Technology Committee when an email includes:

* Cross-domain trade-off
* Risk acceptance
* Architecture direction
* Production stability exposure
* Security, regulatory, or audit exposure
* Local-regional dependency
* Vendor or infrastructure blocker
* Resource or ownership conflict
* CEO / International Banking visibility
* Repeated escalation pattern
* Decision that requires durable record

Use the existing Technology Committee triage-first model.

Do not prepare full committee briefs directly from email unless the topic has passed triage.

---

## Agent Integration Notes

AB-Gatekeeper should use this model as a routing standard when reviewing emails prepared for Abner:

```text
Right context + right structure + right routing + right ask
```

AB-Executive Drafter should use this model to recommend not sending email when Teams, a call, a meeting, or Technology Committee route is more appropriate.

Source-boundary rule:

```text
Do not connect broad Work OS context, political context, leadership assessments, raw working notes, case files, or personal context to work-facing M365 agents.
```

If a private insight is needed for M365 runtime behavior, generalize it into safe routing, drafting, review, or source-boundary rules.

---

## Review Trigger

Review this file when:

* Outlook folders or categories become hard to maintain
* Rules hide executive signal or create duplicate work
* Microsoft To Do becomes ineffective as a personal commitment layer
* Calendar practices stop protecting decision, preparation, or follow-up time
* Microsoft 365 Copilot behavior changes materially
* AB-Gatekeeper or AB-Executive Drafter source boundaries change
* A new M365 agent is proposed
