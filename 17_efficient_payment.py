import sys

DEBUG = False

denomination = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00, 200.00, 500.00]


def largest(rest_value, index, division):
    if rest_value < int(denomination[index] * 100.0):
        largest(rest_value, index - 1, division)
    elif rest_value == int(denomination[index] * 100.0):
        division.append(denomination[index])
        s = ''
        for num in list(reversed(sorted(division))):
            if num % 1 == 0:
                s += '{} '.format(int(num))
            else:
                s += '{0:.2f} '.format(num)
        print(s[:-1])
    elif rest_value > int(denomination[index] * 100.0):
        division.append(denomination[index])
        largest(rest_value - int(denomination[index] * 100.0), index, division)
    else:
        return


def main():

    if DEBUG:
        sys.stdin = open("samples/17_input.txt")

    for _ in range(int(input())):
        value = float(input())

        if value == 0.0:
            print()
        else:
            largest(int(value * 100.0), len(denomination) - 1, [])


if __name__ == "__main__":
    main()
