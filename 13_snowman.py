import sys
import math

DEBUG = True


def sphere_volume(r):
    return 4/3 * math.pi * r**3


def main():

    if DEBUG:
        sys.stdin = open("samples/13_input_01.txt")

    garden = input().split()
    amount_snow = float(garden[0]) * float(garden[1]) * float(garden[2])
    height_snowman = float(input())

    volume_snowman = sphere_volume(2/9 * 1/2 * height_snowman) + \
                     sphere_volume(3/9 * 1/2 * height_snowman) + \
                     sphere_volume(4/9 * 1/2 * height_snowman)

    if volume_snowman > amount_snow:
        print('Let it go!')
    else:
        print('Let\'s do it!')


if __name__ == "__main__":
    main()
