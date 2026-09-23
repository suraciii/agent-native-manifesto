#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Test requirement references through the document checker's public command."""

from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RequirementReferenceTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory(prefix="manifesto-doc-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        files = [ROOT / name for name in ("LICENSE", "LICENSE-CODE", "scripts/check_docs.py")]
        files.extend(
            path for path in ROOT.rglob("*.md")
            if not {".git", "__pycache__"}.intersection(path.relative_to(ROOT).parts)
        )
        for source in files:
            destination = self.root / source.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)

    def run_checker(self):
        return subprocess.run(
            [sys.executable, str(self.root / "scripts/check_docs.py")],
            capture_output=True, text=True, timeout=15,
        )

    def test_current_documents_pass(self):
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_undefined_references_next_to_chinese_are_rejected(self):
        document = self.root / "zh-CN/README.md"
        original = document.read_text(encoding="utf-8")
        for reference in (
            "请参阅 AN-99 的要求。",
            "请参阅AN-99 的要求。",
            "请参阅 AN-99的要求。",
            "请参阅AN-99的要求。",
            "请参阅**AN-99**的要求。",
        ):
            with self.subTest(reference=reference):
                document.write_text(original + f"\n{reference}\n", encoding="utf-8")
                result = self.run_checker()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("zh-CN/README.md: undefined requirement AN-99", result.stderr)

    def test_valid_coverage_next_to_chinese_is_recognized(self):
        document = self.root / "zh-CN/spec/evaluation.md"
        original = document.read_text(encoding="utf-8")
        self.assertIn("AN-07", original)
        document.write_text(original.replace("AN-07", "对应AN-07条"), encoding="utf-8")
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_parts_of_ascii_identifiers_are_not_references(self):
        document = self.root / "zh-CN/README.md"
        document.write_text(
            document.read_text(encoding="utf-8")
            + "\nTOKEN_AN-99_SUFFIX PLAN-99 AN-99suffix AN-991\n",
            encoding="utf-8",
        )
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
