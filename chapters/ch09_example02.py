# Python book chapter 09, example 2
students = [{"name": "مینا", "score": 15}, {"name": "علی", "score": 19}]
ranking = sorted(students, key=lambda row: row["score"], reverse=True)
for row in ranking:
    print(row["name"], row["score"])
