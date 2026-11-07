# Python book chapter 08, worked practice
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags

first = add_tag("python")
second = add_tag("testing")
print(first, second)
assert first == ["python"]
