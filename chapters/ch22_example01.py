# Python book chapter 22, example 1
import json

response_body = '{"status":"ok","items":[{"id":1,"name":"کتاب"}]}'
data = json.loads(response_body)
if data.get("status") == "ok":
    for item in data.get("items", []):
        print(item["id"], item["name"])
