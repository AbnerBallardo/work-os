# Work - Context

Version: v1.4

Context owner: Abner Ballardo. This file should be read as context about Abner Ballardo, his decisions, constraints, operating environment, and personal operating system. Any third-party people, organizations, or systems are included only insofar as they shape Abner Ballardo's context.

## Purpose

Define the **stable realities, constraints, and principles** governing execution in the Work domain.

This context ensures:

* High-quality decisions under pressure
* Effective execution in a complex organization
* Alignment between internal truth and external narrative
* Evidence generation for technology-native enterprise leadership

---

## Scope

Covers:

* Role and responsibilities
* Organizational dynamics
* Technology strategy direction
* Execution constraints
* Enterprise-leadership proof generated through Work

---

## Current Role

* Acting VP Technology / CIO, Scotiabank Peru
* Original entry role: Director of Engineering & Architecture

### Core Responsibilities

* Technology strategy and transformation
* Execution system redesign (delivery, QA, DevOps, data)
* Organizational alignment and leadership
* Stakeholder management (local and international)

### Role Timeline

* Joined Scotiabank on November 17, 2025 as Director of Engineering & Architecture.
* Appointed Acting VP Technology / CIO in December 2025, effective January 2026.
* The VP Technology / CIO path was a key driver in the decision to leave the previous role and join Scotiabank.

### Role Reality

* Formal title remains Acting VP Technology / CIO, but everyday operating scope is the actual VP Technology role.
* Luis Alfredo is SVP Technology and Transformation for International Banking, sometimes referred to as CIO IB, and also acts as Mexico CIO.
* Luis Alfredo has stated that he is not looking for another VP Technology; the intended path is for Abner to become the formal Peru CIO after enough visible wins.
* Sebastian Arcuri behaves as if Abner is the real VP Technology, not as if the organization is waiting for another CIO.
* The Acting qualifier is not actively emphasized in normal forums, email, or communication.
* Current mandate requires VP-level Technology ownership plus residual Engineering and Architecture transition accountability.

### Strategic Positioning

* Work is the primary proving ground for the technology-native enterprise leadership thesis.
* The role should generate evidence that technology-native leadership can improve enterprise outcomes through architecture, AI, risk posture, capital allocation, operating-model design, and organizational accountability.
* The objective is not to remain bounded by technology execution, but to demonstrate whole-business judgment from a technology-native base.

### Delegation Logic

* Raul Hugo was hired as Director of Engineering because carrying VP Technology scope plus Engineering and Architecture directly is not sustainable.
* Engineering should move under Raul as accountable execution owner.
* Architecture should be split from the combined Engineering & Architecture scope, with the target model of a dedicated Director of Architecture.

---

## Organizational Context

### Structure

* Reports to International Banking leadership
* Dotted line to local CEO
* Core Technology execution runs through Delivery, Engineering, SRE, Architecture, Data, and Security leadership
* Architecture and Data are regionalized functions with constrained local authority

### Dynamics

* Increasing centralization from International Banking
* Reduced autonomy at local level
* Local leadership effectiveness depends on both capability and political carrying capacity
* Technology organization has accumulated coordination layers that obscure accountability and create relay work instead of execution ownership

---

### Key Stakeholders

#### International Banking Leadership

* Supports technology transformation
* Strong alignment with structural changes

#### Local CEO

* High pressure for visible results
* Focus on optics and speed
* Lower tolerance for technical complexity explanations
* As of June 25, 2026, expected to combine Peru CEO accountability with broader retail accountability across Mexico, the Caribbean, Chile, Peru, Uruguay, and Brazil

**Implication:**

* Local Peru technology transformation may become a reference case for regional retail execution if progress is made visible, business-readable, and tied to reduced complexity.
* Sebastian's expanded remit increases his exposure to technical debt, architectural constraints, and operating-model weaknesses across markets, not only Peru.

---

### Implication

* Must balance:

  * Structural correctness (internal)
  * Narrative clarity (external)

---

## Strategic Direction

### Technology Transformation Program

Multi-phase transformation:

#### Phase 1 — Foundations Reset

* Delivery reset
* QA reset
* DevOps reset
* Data reset
* Infrastructure reset
* API foundations
* Mobile foundation

Goal:

* Establish reliable execution system

---

#### Phase 2 — Simplification and Optimization

* Reduce internal complexity
* Simplify organizational layers and remove relay roles that only pass information between teams
* Replace with SaaS where appropriate
* Improve data strategy coherence

---

#### Phase 3 — AI Acceleration

* Scale AI capabilities
* Leverage improved foundations

---

### Important Principle

* AI initiatives can start now
* Phase 3 enables full acceleration

---

## Execution Constraints

### 1. Legacy Systems

* Heavy reliance on AS400 and batch processes
* High coupling and complexity

---

### 2. Release Model Limitations

* Bundled releases (20–40 features)
* Long cycles (~3 months)
* High coordination overhead

---

### 3. Observability Gaps

* Limited visibility into production issues (especially mobile)

---

### 4. Organizational Friction

* Vendor onboarding complexity
* Cross-team coordination challenges

---

### 5. Regulatory Pressure

* Strict requirements (e.g., latency constraints)
* Limited tolerance for failure

---

### 6. External Ecosystem Constraints (Consortia & Integrations)

* Industry solutions built under **time-to-market pressure** (e.g., interbank consortia) tend to prioritize speed over structural scalability
* These systems introduce **hidden architectural fragility** that is not visible under normal load conditions

#### Implications

* Latent inefficiencies surface only under:

  * High transaction volumes
  * Cross-platform integrations
  * Regulatory stress conditions

* Local architecture inherits and amplifies external inefficiencies when:

  * Integration boundaries are not well-defined
  * Internal systems already carry structural debt

---

### 7. Regulatory Latency Constraints

* Regulatory bodies (e.g., BCR) enforce **performance thresholds based on percentiles (e.g., P75 latency)**
* Compliance requirements can expose **systemic architectural limitations**, not just performance tuning gaps

#### Implications

* Performance issues are often:

  * Structural (architecture, coupling, flows)
  * Not solvable through localized optimizations

* Late awareness of regulatory enforcement leads to:

  * Artificial urgency
  * Misaligned accountability across functions (Product, Compliance, Technology)

---

### 8. Integration Amplification Effect

* Platform integrations (e.g., interoperability between payment systems) **increase load and interaction complexity**
* This acts as a **multiplier of existing architectural weaknesses**

#### Implications

* Systems that appear stable in isolation:

  * Degrade rapidly when integrated
  * Expose hidden coupling and inefficiencies

* Integration must be treated as:

  * A structural stress test
  * Not just a connectivity exercise

---

### 9. Infrastructure Dependency Constraints

* Infrastructure is highly dependent on GTEP, an internal Scotiabank infrastructure company.
* Giovanni Zamalloa is the head of GTEP in Peru and previously served as Director of Infrastructure.
* GTEP service quality is poor and creates complaints across multiple countries.
* GTEP execution issues create delivery drag and can translate into avoidable financial loss.
* Delivery and Engineering currently carry people who mainly manage the GTEP relationship instead of owning infrastructure capability.

#### Implications

* Infrastructure accountability is diluted.
* Poor service quality becomes an execution constraint for Delivery and Engineering.
* The Infrastructure Reset requires a dedicated Infrastructure Director and clearer local ownership.

---

### 10. Organizational Layering and Relay Roles

* Technology has hidden organizational bloat in middle-management and coordination layers.
* Some roles function primarily as information relays rather than accountable execution owners.
* This creates "secretaries of secretaries" behavior: work is passed, summarized, and escalated without enough decision or delivery ownership.
* The problem is not fully visible in the formal organization chart because accountability dilution is embedded in operating routines.

#### Implications

* Organizational simplification must be based on role function, accountability, dependency impact, and continuity risk.
* Reduction targets may be directionally valid, but names and timing must be sequenced through evidence, not produced under artificial urgency.
* The transformation must distinguish between:

  * Low-value relay roles
  * Critical operational continuity roles
  * Leaders with structural ownership
  * Temporary coordination capacity required during reset execution

---

## Operating Model

### Dual-System Model

```text
Internal System (Google Drive)
→ Truth, decisions, execution control

External System (OneDrive)
→ Communication, alignment, reporting
```

---

### Rules

* All decisions originate internally
* External system reflects decisions, not defines them
* No raw thinking in external system
* M365/Copilot agents are external narrative and execution aids; they reflect decisions and package behavior, but do not create decisions or hold raw Personal OS context

---

### Execution Flow

```text
Context → Executive Judgment → Project (PARA) → Area → Narrative
```

---

### Incident Communication

* Incident communication requires one business-facing source of truth.
* Updates must translate technical status into business-readable impact, ownership, detection source, and next action.
* Side-channel questions should be redirected to the official incident channel to preserve transparency and reduce narrative drift.
* Business stakeholders may need simplified process views to understand activation, prioritization, response, and escalation.

---

## Core Principles

### 1. Structure Before Speed

* Fix system constraints before scaling execution
* Do not attempt to meet regulatory performance targets without structural correction

---

### 2. Visibility Drives Alignment

* Provide clear signals to stakeholders
* Avoid ambiguity in status and priorities

---

### 3. Limit Parallel Execution

* Focus on high-impact initiatives
* Avoid overloading organization
* Sequence organizational reduction so the transformation does not remove critical capacity faster than the new operating model can absorb

---

### 4. Separate Truth from Narrative

* Internal: accurate, detailed
* External: simplified, aligned

---

### 5. Build Foundations for Leverage

* APIs, CI/CD, observability, data
* Enable future acceleration

---

## Areas of Responsibility (Examples)

* Platforms (APIs, mobile, core systems)
* Capabilities (QA, DevOps, SRE, data, infrastructure)
* Organizational structure (teams, leadership)
* Risk domains (security, compliance)

Each must be tracked with:

* Status (G/Y/R)
* Metrics
* Owner

Detailed leadership context is maintained in:

* Work - Leadership Map.md

---

## Failure Signals

If observed:

* Increasing number of active Projects
* Low delivery predictability
* Repeated production issues
* Misalignment between stakeholders
* Pressure for speed overriding structure

→ System degradation is occurring

---

## Hidden Structural Constraints

### Legacy Decision Artifacts

* Existing business rules (e.g., input validations) were defined years ago
* Original decision-makers are no longer in the organization
* Lack of traceability creates ambiguity in root cause analysis

**Implication:**

* Current teams must reverse-engineer intent
* Structural constraints can appear as arbitrary limitations

---

### Cross-Channel Rule Propagation

* Certain rules (e.g., character validation) apply across multiple transaction flows:
  * Plin
  * Transfers
  * Payments

**Implication:**

* Issues perceived as channel-specific are often systemic
* Changes require multi-system impact analysis

---

### Legacy System Constraints (Hypothesis-Driven)

* Core systems (e.g., AS400) may impose data limitations
* Not all constraints are explicitly documented

**Implication:**

* Hypothesis validation is required before architectural decisions
* Technical debt manifests as business rule restrictions

---

## Review Cadence

### Weekly

* Project review (continue / close / kill)
* Area status (G/Y/R)
* Decision extraction

---

### Monthly

* Strategic alignment
* Progress on transformation phases

---

## Guiding Principle

> Technology execution is a system problem, not a delivery problem.

> If execution fails, redesign the system — do not increase pressure.
