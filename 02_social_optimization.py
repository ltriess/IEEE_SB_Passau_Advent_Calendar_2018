#!/usr/bin/env python3
import sys

DEBUG = True

room_occupancy = []
room_dislikes = []


def add_classmate_to_room(name, room_number):
    if name in room_dislikes[room_number]:
        print('hallelujah')
        exit(0)
    if name not in room_occupancy[room_number]:
        room_occupancy[room_number].append(name)


def add_to_dislike_list(name, room_number):
    if name in room_occupancy[room_number]:
        print('hallelujah')
        exit(0)
    if name not in room_dislikes[room_number]:
        room_dislikes[room_number].append(name)


def add_or_create_room(name):
    # student already in a room?
    for room_number, room in enumerate(room_occupancy):
        if name in room:
            return room_number
    # if no, create new room
    room_occupancy.append([name])
    room_dislikes.append([])
    return len(room_occupancy) - 1


def main():

    if DEBUG:
        sys.stdin = open("samples/02_input.txt")

    blank = 1
    current_room = 0
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
                if preference == '+':
                    add_classmate_to_room(name_of_classmate, current_room)
                elif preference == '-':
                    add_to_dislike_list(name_of_classmate, current_room)
                else:
                    raise ValueError
            elif blank == 1:
                current_room = add_or_create_room(input_str)
            else:
                pass
            blank = 0
        else:
            blank += 1

    print('\n'.join((name[0] + ' ' + ' '.join(str(i) for i in name[1:])) for name in sorted(room_occupancy)))


if __name__ == "__main__":
    main()
