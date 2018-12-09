import sys

DEBUG = False


def main():

    if DEBUG:
        sys.stdin = open("samples/07_input.txt")

    days = int(input())
    for _ in range(days):
        elevation_profile = input()
        elevation = 0
        for e in elevation_profile:
            under_start = False
            if e == '/':
                elevation += 1
            elif e == '\\':
                elevation -= 1
            else:
                raise ValueError
            if elevation < 0:
                under_start = True
                break
        if elevation == 0 and not under_start:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
