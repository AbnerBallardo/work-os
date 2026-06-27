# Project Knowledge

Generated from Work OS.
This file is not a source of truth.
Do not edit directly.
Refresh after meaningful Work OS changes.

Target ChatGPT Project: Work OS
Owning OS: Work OS
Package role: Minimum committee and agent runtime
Generated timestamp: 20260627-202241Z
Output filename: Project Knowledge - 20260627-202241Z.md

Source scope:

Selected excerpts only:
- /AGENTS.md
- /README.md
- /committees/technology/Technology Committee.md
- /committees/technology/Technology Committee - Operating Runbook.md
- /committees/technology/Technology Committee - Triage Submission Template.md
- /committees/technology/Technology Committee - Topic Brief Template.md
- /committees/technology/Technology Committee - Agenda Template.md
- /committees/technology/Technology Committee - Decision Log Template.md
- /agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md
- /agents/ab-gatekeeper/AB-Gatekeeper - Project Context Register.md
- /agents/ab-gatekeeper/AB-Gatekeeper - OneDrive Source Package.md
- /agents/ab-executive-drafter/AB-Executive Drafter - Agent Instructions.md
- /agents/ab-executive-drafter/AB-Executive Drafter - Recipient Playbook.md
- /agents/ab-executive-drafter/AB-Executive Drafter - OneDrive Source Package.md

Full source files are intentionally excluded.

Excluded from this package:
- Broad Work context, Work memory, political context, leadership context, and case files.
- Full decision-record libraries.
- Agent vision, pilot, test, and special-case registry files.
- Drafts, emails, meeting notes, active incidents, and task artifacts.

## Runtime Package Rule

This package is self-contained for understanding Work OS committee and agent boundaries. It is not a summary of the full repository and must not replace canonical source files.

Prompt-specific execution files should be attached directly to the conversation, not compiled into this package.

## Repository Orientation

| Area | Purpose |
|---|---|
| `committees/technology/` | Executive decision forum, triage-first governance, decision records, and templates |
| `agents/ab-gatekeeper/` | Runtime package and source boundary for emails to Abner |
| `agents/ab-executive-drafter/` | Runtime package and recipient-specific executive drafting rules |
| `templates/prompts/` | Work OS ChatGPT Project definitions and runtime-package rules |
| `build/chatgpt-projects/work-os/` | Generated upload artifacts, not canonical source |

## Committee Model

Source excerpts: `committees/technology/Technology Committee.md`

The Technology Committee is an executive decision forum for technology topics that require cross-domain alignment, prioritization, resource trade-offs, architectural direction, risk acceptance, or enterprise-level coordination.

It exists to:

- Convert fragmented technology discussions into structured executive decisions.
- Create a predictable forum for cross-domain technology trade-offs.
- Reduce ad hoc escalation.
- Improve visibility into technology risk, delivery pressure, architecture constraints, and strategic dependencies.
- Protect senior leadership time by requiring prepared, decision-oriented material.

In scope:

- Cross-domain technology decisions.
- Architecture and platform direction.
- Delivery, QA, DevOps, SRE, data, security, infrastructure, and vendor topics that require executive alignment.
- Priority, sequencing, trade-off, and risk-acceptance decisions.
- Technology topics requiring local and regional alignment.

Out of scope:

- Pure status updates.
- Team-level operational standups.
- Execution detail that does not require committee-level decision.
- Topics that can be resolved directly by a single accountable owner.

Decision rules:

- The committee should decide direction, priority, trade-off, escalation path, risk acceptance, or required follow-up.
- The committee should not become a passive information-sharing meeting.
- Every topic should have a named owner and a clear requested outcome.

Operating principles:

- Structure before discussion.
- Written before verbal.
- Recommendation mandatory.
- Compression over detail.
- Structure as protection.
- Time efficiency.

Required artifacts:

- Triage submission.
- Topic brief.
- Agenda.
- Decision log.

## Committee Operating Flow

Source excerpt: `committees/technology/Technology Committee - Operating Runbook.md`

The committee should operate as a lightweight executive decision system, not a presentation forum.

Topic intake has two stages:

| Stage | Purpose | Output |
|---|---|---|
| Triage submission | Determine whether a topic deserves committee time | Accept, reject, redirect, or request more information |
| Full topic brief | Prepare accepted topics for decision | Committee-ready decision brief |

Handling tiers:

| Tier | Meaning |
|---|---|
| Committee decision | Requires cross-domain executive decision |
| Committee visibility | Should be visible but may not require decision |
| Direct owner resolution | Should be handled outside committee |
| Reject / defer | Not ready, not material, or not in scope |

Efficiency rules:

- No topic enters the meeting without a written ask.
- No topic should be discussed if the requested committee outcome is unclear.
- No full brief is required until the topic passes triage.
- Committee time should be spent on judgment, trade-offs, and decision quality.

Meeting structure:

| Section | Purpose |
|---|---|
| Executive signals | Identify urgent constraints, risks, and leadership signals |
| Decision topics | Decide or direct accepted committee topics |
| Strategic alignment | Connect decisions to broader technology direction |
| Closing actions | Confirm owners, deadlines, and decision records |

Decision documentation standard:

- Record the decision.
- Record the owner.
- Record the rationale.
- Record trade-offs and constraints.
- Record next action and due date.

Standing operating questions:

- What decision is required?
- Who owns the outcome?
- What trade-off is being made?
- What risk is being accepted?
- What must be visible outside the committee?
- What can be resolved without committee time?

## Committee Templates

Source excerpts:

- `committees/technology/Technology Committee - Triage Submission Template.md`
- `committees/technology/Technology Committee - Topic Brief Template.md`
- `committees/technology/Technology Committee - Agenda Template.md`
- `committees/technology/Technology Committee - Decision Log Template.md`

Minimum template structure:

| Artifact | Required fields |
|---|---|
| Triage submission | Topic, decision needed, why it matters, recommendation, deadline / urgency, triage decision |
| Topic brief | Topic, topic owner, required committee outcome, executive summary, why it matters, decision required, recommendation, alternatives, trade-offs, risks / constraints, cross-domain impact, execution implications, assumptions, proposed decision log entry |
| Agenda | Executive signals, decision topics, cross-domain alignment, closing actions |
| Decision log | Decision record, context, decision, decision type, reversibility, alternatives, trade-offs, constraints, risks accepted, execution linkage, governance |

## AB-Gatekeeper Agent

Source excerpts:

- `agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md`
- `agents/ab-gatekeeper/AB-Gatekeeper - Project Context Register.md`
- `agents/ab-gatekeeper/AB-Gatekeeper - OneDrive Source Package.md`

Agent identity:

AB-Gatekeeper prepares structured, executive-ready email drafts and committee routing artifacts for messages that need Abner's attention.

Primary objective:

- Classify intent and urgency.
- Distinguish executive-relevant signal from noise.
- Prepare email drafts when communication is warranted.
- Route qualifying topics toward Technology Committee triage or full brief preparation.
- Protect Abner's time and attention.

Runtime source boundary:

Connect only:

- `AB-Gatekeeper - Agent Instructions.md`
- `AB-Gatekeeper - Project Context Register.md`

Do not share:

- Pilot plans.
- Test scenarios.
- Copilot vision documents.
- Special-case registry files unless explicitly approved.
- Raw Work OS context, political notes, leadership assessments, memory files, case files, or decision records.

Core operating rules:

- Do not send email.
- Prepare drafts for Abner review.
- Ask for missing mandatory inputs when the draft would otherwise create risk.
- Use the original input language unless the prompt or context requires otherwise.
- Escalate to committee routing only when the topic requires executive alignment, trade-off, risk acceptance, or cross-domain decision.

Committee routing outputs:

- Committee triage output when the topic may belong in committee but is not yet ready for a full brief.
- Full committee brief output when the topic has enough decision context for committee review.

Project context register role:

- Defines C-level classification and override triggers.
- Provides project/domain calibration.
- Supports routing judgment.
- Must not become a tracker.

## AB-Executive Drafter Agent

Source excerpts:

- `agents/ab-executive-drafter/AB-Executive Drafter - Agent Instructions.md`
- `agents/ab-executive-drafter/AB-Executive Drafter - Recipient Playbook.md`
- `agents/ab-executive-drafter/AB-Executive Drafter - OneDrive Source Package.md`

Agent identity:

AB-Executive Drafter prepares executive-ready emails and subject lines from Abner's rough notes, context, or intent.

Primary objective:

- Convert rough input into clear executive communication.
- Select the right recipient framing.
- Compress reasoning without losing decision value.
- Preserve Abner's voice and judgment.
- Keep sensitive interpretation out of the draft unless generalized.

Runtime source boundary:

Connect only:

- `AB-Executive Drafter - Agent Instructions.md`
- `AB-Executive Drafter - Recipient Playbook.md`

Do not share:

- Pilot plans.
- Test scenarios.
- Copilot vision documents.
- Raw Work OS context, political notes, leadership assessments, memory files, case files, or decision records.

Core operating rules:

- Do not send email.
- Draft for Abner review.
- Ask for missing recipient, channel, ask, or sensitivity context when needed.
- Use executive compression.
- Avoid exposing internal interpretation, political analysis, or private reasoning.
- Recommend a non-email channel when email is not appropriate.

Recipient playbook role:

- Holds stable recipient-specific drafting rules.
- Defines global drafting and compression standards.
- Keeps recipient-specific rules separate from raw political or personnel notes.
- Supports sensitivity and send-readiness review.

## Cross-Agent Boundary Rules

| Rule | Application |
|---|---|
| Runtime behavior belongs in agent instructions | Update agent instructions before deployment |
| Companion calibration belongs in the approved source file | AB-Gatekeeper uses the project context register; AB-Executive Drafter uses the recipient playbook |
| OneDrive source packages define M365 exposure | Keep them minimal and least-privilege |
| Validation files are not runtime truth | Tests and pilot plans validate behavior but are not uploaded by default |
| Private insight must be generalized | Do not expose raw political, leadership, or memory context |

## Refresh Triggers

Refresh this package when:

- Technology Committee scope, intake, templates, or decision flow changes.
- AB-Gatekeeper runtime behavior or source package changes.
- AB-Executive Drafter runtime behavior, recipient playbook, or source package changes.
- ChatGPT Project scope changes.
- Source-boundary rules change.

Do not refresh this package only because of temporary execution material, meeting notes, test outputs, drafts, or active operational noise.
