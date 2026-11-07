# Python book chapter 26, example 2
grades = {"S01": [18, 16], "S02": [], "S03": [14]}
for sid, scores in grades.items():
    average = sum(scores) / len(scores) if scores else None
    status = f"{average:.2f}" if average is not None else "بدون نمره"
    print(sid, status)
