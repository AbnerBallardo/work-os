# Work - PARA

Version: v1.1

Context owner: Abner Ballardo. This file should be read as context about Abner Ballardo, his decisions, constraints, operating environment, and personal operating system. Any third-party people, organizations, or systems are included only insofar as they shape Abner Ballardo's context.

---

## Purpose

Define how the execution system (PARA) is applied in the **Work domain**, extending the Master PARA model with domain-specific constraints, structures, and alignment mechanisms.

This file ensures:

* Execution remains structured and visible
* Decisions are translated into coordinated action
* Organizational complexity does not degrade execution quality
* Signal flows upward with minimal noise

---

## Scope

Applies only to:

* Work-related Projects
* Work Areas (ongoing responsibilities)
* Work Resources (supporting knowledge)
* Work Archive
* Work-specific coordination and alignment mechanisms

---

## Relationship to Master - PARA

This file inherits all rules from **Master - PARA.md**.

It adds only:

* Work-specific execution constraints
* Coordination mechanisms across teams
* Signal and alignment structures

It must not redefine:

* Core PARA structure (Projects, Areas, Resources, Archive)
* Global execution rules
* Decision logic (owned by Context)

---

## Execution Model (Work)

### Core Principle

Execution must scale beyond the operator.

Work execution is **multi-team, multi-stakeholder, and dependency-heavy**.

Therefore:

* Structure replaces coordination overhead
* Signals replace status reporting
* Systems replace manual follow-up

---

### Execution Objective

Translate decisions into:

* Coordinated execution
* Predictable delivery
* Visible risk

---

## Projects (Work)

### Definition

A Project is a **cross-functional effort with a defined outcome** that requires coordination across teams, systems, or stakeholders.

### Additional Constraints

* Must have a clearly defined outcome and scope
* Must have explicit ownership
* Must expose dependencies early
* Must surface risks continuously

---

### Anti-Patterns

* Projects used as status containers
* Projects without clear ownership
* Hidden dependencies discovered late
* Progress based on activity instead of outcomes

---

### Project Signal Requirements

Each Project must make visible:

* Current state (on-track / at-risk / blocked)
* Key dependencies
* Active risks
* Next critical milestone

No silent failure allowed.

### Minimum Project Schema

Every active Work Project must contain at least:

* Outcome
* Scope boundary
* Owner
* Current state
* Next critical milestone
* Key dependencies
* Active risks
* Last update

Rule:

* If these fields are missing, the Project is under-defined

---

## Areas (Work)

### Definition

Areas represent **ongoing organizational responsibilities** (e.g., platform stability, team health, delivery capability).

### Additional Constraints

* Must have observable health signals
* Must detect degradation early
* Must not rely on perception alone

---

### Area Health Signals (Examples)

* Delivery predictability
* Incident frequency / severity
* Lead time
* Dependency bottlenecks

---

### Minimum Area Schema

Every Work Area must contain at least:

* Responsibility
* Owner
* Current health status
* 1-3 health signals
* Review cadence
* Last review

Rule:

* If an Area cannot expose current health through signals, it is degraded

---

### Anti-Patterns

* Areas without metrics or signals
* Hidden degradation
* Reactive management only

---

## Resources (Work)

### Definition

Reusable knowledge that supports execution.

### Additional Constraints

* Must directly support Projects or Areas
* Must reduce future coordination or decision load
* Must be structured and actionable

---

### AI Agent Runtime Packages

Work-facing AI agent packages are Work Resources only when they are deployable, sanitized, and bounded to operational behavior.

Rule:

* Runtime packages for AB-Gatekeeper, AB-Executive Drafter, and future Work M365/Copilot agents must follow `/systems/decisions/work/2026-05-27 - Work-Facing AI Agent Runtime Packages.md`

---

### Anti-Patterns

* Documentation without usage
* Knowledge not connected to execution
* Redundant or outdated artifacts

---

## Archive (Work)

### Rule

Archive aggressively.

* Completed projects -> archive
* Obsolete resources -> archive or delete
* Irrelevant areas -> archive

No accumulation in active space.

---

## Narrative PARA (Work Only)

### Role

Narrative PARA is a **controlled Work-facing file structure** used for communication, alignment, reporting, and executive-facing artifacts.

It exists to:

* Package decisions and execution signals for Work audiences
* Align direction across teams and stakeholders
* Preserve controlled communication artifacts
* Enable escalation without exposing private reasoning

---

### Boundary

The main thinking process for Work happens in private PARA and Personal OS-controlled context.

Narrative PARA is not the thinking layer. It is the controlled Work-facing packaging layer.

| Layer | Role | Boundary |
|---|---|---|
| Private Work thinking / judgment | Diagnose, decide, sequence, and pressure-test execution | Personal OS and private PARA context |
| Work execution PARA | Track operator-owned projects, areas, resources, and archive | Private Google Drive PARA unless a corporate system is required |
| Work Narrative PARA | Package decisions, signals, updates, and escalation artifacts | Controlled Work file structure |
| Corporate systems | Official communication, records, and collaboration | Corporate tools and retention rules |

Rule:

* Private thinking produces decisions and signals; Narrative PARA packages only what is needed for alignment, action, or controlled communication.

---

### Inputs

* Decisions from private Work judgment
* Signals from Projects, Areas, and execution systems
* Emerging risks
* Cross-team dependencies
* Organizational tensions

---

### Outputs

* Decision communication
* Executive updates
* Alignment artifacts
* Escalation artifacts
* Risk synthesis
* Cross-team alignment summaries

---

### Validity Rules

A Narrative artifact is valid only if:

* It has a concrete audience
* It has a required action, decision, or awareness outcome
* It reduces ambiguity
* It increases alignment
* It exposes what matters without leaking unnecessary private context

If not, it is noise.

---

### Minimum Narrative Schema

Every Narrative artifact must contain at least:

* Audience
* Objective
* Source decision or execution signal
* Current implication
* Required action, decision, or awareness
* Timestamp or update date

Rule:

* If no concrete audience or required outcome exists, do not create the artifact.

---

### Executive Incident Response Pattern

Use a compressed response structure under executive pressure:

1. Problem classification
2. Current status
3. Action in progress
4. Next update

Rules:

* Separate unrelated issues.
* State known, unknown, and under-analysis items clearly.
* Avoid premature technical deep dive.
* Avoid unvalidated root cause.

---

### Failure Modes

* Narrative replaces execution visibility
* Over-communication without signal
* Stakeholder-specific tailoring that distorts reality
* Re-explaining without structural change
* Private thinking leaks into controlled Work artifacts

---

### Promotion Rule

Promote to Personal OS only when:

* A reusable communication pattern emerges
* A structural coordination issue is identified
* A recurring misalignment reveals a principle

Do not promote:

* Conversations
* Status updates
* Temporary escalations
* Work-facing artifacts that are controlled records rather than reusable patterns

---

### Storage and Review Rule

Narrative PARA must live in a clearly bounded layer inside the controlled Work file structure.

Review cadence:

* Weekly: prune obsolete Narrative artifacts
* At Project close: archive or delete Narrative that no longer improves alignment

Rule:

* Narrative that no longer changes decisions, alignment, or escalation should be deleted or archived.

---

## Coordination Rules

### Dependency Visibility

All cross-team dependencies must be:

* Explicit
* Tracked at project level
* Visible early

---

### Escalation Rule

Escalate when:

* Dependency blocks progress
* Risk becomes systemic
* Decision is unclear or missing

Escalation must:

* Be concise
* Be evidence-based
* Focus on decision, not narrative

---

### Alignment Rule

Alignment is achieved when:

* Decisions are understood
* Trade-offs are explicit
* Execution expectations are clear

Not when:

* Everyone agrees
* Communication volume is high

---

## Execution Constraints (Work-Specific)

### Capacity Model

Work capacity must be measured in two different ways:

#### 1. Operator-Owned Active Projects

Projects where Abner is directly accountable for driving outcome, coordination, or escalation.

Limits:

* Target: <= 5 operator-owned active Projects
* Warning: 6-7
* Hard limit: >= 8 requires explicit pause, delegation, or scope reduction

#### 2. Observed Strategic Load

Programs, dependencies, or executive threads that require awareness but are not fully operator-owned Projects.

Rule:

* Observed load must not be counted as operator-owned Project load
* If observed load repeatedly consumes execution time, convert it into an explicit Project, Area signal, or Narrative artifact

#### Granularity Rule

A Work Project should represent a material outcome with cross-functional coordination cost.

Do not count as separate Projects:

* routine follow-ups
* minor workstreams that are only tasks within a larger outcome
* status requests without owned outcome

Count as separate Projects only when:

* ownership differs materially
* dependencies differ materially
* risk and milestone tracking need to differ materially

### Coordination Cost Constraint

If coordination overhead increases:

Structure is insufficient.

Fix:

* Reduce dependencies
* Clarify ownership
* Simplify scope

---

### Visibility Constraint

If execution is unclear:

The signal system is broken.

Fix:

* Improve project signals
* Remove noise
* Standardize reporting

---

### Leadership Bottleneck Constraint

If decisions or progress depend on the operator:

The system is not scaling.

Fix:

* Push ownership down
* Clarify decision rights
* Remove unnecessary involvement

---

## Failure Signals (Work)

Trigger correction when:

* Projects appear active but lack progress
* Dependencies repeatedly block execution
* Risks are discovered late
* Narrative increases but clarity does not
* Operator becomes execution bottleneck

---

## Guiding Principle

> Work execution must scale through structure, not effort.

> If coordination increases, the system is wrong.

> If clarity depends on the operator, the system is fragile.
