# Python book chapter 12, example 2
from pathlib import Path

path = Path("grades_example.txt")
path.write_text("12\n17\n19\n", encoding="utf-8")
with path.open(encoding="utf-8") as f:
    values = [int(line.strip()) for line in f if line.strip()]
print(sum(values) / len(values))
