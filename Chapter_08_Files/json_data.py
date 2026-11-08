import json
from datetime import date

today = date.today()

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return {
                "_meta": "_date",
                "data": (obj.year, obj.month, obj.day),
            }
        return super().default(obj)

data = {
    "a_int": 42,
    "a_date": today,
}

json_data = json.dumps(data, cls=DateEncoder)
print(json_data)

def object_hook(obj):
    if obj.get("_meta") == "_date":
        return date(*obj["data"])
    return obj

data_out = json.loads(json_data, object_hook=object_hook)
print(data_out)