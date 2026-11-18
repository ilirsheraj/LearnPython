# Data coming from JSON payload
d = {"first": "v1", "second": "v2", "fourth": "v4"}
keys = ("first", "second", "third", "fourth")

def do_something_with_value(value):
    print(value)

def main():
    breakpoint()
    for key in keys:
        do_something_with_value(d[key])

if __name__ == "__main__":
    main()