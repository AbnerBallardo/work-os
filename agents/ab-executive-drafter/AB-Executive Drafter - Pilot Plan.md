# AB-Executive Drafter - Pilot Plan

Version: v1.0
Owner: VP Technology / Acting CIO
Status: Ready for controlled pilot
Parent Artifact: [AB-Executive Drafter - Copilot Agent Vision.md](AB-Executive%20Drafter%20-%20Copilot%20Agent%20Vision.md)

---

## 1. Pilot Objective

Validate AB-Executive Drafter with a controlled group before broad rollout.

The pilot should prove that the agent:

* Improves senior-stakeholder communication quality
* Selects the right recipient framing
* Classifies communication state correctly
* Recommends a safer channel when email is not appropriate
* Produces useful internal and visible subjects
* Applies executive compression
* Handles Spanish and English correctly
* Flags drafts that need Abner review

---

## 2. Pilot Scope

### Included

* Email preparation to Luis Alfredo
* Email preparation to Sebastian
* Recipient selection and joint-recipient recommendation
* Communication state classification
* Channel decision before drafting
* Internal and visible subject generation
* Executive compression
* Email review and rewrite
* Sensitive-context generalization
* Abner-review recommendation

### Deferred

* New senior stakeholders
* Formal approval special-case registry
* Automated sending
* Broad stakeholder relationship modeling
* Any use beyond the curated source package

---

## 3. Pilot Group

Recommended pilot size:

```text
4 to 6 leaders / frequent senders
```

Include:

* Delivery or transformation sender
* Engineering or platform sender
* Infrastructure or operations sender
* Business-facing technology sender
* One frequent Abner-review workflow user

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
| Day 10 | Final review and rollout decision |

---

## 5. Usage Rules

Pilot users should use AB-Executive Drafter for:

* Drafting emails to Luis Alfredo
* Drafting emails to Sebastian
* Deciding whether one joint message is appropriate
* Converting technical notes into executive communication
* Reviewing sensitive or high-exposure drafts before sending
* Deciding whether email, Teams / chat, call, meeting, or no communication is appropriate

Pilot users should not use AB-Executive Drafter for:

* HR-sensitive messages
* Private personnel assessments
* Raw political context
* Confidential strategy not included in the curated source package
* Messages to recipients outside the approved recipient scope
* Messages that should first be aligned with Abner

---

## 6. Metrics

Track these pilot metrics manually.

| Metric | Target Direction |
|---|---|
| % drafts with correct recipient framing | Increase |
| % communication states accepted by sender | Increase |
| % channel recommendations accepted by sender | Increase |
| % visible subjects used without rewrite | Increase |
| % drafts requiring Abner rewrite | Decrease |
| % drafts requiring recipient clarification | Decrease |
| Average draft length | Decrease without losing decision value |
| % outputs delivered in requested language | Increase |
| % high-exposure drafts flagged for Abner review | Accurate, not minimized |

---

## 7. Pilot Feedback Form

For each real use, capture:

```text
Sender:
Date:
Recipient:
Use case:
Language:
Communication state:
Recommended channel:
Was the channel recommendation right? Yes / No
Was the visible subject useful? Yes / No
Was the body useful? Yes / No
Was the draft compressed enough? Yes / No
Was Abner review recommended correctly? Yes / No / Not applicable
Did the stakeholder ask for clarification? Yes / No
What should improve?
```

Do not capture private stakeholder interpretation in the feedback form.

---

## 8. Go / No-Go Criteria

### Go

Proceed to broader use if:

* Recipient framing is consistently correct
* Communication state classification is mostly accepted
* Channel decision prevents unsafe or low-value email use
* Visible subjects are usable without major rewrite
* Drafts are shorter without losing decision value
* Spanish / English handling works
* Abner receives fewer drafts needing structural rewrite

### No-Go / Extend Pilot

Extend pilot if:

* Agent over-produces long emails
* Channel recommendations are ignored or wrong
* Communication states are confusing
* Internal `EXEC` subjects leak into final visible emails when not wanted
* Sensitive-context generalization fails
* Users paste notes and let the agent replace their thinking

---

## 9. Rollout Decision

At the end of the pilot, decide:

| Decision | Meaning |
|---|---|
| Expand current use | Broader team can use for Luis Alfredo and Sebastian drafting |
| Add recipient | Add a new recipient rule card after pattern review |
| Add special cases | Add recurring formal approval / exception rules only if needed |
| Keep pilot limited | More tuning required |
| Pause | Agent is creating more friction or exposure than value |

Default recommendation:

```text
Expand only after channel decision and compression behavior are stable.
```
