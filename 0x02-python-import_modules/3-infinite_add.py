#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    if not args:
        print("0")
    else:
        sum_args = 0
        for arg in args:
            if arg != sys.argv[0]:
                sum_args += int(arg)
        print(sum_args)
