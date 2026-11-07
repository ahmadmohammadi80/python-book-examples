# Python book chapter 22, example 2
from urllib.request import Request

req = Request("https://example.com/api/items", headers={"Accept": "application/json"})
print(req.get_method())
print(req.full_url)
