#!/usr/bin/env python3
import sys

DEBUG = True


def sort(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        sort(n - 1, source, target, helper)
        # move from source to target
        if source[0]:
            disk = source[0].pop()
            print('{} -> {}'.format(source[1], target[1]))
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        sort(n - 1, helper, source, target)


def main():

    if DEBUG:
        sys.stdin = open("samples/05_input.txt")

    n = 0
    while True:
        try:
            input()
            n += 1
        except EOFError:
            break

    source = (list(reversed(range(n))), "A")
    target = ([], "Z")
    helper = ([], "V")
    sort(len(source[0]), source, helper, target)


if __name__ == '__main__':
    main()
