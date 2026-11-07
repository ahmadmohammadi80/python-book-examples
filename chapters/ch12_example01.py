# Python book chapter 12, example 1
from pathlib import Path

path = Path("notes_example.txt")
path.write_text("جلسه اول: متغیرها\nجلسه دوم: توابع\n", encoding="utf-8")
text = path.read_text(encoding="utf-8")
print(text.strip())
