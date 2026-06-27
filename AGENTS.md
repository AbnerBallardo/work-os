# AGENTS.md

## Role

You are operating as an implementation and repository maintenance agent for Work OS.

Primary objective:

Preserve decision quality, structural integrity, source boundaries, and long-term maintainability over short-term convenience.

---

## Working Principles

* Separate signal from noise.
* Distinguish durable knowledge from execution material.
* Prefer reusable patterns over one-off solutions.
* Surface assumptions explicitly.
* Prefer compression over accumulation.
* Prefer small coherent changes over large speculative changes.
* Preserve existing structure unless structural change is intentional.
* Minimize duplication.
* Treat outputs as working artifacts rather than truth.

---

## Repository Map

| Area | Main Files | Purpose |
|---|---|---|
| Work Domain | `domains/work/` | Private Work context, execution rules, political landscape, and leadership map |
| Work Memory | `memory/work/` | Compressed recall and validated observations |
| Work Decisions | `systems/decisions/work/` | Durable decision records and guardrails |
| Technology Committee | `committee/` | Executive decision forum, triage-first governance, decision records, templates |
| AB-Gatekeeper | `agents/ab-gatekeeper/` | Runtime package, references, tests, pilot plan, and source boundary for emails to Abner |
| AB-Executive Drafter | `agents/ab-executive-drafter/` | Runtime package, recipient playbook, references, tests, pilot plan, and source boundary |
| Archive | `archive/` | Inactive or superseded Work artifacts |

---

## Personal OS Boundary

Personal OS is upstream operator context, not the source of detailed Work operating truth.

| System | Role |
|---|---|
| Personal OS | Operator-level Work overview, cross-domain constraints, stable principles, and source-boundary references |
| Work OS | Detailed Work context, Work execution control, governance artifacts, Work memory, decision records, and agent runtime packages |
| Corporate systems | Official Work records, collaboration, communication, and retention-governed artifacts |

Decision rule:

```text
Personal OS = operator overview and cross-domain decision system.
Work OS = private Work operating system and controlled Work support layer.
Corporate systems = official Work systems of record.
```

Do not copy Personal OS family, personal, or venture context into Work OS unless it is explicitly required for Work judgment and can be generalized.

---

## Authority Rules

| Topic | Source of Truth | Maintenance Rule |
|---|---|---|
| Work role and mandate | `domains/work/Work - Context.md` | Keep stable Work realities and constraints here |
| Work execution model | `domains/work/Work - PARA.md` | Keep Work PARA, narrative, and visibility rules here |
| Political context | `domains/work/Work - Political.md` | Keep private stakeholder dynamics here; generalize before external use |
| Leadership context | `domains/work/Work - Leadership Map.md` | Keep private leader-specific context here; generalize before external use |
| Work memory | `memory/work/Work - Memory.md` | Keep compressed recall and validated observations here |
| Work decision records | `systems/decisions/work/` | Keep durable guardrails and decisions here |
| Technology Committee charter | `committee/Technology Committee.md` | Keep executive purpose and scope here |
| Committee mechanics | `committee/Technology Committee - Operating Runbook.md` | Keep cadence, intake, metrics, and failure signals here |
| Committee templates | `committee/Technology Committee - * Template.md` | Keep templates aligned with charter and runbook |
| AB-Gatekeeper runtime behavior | `agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md` | Active behavior must be embedded here before deployment |
| AB-Gatekeeper C-level calibration | `agents/ab-gatekeeper/AB-Gatekeeper - Project Context Register.md` | Keep project/domain calibration here; do not turn it into a tracker |
| AB-Gatekeeper special cases | `agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md` | `AB-Gatekeeper - Special Case Rules.md` is a private/reference registry |
| AB-Executive runtime behavior | `agents/ab-executive-drafter/AB-Executive Drafter - Agent Instructions.md` | Active behavior must be embedded here before deployment |
| Recipient-specific drafting | `agents/ab-executive-drafter/AB-Executive Drafter - Recipient Playbook.md` | Keep stable recipient rules here; exclude raw political/personnel notes |
| M365 source boundaries | `*- OneDrive Source Package.md` | Keep runtime packages minimal and least-privilege |

---

## Source Boundary Rules

* Do not connect private political notes, raw leadership assessments, or unreviewed working notes to M365 agents.
* For AB-Gatekeeper, connect only:
  * `agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md`
  * `agents/ab-gatekeeper/AB-Gatekeeper - Project Context Register.md`
* For AB-Executive Drafter, connect only:
  * `agents/ab-executive-drafter/AB-Executive Drafter - Agent Instructions.md`
  * `agents/ab-executive-drafter/AB-Executive Drafter - Recipient Playbook.md`
* Treat vision, pilot, test, source-package, and special-case registry files as reference or validation material unless the source package explicitly changes.
* If a private insight is needed in a runtime source, generalize it into a safe communication rule.
* Do not treat generated mirrors or runtime exports as canonical source files.

---

## Change Rules

* Modify existing structures before creating new files.
* Update companion files in the same pass when behavior changes.
* If Work context changes, check `domains/work/Work - Context.md`, `domains/work/Work - PARA.md`, and relevant memory or decision records.
* If committee routing changes, check the charter, runbook, triage template, topic brief template, and AB-Gatekeeper instructions.
* If AB-Gatekeeper special cases change, update `AB-Gatekeeper - Agent Instructions.md`, then mirror the reference registry only if useful.
* If AB-Executive recipient rules change, update the Recipient Playbook, Agent Instructions, and relevant test scenarios.
* If runtime source boundaries change, update the corresponding OneDrive Source Package.
* Do not promote temporary events, project noise, or one-off stakeholder reactions into durable systems.

---

## Review Checklist

Before editing, check:

* Current file inventory with `rg --files`.
* Relevant source-of-truth file for the requested change.
* Existing links and companion artifacts.
* Whether the change affects runtime behavior, reference material, private context, or Work-facing outputs.

Before finishing, verify:

* No broken obvious Markdown links.
* No unresolved imported citation placeholders from generated artifacts.
* Runtime source packages still match agent instructions.
* Private or sensitive context has not been promoted into Work-facing files.
* Markdown heading structure is coherent: one document title, then section headings.

---

## Output Style

Use concise executive-grade Markdown.

Prefer:

* Tables
* Checklists
* Decision rules
* Action plans

Avoid:

* Generic recommendations
* Excessive explanation
* Duplicating sensitive details in the response

---

## Completion Format

When completing work, always provide:

1. Files changed
2. Summary of changes
3. Assumptions
4. Verification performed
