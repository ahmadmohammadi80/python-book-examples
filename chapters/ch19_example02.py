# Python book chapter 19, example 2
import csv
from io import StringIO

buffer = StringIO()
writer = csv.writer(buffer)
writer.writerow(["نام", "توضیح"])
writer.writerow(["کالا", "مناسب خانه، اداره"])
buffer.seek(0)
for row in csv.reader(buffer):
    print(row)
