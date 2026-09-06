from datetime import date, datetime, timedelta, timezone
import time

# Lets start with today
print("Date Time")
today = date.today()
print(today)

print(today.ctime())
print(today.isoformat())
print(today.weekday())

print(today.day, today.month, today.year)
print(today.timetuple())
print("-" * 50)
print()

print("Let's play with time now")
print(time.ctime())
print(time.daylight)
print(time.gmtime())
print(f"The beginning of time:\n:{time.gmtime(0)}")
print(f"The local time is {time.localtime()}")
print(time.time())
print("-" * 50)
print()

print("Let's play with datetime object")
now = datetime.now()
print(now)
utcnow = datetime.now(timezone.utc)
print(utcnow)

print(now.date())
print(now.day, now.month, now.year)
print(now.time())
print(now.hour, now.minute, now.second, now.microsecond)
print(now.ctime())
print(now.isoformat())
print(now.timetuple())
print(now.tzinfo)
print(utcnow.tzinfo)
print(now.weekday())
