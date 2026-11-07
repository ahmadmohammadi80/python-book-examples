# Python book chapter 04, example 1
raw = "   سارا محمدی   "
clean = " ".join(raw.strip().split())
print(clean)
print("تعداد نویسه‌ها:", len(clean))
