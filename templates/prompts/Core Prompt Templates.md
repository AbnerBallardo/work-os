# Core Prompt Templates

Version: v1.0

Purpose: Reusable prompt bodies for common Work OS interaction patterns.

Scope: Work OS prompt patterns for private Work reasoning, repository
maintenance, governance review, executive communication, and controlled
Work-facing artifact preparation. Keep temporary execution prompts,
meeting-specific prompts, and high-churn tool examples out of this file.

---

## Tool Routing

| Tool | Use For | Boundary |
|---|---|---|
| Codex | Repository implementation, maintenance, verification, and file changes | Read source-of-truth files before editing; report changed files and verification |
| ChatGPT / Work OS Project | Private reasoning, synthesis, decision support, writing, governance, and source-boundary review | Use uploaded Work OS runtime package plus prompt-specific attachments; do not treat outputs as source of truth |
| Microsoft Copilot | Corporate-boundary drafting, summarization, and meeting or document support | Use reviewed corporate material only; do not paste raw private Work OS, Personal OS, political, leadership, or memory context |
| Perplexity | External research, current information, comparison, and evidence gathering | Use sanitized briefs; do not upload broad Work OS context |

Decision rule:

```text
Route by source boundary first, then by task.
```

---

## Selection Guide

| Need | Template | Use In |
|---|---|---|
| Understand a situation | Analysis | ChatGPT Project / Generic |
| Make a decision | Decision | ChatGPT Project / Generic |
| Turn a decision into action | Execution | ChatGPT Project / Generic |
| Produce a deliverable | Artifact | ChatGPT Project / Generic |
| Improve an existing artifact | Review | ChatGPT Project / Codex / Generic |
| Implement a repository change | Codex Repository Change | Codex |
| Decide whether information belongs in Work OS | Work OS Evolution | ChatGPT Project / Codex |
| Compress notes into reusable Work knowledge | Knowledge Compression | ChatGPT Project |
| Evaluate structure, coupling, and governance | Architecture Review | ChatGPT Project / Codex |
| Design a durable workflow or governance system | System Design | ChatGPT Project |
| Challenge an idea before acting | Strategic Critique | ChatGPT Project |
| Reduce workflow friction without losing control | Workflow Optimization | ChatGPT Project / Codex |
| Test ownership, accountability, and controls | Governance Review | ChatGPT Project |
| Translate technical detail for executives | Executive Communication | ChatGPT Project / Codex |
| Check consistency across Work OS boundaries | Work OS Consistency Check | ChatGPT Project / Codex |
| Review exposure before using Work material elsewhere | Source-Boundary Review | ChatGPT Project / Codex |
| Synthesize meeting material | Meeting Synthesis | ChatGPT Project / Copilot |
| Review selected executive project narratives | Narrative / Project Review | ChatGPT Project / Codex |
| Improve Microsoft 365 usage | Microsoft 365 Workflow Review | ChatGPT Project / Codex |
| Prepare a stakeholder-safe update | Stakeholder-Safe Update | ChatGPT Project / Codex |
| Prepare a Work decision record | Decision Record Preparation | ChatGPT Project / Codex |
| Research current or external evidence | Perplexity Sanitized Research Brief | Perplexity |
| Synthesize sourced research | ChatGPT Synthesis From Research | ChatGPT Project |

Rule:

```text
Use the smallest template that preserves decision quality and source boundaries.
```

---

## Analysis

Use in: ChatGPT Project / Generic

```markdown
## Context
[Situation]
## Objective
Understand the situation.
## Constraints
- Preserve Work OS information-handling boundaries.
- Separate stable signal from temporary noise.
## Ask
Provide:
- Structured breakdown
- Key insights
- Hidden risks or tensions
- What should remain contextual only
```

---

## Decision

Use in: ChatGPT Project / Generic

```markdown
## Context
[Situation]
## Objective
Define the decision to be made.
## Constraints
[List constraints]
## Decision Type
[Durable / reversible / operational / exploratory]
## Ask
Provide:
1. Structured analysis
2. Trade-offs
3. Clear recommendation
4. Next actions
5. What should not be promoted into durable Work OS knowledge yet
```

---

## Execution

Use in: ChatGPT Project / Generic

```markdown
## Context
[Situation]
## Decision Already Made
[Decision]
## Objective
Translate into execution.
## Constraints
- Preserve system-of-record boundaries.
- Route official work to the correct corporate system.
- Keep Work OS as the private reasoning layer.
## Ask
Provide:
- Step-by-step plan
- Dependencies
- Risks
- System-of-record routing
- First 3 actions
```

---

## Artifact

Use in: ChatGPT Project / Generic

```markdown
## Context
[Situation]
## Objective
Create a deliverable.
## Audience
[Audience]
## Constraints
[Format, tone, source boundary, and exposure limits]
## Ask
Produce final output only.
```

---

## Review

Use in: ChatGPT Project / Codex / Generic

```markdown
## Artifact
[Paste or attach content]
## Objective
Improve quality.
## Constraints
- Preserve intent.
- Preserve source-boundary rules.
- Do not add unsupported facts.
## Ask
Provide:
- Key issues
- Specific improvements
- Refined version only if the improvement is straightforward and does not change intent
```

---

## Codex Repository Change

Use in: Codex

```markdown
## Context
[Repository, file, feature, issue, or requested change]
## Objective
Implement the requested change while preserving Work OS structure and source boundaries.
## Constraints
- Read relevant source-of-truth files before editing.
- Prefer modifying existing files over creating new ones.
- Do not treat generated artifacts as canonical.
- Preserve sensitive information boundaries.
- Keep the change small and coherent.
## Ask
Inspect, update files, verify the change, and report:
1. Files changed
2. Summary of changes
3. Assumptions
4. Verification performed
```

---

## Work OS Evolution

Use in: ChatGPT Project / Codex

```markdown
## Context
[Conversation, notes, files, or proposed addition]
## Objective
Determine whether this information should evolve Work OS.
## Constraints
- Promote only durable, reusable, decision-relevant material.
- Keep temporary, operational, or high-churn material out of durable systems.
- Generalize sensitive detail when full fidelity is not required.
- Preserve Work OS / Personal OS / corporate system boundaries.
## Ask
Provide:
1. Durable knowledge to retain
2. Temporary execution material
3. Files or systems that should be updated
4. Information that should be discarded or left contextual
5. Suggested Codex implementation prompt
```

---

## Knowledge Compression

Use in: ChatGPT Project

```markdown
## Context
[Conversation, notes, documents, or findings]
## Objective
Compress the information into reusable Work knowledge.
## Constraints
- Separate stable principles from situational detail.
- Preserve decision logic over narrative detail.
- Do not promote temporary facts by default.
- Avoid reproducing sensitive details unless they materially affect private judgment.
## Ask
Produce:
- Executive summary
- Stable principles
- Decision rules
- Reusable frameworks
- Source-boundary implications
- Information that should remain contextual only
```

---

## Architecture Review

Use in: ChatGPT Project / Codex

```markdown
## Context
[Architecture, organization, workflow, platform, committee, or repository structure]
## Objective
Evaluate the architecture.
## Constraints
[Known constraints, maturity level, ownership model, corporate systems, or exposure limits]
## Ask
Review:
- Structural strengths
- Structural weaknesses
- Hidden coupling
- Scalability risks
- Governance implications
- Simpler alternatives
Recommend the highest-leverage changes.
```

---

## System Design

Use in: ChatGPT Project

```markdown
## Context
[Problem or opportunity]
## Objective
Design a durable system.
## Constraints
[Constraints, boundaries, users, tools, non-goals, and exposure limits]
## Ask
Produce:
- Components
- Responsibilities
- Interfaces
- Decision points
- System-of-record boundaries
- Failure modes
- Future evolution
```

---

## Strategic Critique

Use in: ChatGPT Project

```markdown
## Proposal
[Idea, plan, argument, or draft recommendation]
## Objective
Stress-test the proposal.
## Constraints
[Audience, stakes, timing, strategic boundaries, or known constraints]
## Ask
Identify:
- Hidden assumptions
- Weak arguments
- Risks
- Missing perspectives
- Stronger alternatives
Recommend whether to proceed, revise, or reject.
```

---

## Workflow Optimization

Use in: ChatGPT Project / Codex

```markdown
## Workflow
[Current process]
## Objective
Reduce friction without losing governance.
## Constraints
[Tools, ownership, compliance, visibility, coordination limits, and system boundaries]
## Ask
Identify:
- Bottlenecks
- Unnecessary complexity
- Missing automation
- Decision points
- Simplifications
- Risks introduced by the simplified workflow
Provide an improved workflow.
```

---

## Governance Review

Use in: ChatGPT Project

```markdown
## Context
[Process, organization, technology, workflow, committee, or decision system]
## Objective
Evaluate governance quality.
## Constraints
[Existing ownership, controls, maturity, authority, and operating boundaries]
## Ask
Review:
- Ownership
- Accountability
- Decision rights
- Escalation path
- Controls
- Failure scenarios
- Documentation depth required
Recommend improvements.
```

---

## Executive Communication

Use in: ChatGPT Project / Codex

```markdown
## Context
[Technical or operational information]
## Audience
[Executive or stakeholder group]
## Objective
Communicate clearly.
## Constraints
- Avoid implementation detail unless required for the decision.
- Preserve risk, recommendation, and expected outcome.
- Keep language concise and business-readable.
- Generalize private Work OS reasoning into safe communication language.
## Ask
Produce:
- Executive summary
- Key decision or requested action
- Risks
- Recommendation
- Expected outcome
```

---

## Work OS Consistency Check

Use in: ChatGPT Project / Codex

```markdown
## Context
[New document, workflow, decision, runtime package, or proposed change]
## Objective
Verify consistency with Work OS.
## Constraints
- Respect source-of-truth boundaries.
- Avoid duplicating rules across files or systems.
- Keep execution material out of durable truth unless promoted intentionally.
- Treat generated artifacts as outputs, not canonical source.
## Ask
Identify:
- Conflicts
- Duplications
- Missing references
- Exposure or source-boundary risks
- Opportunities for reuse
- Recommended source-of-truth location
```

---

## Source-Boundary Review

Use in: ChatGPT Project / Codex

```markdown
## Context
[Material, target surface, and intended use]
## Objective
Review source-boundary and exposure risk before use.
## Target Surface
[Private Work OS reasoning / Work OS ChatGPT Project / M365 Copilot / OneDrive source package / corporate system / public output]
## Constraints
- Apply Work OS information-handling rules.
- Use minimum necessary exposure.
- Generalize political, leadership, stakeholder, or institutional detail before external use.
- Do not connect raw Work OS, Personal OS, memory, or unreviewed working notes to Work-facing agents.
## Ask
Provide:
1. Material safe to use as-is
2. Material that must be generalized or removed
3. Required source-of-truth or system-of-record routing
4. Recommended safe version
5. Residual risks
```

---

## Meeting Synthesis

Use in: ChatGPT Project / Copilot

```markdown
## Inputs
[Meeting notes, transcript excerpts, agenda, or follow-up fragments]
## Objective
Synthesize the meeting into decisions, actions, risks, and reusable signals.
## Constraints
- Do not recreate the corporate meeting record in Work OS.
- Separate decisions from discussion.
- Separate Abner-owned actions from team-owned or corporate-system actions.
- Generalize sensitive context unless full fidelity is required for private judgment.
## Ask
Provide:
- Decisions made
- Open decisions
- Abner-owned actions
- Team-owned or corporate-system actions
- Risks, dependencies, and escalation signals
- Material that should become Work OS memory, decision record, narrative artifact, or nothing
```

---

## Narrative / Project Review

Use in: ChatGPT Project / Codex

```markdown
## Context
[Project narrative, update, signal set, or draft artifact]
## Objective
Review whether the narrative is decision-ready and audience-safe.
## Constraints
- Treat Narrative PARA as selected executive visibility, not the full project inventory.
- Preserve concrete audience, objective, implication, and required action.
- Do not expose private reasoning that is not needed for alignment.
- Route execution truth to the correct corporate system.
## Ask
Review:
- Audience
- Objective
- Current state
- Decision or awareness needed
- Dependencies and risks
- Missing owner, milestone, or action
- Whether this belongs in Narrative PARA, another Work OS layer, a corporate system, or nowhere
```

---

## Microsoft 365 Workflow Review

Use in: ChatGPT Project / Codex

```markdown
## Workflow
[Current Microsoft 365 workflow, friction, or proposed change]
## Objective
Improve the workflow without redefining system authority.
## Constraints
- Keep Operating Stack as durable tool authority.
- Keep Microsoft 365 playbooks as working guidance.
- Keep Jira as delivery execution truth and Confluence as documentation truth where applicable.
- Do not mirror corporate records into Work OS.
- Do not paste private Work OS context into Microsoft 365 tools.
## Ask
Provide:
1. Workflow diagnosis
2. Simplified workflow
3. Correct tool routing
4. Promotion rules for decisions, actions, notes, and records
5. Work OS files to update, if any
```

---

## Stakeholder-Safe Update

Use in: ChatGPT Project / Codex

```markdown
## Context
[Private context, draft notes, current state, or source material]
## Audience
[Audience]
## Objective
Prepare a stakeholder-safe update.
## Constraints
- Share only what the audience needs for action, decision, or awareness.
- Convert private reasoning into safe external language.
- Avoid unnecessary sensitive detail.
- Preserve ownership, risk, recommendation, and next step.
## Ask
Produce:
- Stakeholder-safe update
- Information deliberately excluded
- Risks if the update is forwarded
- Suggested follow-up action
```

---

## Decision Record Preparation

Use in: ChatGPT Project / Codex

```markdown
## Context
[Decision context, options, constraints, and evidence]
## Objective
Prepare a Work OS decision record.
## Constraints
- Use the Work OS decision-record structure.
- Classify the decision as Durable or Operational.
- Classify reversibility conservatively.
- Preserve execution linkage and governance triggers.
- Do not include raw corporate records or unnecessary sensitive detail.
## Ask
Draft:
1. Title
2. Date / version
3. Owner
4. Areas affected
5. Context
6. Decision
7. Type
8. Reversibility
9. Alternatives considered
10. Trade-offs
11. Constraints applied
12. Risks accepted
13. Execution linkage
14. Governance
```

---

## Perplexity Sanitized Research Brief

Use in: Perplexity

```markdown
## Research Question
[Question]
## Public Context
[Minimum necessary context]
## Exclusions
Do not use or infer private Work OS, Personal OS, political, leadership, memory,
corporate, or operational context beyond what is stated here.
## Ask
Provide:
- Current answer
- Evidence quality
- Source comparison
- Risks or uncertainty
- What should be validated before acting
```

---

## ChatGPT Synthesis From Research

Use in: ChatGPT Project

```markdown
## Inputs
[Paste sourced notes, Perplexity findings, or research excerpts]
## Objective
Synthesize the research into a decision-ready view.
## Constraints
- Separate evidence from interpretation.
- Identify what is stable enough to retain.
- Do not promote transient findings into durable Work OS knowledge by default.
- Preserve Work OS information-handling boundaries.
## Ask
Provide:
1. Key synthesis
2. Decision implications
3. Open questions
4. Durable Work OS updates, if any
```
