#!/usr/bin/env python3
"""Build timestamped ChatGPT Project runtime packages from a repo config."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any, Optional


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "chatgpt-project-builds.json"


def utc_timestamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%SZ")


def repo_path(path: str) -> Path:
    if not path.startswith("/"):
        raise ValueError(f"Repository-relative paths must start with '/': {path}")
    return ROOT / path.removeprefix("/")


def display_path(path: Path) -> str:
    return "/" + str(path.relative_to(ROOT))


def read_repo_file(path: str) -> str:
    file_path = repo_path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Missing source file: {path}")
    return file_path.read_text(encoding="utf-8").rstrip() + "\n"


def load_config(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"Missing build config: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def expand_path(path: str) -> list[str]:
    source_path = repo_path(path)
    if path.endswith("/"):
        if not source_path.is_dir():
            raise FileNotFoundError(f"Missing source directory: {path}")
        return [display_path(file_path) for file_path in sorted(source_path.glob("*.md"))]
    if not source_path.is_file():
        raise FileNotFoundError(f"Missing source file: {path}")
    return [path]


def expand_full_sources(sources: list[dict[str, Any]]) -> list[str]:
    expanded: list[str] = []
    for source in sources:
        if source.get("include", "full") != "full":
            continue
        expanded.extend(expand_path(source["path"]))
    return expanded


def h1_headings(content: str, excluded_heading: Optional[str] = None) -> list[str]:
    headings = [line for line in content.splitlines() if line.startswith("# ")]
    if excluded_heading:
        headings = [heading for heading in headings if heading != excluded_heading]
    return headings


def selected_section_content(source: dict[str, Any]) -> str:
    path = source["path"]
    content = read_repo_file(path)
    heading = source["section_heading"]
    root_heading = source.get("root_heading")
    include_shared = source.get("include_shared_before_first_h1", False)

    headings = h1_headings(content, excluded_heading=root_heading)
    if heading not in headings:
        raise ValueError(f"Missing selected heading `{heading}` in {path}")

    section_start = content.index(heading)
    next_candidates = [
        content.index(candidate)
        for candidate in headings
        if content.index(candidate) > section_start
    ]
    section_end = min(next_candidates) if next_candidates else len(content)
    section = content[section_start:section_end].rstrip()

    if not include_shared:
        return section + "\n"

    first_heading = content.index(headings[0])
    shared = content[:first_heading].rstrip()
    return f"{shared}\n\n---\n\n{section}\n"


def source_manifest_entries(sources: list[dict[str, Any]]) -> list[str]:
    entries: list[str] = []
    for source in sources:
        include = source.get("include", "full")
        if include == "full":
            entries.extend(f"`{path}`" for path in expand_path(source["path"]))
            continue
        if include == "selected_section":
            label = source.get("manifest_label", f"selected section: `{source['section_heading']}`")
            entries.append(f"`{source['path']}` {label}")
            continue
        raise ValueError(f"Unsupported source include mode: {include}")
    return entries


def selected_scope_entries(sources: list[dict[str, Any]]) -> list[str]:
    entries: list[str] = []
    for source in sources:
        if source.get("include") == "selected_section":
            entries.append(
                f"- `{source['path']}`\n"
                f"  - {source.get('scope_label', 'Selected source section')}\n"
                f"  - `{source['section_heading']}`"
            )
    return entries


def header(config: dict[str, Any], package: dict[str, Any], artifact: dict[str, Any], timestamp: str, output_name: str) -> str:
    generated_from = config["generated_from"]
    refresh_trigger = config.get("refresh_trigger", f"meaningful {generated_from} changes")
    lines = [
        f"# {artifact['title']}",
        "",
        f"Generated from {generated_from}.",
        "This file is not a source of truth.",
        "Do not edit directly.",
        f"Refresh after {refresh_trigger}.",
        "",
        f"{package['target_label']}: {package['target_name']}",
        f"Owning OS: {package['owning_os']}",
        f"{generated_from} package role: {package['package_role']}",
        f"Generated timestamp: {timestamp}",
        f"Output filename: {output_name}",
        "",
    ]
    return "\n".join(lines) + "\n"


def runtime_rule(config: dict[str, Any], package: dict[str, Any], artifact: dict[str, Any], companion: str | None) -> str:
    generated_from = config["generated_from"]
    lines = ["## Runtime Package Rule", ""]
    lines.extend(artifact.get("runtime_rule_lines", package.get("runtime_rule_lines", config.get("runtime_rule_lines", []))))
    if companion:
        lines.append(f"- Upload this file with its companion `{companion}`.")
    if not lines[-1] == "":
        lines.append("")
    return "\n".join(line.replace("{generated_from}", generated_from) for line in lines) + "\n"


def compilation_scope(artifact: dict[str, Any]) -> str:
    full_sources = expand_full_sources(artifact["sources"])
    selected_entries = selected_scope_entries(artifact["sources"])
    lines = ["## Compilation Scope", "", f"### `{artifact['base_filename']}.md`", ""]
    if full_sources:
        lines.extend(["Full files:", ""])
        lines.extend(f"- `{source}`" for source in full_sources)
    if selected_entries:
        if full_sources:
            lines.append("")
        lines.extend(["Selected sections:", ""])
        lines.extend(selected_entries)
    lines.append("")
    return "\n".join(lines) + "\n"


def source_manifest(artifact: dict[str, Any]) -> str:
    lines = ["## Source Manifest"]
    lines.extend(f"- {entry}" for entry in source_manifest_entries(artifact["sources"]))
    lines.append("")
    return "\n".join(lines) + "\n"


def merged_sources(sources: list[dict[str, Any]]) -> str:
    chunks: list[str] = []
    for source in sources:
        include = source.get("include", "full")
        if include == "full":
            for expanded in expand_path(source["path"]):
                chunks.append(f"---\n\n# Merged Source: {expanded}\n\n{read_repo_file(expanded).rstrip()}\n")
            continue
        if include == "selected_section":
            chunks.append(
                f"---\n\n# Selected Source Section: {source['path']}\n\n"
                f"{selected_section_content(source).rstrip()}\n"
            )
            continue
        raise ValueError(f"Unsupported source include mode: {include}")
    return "\n".join(chunks).rstrip() + "\n"


def output_filename(artifact: dict[str, Any], timestamp: str) -> str:
    return f"{artifact['base_filename']} - {timestamp}.md"


def companion_filename(package: dict[str, Any], artifact: dict[str, Any], timestamp: str) -> Optional[str]:
    companion_base = artifact.get("companion_base_filename")
    if not companion_base:
        return None
    companion = next(
        (candidate for candidate in package["artifacts"] if candidate["base_filename"] == companion_base),
        None,
    )
    if companion is None:
        raise ValueError(f"Missing companion artifact `{companion_base}` in package `{package['slug']}`")
    return output_filename(companion, timestamp)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def clean_generated_markdown(output_root: Path) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    for file_path in output_root.glob("*/*.md"):
        file_path.unlink()


def build_artifact(config: dict[str, Any], package: dict[str, Any], artifact: dict[str, Any], timestamp: str) -> Path:
    output_root = ROOT / config.get("output_root", "build/chatgpt-projects")
    output_name = output_filename(artifact, timestamp)
    output_path = output_root / package["slug"] / output_name
    companion = companion_filename(package, artifact, timestamp)

    content = (
        header(config, package, artifact, timestamp, output_name)
        + runtime_rule(config, package, artifact, companion)
        + compilation_scope(artifact)
        + source_manifest(artifact)
        + f"## {artifact.get('compiled_heading', 'Compiled Context')}\n\n"
        + merged_sources(artifact["sources"])
    )

    write_file(output_path, content)
    return output_path


def verify(config: dict[str, Any], outputs: list[Path]) -> None:
    generated_from = config["generated_from"]
    for path in outputs:
        if not path.is_file():
            raise RuntimeError(f"Missing generated file: {path.relative_to(ROOT)}")
        content = path.read_text(encoding="utf-8")
        if f"Generated from {generated_from}." not in content:
            raise RuntimeError(f"Generated header missing: {path.relative_to(ROOT)}")
        if "## Source Manifest" not in content:
            raise RuntimeError(f"Source manifest missing: {path.relative_to(ROOT)}")


def build_all(config: dict[str, Any], timestamp: str) -> list[Path]:
    output_root = ROOT / config.get("output_root", "build/chatgpt-projects")
    if config.get("clean_output", True):
        clean_generated_markdown(output_root)

    outputs: list[Path] = []
    for package in config["packages"]:
        for artifact in package["artifacts"]:
            outputs.append(build_artifact(config, package, artifact, timestamp))
    verify(config, outputs)
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Path to the repo-specific build config.")
    parser.add_argument("--timestamp", default=utc_timestamp(), help="UTC build timestamp in YYYYMMDD-HHMMSSZ format.")
    args = parser.parse_args()

    config = load_config(Path(args.config))
    outputs = build_all(config, args.timestamp)
    print(f"Generated {len(outputs)} files with timestamp {args.timestamp}:")
    for output in outputs:
        print(f"- {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
