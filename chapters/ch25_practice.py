# Python book chapter 25, worked practice
from pathlib import Path

files = [Path("report.csv"), Path("notes.txt"), Path("photo.jpg")]
plan = [(f.name, f.suffix.lower().lstrip(".") or "other") for f in files]
for filename, folder in plan:
    print(f"DRY RUN: {filename} -> {folder}/")
