from typing import Optional

def greeter_name(name: str = "stranger") -> str:
    return f"Hello {name}!"

def greeter_optional(name: Optional[str] = None) -> str:
    if name is not None:
        return f"Hello {name}!"
    return "No one to greet"

def main():
    print(greeter_name())
    print(greeter_optional())

if __name__ == "__main__":
    main()