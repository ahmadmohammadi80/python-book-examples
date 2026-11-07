# Python book chapter 20, worked practice
from pathlib import Path

files = ["src/main.py", ".venv/pyvenv.cfg", "tests/test_app.py"]
public_files = [Path(f) for f in files if not f.startswith(".venv/")]
for path in public_files:
    print(path.as_posix())
