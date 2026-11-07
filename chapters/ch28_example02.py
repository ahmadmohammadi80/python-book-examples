# Python book chapter 28, example 2
from uuid import uuid4

def new_task(title):
    if not title.strip():
        raise ValueError("عنوان لازم است")
    return {"id": str(uuid4())[:8], "title": title.strip(), "done": False}

print(new_task("مطالعه" )["done"])
