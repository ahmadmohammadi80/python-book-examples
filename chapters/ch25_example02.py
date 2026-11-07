# Python book chapter 25, example 2
from pathlib import Path
from shutil import copy2

source = Path("source_note.txt")
source.write_text("اطلاعات نمونه", encoding="utf-8")
backup = Path("source_note.backup.txt")
copy2(source, backup)
print(backup.read_text(encoding="utf-8"))
