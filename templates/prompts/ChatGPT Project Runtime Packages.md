# ChatGPT Project Runtime Packages

Version: v1.0

---

## Purpose

Define how Work OS source files are compiled into the Work OS ChatGPT Project runtime package.

This file is a source-side template and control artifact.

It does not contain compiled project knowledge.

The generated package must contain the minimum Work OS material needed by the target ChatGPT Project to understand committee governance and agent runtime boundaries. The ChatGPT Project should not need access to the Work OS repository, folder structure, or listed source files to understand and apply the package.

---

## Source Boundary

Canonical Work OS rules remain in:

| Runtime need | Source |
|---|---|
| Repository maintenance rules | `/AGENTS.md` |
| Repository orientation | `/README.md` |
| Committee plans and governance | `/committees/` |
| Agent runtime behavior and source boundaries | `/agents/` |
| ChatGPT Project definitions and custom-instruction intent | `/templates/prompts/ChatGPT Project Custom Instructions.md` |

Broad Work context, memory, political context, leadership context, case files, and general decision records remain canonical Work OS material, but they are excluded from the default ChatGPT Project package unless a prompt-specific review explicitly requires them as attachments.

---

## Build Boundary

`/build/` contains compiled runtime artifacts only.

Do not store:

* source rules,
* decisions,
* templates,
* operational notes,
* task lists,
* meeting logs,
* corporate records,
* raw PARA material,
* or unreviewed sensitive detail.

Compiled files should be replaceable and refreshed from source.

---

## Package Rule

The Work OS-owned ChatGPT Project receives:

```text
Project Instructions - <YYYYMMDD-HHMMSSZ>.md
Project Knowledge - <YYYYMMDD-HHMMSSZ>.md
```

These two files are the Work OS project definition.

Use this package for committee planning, source-boundary review, and agent runtime-package upkeep.

Refresh it after meaningful changes to Work OS ChatGPT Project scope, committee governance, agent runtime behavior, source boundaries, or project boundaries.

Runtime package rule:

```text
Work OS source files -> project-specific runtime merge -> ChatGPT Project upload
```

Runtime context assumption:

* Everyday prompts assume `Project Instructions - <YYYYMMDD-HHMMSSZ>.md` and `Project Knowledge - <YYYYMMDD-HHMMSSZ>.md` are already uploaded in the ChatGPT Project sources section.
* Prompt-specific execution files are attached to the conversation using the prompt; do not compile drafts, emails, meeting notes, active incident details, source structures, or task artifacts into the permanent project package unless they become durable Work OS material.
* A generated package should therefore carry durable recurring context, not every possible prompt input.

Generated files are runtime artifacts, not summaries and not sources of truth.

Generated filenames must keep the current package role name and append the compile timestamp before `.md`.

Use one UTC timestamp for every file generated in the same build run:

```text
<current generated filename without extension> - <YYYYMMDD-HHMMSSZ>.md
```

Examples:

```text
Project Instructions - 20260627-165347Z.md
Project Knowledge - 20260627-165347Z.md
```

The same timestamp must appear in the generated file header. The timestamp is freshness metadata, not a source-of-truth marker.

`Project Instructions - <YYYYMMDD-HHMMSSZ>.md` and `Project Knowledge - <YYYYMMDD-HHMMSSZ>.md` are merged runtime artifacts, not summaries.

Merge means selected source excerpts are carried into the generated artifact with enough original wording to preserve rules, boundaries, and operating intent. The build may add headers, separators, traceability, and upload-specific framing. It must not compile full source files for this project.

The source manifest identifies build inputs for refresh and traceability. It is not an upload checklist and must not replace the compiled context.

---

## Compilation Rules

When refreshing the Work OS ChatGPT Project package:

* Preserve source-of-truth hierarchy.
* Preserve information-handling and exposure boundaries.
* Merge only selected source excerpts into coherent runtime files.
* Include only information that materially improves the target project's recurring reasoning quality for committees and agents.
* Preserve materially relevant source meaning, relationships, rules, constraints, named committees, agent roles, and decision gates.
* Compress aggressively outside committee and agent understanding.
* Do not compile any full source file.
* If only part of a source file is selected, include the minimum relevant excerpt and document that full-file compilation is excluded.
* Reorganization is allowed only through ordering, separators, headers, and traceability notes.
* Exclude source material that does not add value to committee or agent understanding.
* Remove temporary, high-churn, operational, draft-specific, or project-specific material unless it is required for the runtime role.
* Preserve exact wording where the source language defines a rule, boundary, or decision gate.
* Do not introduce new Work OS decisions in generated files.
* Do not edit generated files directly; refresh them from canonical sources.
* Mark generated files as non-canonical.

---

## Compilation Scope Types

Use one explicit source-scope type for the Work OS ChatGPT Project.

| Scope type | Meaning | Generated artifact behavior |
|---|---|---|
| Selected excerpt | Only the minimum relevant source material is compiled. | Carry only the excerpt needed for committee and agent understanding; label it as a selected source excerpt. |

Rules:

* Do not list a whole folder when only specific files are compiled.
* Do not compile a full file into the Work OS ChatGPT Project package.
* Do not compile every section of a shared source file when only one project section applies.
* If a selected excerpt depends on shared rules from the same file, include the shared rule as a separate selected excerpt.
* The generated source scope must show each source was compiled as a selected excerpt.

---

## Project Instructions Compilation

For the Project Instructions artifact, compile:

Selected excerpts only:

* `/AGENTS.md`
* `/README.md`
* `/templates/prompts/ChatGPT Project Runtime Packages.md`
* `/templates/prompts/ChatGPT Project Custom Instructions.md`

Do not compile project knowledge files into the project instructions artifact.

---

## Generated File Structure

Use this structure for every generated package:

### `Project Instructions - <YYYYMMDD-HHMMSSZ>.md`

* Generated-artifact header
* Compile timestamp
* Output filename
* Project role
* Custom-instruction intent from `templates/prompts/ChatGPT Project Custom Instructions.md`
* Operating rules
* Source boundaries
* Expected behavior
* Exclusions
* Promotion rule for outputs

### `Project Knowledge - <YYYYMMDD-HHMMSSZ>.md`

* Generated-artifact header
* Compile timestamp
* Output filename
* Runtime package rule
* Source manifest
* Selected source excerpts
* Relevant committee and agent decision rules
* Committee, agent, and domain boundaries
* Refresh triggers

---

## Verification Rules

Before finalizing a generated package, verify:

* The package is project-specific.
* The package is self-contained for upload.
* The package includes only selected source excerpts, not full source files.
* The package is structured for model comprehension while minimizing source exposure.
* The package excludes operational or high-churn material.
* The package excludes broad Work context, memory, political context, leadership context, case files, and validation artifacts unless explicitly required for committee or agent understanding.
* The package preserves Work OS as the source of truth.
* The package follows Work OS information-handling and source-boundary rules.
* The package does not redefine corporate systems of record.
* The package can be refreshed from the listed sources.
* Runtime prompts can assume project sources are uploaded and can rely on direct conversation attachments for prompt-specific working files.

---

## Current Runtime Packages

| Project | Runtime path |
|---|---|
| Work OS | `/build/chatgpt-projects/work-os/` |
