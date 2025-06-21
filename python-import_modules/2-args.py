#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # sys.argv[0] skriptin adıdır, ona görə 1-dən başlamaq lazımdır
    count = len(args)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
