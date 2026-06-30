# AGENTS.md

## Role

You are operating as an implementation and repository maintenance agent for Abner Ballardo's Work OS.

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
* Keep files in English.

---

## Repository Map

| Area | Main Files | Purpose |
|---|---|---|
| Work context | `context/` | Private Work context, execution rules, political landscape, leadership map, and information-handling rules |
| Work memory | `memory/` | Compressed recall and validated observations |
| Work decisions | `systems/decisions/work/` | Durable decision records and guardrails |
| Work resources | `resources/` | Reusable execution playbooks and working guidance subordinate to context authority |
| Committees | `committees/` | Committee plans and governance materials |
| Technology Committee | `committees/technology/` | Executive decision forum, triage-first governance, decision records, and templates |
| AB-Gatekeeper | `agents/ab-gatekeeper/` | Runtime package, references, tests, pilot plan, and source boundary for emails to Abner |
| AB-Executive Drafter | `agents/ab-executive-drafter/` | Runtime package, recipient playbook, references, tests, pilot plan, and source boundary |
| Prompt templates | `templates/prompts/` | Reusable Work OS prompt templates, ChatGPT Project definitions, and runtime-package rules |
| ChatGPT Project builds | `build/chatgpt-projects/work-os/` | Generated upload artifacts when present |
| Archive | `archive/` | Inactive or superseded Work artifacts |
| Repository guide | `README.md` | Orientation only |

---

## System Boundaries

| System | Role |
|---|---|
| Work OS | Detailed Work context, Work execution control, governance artifacts, Work memory, decision records, and agent runtime packages |
| Personal OS | Operator-level Work overview, cross-domain constraints, stable principles, and source-boundary references |
| Corporate systems | Official Work records, collaboration, communication, and retention-governed artifacts |
| Content OS | Public-expression governance; Work material may be used only after generalization and exposure review |

Decision rule:

```text
Work OS = private Work operating system and controlled Work support layer.
Personal OS = operator overview and cross-domain decision system.
Corporate systems = official Work systems of record.
Content OS = public-expression system, not Work context storage.
```

Do not copy Personal OS family, personal, venture, or Content OS context into Work OS unless it is explicitly required for Work judgment and can be generalized.

---

## Authority Rules

| Topic | Source of Truth | Maintenance Rule |
|---|---|---|
| Work role and mandate | `context/Context.md` | Keep stable Work realities and constraints here |
| Work execution model | `context/PARA.md` | Keep Work PARA, narrative, and visibility rules here |
| Work operating stack | `context/Operating Stack.md` | Keep corporate tool roles, device constraints, and system boundaries here |
| Political context | `context/Political.md` | Keep private stakeholder dynamics here; generalize before external use |
| Leadership context | `context/Leadership Map.md` | Keep private leader-specific context here; generalize before external use |
| Information handling | `context/Information Handling Policy.md` | Keep repository sensitivity, exposure, externalization, and AI usage rules here |
| Microsoft 365 working playbooks | `resources/microsoft-365/` | Keep changing email, calendar, notes, tasks, Teams, and Copilot execution guidance here; subordinate to `context/Operating Stack.md` |
| Work memory | `memory/Work - Memory.md` | Keep compressed recall and validated observations here |
| Work decision records | `systems/decisions/work/` | Keep durable guardrails and decisions here |
| Technology Committee charter | `committees/technology/Technology Committee.md` | Keep executive purpose and scope here |
| Committee mechanics | `committees/technology/Technology Committee - Operating Runbook.md` | Keep cadence, intake, metrics, and failure signals here |
| Committee templates | `committees/technology/Technology Committee - * Template.md` | Keep templates aligned with charter and runbook |
| AB-Gatekeeper runtime behavior | `agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md` | Active behavior must be embedded here before deployment |
| AB-Gatekeeper calibration | `agents/ab-gatekeeper/AB-Gatekeeper - Project Context Register.md` | Keep project/domain calibration here; do not turn it into a tracker |
| AB-Gatekeeper special cases | `agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md` | `AB-Gatekeeper - Special Case Rules.md` is a private/reference registry |
| AB-Executive runtime behavior | `agents/ab-executive-drafter/AB-Executive Drafter - Agent Instructions.md` | Active behavior must be embedded here before deployment |
| Recipient-specific drafting | `agents/ab-executive-drafter/AB-Executive Drafter - Recipient Playbook.md` | Keep stable recipient rules here; exclude raw political/personnel notes |
| M365 source boundaries | `*- OneDrive Source Package.md` | Keep runtime packages minimal and least-privilege |
| Reusable Work OS prompt templates | `templates/prompts/Core Prompt Templates.md` | Keep stable prompt patterns here; exclude temporary execution prompts and high-churn examples |
| Work OS ChatGPT Project definitions | `templates/prompts/ChatGPT Project Custom Instructions.md` | Keep project role, runtime assumptions, and source scope here |
| Work OS ChatGPT Project runtime packaging | `templates/prompts/ChatGPT Project Runtime Packages.md` | Keep compilation rules and generated package contract here |
| Generated packages | `build/chatgpt-projects/` | Treat as generated upload artifacts, not canonical source |

---

## Source Boundary Rules

* Read the relevant source-of-truth file before making structural edits.
* Apply `context/Information Handling Policy.md` before exposing Work OS content outside private Work OS reasoning.
* Do not connect private political notes, raw leadership assessments, broad Work context, memory, or unreviewed working notes to M365 agents.
* For AB-Gatekeeper, connect only:
  * `agents/ab-gatekeeper/AB-Gatekeeper - Agent Instructions.md`
  * `agents/ab-gatekeeper/AB-Gatekeeper - Project Context Register.md`
* For AB-Executive Drafter, connect only:
  * `agents/ab-executive-drafter/AB-Executive Drafter - Agent Instructions.md`
  * `agents/ab-executive-drafter/AB-Executive Drafter - Recipient Playbook.md`
* Treat vision, pilot, test, source-package, and special-case registry files as reference or validation material unless the source package explicitly changes.
* If a private insight is needed in a runtime source, generalize it into a safe communication, routing, or review rule.
* Do not treat generated mirrors or runtime exports as canonical source files.
* Keep `build/chatgpt-projects/` as generated ChatGPT upload material.

---

## Change Rules

* Modify existing structures before creating new files.
* Update companion files in the same pass when behavior changes.
* If Work context changes, check `context/Context.md`, `context/PARA.md`, `context/Operating Stack.md`, `context/Information Handling Policy.md`, and relevant memory or decision records.
* If committee routing changes, check the charter, runbook, triage template, topic brief template, and AB-Gatekeeper instructions.
* If AB-Gatekeeper special cases change, update `AB-Gatekeeper - Agent Instructions.md`, then mirror the reference registry only if useful.
* If AB-Executive recipient rules change, update the Recipient Playbook, Agent Instructions, and relevant test scenarios.
* If runtime source boundaries change, update the corresponding OneDrive Source Package.
* If Microsoft 365 workflow guidance changes, update `resources/microsoft-365/` and keep `context/Operating Stack.md` limited to durable tool authority and boundaries.
* If information-handling or exposure rules change, update `context/Information Handling Policy.md`, README, runtime templates, and `/config/chatgpt-project-builds.json`.
* If ChatGPT Project runtime scope changes, update `templates/prompts/ChatGPT Project Custom Instructions.md`, `templates/prompts/ChatGPT Project Runtime Packages.md`, and `/config/chatgpt-project-builds.json`; generated `build/chatgpt-projects/work-os/` files are produced after push by GitHub Actions before Drive sync.
* Do not promote temporary events, project noise, or one-off stakeholder reactions into durable systems.

---

## Review Checklist

Before editing, check:

* Current file inventory with `rg --files`.
* Relevant source-of-truth file for the requested change.
* Existing links and companion artifacts.
* Whether the change affects runtime behavior, reference material, private context, or Work-facing outputs.

Before finishing, verify:

* Affected headings and navigation remain coherent.
* No broken obvious Markdown links.
* No unresolved imported citation placeholders from generated artifacts.
* Runtime source packages still match agent instructions.
* Information-handling references remain aligned with `context/Information Handling Policy.md`.
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
* Explicit assumptions

Avoid:

* Generic recommendations
* Excessive explanation
* Duplicating sensitive details in the response
* Unnecessary new files

---

## Completion Format

When completing work, always provide:

1. Files changed
2. Summary of changes
3. Assumptions
4. Verification performed
