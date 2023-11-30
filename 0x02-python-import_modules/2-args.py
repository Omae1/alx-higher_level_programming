#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    if arg == 1:
        print("{} argument".format(arg), end="")
    else:
        print("{} arguments".format(arg), end="")
    if arg > 0:
        print(":")
    else:
        print(".")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
