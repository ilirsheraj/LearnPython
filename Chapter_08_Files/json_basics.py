import sys
import json

# First create a dictionary
data = {
    "big_number": 2 ** 3141,
    "max_float": sys.float_info.max,
    "a_list": [2, 3, 5, 7]
}

print(type(data))

# First create a JSON formatted string
json_data = json.dumps(data)
data_out = json.loads(json_data)

assert data == data_out