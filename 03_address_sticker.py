#!/usr/bin/env python3
import sys

DEBUG = True


def print_address_line(s, width):
    space = width - len(s)
    space_left = space // 2
    space_right = space - space_left
    print('*{}{}{}*'.format(' ' * space_left, s, ' ' * space_right))


def main():

    if DEBUG:
        sys.stdin = open("samples/03_input.txt")

    width = int(input())
    lines = int(input())
    print('*' * (width + 2))
    for _ in range(lines):
        line = input()
        if len(line) > width:
            # split line
            words = line.split(' ')
            count = 0
            s = ''
            for word in words:
                if len(word) > width:
                    raise ValueError
                elif (s == '' and len(word) <= width) or (not s == '' and (len(word) + count + 1 <= width)):
                    if not s == '':
                        s += ' '
                        count += 1
                    s += '{}'.format(word)
                    count += len(word)
                else:
                    print_address_line(s, width)
                    s = word
                    count = len(word)
            print_address_line(s, width)
        else:
            print_address_line(line, width)
    print('*' * (width + 2))


if __name__ == "__main__":
    main()
