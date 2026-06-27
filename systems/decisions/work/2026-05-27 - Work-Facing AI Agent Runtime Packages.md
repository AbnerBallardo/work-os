# Work-Facing AI Agent Runtime Packages

Version: v1.0

---

## Title

Work-Facing AI Agent Runtime Packages

---

## Date / Version

2026-05-27 / v1.0

---

## Owner

Abner Ballardo

---

## Domains Affected

* Work
* Personal OS
* Prompting
* Operating Stack

---

## Context

Work-facing AI agents can improve executive communication, routing, drafting, and governance workflows. They also create exposure risk if they are connected directly to Personal OS source files.

Work OS contains the detailed private Work decision and context layer. Personal OS contains only operator-level Work overview and cross-domain constraints. Work-facing agents require only enough context to execute their defined behavior safely.

---

## Decision

Work-facing AI agents must use minimal, sanitized runtime packages.

Work OS remains the private Work decision/context layer.

Work OS artifacts may package:

* Agent behavior
* Test scenarios
* Source boundaries
* Rollout plans

Work OS artifacts must not expose raw private Work context or raw Personal OS context.

Applies to:

* AB-Gatekeeper
* AB-Executive Drafter
* Future Work M365/Copilot agents

Rules:

* Runtime instructions first
* Companion source only when necessary
* Test scenarios required for agent behavior
* OneDrive source package required before deployment
* Private Work OS and Personal OS source files never connected directly unless explicitly listed in a reviewed source package
* Political or leadership insight must be generalized into safe rules

---

## Type

Durable

---

## Reversibility

Irreversible

Rule:

* Agent package structure can be revised, but raw context exposure is treated as partially irreversible once deployed or shared.

---

## Alternatives Considered

* Connect Personal OS Work files directly to Work-facing agents.
* Copy full Work-domain context into OneDrive as agent knowledge.
* Keep agent behavior only in the M365/Copilot instruction field.
* Build each Work-facing agent as a one-off without shared package rules.

---

## Trade-Offs

* Lower exposure risk at the cost of maintaining sanitized companion artifacts.
* Better repeatability at the cost of requiring test scenarios before deployment.
* Less raw context may reduce nuance, but improves safety and team-facing usability.
* Runtime packages create extra setup work, but prevent agent configuration from becoming implicit or platform-specific.

---

## Constraints Applied

* Treat Work OS and Personal OS as highly sensitive by default.
* Apply minimum necessary exposure to all Work-facing AI agents.
* Keep Work OS as the private Work source-of-truth layer.
* Keep Work OS runtime artifacts deployable, reviewable, and safe for operational use.
* Separate private context, generalized behavior rules, test coverage, and rollout material.

---

## Risks Accepted

* Sanitized rules may omit context that would improve a private drafting workflow.
* Companion source packages can become stale if private Work OS context changes.
* Test scenarios may not cover every executive communication edge case.
* M365/Copilot platform behavior may change and require package updates.

---

## Execution Linkage

* PARA reference: Work AI agent deployment and Work OS source packages
* Dependencies: Work-facing agent instructions, sanitized companion sources, test scenarios, OneDrive source package, M365/Copilot deployment constraints

---

## Governance

* Review trigger: Before deploying or materially updating any Work-facing M365/Copilot agent.
* Invalidation condition: A future Work agent platform provides verified private-source isolation, access governance, auditability, and source redaction strong enough to remove the need for sanitized packages.
* Status: Active
