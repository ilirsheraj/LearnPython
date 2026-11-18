def debug(*msg, print_separator=True):
    print(*msg)
    if print_separator:
        print("-" * 40)

def main():
    debug("Data is ...")
    debug("Different", "Strings", "Are not a problem")
    debug("After while loop", print_separator=False)

if __name__ == "__main__":
    main()