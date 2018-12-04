#!/usr/bin/env python3
import sys

DEBUG = True


def main():

    if DEBUG:
        sys.stdin = open("samples/03_input.txt")

    width = int(input())
    lines = int(input())
    print('*' * (width + 2))
    for _ in range(lines):
        line = input()
        if len(line) > width:
            # TODO: split line into two
            pass
        else:
            print('*{}*'.format(line.center(width)))
    print('*' * (width + 2))


if __name__ == "__main__":
    main()
