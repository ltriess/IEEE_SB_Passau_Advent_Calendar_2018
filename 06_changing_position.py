import sys

DEBUG = True


def main():

    if DEBUG:
        sys.stdin = open("samples/06_input_01.txt")

    num_people = int(input())
    queue = [int(s) for s in input().split(' ')]
    shifts = [(x - (n + 1)) for n, x in enumerate(queue)]

    if not (sum(shifts) == 0 and all(i <= 2 for i in shifts)):
        print('CHAOS')
    else:
        print(sum([abs(n) for n in shifts]) // 2)


if __name__ == "__main__":
    main()
