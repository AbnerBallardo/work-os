# AB-Gatekeeper - Special Case Rules

Version: v1.1  
Owner: VP Technology / Acting CIO  
Status: Active rule registry  
Applies To: AB-Gatekeeper email preparation and review  
Runtime Authority: [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md)  
Design Reference: [AB-Gatekeeper - Copilot Agent Vision.md](AB-Gatekeeper%20-%20Copilot%20Agent%20Vision.md)

---

## 1. Purpose

Define special-case validation rules for recurring email types that require additional controls beyond the standard AB-Gatekeeper email model.

This file is designed to grow over time.

Add new special cases here as a private/reference registry.

Active special cases must be embedded in [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md) before deployment.

---

## 2. Operating Principle

Special-case rules are validation overlays.

The agent must apply them after:

```text
Intent classification -> C-level classification -> Subject taxonomy
```

And before:

```text
Final email draft
```

If a special case applies, the agent must validate the mandatory fields before producing the final email.

---

## 3. Global Rules

| Rule | Requirement |
|---|---|
| Special-case detection | If the topic matches a registered special case, apply the rule automatically |
| Mandatory fields | If a mandatory field is missing, the agent must ask for it before finalizing |
| Maximum friction | Ask only for missing mandatory fields, up to three clarification questions |
| Email ownership | The business / technology requester remains accountable for the request |
| Security inclusion | When the rule requires Security review, include the Security reviewer in the email |
| Subject keywords | `ABG`, intent, C-level, TC, and domain tags remain in English |
| Bilingual support | Body can be Spanish or English according to the language policy |
| Do-not-send gate | If mandatory controls are missing, recommend not sending until corrected |

---

## 4. Special Case Rule Template

Use this structure to add future cases.

```text
## SC-XXX - [Special Case Name]

### Trigger

[Terms, patterns, or request type that activate this rule]

### Default Classification

Intent:
C-level:
Domain / forum tags:
TC routing:

### Mandatory Inputs

* [Required input]
* [Required input]
* [Required input]

### Required Recipients / Reviewers

* [Required role or person type]

### Email Must Include

* [Required content]
* [Required content]
* [Required content]

### Blocking Conditions

The agent must not finalize the email if:

* [Blocking condition]
* [Blocking condition]

### Subject Example

ABG | [INTENT] | [C-Level] | [Domain/Forum] | [Case] - [Specific ask]
```

---

## 5. SC-001 - TRA Approval Request

### Trigger

Apply this rule when the email requests approval for a TRA or references a TRA document.

Common trigger terms:

* `TRA`
* `TRA-NNN`
* `Thread Risk Assessment`
* `Threat Risk Assessment`
* Risk assessment approval
* Security assessment approval

### Default Classification

| Field | Default |
|---|---|
| Intent | `DECISION` |
| C-level | `C2` by default; use `C3` if the project, risk, or business context is new to Abner |
| Domain / forum tags | `SEC` plus impacted domain if known |
| TC routing | `TC1` by default; escalate to `TC2` / `TC3` if cross-domain, regulatory, CEO, International Banking, or material risk acceptance is involved |

### Mandatory Inputs

* TRA document URL
* TRA identifier in `TRA-NNN` format, where `NNN` is a number
* Name of the Security reviewer
* Security review status or confirmation
* System, project, product, or initiative affected
* Approval requested from Abner
* Deadline or required approval date

### Required Recipients / Reviewers

* The Security reviewer who reviewed the request must be included in the email.
* If possible, include the Security reviewer in `CC`.
* If the email format does not use explicit recipients, the body must state: `Security reviewer: [Name]`.
* If the agent produces a recipient recommendation, it must include `CC: [Security reviewer]`.

### Email Must Include

Use the Approval Email Body Structure from [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md).

* TRA document URL
* TRA ID
* Security reviewer name
* What Abner is being asked to approve
* Why approval is needed now
* Risk / control implication in executive language
* Deadline / next step
* Owner accountable for execution after approval

### Blocking Conditions

The agent must not finalize the email if:

* TRA document URL is missing
* TRA ID is missing or does not follow `TRA-NNN`
* Security reviewer is missing
* Approval requested from Abner is not explicit
* Deadline or next step is missing

### Subject Examples

```text
ABG | DECISION | C2 | SEC | TRA-123 - Approve risk assessment for [Project]
```

```text
ABG | DECISION | C3 | SEC/TC | TRA-456 - Approve risk acceptance for [Platform]
```

---

## 6. SC-002 - Vulnerability Deadline Extension Approval

### Trigger

Apply this rule when the email requests approval to extend the remediation deadline for one or more vulnerabilities.

Common trigger terms:

* Vulnerability
* Vulnerabilities
* CVE
* Remediation deadline
* Deadline extension
* Exception
* Risk acceptance
* Vulnerability extension

### Default Classification

| Field | Default |
|---|---|
| Intent | `DECISION` |
| C-level | `C2` by default; use `C3` if the exposure, affected platform, or risk context is new to Abner |
| Domain / forum tags | `SEC` plus `PROD`, `ENG`, `INFRA`, or impacted domain if known |
| TC routing | `TC1` by default; escalate to `TC2` / `TC3` if material risk, regulatory exposure, production criticality, cross-domain conflict, or repeated extension exists |

### Mandatory Inputs

* Vulnerability identifier(s), CVE(s), or scanner finding ID(s)
* Severity / risk rating
* Affected system, application, platform, or asset group
* Current remediation deadline
* Requested new remediation deadline
* Reason for extension
* Compensating controls or interim mitigation
* Remediation owner
* Name of the Security reviewer
* Security review status or confirmation

### Required Recipients / Reviewers

* The Security reviewer who reviewed the request must be included in the email.
* If possible, include the Security reviewer in `CC`.
* If the email format does not use explicit recipients, the body must state: `Security reviewer: [Name]`.
* If the agent produces a recipient recommendation, it must include `CC: [Security reviewer]`.

### Email Must Include

Use the Approval Email Body Structure from [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md).

* Vulnerability ID(s) / CVE(s) / finding ID(s)
* Severity / risk rating
* Affected system or scope
* Current deadline and requested new deadline
* Reason for extension
* Risk implication of approving the extension
* Compensating controls / interim mitigation
* Security reviewer name
* Remediation owner
* Next checkpoint or review date

### Blocking Conditions

The agent must not finalize the email if:

* Vulnerability identifier(s) are missing
* Severity / risk rating is missing
* Current and requested new deadlines are missing
* Security reviewer is missing
* Compensating controls or interim mitigation are missing
* Remediation owner is missing
* Approval requested from Abner is not explicit

### Subject Examples

```text
ABG | DECISION | C2 | SEC | Vulnerabilities - Approve remediation deadline extension for [System]
```

```text
ABG | DECISION | C3 | SEC/PROD | Critical Vulnerability - Approve extension with compensating controls
```

---

## 7. Maintenance Rule

When a new recurring approval or exception pattern appears, add a new `SC-XXX` section using the rule template.

Do not change the core AB-Gatekeeper model unless the new case changes the general operating rules.

For active deployment, update [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md) in the same pass.

Use the next sequential ID:

```text
SC-003, SC-004, SC-005...
```
