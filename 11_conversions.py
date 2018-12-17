import sys

DEBUG = True

alp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']


def num2base(n, b):
    if n == 0:
        return 0
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    s = ''
    for d in reversed(digits):
        s += str(alp[d])
    return s


def main():

    if DEBUG:
        sys.stdin = open("samples/11_input.txt")

    N = int(input())
    for _ in range(N):
        inputs = input().split()
        number = inputs[0]
        base_src = int(inputs[1])
        base_tar = int(inputs[2])

        output = num2base(int(number, base_src), base_tar)
        print(output)


if __name__ == "__main__":
    main()
