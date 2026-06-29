# Scripts

## Purpose

This directory contains repository maintenance scripts.

`build_chatgpt_projects.py` builds timestamped ChatGPT Project runtime packages from repository source files and a repo-specific JSON config.

It is a generic builder. Package scope and source-boundary decisions belong in canonical source files and `/config/chatgpt-project-builds.json`, not in the script.

## Builder Contract

| Element | Rule |
|---|---|
| Script | `/scripts/build_chatgpt_projects.py` |
| Default config | `/config/chatgpt-project-builds.json` |
| Default output root | `/build/chatgpt-projects/` |
| Output role | Generated ChatGPT Project upload artifacts |
| Source authority | Canonical repository files listed by the config |
| Generated authority | None; generated files are replaceable runtime artifacts |

Decision rule:

```text
Change package scope in config and canonical templates.
Change build mechanics in the script only when generation behavior itself changes.
```

## Inputs

The builder reads a JSON config with:

| Field | Purpose |
|---|---|
| `generated_from` | Repository or source-system label used in generated headers |
| `refresh_trigger` | Refresh rule shown in generated files |
| `output_root` | Repository-relative output directory |
| `clean_output` | Whether existing generated Markdown files under package folders are removed before rebuild |
| `runtime_rule_lines` | Default runtime rules inserted into generated artifacts |
| `packages` | Runtime packages to generate |
| `artifacts` | Files generated for each package |
| `sources` | Source files or selected source sections compiled into an artifact |

Source paths are repository-relative and must start with `/`.

Supported source include modes:

| Include mode | Behavior |
|---|---|
| `full` | Compile a full file, or every Markdown file in a listed directory ending with `/` |
| `selected_section` | Compile one selected `#` heading section from one source file |

Selected sections are the preferred scope when runtime packages should minimize source exposure.

## Outputs

For each package artifact, the builder writes:

```text
<output_root>/<package slug>/<base filename> - <YYYYMMDD-HHMMSSZ>.md
```

Each generated file includes:

* generated-artifact header,
* runtime package rule,
* compilation scope,
* source manifest,
* compiled source content.

When companion artifacts are configured, both files use the same timestamp and reference each other by generated filename.

## Generated-vs-Source Boundary

Generated files under `/build/chatgpt-projects/` are working artifacts for upload and verification.

Do not edit generated files directly.

Do not promote generated output back into canonical source.

Refresh generated files from source after changes to:

* package scope,
* prompt templates,
* source-boundary rules,
* information-handling rules,
* runtime behavior,
* config source paths,
* builder generation behavior.

## Build Flow

1. Load the config.
2. Optionally clean existing generated Markdown files under package output folders.
3. For each package artifact, compute the timestamped output filename.
4. Build the generated header and runtime rule.
5. Add compilation scope and source manifest.
6. Merge configured source content.
7. Normalize local Markdown links in selected excerpts into source-path notes.
8. Write generated files.
9. Verify each output exists and contains the generated header and source manifest.

## Commands

Default build:

```bash
python3 scripts/build_chatgpt_projects.py
```

Explicit config:

```bash
python3 scripts/build_chatgpt_projects.py --config config/chatgpt-project-builds.json
```

Deterministic timestamp for verification:

```bash
python3 scripts/build_chatgpt_projects.py --config config/chatgpt-project-builds.json --timestamp 20260629-000000Z
```

Validate config JSON:

```bash
python3 -m json.tool config/chatgpt-project-builds.json
```

## Verification Checklist

Before finishing script or config changes:

* Validate `/config/chatgpt-project-builds.json` with `python3 -m json.tool`.
* Run `python3 scripts/build_chatgpt_projects.py --config config/chatgpt-project-builds.json`.
* Confirm the expected generated files were created.
* Confirm generated files remain self-contained and marked non-canonical.
* Confirm selected-section scope did not accidentally become full-file scope.
* Run Markdown lint for changed Markdown files when available.
* Run `git diff --check`.

Generated `/build/chatgpt-projects/` files are verification outputs in this repo unless a release or sync workflow explicitly requires keeping them.

## Common Failure Modes

| Symptom | Likely cause | Fix |
|---|---|---|
| `Missing build config` | Config path is wrong or absent | Use `--config config/chatgpt-project-builds.json` or restore the config |
| `Missing source file` | Config references a moved, renamed, or untracked file | Update the config path or restore the source |
| `Missing source directory` | A directory path ending with `/` does not exist | Update the config path or restore the directory |
| `Missing selected heading` | `section_heading` no longer matches a source `#` heading | Update the config heading or source heading intentionally |
| `Unsupported source include mode` | Config uses an unknown `include` value | Use `full` or `selected_section` |
| Missing generated companion reference | `companion_base_filename` does not match another artifact in the package | Align artifact base filenames in the config |
| Generated output is treated as source | Build artifacts were confused with canonical files | Edit canonical source and regenerate |

## Maintenance Rules

* Keep the script generic.
* Keep repository-specific package decisions in config and prompt templates.
* Prefer selected excerpts for packages that should minimize source exposure.
* Keep generated artifacts self-contained for upload.
* Keep generated artifacts explicitly non-canonical.
* Do not add temporary operational material to runtime packages unless it becomes durable source material first.
