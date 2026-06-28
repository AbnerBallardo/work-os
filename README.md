# Work OS

Version: v1.0

---

## Purpose

Work OS is a **versioned control system for Work operating context, governance, executive decision support, and least-privilege agent runtime packages**, designed to:

* Preserve decision quality under Work pressure
* Separate private Work reasoning from Work-facing narrative artifacts
* Maintain reusable Work governance and execution patterns
* Maintain sanitized runtime packages for Work agents
* Keep Work operating context traceable, reviewable, and bounded

It defines **how Work context, execution rules, governance artifacts, and agent runtime sources are structured, constrained, maintained, and prepared for use**.

---

## System Model

```text
Context -> Judgment -> Execution Control -> Narrative -> Runtime Packages -> Feedback
     |          |             |               |                |
  Context   Decisions      Memory         Committee          Agents
```

### Layers

| Layer | Role | Nature |
|---|---|---|
| Context | Stable Work context, execution model, political landscape, and leadership map | Stable but reviewable |
| Memory | Compressed Work recall and validated observations | Curated |
| Decisions | Durable Work decision records and guardrails | Stable |
| Committees | Committee plans, governance, intake, templates, and decision-support mechanics | Stable / reusable |
| Agents | Runtime instructions, source boundaries, tests, and pilot material | Stable / deployable |
| Templates | Source-side prompt and runtime-package definitions | Stable / reusable |
| Build | Generated ChatGPT Project upload artifacts | Generated |
| Archive | Inactive or superseded Work artifacts | Historical |

---

## Canonical Sources

These files define the system. They are the **sources of truth**:

| Concept | Source File |
|---|---|
| Repository maintenance rules | `/AGENTS.md` |
| Work role, constraints, and operating context | `/context/Work - Context.md` |
| Work execution and narrative PARA rules | `/context/Work - PARA.md` |
| Work corporate tool and system boundaries | `/context/Work - Operating Stack.md` |
| Work political landscape | `/context/Work - Political.md` |
| Work leadership landscape | `/context/Work - Leadership Map.md` |
| Information handling and exposure rules | `/context/Information Handling Policy.md` |
| Compressed Work recall | `/memory/Work - Memory.md` |
| Work decision records | `/systems/decisions/work/` |
| Technology Committee charter | `/committees/technology/Technology Committee.md` |
| Committee mechanics | `/committees/technology/Technology Committee - Operating Runbook.md` |
| Committee templates | `/committees/technology/Technology Committee - * Template.md` |
| AB-Gatekeeper runtime behavior | `/agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md` |
| AB-Gatekeeper project calibration | `/agents/ab-gatekeeper/AB-Gatekeeper - Project Context Register.md` |
| AB-Executive Drafter runtime behavior | `/agents/ab-executive-drafter/AB-Executive Drafter - Agent Instructions.md` |
| AB-Executive Drafter recipient rules | `/agents/ab-executive-drafter/AB-Executive Drafter - Recipient Playbook.md` |
| M365 source boundaries | `/agents/*/* - OneDrive Source Package.md` |
| Work OS ChatGPT Project definitions | `/templates/prompts/ChatGPT Project Custom Instructions.md` |
| Work OS ChatGPT Project runtime packaging | `/templates/prompts/ChatGPT Project Runtime Packages.md` |

**Rule:**

This file is **not a source of truth**.

It is a **navigation and orientation layer**.

---

## Sensitivity

This repository is classified as **Highly Sensitive**.

Handling rules live in:

* `/context/Information Handling Policy.md`

---

## System Boundaries

### Work OS

Contains:

* Private Work operating context
* Work execution and narrative rules
* Work governance artifacts
* Committee operating templates
* Sanitized agent runtime sources
* Runtime-package source boundary documents
* Work OS ChatGPT Project templates and generated upload artifacts
* Pilot, test, and reference material for maintained agents
* Compressed Work memory and durable Work decision records

### Personal OS

Contains only:

* Operator-level Work overview
* Cross-domain Work implications
* Stable Work principles that affect Personal OS decisions
* Repository and source-boundary references

Personal OS does not store detailed Work political context, leadership maps, operational cases, Work agent packages, or Work governance artifacts.

### Corporate Systems

Contain:

* Official Work records
* Corporate communication
* Team collaboration artifacts
* Retention-governed documents

Work OS does not replace corporate systems of record.

---

## Admission Criteria

Material belongs in Work OS only if it is:

* Reusable across future Work execution, governance, or agent activity
* Stable enough to govern repeated decisions
* Useful for private Work judgment, narrative control, committee mechanics, agent behavior, source boundaries, or validation
* Generalizable beyond one event, person, meeting, or short-lived project

Otherwise:

-> Keep it in the Work execution layer, corporate system of record, or archive/delete it.

---

## Repository Navigation

```text
/context/                      -> Work context, execution rules, operating stack, political map, leadership map, and information-handling rules
/memory/                       -> Compressed Work recall and validated observations
/systems/decisions/work/         -> Durable Work decision records
/committees/                   -> Committee plans and governance materials
/committees/technology/        -> Technology Committee charter, runbook, and templates
/agents/ab-gatekeeper/         -> Gatekeeper runtime package, references, tests, and pilot material
/agents/ab-executive-drafter/  -> Executive drafting runtime package, playbook, tests, and pilot material
/templates/prompts/            -> ChatGPT Project source-side templates and package rules
/build/chatgpt-projects/work-os/ -> Generated upload package for the Work OS ChatGPT Project
/archive/                      -> Inactive or superseded Work artifacts
/AGENTS.md                     -> Codex maintenance instructions
/README.md                     -> Repository orientation
```

---

## Usage Model

### Codex

Use Codex for repository maintenance and system improvement:

* Structural review
* Rule compression
* File organization
* Runtime package refresh
* Source-boundary review
* Git-based change control

Codex should edit source files only when a reusable Work context, governance rule, agent behavior, runtime package, or boundary needs to change.

### M365 Agents

Use M365 agents for Work-facing execution support:

* Email triage
* Committee routing
* Executive drafting
* Message compression
* Decision-support preparation

M365 agents are runtime environments.

They are not:

* Sources of truth
* Private context stores
* Backlogs
* Stakeholder dossiers
* Raw Work OS mirrors

Default runtime source rule:

```text
Only connect the files listed in the relevant OneDrive Source Package.
```

### ChatGPT Project

Use one ChatGPT Project by default:

| Project | Role | Runtime package |
|---|---|---|
| Work OS | Private Work OS reasoning, maintenance, and source-boundary review | `/build/chatgpt-projects/work-os/` |

ChatGPT Project uploads are generated runtime artifacts.

They are not:

* canonical source files
* corporate records
* M365 agent source packages
* permanent storage for prompt-specific execution material

Runtime package source rule:

```text
templates/prompts/ChatGPT Project Runtime Packages.md
```

Project definition source rule:

```text
templates/prompts/ChatGPT Project Custom Instructions.md
```

---

## Current Agent Set

| Agent | Role | Runtime sources |
|---|---|---|
| AB-Gatekeeper | Triage emails, classify depth, and route committee-relevant topics | `/agents/ab-gatekeeper/AB-Gatekeeper - OneDrive Source Package.md` |
| AB-Executive Drafter | Draft executive-ready messages using recipient and communication-state rules | `/agents/ab-executive-drafter/AB-Executive Drafter - OneDrive Source Package.md` |

Hard rule:

* Keep runtime packages minimal and least-privilege.
* Add a new permanent agent only after explicit source-boundary review.
* Do not create permanent agents for one-off topics, meetings, stakeholders, or temporary initiatives.

---

## Decision Flow

```text
Signal -> Interpretation -> Decision -> Execution Control -> Narrative -> Feedback -> Source Update
```

Canonical control:

* Work context: `/context/Work - Context.md`
* Work execution model: `/context/Work - PARA.md`
* Work operating stack: `/context/Work - Operating Stack.md`
* Information handling: `/context/Information Handling Policy.md`
* Work memory: `/memory/Work - Memory.md`
* Governance: `/committees/technology/Technology Committee.md`
* Mechanics: `/committees/technology/Technology Committee - Operating Runbook.md`
* Agent behavior: `/agents/*/* - Agent Instructions.md`
* Runtime boundaries: `/agents/*/* - OneDrive Source Package.md`

---

## Versioning

```text
Version: vX.Y
```

Change when:

* Canonical source boundaries change
* Information-handling or exposure rules change
* A new durable Work OS layer is added
* Agent runtime source rules change
* Committee governance materially changes

---

## AI Usage

AI tools may:

* Review structure
* Compress rules
* Draft artifacts from explicit source files
* Identify boundary drift
* Prepare runtime packages

AI tools may not:

* Treat chat history as source of truth
* Promote temporary Work events without review
* Connect private Work context directly to Work-facing agents
* Replace executive judgment

---

## Guiding Principle

> Work OS owns detailed Work operating context and controlled Work execution support.
>
> Personal OS owns only the operator-level Work overview needed for cross-domain judgment.
