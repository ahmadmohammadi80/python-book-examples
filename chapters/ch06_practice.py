# Python book chapter 06, worked practice
def admission(score, attendance):
    if not 0 <= score <= 20:
        return "نمره نامعتبر"
    if not 0 <= attendance <= 100:
        return "حضور نامعتبر"
    if score >= 10 and attendance >= 75:
        return "قبول"
    return "رد"

print(admission(15, 80))
print(admission(17, 60))
