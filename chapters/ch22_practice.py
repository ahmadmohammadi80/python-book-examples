# Python book chapter 22, worked practice
def read_api_response(status, payload):
    if status != 200:
        raise ValueError(f"HTTP {status}")
    if not isinstance(payload, dict) or "items" not in payload:
        raise ValueError("قالب پاسخ نامعتبر")
    return payload["items"]

print(read_api_response(200, {"items": [1, 2]}))
