from time import sleep

def debug(*msg, timestamp=[None]):
    print(*msg)
    # Import time module locally
    from time import time
    if timestamp[0] is None:
        timestamp[0] = time()
    else:
        now = time()
        print("Time elapsed: {:.3f}s".format(now - timestamp[0]))
        timestamp[0] = now

def main():
    debug("Entering a nasty piece of code ...")
    sleep(0.3)
    debug("First step done.")
    sleep(0.5)
    debug("Second step done.")

if __name__ == "__main__":
    main()