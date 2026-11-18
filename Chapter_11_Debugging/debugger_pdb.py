# Data coming from JSON payload
import pdb
d = {"first": "v1", "second": "v2", "fourth": "v4"}
keys = ("first", "second", "third", "fourth")

def do_something_with_value(value):
    print(value)

def main():
    pdb.set_trace()
    for key in keys:
        do_something_with_value(d[key])

if __name__ == "__main__":
    main()