# AB-Gatekeeper - Pilot Plan

Version: v1.1  
Owner: VP Technology / Acting CIO  
Status: Ready for controlled pilot  
Parent Artifact: [AB-Gatekeeper - Copilot Agent Vision.md](AB-Gatekeeper%20-%20Copilot%20Agent%20Vision.md)

---

## 1. Pilot Objective

Validate AB-Gatekeeper with a controlled group before broad rollout.

The pilot should prove that the agent:

* Reduces email rework
* Improves subject-line triage
* Applies `C1 / C2 / C3` correctly
* Detects Technology Committee routing when relevant
* Produces concise Word-ready committee briefs only after triage acceptance
* Handles Spanish and English correctly
* Blocks incomplete special-case approval emails

---

## 2. Pilot Scope

### Included

* Email preparation to Abner
* Subject line classification
* Email review and rewrite
* C-level classification
* Special-case approval validation for TRA and vulnerability deadline extensions
* Word Paste Mode validation for accepted committee briefs

### Deferred

* Broad Technology Committee automation
* Full committee brief generation at scale
* Automated decision-log updates
* Any use beyond the curated source package

---

## 3. Pilot Group

Recommended pilot size:

```text
5 to 8 leaders / frequent senders
```

Include:

* Delivery representative
* Engineering representative
* SRE / incident representative
* Security representative
* Architecture or Data representative
* One frequent executive-communication sender

---

## 4. Pilot Duration

Recommended duration:

```text
2 weeks
```

Cadence:

| Timing | Activity |
|---|---|
| Day 0 | Configure agent and source package |
| Day 1 | Run test scenarios |
| Days 2-10 | Controlled pilot use |
| Day 5 | Mid-pilot review |
| Day 10 | Final review and decision |

---

## 5. Usage Rules

Pilot users should use AB-Gatekeeper for:

* Emails requesting Abner decision / action / review
* Risk or blocker emails
* Security approval emails
* TRA approval emails
* Vulnerability deadline extension emails
* Possible Technology Committee topics
* Accepted `TC2` / `TC3` committee brief formatting checks

Pilot users should not use AB-Gatekeeper for:

* HR-sensitive messages
* Private personnel assessments
* Raw political context
* Confidential strategy not included in the curated source package
* Messages that do not require executive awareness or action

---

## 6. Metrics

Track these pilot metrics manually.

| Metric | Target Direction |
|---|---|
| % emails using ABG subject format | Increase |
| % emails requiring Abner clarification | Decrease |
| Average rework per email | Decrease |
| % C-level classifications accepted by sender | Increase |
| % special-case emails blocked for missing controls | Accurate, not minimized |
| % outputs delivered in requested language | Increase |
| % committee candidates redirected correctly | Increase |
| % accepted committee briefs passing Word Paste Mode validation | Increase |
| Sender satisfaction | Increase |

---

## 7. Pilot Feedback Form

For each real use, capture:

```text
Sender:
Date:
Use case:
Language:
Intent:
C-level:
TC routing:
Special-case rule applied:
Was the subject useful? Yes / No
Was the body useful? Yes / No
Did Abner ask for clarification? Yes / No
What should improve?
```

---

## 8. Go / No-Go Criteria

### Go

Proceed to broader use if:

* Subject format is consistently correct
* C-level classification is mostly accepted
* Spanish / English handling works
* TRA and vulnerability cases block missing mandatory inputs
* Users report lower friction
* Abner receives fewer incomplete messages

### No-Go / Extend Pilot

Extend pilot if:

* Agent over-produces long emails
* C-level classification is frequently wrong
* Special-case mandatory fields are missed
* Users bypass the structure
* Subject keywords are translated or inconsistent
* Committee routing creates confusion
* Accepted committee briefs remain too verbose or paste poorly into Word

---

## 9. Rollout Decision

At the end of the pilot, decide:

| Decision | Meaning |
|---|---|
| Expand email use | Broader team can use for email drafting |
| Add committee routing | Enable more formal Technology Committee use |
| Keep pilot limited | More tuning required |
| Pause | Agent is creating more friction than value |

Default recommendation:

```text
Expand only after email behavior is stable.
```
