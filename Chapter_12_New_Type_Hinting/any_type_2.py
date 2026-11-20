from typing import Any

def reverse(items: list) -> list:
    return list(reversed(items))

def reverse_any(items: list[Any]) -> list[Any]:
    return list(reversed(items))

def main():
    numbers = [1, 2, 3, 4]
    mixed: list[Any] = ["a", 42, True, None]

    print(reverse(numbers))
    print(reverse_any(numbers))
    print(reverse(mixed))
    print(reverse_any(mixed))

    rev_words_bare = reverse(["hi", "there"])
    rev_words_any = reverse_any(["hi", "there"])
    print(rev_words_bare)
    print(rev_words_any)

if __name__ == "__main__":
    main()