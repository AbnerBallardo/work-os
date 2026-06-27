# ChatGPT Project Runtime Packages

Version: v1.0

---

## Purpose

Define how Work OS source files are compiled into the Work OS ChatGPT Project runtime package.

This file is a source-side template and control artifact.

It does not contain compiled project knowledge.

The generated package must contain the relevant Work OS material needed by the target ChatGPT Project. The ChatGPT Project should not need access to the Work OS repository, folder structure, or listed source files to understand and apply the package.

---

## Source Boundary

Canonical Work OS rules remain in:

| Runtime need | Source |
|---|---|
| Repository maintenance rules | `/AGENTS.md` |
| Repository orientation | `/README.md` |
| Work operating context | `/context/` |
| Compressed Work recall | `/memory/` |
| Durable decisions and guardrails | `/systems/decisions/` |
| Committee plans and governance | `/committees/` |
| Agent runtime behavior and source boundaries | `/agents/` |
| ChatGPT Project definitions and custom-instruction intent | `/templates/prompts/ChatGPT Project Custom Instructions.md` |

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

Use this package for Work OS maintenance, private Work reasoning, committee planning, source-boundary review, and agent runtime-package upkeep.

Refresh it after meaningful changes to Work OS structure, Work context, Work memory, decision records, committee governance, agent runtime behavior, source boundaries, or project boundaries.

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

Merge means the selected source files, or selected source sections when a full file is intentionally excluded, are carried into the generated artifact materially intact. The build may add headers, separators, traceability, and upload-specific framing, but it must not compress, paraphrase, shorten, or replace the selected source content with a synopsis.

The source manifest identifies build inputs for refresh and traceability. It is not an upload checklist and must not replace the compiled context.

---

## Compilation Rules

When refreshing the Work OS ChatGPT Project package:

* Preserve source-of-truth hierarchy.
* Preserve information-handling and exposure boundaries.
* Merge selected source files or selected source sections into coherent runtime files.
* Include all information that materially improves the target project's recurring reasoning quality.
* Preserve materially relevant source meaning, relationships, rules, constraints, named committees, agent roles, and decision gates.
* Do not summarize, paraphrase, compress, or shorten selected source material.
* If a source file is selected, include its content materially intact unless a specific exclusion is documented.
* If only part of a source file is selected, include the selected section materially intact and document the exclusion.
* Reorganization is allowed only through ordering, separators, headers, and traceability notes.
* Exclude source material that does not add value to the target project.
* Remove temporary, high-churn, operational, draft-specific, or project-specific material unless it is required for the runtime role.
* Preserve exact wording for selected source content.
* Do not introduce new Work OS decisions in generated files.
* Do not edit generated files directly; refresh them from canonical sources.
* Mark generated files as non-canonical.

---

## Compilation Scope Types

Use two explicit source-scope types.

| Scope type | Meaning | Generated artifact behavior |
|---|---|---|
| Full file | The whole source file is relevant to the project runtime. | Carry the file materially intact into the generated package. |
| Selected section | Only a named section is relevant to the project runtime. | Carry only that section materially intact and label it as a selected source section. |

Rules:

* Do not list a whole folder when only specific files are compiled.
* Do not compile every section of a shared source file when only one project section applies.
* If a selected section depends on shared rules from the same file, include the shared rules as a separate selected section.
* The generated source scope must show whether a source was compiled as a full file or as a selected section.

---

## Project Instructions Compilation

For the Project Instructions artifact, compile:

Full files:

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
* Merged source files or selected source sections
* Relevant decision rules
* Committee, agent, and domain boundaries
* Refresh triggers

---

## Verification Rules

Before finalizing a generated package, verify:

* The package is project-specific.
* The package is self-contained for upload.
* The package includes selected source content materially intact, not only references or summaries.
* The package is structured for model comprehension without reducing selected source content.
* The package excludes operational or high-churn material.
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
