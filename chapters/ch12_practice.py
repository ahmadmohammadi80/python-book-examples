# Python book chapter 12, worked practice
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "notes.txt"
    path.write_text("سطر یک\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as f:
        f.write("سطر دو\n")
    print(path.read_text(encoding="utf-8").count("\n"))
