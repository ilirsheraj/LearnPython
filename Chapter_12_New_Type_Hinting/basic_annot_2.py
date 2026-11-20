def greeter(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."

def main():
    for name, age in {"Lali": 20, "Fiku": 12, "Noci":30, "Rroku":31}.items():
        print(greeter(name, age))

if __name__ == '__main__':
    main()