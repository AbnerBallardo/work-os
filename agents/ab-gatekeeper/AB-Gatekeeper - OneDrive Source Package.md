# AB-Gatekeeper - OneDrive Source Package

Version: v1.3
Owner: VP Technology / Acting CIO  
Status: Updated for minimal work-stack sharing and Word-safe committee brief generation  
Applies To: Files shared with the M365 Copilot Agent  

---

## 1. Purpose

Define the curated OneDrive source package for AB-Gatekeeper.

Only the required runtime files below should be connected to the agent.

Do not share raw Personal OS, political notes, leadership assessments, personnel context, or unreviewed working notes.

---

## 2. Recommended Work-Stack Folder

Create or use a controlled OneDrive folder:

```text
AB-Gatekeeper - Agent Sources
```

Only files in this package should be shared with the agent.

---

## 3. Required Work-Stack Source Files

| File | Purpose |
|---|---|
| [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md) | Self-contained agent behavior, templates, routing rules, Word-safe committee brief controls, and special-case validation |
| [AB-Gatekeeper - Project Context Register.md](AB-Gatekeeper%20-%20Project%20Context%20Register.md) | Self-contained default C-level calibration |

---

## 4. Committee Brief Scope

Committee brief generation is in scope only after a topic passes triage and is accepted for `TC2` / `TC3` review.

The runtime source package remains limited to the two required work-stack files.

Reason:

```text
The Word Paste Mode brief contract is embedded in AB-Gatekeeper - Agent Instructions.md.
```

Do not add committee templates to the agent source folder unless pilot testing shows that embedded instructions are not enough.

Use [Technology Committee - Topic Brief Template.md](../../committees/technology/Technology%20Committee%20-%20Topic%20Brief%20Template.md) as a validation reference for Word-ready full briefs.

---

## 5. Validation and Private Reference Files

Keep these files outside the M365 agent source folder unless there is a specific reason to expose a sanitized extract.

| File | Use When |
|---|---|
| [AB-Gatekeeper - Copilot Agent Vision.md](AB-Gatekeeper%20-%20Copilot%20Agent%20Vision.md) | Strategy / roadmap reference only |
| [AB-Gatekeeper - Special Case Rules.md](AB-Gatekeeper%20-%20Special%20Case%20Rules.md) | Private/reference registry; active rules must be embedded in Agent Instructions before deployment |
| [AB-Gatekeeper - Test Scenarios.md](AB-Gatekeeper%20-%20Test%20Scenarios.md) | Testing / validation only |
| [AB-Gatekeeper - Pilot Plan.md](AB-Gatekeeper%20-%20Pilot%20Plan.md) | Rollout planning only |
| [Technology Committee.md](../../committees/technology/Technology%20Committee.md) | Governance reference; not required because routing rules are embedded |
| [Technology Committee - Operating Runbook.md](../../committees/technology/Technology%20Committee%20-%20Operating%20Runbook.md) | Governance reference; not required because routing rules are embedded |
| [Technology Committee - Triage Submission Template.md](../../committees/technology/Technology%20Committee%20-%20Triage%20Submission%20Template.md) | Governance reference; not required because triage structure is embedded |
| [Technology Committee - Topic Brief Template.md](../../committees/technology/Technology%20Committee%20-%20Topic%20Brief%20Template.md) | Governance and validation reference; Word Paste Mode is embedded in agent instructions |
| [Technology Committee - Agenda Template.md](../../committees/technology/Technology%20Committee%20-%20Agenda%20Template.md) | Governance reference |
| [Technology Committee - Decision Log Template.md](../../committees/technology/Technology%20Committee%20-%20Decision%20Log%20Template.md) | Governance reference |
| Personal OS operator or capacity context | Private cross-domain context; use only through a reviewed, sanitized extract |
| Work OS `context/Context.md` | Private source for stable Work-domain realities and truth-vs-narrative boundary |
| Work OS `context/PARA.md` | Private source for execution and narrative-layer rules |
| Work OS `context/Political.md` | Private stakeholder dynamics; use only to derive safe communication rules |
| Work OS `context/Leadership Map.md` | Private leadership and delegation context; do not expose to the agent |

---

## 6. Do Not Share

Do not share these source types with the agent:

* Raw Work OS memory, broad context, or case files
* Political, leadership, stakeholder, personnel, or raw strategic interpretation
* Private Personal OS files or operator/capacity context
* Draft emails, meeting notes, incident details, active execution material, or informal notes
* Full decision-record libraries
* Test, pilot, or vision files unless explicitly approved
* Documents with unresolved contradictory instructions

---

## 7. Source Package Maintenance

Review the source package when:

* New special cases are added
* Project context changes
* Committee rules change
* A pilot issue exposes a missing instruction
* The agent starts producing incorrect classifications
* Full committee brief output becomes too verbose or does not paste cleanly into Word

Rule:

```text
Update source files first, then update the agent.
```

---

## 8. Launch Checklist

| Step | Status |
|---|---|
| Source folder created |  |
| Two required work-stack files added |  |
| Private/reference files excluded |  |
| Agent instructions copied into M365 agent setup |  |
| Source files connected to agent |  |
| Test scenarios executed |  |
| Word Paste Mode committee brief scenario executed |  |
| Pilot group selected |  |
| Feedback log started |  |
