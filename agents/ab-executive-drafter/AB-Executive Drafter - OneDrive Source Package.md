# AB-Executive Drafter - OneDrive Source Package

Version: v1.3
Owner: VP Technology / Acting CIO
Status: Ready for minimal work-stack sharing
Applies To: Files shared with the M365 Copilot Agent

---

## 1. Purpose

Define the curated OneDrive source package for AB-Executive Drafter.

The agent should use only approved source files.

Only connect approved runtime files.

Do not share raw Personal OS, political notes, leadership assessments, private personnel context, or unresolved working
notes.

---

## 2. Recommended Work-Stack Folder

Create or use a controlled OneDrive folder:

```text
AB-Executive Drafter - Agent Sources
```

Only files in this package should be shared with the agent.

---

## 3. Required Work-Stack Source Files

| File | Purpose |
|---|---|
| [AB-Executive Drafter - Agent Instructions.md](AB-Executive%20Drafter%20-%20Agent%20Instructions.md) | Self-contained agent behavior, language policy, communication state, channel decision, subject rules, compression rules, and output structures |
| [AB-Executive Drafter - Recipient Playbook.md](AB-Executive%20Drafter%20-%20Recipient%20Playbook.md) | Self-contained recipient-specific drafting and compression rules for Luis Alfredo and Sebastian |

---

## 4. Validation and Private Reference Files

Keep these files outside the M365 agent source folder unless there is a specific reason to expose a sanitized extract.

| File / Source Type | Use When |
|---|---|
| [AB-Executive Drafter - Copilot Agent Vision.md](AB-Executive%20Drafter%20-%20Copilot%20Agent%20Vision.md) | Strategy / roadmap reference only |
| [AB-Executive Drafter - Test Scenarios.md](AB-Executive%20Drafter%20-%20Test%20Scenarios.md) | Testing / validation only |
| [AB-Executive Drafter - Pilot Plan.md](AB-Executive%20Drafter%20-%20Pilot%20Plan.md) | Rollout planning only |
| Personal OS master files | Private operator, decision, prompting, and execution-system context |
| Personal OS `Work - Context.md` | Private source for stable Work-domain realities and truth-vs-narrative boundary |
| Personal OS `Work - PARA.md` | Private source for execution, narrative-layer, and pruning rules |
| Personal OS `Work - Political.md` | Private stakeholder dynamics; use only to derive safe communication rules |
| Personal OS `Work - Leadership Map.md` | Private leadership and delegation context; use only to derive sanitized guidance |
| Personal OS `Personal - Context.md` | Private capacity context; use only to avoid adding unnecessary cognitive load |
| Raw stakeholder notes | Private working context |
| CV or personal profile | Personal reference only |

---

## 5. Do Not Share

Do not share these source types with the agent:

* Raw Work OS memory
* Political context
* Leadership assessments
* Case files
* Draft emails
* Meeting notes
* Incident details
* Active execution material
* Full decision-record libraries
* Test, pilot, or vision files unless explicitly approved
* Private leadership assessments
* Political interpretation notes
* Sensitive personnel context
* Raw strategic thinking
* Personal OS files not intended for team consumption
* Informal notes not reviewed for team use
* Documents with unresolved contradictory instructions

---

## 6. Source Package Maintenance

Review the source package when:

* Recipient rules change
* A new senior stakeholder is added
* A test case exposes a weak subject or unsafe draft
* A channel decision pattern produces the wrong recommendation
* Compression rules produce too much detail or remove decision-useful information
* The team starts using the agent for a new communication pattern
* Abner changes the preferred drafting pattern for Luis Alfredo or Sebastian

Rule:

```text
Update source files first, then update the agent.
```

---

## 7. Launch Checklist

| Step | Status |
|---|---|
| Source folder created |  |
| Two required work-stack files added |  |
| Private Personal OS files excluded |  |
| Agent instructions copied into M365 agent setup |  |
| Source files connected to agent |  |
| Test scenarios executed |  |
| Pilot plan reviewed |  |
| Pilot group selected |  |
| Feedback log started |  |
