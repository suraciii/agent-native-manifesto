#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check the Markdown conventions used in this repository, without network access."""

from collections import Counter
from pathlib import Path
import json
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)\)")
REQUIREMENT = re.compile(r"\b(?:AN|CLI|HTTP|MCP|SDK|FILE|DOC|UI)-\d{2}\b")
DEFINITION = re.compile(r"^#{2,3} ((?:AN|CLI|HTTP|MCP|SDK|FILE|DOC|UI)-\d{2}) — .+$", re.M)


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


def check():
    errors = []
    documents = {}
    json_count = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "__pycache__"} for part in path.relative_to(ROOT).parts):
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

    definitions = Counter()
    for name in ("spec/core.md", "spec/interfaces.md", "spec/evaluation.md"):
        if ROOT / name not in documents:
            errors.append(f"missing required document: {name}")
    for path, source in documents.items():
        if path.is_relative_to(ROOT / "spec"):
            definitions.update(DEFINITION.findall(source))
    if not definitions:
        errors.append("no requirement definitions found")
    for identifier, count in definitions.items():
        if count != 1:
            errors.append(f"{identifier}: defined {count} times")

    for path, text in documents.items():
        for identifier in sorted(set(REQUIREMENT.findall(text)) - definitions.keys()):
            errors.append(f"{path.relative_to(ROOT)}: undefined requirement {identifier}")

    evaluation = documents.get(ROOT / "spec/evaluation.md", "")
    covered = set(REQUIREMENT.findall(evaluation))
    for identifier in sorted(definitions.keys() - covered):
        errors.append(f"spec/evaluation.md: no coverage reference for {identifier}")

    if errors:
        print("Document checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"Checked {len(documents)} Markdown files, {link_count} local links, "
        f"{len(definitions)} requirement definitions, and {json_count} JSON examples."
    )
    print("External links, protocol schemas, and application behavior were not checked.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
