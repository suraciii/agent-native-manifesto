#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check the Markdown conventions used in this repository, without network access."""

from collections import Counter
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)\)")
REQUIREMENT = re.compile(r"\b(?:AN|CLI|HTTP|MCP|SDK|FILE|DOC|UI)-\d{2}\b")
DEFINITION = re.compile(r"^#{2,3} ((?:AN|CLI|HTTP|MCP|SDK|FILE|DOC|UI)-\d{2}) — .+$", re.M)


def prose(text):
    """Keep line numbers while excluding fenced examples from link checks."""
    result = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            result.append("")
        else:
            result.append(line if fence is None else "")
    return "\n".join(result)


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
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if not text.startswith("# "):
            errors.append(f"{relative}: start with a document title")
        if not text.endswith("\n"):
            errors.append(f"{relative}: missing final newline")
        documents[path] = prose(text)

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
    for name in ("spec/core.md", "spec/interfaces.md"):
        source = documents.get(ROOT / name)
        if source is None:
            errors.append(f"missing required document: {name}")
            continue
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
        f"and {len(definitions)} requirement definitions."
    )
    print("External links and application behavior were not checked.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
