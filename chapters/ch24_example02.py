# Python book chapter 24, example 2
import csv
from io import StringIO

source = StringIO("day,sales\n1,100\n2,180\n3,90\n")
rows = list(csv.DictReader(source))
total = sum(int(r["sales"]) for r in rows)
print("جمع فروش:", total)
