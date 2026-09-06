from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import arrow

f_bday = datetime(1975, 12, 29, 12, 50,
                  tzinfo=ZoneInfo('Europe/Rome'))
print(f_bday)
h_bday = datetime(1981, 10, 7, 15, 30, 50,
                  tzinfo=timezone(timedelta(hours=2)))
print(h_bday)

diff = h_bday - f_bday
print(diff)
print(f"Difference in days: {diff.days}")
print(f"Difference in seconds: {diff.total_seconds()}")
print("-" * 50)

print("Play with Arrow Third Party Library")
print(arrow.now())
print(arrow.utcnow())
local = arrow.now("Europe/Tirane")
print(local)
print(local.datetime)
print(local.to("utc"))
print(local.to("Europe/Moscow"))
print(local.isoformat())
print(local.datetime)