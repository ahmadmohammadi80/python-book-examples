# Python book chapter 19, example 1
import json

profile = {"name": "نرگس", "skills": ["Python", "SQL"], "active": True}
text = json.dumps(profile, ensure_ascii=False, indent=2)
restored = json.loads(text)
print(restored["skills"][0])
