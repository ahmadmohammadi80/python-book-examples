# Python book chapter 25, example 1
from pathlib import Path

folder = Path("sample_docs")
folder.mkdir(exist_ok=True)
(folder / "report.txt").write_text("sample", encoding="utf-8")
for source in folder.glob("*.txt"):
    target = source.with_name("archived_" + source.name)
    print(f"DRY RUN: {source} -> {target}")
