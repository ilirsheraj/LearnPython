def another_greeter(name: str | None = None) -> str:
    if name is not None:
        return f"Hello, {name}!"
    return "No-one to greet!"

def main():
    print(another_greeter())
    print(another_greeter(name="Llazi"))

if __name__ == "__main__":
    main()