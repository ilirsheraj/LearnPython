def try_syntax(numerator, denominator):
    try:
        print(f"In the try block: {numerator}/{denominator}")
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print(f"The result is: {result}")
        return result
    finally:
        print("Exiting")

def main():
    print(try_syntax(12, 4))
    print()
    print(try_syntax(11, 0))

if __name__ == "__main__":
    main()