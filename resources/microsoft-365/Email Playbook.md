# Email Playbook

Version: v1.0
Status: Active
Owner: Abner Ballardo
System: Work OS
Classification: Highly Sensitive
Role: Microsoft 365 email signal-intake playbook

Canonical boundary source: [Operating Stack.md](../../context/Operating%20Stack.md)

---

## Purpose

Define the working model for Outlook email intake, folders, categories, flags, routing, and email-oriented Microsoft 365 Copilot usage.

This playbook supports:

* Executive signal intake
* Delegation and routing
* Personal next-action tracking
* Technology Committee triage
* Source-boundary discipline

Rule:

* Keep durable tool roles and system boundaries in [Operating Stack.md](../../context/Operating%20Stack.md).
* Keep changing folder names, category labels, rule logic, flags, and prompt examples here.
* Do not treat this file as an Outlook mirror, email archive, task list, project tracker, corporate record, or Work-facing agent source package.

---

## Tool Roles

| Tool | Role | Not For |
|---|---|---|
| Outlook Inbox | Executive signal intake | Project tracking, decision logs, knowledge storage |
| Outlook Folders | Noise reduction | Encoding durable meaning |
| Outlook Categories | Signal classification | Long-term truth or project taxonomy |
| Outlook Flags / Microsoft To Do | Abner-owned personal commitments | Team tasks, project work owned by others |
| Microsoft Teams | Fast coordination | Durable decisions or controlled executive records |
| Microsoft 365 Copilot | Compression, preparation, search, and drafting support | Final judgment, source of truth, private Work OS context storage |
| Jira | Delivery execution tracking | Personal reminders or executive signal intake |
| Confluence | Team and delivery documentation | Email archive or decision queue |
| Microsoft Lists | Structured intake or lightweight governance registers | Delivery backlog or project tracker |
| Work OS | Private reasoning and source-boundary control | Corporate records or raw Microsoft 365 export storage |

Decision rule:

```text
Email = signal intake
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
* From Sebastián Arcuri / Local CEO or Luis Alfredo
* From regional, corporate, regulatory, audit, risk, security, or executive stakeholders
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
1-Executive
2-Governance-Risk
3-Automated
4-Vendors
Archive
```

Rules:

* Keep folder count low.
* Do not create folders for every project.
* Do not create folders for every stakeholder.
* Do not create folders for Jira projects or Confluence spaces.
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

* Sebastián Arcuri / Local CEO or Luis Alfredo
* Direct manager, regional, or International Banking executive senders
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

Review Outlook rules monthly while the model is stabilizing, then quarterly after rules stop creating misses or duplicate review.

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
* Jira-owned project execution work
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
* Move delivery work to Jira
* Route to Technology Committee
* Capture structured governance follow-up in Microsoft Lists
* Archive

---

## Microsoft 365 Copilot Email Model

Microsoft 365 Copilot is a compression, preparation, and drafting layer.

Use it for:

* Morning executive signal scan
* Inbox prioritization
* Email thread summarization
* Email drafting and coaching
* Cross-surface catch-up across email, meetings, chats, and files
* Preparing concise executive replies
* Preparing Sebastián / Luis Alfredo interactions
* Preparing Technology Committee intake drafts
* Summarizing long threads into decision-ready structure

Do not use it to:

* Make final executive decisions
* Replace risk acceptance ownership
* Create corporate records outside approved systems
* Store private Work OS context
* Expose private political or leadership notes
* Connect broad Work OS sources to Work-facing agents
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
Show open threads involving Sebastián or Luis Alfredo where I owe a response, decision, review, or follow-up. Separate direct asks from FYI messages.
```

Decision extraction:

```text
Summarize this thread into: decision needed, recommendation, alternatives, risks, owner, deadline, and next visible signal.
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
* Local CEO / International Banking visibility
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

Review this playbook when:

* Outlook folders or categories become hard to maintain
* Rules hide executive signal or create duplicate work
* Microsoft To Do becomes ineffective as a personal commitment layer
* Microsoft 365 Copilot behavior changes materially
* AB-Gatekeeper or AB-Executive Drafter source boundaries change
* A new M365 email agent is proposed
