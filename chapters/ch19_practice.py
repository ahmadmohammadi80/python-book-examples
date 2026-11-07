# Python book chapter 19, worked practice
import csv
import io

buffer = io.StringIO(newline="")
writer = csv.writer(buffer)
writer.writerow(["نام", "توضیح"])
writer.writerow(["مداد", "نوک نرم، مشکی"])
buffer.seek(0)
rows = list(csv.reader(buffer))
print(rows[1][1])
