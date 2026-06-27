# Project Knowledge

Generated from Work OS.
This file is not a source of truth.
Do not edit directly.
Refresh after meaningful Work OS changes.

Target ChatGPT Project: Work OS
Owning OS: Work OS
Package role: Minimum committee and agent runtime
Generated timestamp: 20260627-204038Z
Output filename: Project Knowledge - 20260627-204038Z.md

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

## Committee Admission

Source excerpt: `committees/technology/Technology Committee.md`

A topic belongs in Technology Committee only when it requires at least one of these outcomes.

| Committee Outcome | Meaning |
|---|---|
| Direction | Decide the strategic or architectural path |
| Priority | Decide sequencing across domains |
| Trade-off | Decide between speed, risk, cost, capacity, or control |
| Risk acceptance | Make explicit what risk the organization is accepting |
| Escalation path | Decide what needs local, regional, business, or corporate escalation |
| Ownership | Confirm who owns the outcome |
| Cross-domain alignment | Align Engineering, Architecture, Security, Delivery, Data, SRE, Infrastructure, or business stakeholders |

The committee is not a status meeting. Pure status updates, tactical coordination, incident investigation, deep technical debugging, local team decisions, raw operational noise, and information-only topics should be redirected.

## Standing Topic Categories

Source excerpt: `committees/technology/Technology Committee.md`

| Category | Why It Belongs |
|---|---|
| Technology organization design | Decisions on Engineering, SRE, Infrastructure, director structures, reporting model, and capability ownership |
| Stability and incident readiness | Monitoring maturity, SRE coverage, incident detection, and operational resilience |
| Critical vendor / platform risk | Unsupported platforms, material vendor service gaps, and production, security, continuity, or commercial exposure |
| Architecture direction | Build vs. buy, vendor recommendation, platform modernization, and legacy constraints |
| Business-owned technology decisions | Topics where Technology has a recommendation but business must decide |
| Technology finance and performance | Budget, value, licensing, investment justification, productivity, and delivery pressure |
| Local-regional alignment | Topics requiring coordination with International Banking, Canada, Corporate Security, or regional functions |

## Executive Signals

Source excerpt: `committees/technology/Technology Committee.md`

An executive signal is a leadership concern, risk pattern, organizational constraint, business pressure, or material event that may require committee visibility or decision, even before it becomes a formal topic.

| Signal Pattern | Generalized Rule |
|---|---|
| Users detect incidents before Technology | Treat as a monitoring maturity and operating model signal, not only an incident defect |
| Repeated executive pressure on the same topic | Convert into a written decision ask or escalation path |
| Business expects Technology to push a decision | Clarify whether the decision is technical, business-owned, or jointly owned |
| Vendor service gap creates production exposure | Route to risk acceptance, remediation ownership, and commercial escalation |
| Org design debates emerge from headcount ratios | Convert into capability model, accountability, and continuity discussion |

## Committee Operating Flow

Source excerpt: `committees/technology/Technology Committee - Operating Runbook.md`

Triage-first rule:

```text
No topic enters the Technology Committee agenda unless the requested outcome is explicit: decide, align, accept risk, escalate, redirect, or record.
```

| Section | Purpose | Input |
|---|---|---|
| Executive signals | Surface material risks, leadership asks, or constraints | Short signal list |
| Decision topics | Decide accepted topics | Topic briefs |
| Cross-domain alignment | Clarify dependencies and impacts | Owners and domains |
| Closing actions | Confirm decision, owner, next action, and due date | Decision log |

Escalation rule:

```text
Escalate only when the committee has identified what decision is needed, who owns it, what trade-off is being made, and what risk is being accepted.
```

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
| Triage submission | Topic, executive signal, decision needed, requested committee outcome, decision owner, business owner / technology owner, why it matters, recommendation, deadline / urgency, consequence of no decision, recommended routing, triage decision |
| Topic brief | Topic, topic owner, required committee outcome, decision boundary, executive summary, why it matters, decision required, recommendation, alternatives, trade-offs, risks / constraints, risk accepted, cross-domain impact, execution implications, execution linkage, assumptions, proposed decision log entry |
| Agenda | Executive signals, decision topics, cross-domain alignment, closing actions |
| Decision log | Decision record, context, decision, decision taxonomy, reversibility, alternatives, trade-offs, constraints, risks accepted, execution linkage, governance |

Decision taxonomy:

| Decision Type | Use When |
|---|---|
| Architecture direction | Platform, vendor, build / buy, modernization |
| Risk acceptance | Known exposure remains after decision |
| Resource allocation | Capacity, budget, team structure, ownership |
| Escalation | Topic must move to business, regional, corporate, or vendor negotiation |
| Operating model | Changes in accountability, process, governance, or forum design |
| Visibility only | No decision, but leadership awareness is required |

Decision log completeness rule:

```text
A decision log entry is incomplete unless it records the decision, owner, rationale, trade-offs, constraints, accepted risks, next action, and due date.
```

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

Route to Technology Committee triage when an email or message includes:

- Cross-domain technology impact.
- Architecture or platform direction.
- Business decision needed after Technology recommendation.
- Vendor risk with production, security, continuity, or commercial exposure.
- Incident pattern or monitoring maturity issue.
- Local-regional dependency or escalation.
- Resource, ownership, or organization design trade-off.
- Risk acceptance that should not remain implicit.

Executive signal classification:

| Level | Meaning | Gatekeeper Action |
|---|---|---|
| `ES1` | Informational / low signal | Summarize or ignore |
| `ES2` | Needs response but single-owner | Draft response or redirect |
| `ES3` | Cross-domain or executive relevance | Prepare triage artifact |
| `ES4` | Material risk, escalation, or decision | Prepare committee routing and executive draft |
| `ES5` | Critical exposure or urgent executive concern | Prepare immediate escalation draft and committee decision framing |

Project context register rule:

The register calibrates routing judgment. It must not track project status, tasks, commitments, stakeholder histories, or temporary execution notes.

## AB-Executive Drafter Agent

Source excerpts:

- `agents/ab-executive-drafter/AB-Executive Drafter - Agent Instructions.md`
- `agents/ab-executive-drafter/AB-Executive Drafter - Recipient Playbook.md`
- `agents/ab-executive-drafter/AB-Executive Drafter - OneDrive Source Package.md`

Agent identity:

AB-Executive Drafter prepares executive-ready emails and subject lines from Abner's rough notes, context, or intent.

When drafting for Abner:

- Be direct, short, and decision-oriented.
- Avoid over-explaining.
- Separate fact, implication, and ask.
- Do not expose private interpretation, political analysis, or raw leadership assessment.
- Convert sensitive context into neutral business language.

Channel selection:

| Channel | Use When |
|---|---|
| WhatsApp | Fast alignment, pre-brief, informal executive heads-up |
| Teams | Concise operational update, visible leadership response, active thread |
| Email | Formal decision, escalation, evidence trail, stakeholder alignment |
| Committee brief | Cross-domain decision, trade-off, risk acceptance, or governance record |

Sensitivity rule:

```text
If the input contains political, leadership, or private interpretation, the draft must express only the business-relevant implication and requested action.
```

## Cross-Agent Boundary Rules

| Rule | Application |
|---|---|
| Runtime behavior belongs in agent instructions | Update agent instructions before deployment |
| Companion calibration belongs in the approved source file | AB-Gatekeeper uses the project context register; AB-Executive Drafter uses the recipient playbook |
| OneDrive source packages define M365 exposure | Keep them minimal and least-privilege |
| Validation files are not runtime truth | Tests and pilot plans validate behavior but are not uploaded by default |
| Private insight must be generalized | Do not expose raw political, leadership, or memory context |

Only connect approved runtime files.

Do not connect:

- Raw Work OS memory.
- Political context.
- Leadership assessments.
- Case files.
- Draft emails.
- Meeting notes.
- Incident details.
- Active execution material.
- Full decision-record libraries.
- Test, pilot, or vision files unless explicitly approved.

## Refresh Triggers

Refresh this package when:

- Technology Committee scope, intake, templates, or decision flow changes.
- AB-Gatekeeper runtime behavior or source package changes.
- AB-Executive Drafter runtime behavior, recipient playbook, or source package changes.
- ChatGPT Project scope changes.
- Source-boundary rules change.

Do not refresh this package only because of temporary execution material, meeting notes, test outputs, drafts, or active operational noise.
