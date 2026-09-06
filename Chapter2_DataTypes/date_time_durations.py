from datetime import date, datetime, timedelta, timezone
import time
import calendar
from zoneinfo import ZoneInfo

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