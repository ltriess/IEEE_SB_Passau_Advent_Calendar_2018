#!/usr/bin/env python3
import sys

DEBUG = True


class Room:
    def __init__(self):
        self.r = set()
        self.d = set()


rooms = []


def is_resident(n):
    for i, r in enumerate(rooms):
        if n in r.r:
            return i, r
    return None


def merge(a, b):
    a, b = min(a, b), max(a, b)
    rooms[a].r = rooms[a].r.union(rooms[b].r)
    rooms[a].d = rooms[a].d.union(rooms[b].d)
    del rooms[b]
    return a, rooms[a]


def print_rooms():
    to_print = [list(sorted(list(r.r))) for r in rooms]
    for room in sorted(to_print):
        print(' '.join(room))


def main():

    if DEBUG:
        sys.stdin = open("samples/02_input.txt")

    room = None
    while True:
        try:
            s = input()
            if not s:
                room = None
            elif s[0] == '+':
                s = s[2:]
                if s in room[1].d:
                    print("hallelujah")
                    return
                a = is_resident(s)
                if a and a[0] != room[0]:
                    if room[1].r.intersection(a[1].d) or room[1].d.intersection(a[1].r):
                        print("hallelujah")
                        return
                    room = merge(room[0], a[0])
                else:
                    room[1].r.add(s)
            elif s[0] == '-':
                s = s[2:]
                if s in room[1].r:
                    print("hallelujah")
                    return
                room[1].d.add(s)
            else:
                a = is_resident(s)
                if a:
                    room = a
                else:
                    rooms.append(Room())
                    rooms[-1].r.add(s)
                    room = len(rooms) - 1, rooms[-1]

        except EOFError:
            break

    print_rooms()


if __name__ == "__main__":
    main()
