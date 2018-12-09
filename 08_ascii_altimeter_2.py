import sys

DEBUG = True


def map_char(a):
    return 1 if a == '/' else -1


def main():

    if DEBUG:
        sys.stdin = open("samples/08_input.txt")

    elevation_profile = input()

    height_position = []
    sum = 0
    for e in elevation_profile:
        sum += map_char(e)
        height_position.append(sum)

    output_print = [[' ' for _ in range(len(elevation_profile))] for _ in range(max(height_position))]
    current_height = 0
    for w, e in enumerate(elevation_profile):
        if e == '/':
            output_print[current_height][w] = e
        else:
            output_print[current_height - 1][w] = e
        current_height += map_char(e)

    print('\n'.join(''.join(map(str, line)) for line in reversed(output_print)))


if __name__ == "__main__":
    main()
