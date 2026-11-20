from typing import Any

def square(n):
    return n**2

def square_annotated(n: Any) -> Any:
    return n**2

def main():
    print(square(3))
    print(square_annotated(3))

if __name__ == '__main__':
    main()