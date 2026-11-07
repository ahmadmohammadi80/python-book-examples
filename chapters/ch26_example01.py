# Python book chapter 26, example 1
def add_grade(grades, student_id, score):
    if not 0 <= score <= 20:
        raise ValueError("نمره خارج از بازه")
    grades.setdefault(student_id, []).append(score)

def average_grade(grades, student_id):
    values = grades.get(student_id, [])
    return sum(values) / len(values) if values else None

book = {}
add_grade(book, "S01", 18)
add_grade(book, "S01", 16)
print(average_grade(book, "S01"))
