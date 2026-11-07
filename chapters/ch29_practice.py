# Python book chapter 29, worked practice
def create_task(payload):
    if not isinstance(payload, dict):
        raise ValueError("بدنه باید شیء باشد")
    title = payload.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("عنوان لازم است")
    return {"id": 1, "title": title.strip(), "done": False}

print(create_task({"title": "تمرین API"}))
