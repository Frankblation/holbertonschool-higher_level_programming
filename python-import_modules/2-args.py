#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name

    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
        print(".")
    else:
        print("{} argument{}:".format(num_args, 's' if num_args > 1 else ''))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
