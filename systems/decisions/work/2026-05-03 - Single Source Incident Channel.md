# Single Source Incident Channel

Version: v1.0

---

## Title

Single Source Incident Channel

---

## Date / Version

2026-05-03 / v1.0

---

## Owner

Technology

---

## Domains Affected

* Work

---

## Context

Incident communication was fragmented across engineering, SR, Teams, WhatsApp, and other side channels. This created duplicated effort, inconsistent visibility, and confusion when lower-severity incidents behaved with higher business criticality.

Business stakeholders needed transparent, business-readable incident updates. A single Teams channel improved visibility and created a shared source of truth. A simplified process diagram also helped business roles understand activation, prioritization, response, and escalation without requiring technical process detail.

---

## Decision

Critical incident communication should use one official Teams channel as the business-facing source of truth.

Incident updates should include:

* What happened
* Business impact
* How the incident was detected
* Owner
* Current action
* Next update timing

Side-channel questions may be acknowledged, but answers should redirect to the official channel.

Business stakeholders should receive simplified incident process views when operating-model changes need executive alignment. These artifacts do not need to be the official technical process; they can be distilled communication artifacts designed for clarity.

---

## Type

Durable

---

## Reversibility

Reversible

---

## Alternatives Considered

* Continue using multiple channels depending on incident type and stakeholder preference.
* Use only the official technical incident process documentation.
* Communicate incidents through ad hoc executive updates.

---

## Trade-Offs

* Centralizing communication requires discipline to redirect side-channel questions.
* Business-friendly language may omit technical detail that engineering still needs elsewhere.
* A distilled process diagram can be mistaken for the official technical process unless positioned clearly.

---

## Constraints Applied

* External communication must simplify internal complexity.
* Incident communication must preserve one source of truth.
* Technical process detail should remain internal unless needed for business decisions.

---

## Risks Accepted

* Some stakeholders may continue using informal channels during the transition.
* Teams may need coaching to produce concise business-readable updates.
* The Teams channel may become noisy unless update format and ownership remain disciplined.

---

## Execution Linkage

* PARA reference: Work - PARA.md
* Dependencies: SRE operating model, incident severity taxonomy, Teams channel governance, AI-assisted message drafting

---

## Governance

* Review trigger: 30 days after launch or after the next P1/P2 incident.
* Invalidation condition: The official channel stops being the most trusted source of truth or creates material coordination overhead.
* Status: Active
