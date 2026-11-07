import json

info = {
    "full_name": "Sherlock Holmes",
    "address": {
        "street": "123 Main St.",
        "zip": "NW1 6XE",
        "city": "London",
        "Country": "UK"
    }
}

print(json.dumps(info, indent=2, sort_keys=True))