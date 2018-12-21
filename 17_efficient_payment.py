import sys

DEBUG = False

denom = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
strval = ['0.01', '0.02', '0.05', '0.10', '0.20', '0.50', '1', '2', '5', '10', '20', '50', '100', '200', '500']


def main():

    if DEBUG:
        sys.stdin = open("samples/17_input.txt")

    for _ in range(int(input())):
        value = int(round(100 * float(input())))

        if value == 0:
            print()
        else:
            idx = len(denom) - 1
            outstr = ''
            while True:
                if value > denom[idx]:
                    outstr += '{} '.format(strval[idx])
                    value -= denom[idx]
                elif value == denom[idx]:
                    outstr += strval[idx]
                    print(outstr)
                    break
                elif value < denom[idx]:
                    idx -= 1
                else:
                    raise ValueError


if __name__ == "__main__":
    main()
