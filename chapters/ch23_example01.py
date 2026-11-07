# Python book chapter 23, example 1
from http import HTTPStatus
import json

def build_response():
    body = {"message": "سلام", "version": 1}
    return HTTPStatus.OK, json.dumps(body, ensure_ascii=False)

status, text = build_response()
print(status.value, text)
