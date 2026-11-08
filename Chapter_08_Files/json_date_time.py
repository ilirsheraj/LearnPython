import json
from datetime import datetime, timedelta, timezone

now = datetime.now()
now_tz = datetime.now(tz=timezone(timedelta(hours=1)))
# print(now)
# print(now_tz)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            try:
                off = obj.utcoffset().seconds
            except AttributeError:
                off = None

            return {
                "_meta": "_datetime",
                "data": obj.timetuple()[:6] + (obj.microsecond, ),
                "utcoffset": off,
            }

data = {
    "a_int": 42,
    "a_float": 3.1415965,
    "a_datetime": now,
    "a_datetime_tz": now_tz,
}

json_data = json.dumps(data, cls=DateTimeEncoder)
print(json_data)