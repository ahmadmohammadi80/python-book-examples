"""Syntax and package-layout checks only; no chapter samples executed."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepoStructureTest(unittest.TestCase):
    def test_all_30_chapters_have_three_files(self):
        for n in range(1, 31):
            for suffix in ("example01", "example02", "practice"):
                self.assertTrue((ROOT / "chapters" / f"ch{n:02d}_{suffix}.py").is_file())

    def test_all_94_py_files_compile(self):
        files = list((ROOT / "chapters").glob("*.py")) + list((ROOT / "projects").glob("*.py"))
        self.assertEqual(len(files), 94)
        for file in files:
            with self.subTest(path=str(file.relative_to(ROOT))):
                compile(file.read_text(encoding="utf-8-sig"), str(file), "exec")


if __name__ == "__main__":
    unittest.main()
