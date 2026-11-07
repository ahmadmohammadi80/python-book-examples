# Python book chapter 18, example 2
from datetime import datetime, timedelta, timezone

start = datetime(2026, 11, 6, 12, tzinfo=timezone.utc)
deadline = start + timedelta(days=4)
print(deadline.date())
