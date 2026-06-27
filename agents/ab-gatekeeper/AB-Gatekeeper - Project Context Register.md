# AB-Gatekeeper - Project Context Register

Version: v1.2
Owner: VP Technology / Acting CIO
Status: Active register
Applies To: AB-Gatekeeper C-level classification
Work-Stack Package: Self-contained C-level calibration source
Companion Source: [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md)

---

## 1. Purpose

Provide default C-level guidance for AB-Gatekeeper.

This register helps the agent decide how much context Abner needs in an email.

It is not a project tracker.

It does not replace judgment.

This file is safe to share with the work-stack agent together
with [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md).

Do not add private leadership assessments, political notes, personnel context, or raw Personal OS material.

---

## 2. C-Level Definitions

| Level | Meaning                          | Email Rule                         |
|-------|----------------------------------|------------------------------------|
| `C1`  | Abner already has strong context | Send delta only                    |
| `C2`  | Abner has partial context        | Send delta plus concise background |
| `C3`  | Abner has low or no context      | Send full structured context       |

Rule:

```text
Default C-level is a starting point, not a final classification.
```

---

## 3. Override Triggers

Increase context depth when any trigger applies:

| Trigger                                 | Effect                                                         |
|-----------------------------------------|----------------------------------------------------------------|
| Regulatory exposure                     | Increase to `C3` unless Abner already has current context      |
| Production instability                  | Increase by one level                                          |
| Security risk / approval                | Use at least `C2`                                              |
| Architecture exception                  | Use at least `C2`; increase to `C3` if strategic impact exists |
| Material budget / capacity impact       | Use at least `C2`                                              |
| CEO / International Banking exposure    | Use `C3` unless context is already active                      |
| Cross-domain dependency conflict        | Use at least `C2`                                              |
| Repeated extension / repeated exception | Use at least `C2`; consider `TC2` / `TC3`                      |
| New topic / first-time request          | Use `C3`                                                       |

---

## 4. TC Routing Reference

The register is focused on C-level context, but some override triggers may also affect Technology Committee routing.

| Tier  | Meaning                                           | Handling                                |
|-------|---------------------------------------------------|-----------------------------------------|
| `TC0` | Information only                                  | Convert to async update                 |
| `TC1` | Domain-level decision                             | Redirect to functional leadership       |
| `TC2` | Cross-domain trade-off                            | Accept if unresolved locally            |
| `TC3` | CEO / International Banking / regulatory exposure | Accept with external narrative protocol |

Rule:

```text
C-level = communication depth
TC-level = governance routing
```

---

## 5. Active Register

### Critical / Delta-Only Projects

The following projects are `C1` by default because Abner already has strong active context.

For normal updates, send delta only:

* What changed
* Why it matters
* Decision / action required, if any
* Owner
* Deadline / next step

Do not repeat background context unless an override trigger applies.

| Project | Default C-Level | Normal Email Behavior |
|---------|-----------------|-----------------------|
| Valinor | `C1` | Delta only |
| PLIN SLA | `C1` | Delta only |
| WIFI Improvements in Buildings | `C1` | Delta only |

Use `C2` or `C3` when there is a new decision, material risk, SLA/regulatory exposure, executive escalation, scope change, budget impact, ownership change, or cross-domain conflict.

---

| Project / Domain                           | Default C-Level | Owner                                 | Known Context Already Held by Abner                                                    | Exception Triggers                                                                             | Last Reviewed |
|--------------------------------------------|-----------------|---------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|---------------|
| Valinor                                    | `C1`            | Program / Delivery Owner              | Abner has active context on the program; normal updates should be delta-only           | New decision required, material risk, scope / budget / owner change, cross-domain conflict, executive escalation | 2026-05-25    |
| PLIN SLA                                   | `C1`            | Service / Platform Owner              | Abner has active context on PLIN SLA; normal updates should focus on SLA delta         | SLA breach risk, regulatory exposure, production impact, recurring degradation, executive escalation | 2026-05-25    |
| WIFI Improvements in Buildings             | `C1`            | Infrastructure / Workplace Owner      | Abner has active context on building WIFI improvements; normal updates should be delta-only | Rollout delay, user impact, vendor / infrastructure blocker, budget impact, executive escalation | 2026-05-25    |
| Technology Committee governance            | `C1`            | Technology Leadership                 | Committee purpose, triage-first model, TC routing, decision-readiness standard         | Change to committee authority, intake channel, decision rights, executive escalation           | 2026-05-25    |
| TRA approval requests                      | `C2`            | Requesting owner + Security reviewer  | Security approval requests require explicit review evidence and approval ask           | Missing TRA URL, missing `TRA-NNN`, regulatory / material risk, cross-domain exposure          | 2026-05-25    |
| Vulnerability deadline extensions          | `C2`            | Remediation owner + Security reviewer | Deadline extensions require risk rationale, mitigation, owner, and Security reviewer   | Critical severity, production exposure, repeated extension, regulatory exposure                | 2026-05-25    |
| Production incidents / service degradation | `C2`            | SRE / Incident Owner                  | Abner needs concise status, impact, action, and next update                            | Customer impact, regulatory impact, executive escalation, unresolved root cause                | 2026-05-25    |
| Mobile Banking                             | `C1`            | Platform / Product Owner              | Abner has active context on mobile execution and production sensitivity                | Production instability, customer impact, release risk, regulatory / executive exposure         | 2026-05-25    |
| Delivery execution / milestones            | `C1`            | Delivery Owner                        | Abner has active context on delivery reset and execution visibility                    | Missed milestone, cross-domain blocker, business escalation, priority conflict                 | 2026-05-25    |
| Architecture exceptions                    | `C2`            | Architecture Owner                    | Abner expects architecture issues to be framed as trade-offs and platform implications | Strategic platform impact, regulatory exposure, irreversible decision, cross-domain dependency | 2026-05-25    |
| Data capability / data availability        | `C2`            | Data Owner                            | Abner has context that data is a structural capability gap                             | Real-time capability gap, regulatory reporting, executive dashboard, cross-domain dependency   | 2026-05-25    |
| Infrastructure / GTEP dependency           | `C2`            | Infrastructure / Service Owner        | Abner has context that GTEP service quality can create execution drag                  | Capacity blocker, production impact, cross-country escalation, dependency unresolved locally   | 2026-05-25    |
| Security approvals and exceptions          | `C2`            | Security Reviewer + Request Owner     | Security exceptions require reviewer evidence and explicit risk / control framing      | Material risk acceptance, regulatory exposure, missing mitigation, repeated exception          | 2026-05-25    |
| Vendor constraints                         | `C2`            | Vendor / Service Owner                | Abner needs impact, dependency, and decision/action required                           | Contractual exposure, capacity blocker, financial impact, executive escalation                 | 2026-05-25    |
| New initiatives not previously discussed   | `C3`            | Requesting Owner                      | No assumed context                                                                     | Any first-time request should include full structured context                                  | 2026-05-25    |

---

## 6. Register Maintenance

Update this file when:

* A project becomes familiar enough to move from `C3` to `C2` or `C1`
* A project becomes sensitive enough to require more context
* A recurring email pattern becomes a special case
* Ownership changes
* Abner explicitly asks for more or less context on a topic

Do not use this register to store sensitive leadership assessments or private political context.

---

## 7. Add New Entry Template

```text
| [Project / Domain] | [C1 / C2 / C3] | [Owner] | [Known context already held by Abner] | [Exception triggers] | [YYYY-MM-DD] |
```
