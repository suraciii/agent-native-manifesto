#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check the Markdown conventions used in this repository, without network access."""

from collections import Counter
from os.path import relpath
from pathlib import Path
import json
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {"English": ROOT, "简体中文": ROOT / "zh-CN"}
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)\)")
REQUIREMENT = re.compile(r"\b(?:AN|CLI|HTTP|MCP|SDK|FILE|DOC|UI)-\d{2}\b", re.ASCII)
DEFINITION = re.compile(r"^#{2,3} ((?:AN|CLI|HTTP|MCP|SDK|FILE|DOC|UI)-\d{2}) — .+$", re.M | re.ASCII)


def reject_constant(value):
    raise ValueError(f"non-JSON constant: {value}")


def markdown_parts(text):
    """Keep prose line numbers and collect JSON examples using the same fences."""
    result = []
    examples = []
    fence = None
    language = ""
    start = 0
    body = []
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is None and marker:
            fence = marker.group(1)
            language = marker.group(2).strip()
            start = number
            body = []
            result.append("")
        elif fence is not None:
            if (marker and marker.group(1)[0] == fence[0]
                    and len(marker.group(1)) >= len(fence)
                    and not marker.group(2).strip()):
                if language == "json":
                    examples.append((start, "\n".join(body)))
                fence = None
            else:
                body.append(line)
            result.append("")
        else:
            result.append(line)
    return "\n".join(result), examples, start if fence is not None else None


def anchors(text):
    counts = Counter()
    result = set()
    for line in text.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        title = heading.group(1).lower().replace("`", "")
        slug = "".join(
            char for char in title
            if char in "-_ " or unicodedata.category(char)[0] in "LN"
        ).replace(" ", "-")
        count = counts[slug]
        counts[slug] += 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def language_root(path):
    for root in LANGUAGES.values():
        if root != ROOT and path.is_relative_to(root):
            return root
    return ROOT


def check():
    errors = []
    documents = {}
    json_count = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", ".github", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if not text.startswith("# "):
            errors.append(f"{relative}: start with a document title")
        if not text.endswith("\n"):
            errors.append(f"{relative}: missing final newline")
        document, examples, unclosed = markdown_parts(text)
        if unclosed is not None:
            errors.append(f"{relative}:{unclosed}: unclosed fenced example")
        for line, example in examples:
            json_count += 1
            try:
                json.loads(example, parse_constant=reject_constant)
            except ValueError as error:
                errors.append(f"{relative}:{line}: invalid JSON example: {error}")
        documents[path] = document

    reader_paths = {Path("README.md"), Path("CONTRIBUTING.md")}
    reader_paths.update(
        path.relative_to(ROOT) for path in documents
        if language_root(path) == ROOT
        and any(path.is_relative_to(ROOT / folder) for folder in ("docs", "spec", "examples"))
    )
    language_switches = {}
    for root in LANGUAGES.values():
        if root != ROOT:
            translated_paths = {
                path.relative_to(root) for path in documents if language_root(path) == root
            }
            for extra in sorted(translated_paths - reader_paths):
                errors.append(f"{(root / extra).relative_to(ROOT)}: no English counterpart")
        for relative in sorted(reader_paths):
            path = root / relative
            if path not in documents:
                errors.append(f"missing reader document: {path.relative_to(ROOT)}")
                continue
            switch = " | ".join(
                label if target_root == root else
                f"[{label}]({Path(relpath(target_root / relative, path.parent)).as_posix()})"
                for label, target_root in LANGUAGES.items()
            )
            language_switches[path] = switch
            if documents[path].splitlines()[2:3] != [switch]:
                errors.append(f"{path.relative_to(ROOT)}: language switch must follow the title")

    link_count = 0
    for path, text in documents.items():
        for number, line in enumerate(text.splitlines(), 1):
            for match in LINK.finditer(line):
                url = urlsplit(match.group(1))
                if url.scheme or url.netloc:
                    continue
                link_count += 1
                destination = (path.parent / unquote(url.path)).resolve() if url.path else path
                location = f"{path.relative_to(ROOT)}:{number}"
                if not destination.is_relative_to(ROOT):
                    errors.append(f"{location}: link escapes repository: {match.group(1)}")
                elif not destination.exists():
                    errors.append(f"{location}: missing target: {match.group(1)}")
                elif url.fragment and destination.suffix == ".md":
                    target_text = documents.get(destination)
                    if target_text is None or unquote(url.fragment) not in anchors(target_text):
                        errors.append(f"{location}: missing anchor: {match.group(1)}")
                if (destination in documents
                        and destination.relative_to(language_root(destination)) in reader_paths
                        and language_root(path) != language_root(destination)
                        and line != language_switches.get(path)):
                    errors.append(f"{location}: body link leaves the selected language: {match.group(1)}")

    definitions_by_language = {}
    for label, root in LANGUAGES.items():
        local_documents = {
            path: source for path, source in documents.items() if language_root(path) == root
        }
        definitions = Counter()
        for name in ("spec/core.md", "spec/interfaces.md", "spec/evaluation.md"):
            if root / name not in local_documents:
                errors.append(f"missing required document: {(root / name).relative_to(ROOT)}")
        for path, source in local_documents.items():
            if path.is_relative_to(root / "spec"):
                definitions.update(DEFINITION.findall(source))
        if not definitions:
            errors.append(f"{label}: no requirement definitions found")
        for identifier, count in definitions.items():
            if count != 1:
                errors.append(f"{label}: {identifier}: defined {count} times")

        for path, text in local_documents.items():
            for identifier in sorted(set(REQUIREMENT.findall(text)) - definitions.keys()):
                errors.append(f"{path.relative_to(ROOT)}: undefined requirement {identifier}")

        evaluation = local_documents.get(root / "spec/evaluation.md", "")
        covered = set(REQUIREMENT.findall(evaluation))
        for identifier in sorted(definitions.keys() - covered):
            errors.append(f"{(root / 'spec/evaluation.md').relative_to(ROOT)}: no coverage reference for {identifier}")
        definitions_by_language[root] = definitions

    original = definitions_by_language[ROOT].keys()
    for root, definitions in definitions_by_language.items():
        if root == ROOT:
            continue
        for identifier in sorted(original - definitions.keys()):
            errors.append(f"{root.relative_to(ROOT)}: missing translated requirement {identifier}")
        for identifier in sorted(definitions.keys() - original):
            errors.append(f"{root.relative_to(ROOT)}: requirement has no English definition: {identifier}")

    if errors:
        print("Document checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    counts = ", ".join(
        f"{label}: {len(definitions_by_language[root])}" for label, root in LANGUAGES.items()
    )
    print(
        f"Checked {len(documents)} Markdown files, {link_count} local links, "
        f"requirement definitions ({counts}), and {json_count} JSON examples."
    )
    print("Translation meaning, external links, protocol schemas, and application behavior were not checked.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
