import sys
import cmath

DEBUG = False

tolerance = 20e-3  # seconds
velocity_sound = 343.0  # meter per second


def main():

    if DEBUG:
        sys.stdin = open("samples/24_input.txt")

    for _ in range(int(input())):
        inp = input().split()
        width_stage = int(inp[0])
        y = int(inp[1])
        x = int(inp[2])

        if abs(cmath.sqrt(y ** 2 + ((width_stage / 2) - x) ** 2) / velocity_sound -
               cmath.sqrt(y ** 2 + ((width_stage / 2) + x) ** 2) / velocity_sound) > tolerance:
            print('No')
        else:
            print('Yes')


if __name__ == "__main__":
    main()
