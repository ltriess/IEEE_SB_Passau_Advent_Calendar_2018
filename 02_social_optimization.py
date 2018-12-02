#!/usr/bin/env python3
import sys

DEBUG = True


def room_occupancy(relationships):

    return NotImplementedError


def main():

    if DEBUG:
        sys.stdin = open("samples/02_input.txt")

    blank = 1
    current_student = ''
    relationships = {}
    while blank < 2:
        if DEBUG:
            try:
                input_str = input()
            except EOFError:
                break
        else:
            input_str = input()
        if input_str:
            if blank == 0:
                preference, name_of_classmate = input_str.split(' ')
                relationships[current_student][preference].append(name_of_classmate)
            elif blank == 1:
                current_student = input_str
                relationships[current_student] = {'+': [], '-': []}
            else:
                pass
            blank = 0
        else:
            blank += 1

    print('{}'.format(room_occupancy(relationships)))


if __name__ == "__main__":
    main()
